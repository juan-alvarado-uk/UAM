'''
Este programa sirve para convertir en imagen los textos de pregunta de examen 
para poner un poquito mayor el grado de dificultad para los exámenes en google forms.

Luego de hacerlos imagen, usando credenciales de autorización de google para drive y
configurando un proyecto en la consola de proyectos de google, se suben las imágenes
a Drive y se genera un mapa con los ID de los archivos para usarlos luego en un form

las entradas necesarias son examenes.json, en este mismo directorio, que tiene muchas cosas
pero sobre todo tiene las preguntas de examen, lo segundo es el ambiente de conda "examenesDrive"
que ya tiene todas las dependencias instaladas.

lo tercero y muy importante es el archivo credentials.json de google, 
pero ese NO SE PUEDE/DEBE versionar, GitHub lo restringe pues es riesgoso.
Ese archivo solo se debe tener localmente. Luego cuando este script corre genera un 
token.json que también se queda localmente. El gitignore ya incluye a los dos archivos 
para evitar problemas en los commits. (TODO tal vez hay que incluir .env)

Mayor información en el archivo: "configurar_examen.md"
'''
from __future__ import print_function
import json
import os
# from weasyprint import HTML
from playwright.sync_api import sync_playwright
import tempfile
import pathlib

import os.path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def pregunta_a_html(p):
    # p es un dict con id, enunciado, opciones, etc.
    '''opciones_html = "".join(
        f"<li>{op}</li>" for op in p["opciones"]
    )'''
    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <style>
          body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 16px;
            margin: 16px;
            max-width: 400px;
          }}
          .id {{ color: #666; font-size: 12px; margin-bottom: 4px; }}
          .enunciado {{ font-weight: 600; margin-bottom: 8px; }}
          ol {{ padding-left: 24px; }}
        </style>
      </head>
      <body>
        <div class="enunciado">{p["enunciado"]}</div>
      </body>
    </html>
    """

    return html


def generar_imagenes_desde_json(ruta_json, carpeta_salida="outs_imgs"):
    os.makedirs(carpeta_salida, exist_ok=True)

    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    mapas = []  # lista de {id_pregunta, path_local}
    for examen in data["examenes"]:
        for p in examen["preguntas"]:
            html = pregunta_a_html(p)
            file_name = f"{p['id']}.png"
            path = os.path.join(carpeta_salida, file_name)
            # un PNG por “página”
            HTML(string=html).write_png(path)
            mapas.append({"id_pregunta": p["id"], "path": path})
    return mapas




def generar_imagenes_playwright(ruta_json, carpeta_salida="outs_imgs"):
    print("ENTRANDO A PLAYWRITE $$$$$$#######$$$$$$$$#######$$$$$$$$")
    os.makedirs(carpeta_salida, exist_ok=True)
    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    mapas = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 420, "height": 50})

        for examen in data["examenes"]:
            for p_ in examen["preguntas"]:
                html = pregunta_a_html(p_)
                tmp_html = pathlib.Path(tempfile.gettempdir()) / f"{p_['id']}.html"
                tmp_html.write_text(html, encoding="utf-8")

                page.goto(tmp_html.as_uri())
                # Ajuste simple: capturar página completa
                file_name = f"{p_['id']}.png"
                path = os.path.join(carpeta_salida, file_name)
                page.screenshot(path=path, full_page=True)
                mapas.append({"id_pregunta": p_["id"], "path": path})

        browser.close()
    return mapas



SCOPES = ["https://www.googleapis.com/auth/drive.file"]  # acceso a archivos creados por la app

def get_drive_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("drive", "v3", credentials=creds)
    return service


def subir_imagenes_a_drive(mapa_paths, folder_id):
    """
    mapa_paths: lista de dicts {id_pregunta, path}
    folder_id: ID de carpeta de Drive donde se guardarán las imágenes
    """
    service = get_drive_service()
    resultado = {}

    for item in mapa_paths:
        file_metadata = {
            "name": os.path.basename(item["path"]),
            "parents": [folder_id]
        }
        media = MediaFileUpload(item["path"], mimetype="image/png")
        f = service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()
        file_id = f["id"]

        # (Opcional) Hacer el archivo accesible mediante enlace dentro de la organización
        service.permissions().create(
            fileId=file_id,
            body={
                "role": "reader",
                "type": "anyone"
            }
        ).execute()

        resultado[item["id_pregunta"]] = file_id

    return resultado


def main():
    ruta_json = "examenes.json"          # el JSON que ya tienes
    carpeta_png = "outs_imgs"
    folder_drive_id = "15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2"     # carpeta en Drive

    # 1) JSON -> PNG por pregunta
    mapa_local = generar_imagenes_playwright(ruta_json, carpeta_png)
    # print("Creado el mapa:", mapa_local)
    # mapa_local = generar_imagenes_desde_json(ruta_json, carpeta_png)
    # o: mapa_local = generar_imagenes_playwright(ruta_json, carpeta_png)

    # 2) PNG -> Drive
    mapa_drive = subir_imagenes_a_drive(mapa_local, folder_drive_id)

    # 3) Guardar el mapa para luego usarlo desde Apps Script / Forms
    with open("mapa_pregunta_drive.json", "w", encoding="utf-8") as f:
        json.dump(mapa_drive, f, ensure_ascii=False, indent=2)

    print("Listo. Mapa id_pregunta -> fileId guardado en mapa_pregunta_drive.json")

if __name__ == "__main__":
    main()
