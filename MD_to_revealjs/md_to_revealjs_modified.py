#!/usr/bin/env python3
"""
Convierte un Markdown en una presentación Reveal.js.

- H1: slide de título + slides de contenido.
- H2/H3: slides de contenido heredando título más específico.
- Texto cortado por frases para evitar slides saturadas.
- Tablas largas se parten en varias slides.
- Bloques de código se respetan como bloque completo.
- Imágenes decorativas solo en slides de texto, en layout de dos columnas.
"""

import re
import argparse
import random
from typing import List, Dict, Any
from pathlib import Path
import os

# ===================== CONFIG IMÁGENES DECORATIVAS =====================
# Extensiones de imagen que queremos considerar
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".webp")
IMAGE_URL_PREFIX = "https://juan-alvarado-uk.github.io/UAM/"
IMAGE_URL_PREFIX2 = "../../"


def load_decorative_images_from_parent(folder_name: str = "img") -> list:
    """
    Busca imágenes en ../<folder_name> respecto al directorio del script
    y devuelve rutas RELATIVAS respecto al cwd actual.
    """
    # Devuelve directamente los links de las imágenes en Google Drive (Cuajimalpa)
    return [
        "https://drive.google.com/thumbnail?id=1-8BJ3_0oNuQ9sIrSRd184rJZiEhfpUoS&sz=s4000",
        "https://drive.google.com/thumbnail?id=1-U9yc572hW6_dymagg4zrY35R-3o9FeH&sz=s4000",
        "https://drive.google.com/thumbnail?id=1-ULMJtWOl4_vWfD3XPvA6me4WuwNUc30&sz=s4000",
        "https://drive.google.com/thumbnail?id=1-s5QsBuxnktxHY_n25nTzTGKh1ME5Zc-&sz=s4000",
        "https://drive.google.com/thumbnail?id=1-zMLLmGb4CDfmp6MeVg1T3nefqju01DS&sz=s4000",
        "https://drive.google.com/thumbnail?id=10WlwgZLV9bEaVh3gduRN_4mfx4UWuVZU&sz=s4000",
        "https://drive.google.com/thumbnail?id=10pMdqT899hiZaqMq5QjWVSSbC4PASCTw&sz=s4000",
        "https://drive.google.com/thumbnail?id=131L25xNXQ3Nyez8CSnoECgD1JoPsO3rj&sz=s4000",
        "https://drive.google.com/thumbnail?id=13HemcLSUduvwW5z8mD7b35XGY0NAuYwj&sz=s4000",
        "https://drive.google.com/thumbnail?id=13WH7rxhiM5O8jxG1uD0CVbcH8y2Q6bfy&sz=s4000",
        "https://drive.google.com/thumbnail?id=14x41OCgVv_P_i-FmfoK0ek3ORT7ZnrvX&sz=s4000",
        "https://drive.google.com/thumbnail?id=15lngYqOjPk9qi-ZI_F0b9nBCCQh7eVwO&sz=s4000",
        "https://drive.google.com/thumbnail?id=15rCHj2kUWpBCumUsguCqsjC93CMYYMu_&sz=s4000",
        "https://drive.google.com/thumbnail?id=1678iEhgQgMnEYW8zR_nMO7JUj-nNVhLx&sz=s4000",
        "https://drive.google.com/thumbnail?id=16llWLmDbY_L-o26j_sn1yz51_kGGkZPF&sz=s4000",
        "https://drive.google.com/thumbnail?id=17L-Z4s2KaP48ehRDn2ppIa6fXgIGZtsp&sz=s4000",
        "https://drive.google.com/thumbnail?id=17nPco_fKiufJOc0n6CWPK5iYm8uxEUrW&sz=s4000",
        "https://drive.google.com/thumbnail?id=19F7uBnqVo3ea1dNykHuokuzuUEIZ-yHl&sz=s4000",
        "https://drive.google.com/thumbnail?id=1CENNu7Y3go_MP1ltMa1WyMqZANMiG8EQ&sz=s4000",
        "https://drive.google.com/thumbnail?id=1CFXajhi6IdtSOdeDIbrNtxrrqOrboiSh&sz=s4000",
        "https://drive.google.com/thumbnail?id=1CNLXWlyf8x1biKFBRyCNUdpGJhz1sepV&sz=s4000",
        "https://drive.google.com/thumbnail?id=1CNU32ax_lgZ-_Zjs9iLrVR5DfEMmGcjU&sz=s4000",
        "https://drive.google.com/thumbnail?id=1CeIb-HQaS0k2g5pJnxZ_NuIJv3J39SC_&sz=s4000",
        "https://drive.google.com/thumbnail?id=1ChbxlM_dnVnmWuhhZP7Ycuhkq9nELgGb&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Cyse2GuhPwcCvx0W3GvCdFkhTzfU3uyS&sz=s4000",
        "https://drive.google.com/thumbnail?id=1D4pCfDKH1tQt3QvWUNz4xPVS6aY9QhGB&sz=s4000",
        "https://drive.google.com/thumbnail?id=1EV0i1uia4JOyqzhIdFvrecEJwFtnD4yF&sz=s4000",
        "https://drive.google.com/thumbnail?id=1G99x933S3AsbHPyXlmkMw9RNP4sdO9Xb&sz=s4000",
        "https://drive.google.com/thumbnail?id=1He4A37oOcTJPUhu0PNZGTtyKSbglrIJj&sz=s4000",
        "https://drive.google.com/thumbnail?id=1IBK_hrMia1v7CAvw7pCnhesYMQJsc1eT&sz=s4000",
        "https://drive.google.com/thumbnail?id=1IpGvkAi3sKSaMD_jNRM0n0E7e5izFMaO&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Ip_88wr2so19QifwwNOzjtruXcCLGiJt&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Jby69ljDK6PgA_yLBooXTct0KJwFtRiA&sz=s4000",
        "https://drive.google.com/thumbnail?id=1KFQLfqViO2P90GRBhClYGM2ptki9JopY&sz=s4000",
        "https://drive.google.com/thumbnail?id=1LBnWHkDvBECORA0gixEmbZwrXa8QOtIW&sz=s4000",
        "https://drive.google.com/thumbnail?id=1LNKu3yMFAdjjFNTZ6ZUhlV1dpFPB0j68&sz=s4000",
        "https://drive.google.com/thumbnail?id=1LlKZO3iOWv2UmXisVYvB1MP9vJHmqZLm&sz=s4000",
        "https://drive.google.com/thumbnail?id=1LrM7C5XITYFXmIHQEKi1SY7j98wtV7KG&sz=s4000",
        "https://drive.google.com/thumbnail?id=1MCOVmDqGuYCY7yMWB-Xuc1e75AFXmtQc&sz=s4000",
        "https://drive.google.com/thumbnail?id=1MPgQCarXGVw0zxACcEvb5N2cJNLfUUEI&sz=s4000",
        "https://drive.google.com/thumbnail?id=1MS3HiCLrh9YVk0QK7F8cxKL-PZJi13PA&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Mi9uUooks5CdHVTwOhN3RLzXE3yD5QJF&sz=s4000",
        "https://drive.google.com/thumbnail?id=1O9tODHaKu-phMlYqEmr9cL3WBmrEHhz4&sz=s4000",
        "https://drive.google.com/thumbnail?id=1OE4rSgFu3JFz36kgDK2XIaYgS3K-Hcg7&sz=s4000",
        "https://drive.google.com/thumbnail?id=1OMAk2ERQNPg8Ojqn12Tx-6JBAXUG5sX6&sz=s4000",
        "https://drive.google.com/thumbnail?id=1OsPav3kdWWEphilwyUzFRAvk-KcJ5fzZ&sz=s4000",
        "https://drive.google.com/thumbnail?id=1PTd5oRGWrExWdPCiQM08WOlUvvRP72c6&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Pxvv7MhZoZZNf62f3isCRSq9TC8IM-TV&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Q5mY7BHyBG9OCvc5nNzjnsZYKGZMyHPx&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Rzmr4vgZGpje9PlpVQgISIb1qpBW04QR&sz=s4000",
        "https://drive.google.com/thumbnail?id=1S1OY5sv5VM0Dii-dLgqZNaPKmUncMHaF&sz=s4000",
        "https://drive.google.com/thumbnail?id=1S7OdDEBjANOTlxlwnXdSxfSsEBEs0JaW&sz=s4000",
        "https://drive.google.com/thumbnail?id=1SY7LBQtEjhDUmGOQA_rZnmR1739FXmXY&sz=s4000",
        "https://drive.google.com/thumbnail?id=1SspDxauJkT5Yv10Oy52FqsPvMbKnfXs9&sz=s4000",
        "https://drive.google.com/thumbnail?id=1Tfa4evCDVO44q7GuMk1--UDcoOz4ADxu&sz=s4000",
        "https://drive.google.com/thumbnail?id=1UEA0vwtWueOn0F-dM8o4YWDR_TA0NqZR&sz=s4000",
        "https://drive.google.com/thumbnail?id=1UL5cHenqjlGzgzvWAcG_yoKGjt0NErGc&sz=s4000",
        "https://drive.google.com/thumbnail?id=1WHE1zP2V24Z_X1Rfk28O6F1tm4UIdEs2&sz=s4000",
        "https://drive.google.com/thumbnail?id=1YiKWbdLLFIbOxFHdYksPGjBYigg6vJkD&sz=s4000",
        "https://drive.google.com/thumbnail?id=1ZijMNcIC_IihaE_8mY5ruBAwojUVJQPc&sz=s4000",
        "https://drive.google.com/thumbnail?id=1_SwPm3V2frsslEClPf2Dg06it5JVK1hx&sz=s4000",
        "https://drive.google.com/thumbnail?id=1ahEyJs0X7QObv4zPgzuXYheqXdTW15ES&sz=s4000",
        "https://drive.google.com/thumbnail?id=1bAq9WDsQdY_t5H_M6TONXhCXihGyOOQg&sz=s4000",
        "https://drive.google.com/thumbnail?id=1bUPUgBseEBWlBj0kNhz7N1nF83AOWI3X&sz=s4000",
        "https://drive.google.com/thumbnail?id=1ci1xXWV4PZiWGWhPn4NCrFs-Ra5PVIEr&sz=s4000",
        "https://drive.google.com/thumbnail?id=1dM3t9czEwQ5BA-ENqKwBNmMhYjSlGRQ5&sz=s4000",
        "https://drive.google.com/thumbnail?id=1e69h1W0KZ4QwfMTooQS_edVFDJ7Iw8ze&sz=s4000",
        "https://drive.google.com/thumbnail?id=1f6bOauPR9wuXtdab2xOZYSvpt4SXg_Gi&sz=s4000",
        "https://drive.google.com/thumbnail?id=1fJEo06jYyRtTpMPB1tHzrkIjF5B-ggEi&sz=s4000",
        "https://drive.google.com/thumbnail?id=1gIRDgsKbTbivN8EOkJiiXD-pO1GGFIMS&sz=s4000",
        "https://drive.google.com/thumbnail?id=1gb3CglJVHm8IKNI8LUNjhyzSYTXvuxWn&sz=s4000",
        "https://drive.google.com/thumbnail?id=1h1Dx62P5WWxmQSynFbBGJc-mQKD15nRp&sz=s4000",
        "https://drive.google.com/thumbnail?id=1h2UaoyLvryxUwGkE1WhD1kF1_jf2ap97&sz=s4000",
        "https://drive.google.com/thumbnail?id=1hRyDwAKqekvJS5zWQVlDdgC25oz40QGt&sz=s4000",
        "https://drive.google.com/thumbnail?id=1iHf73OzsBgZobvIvp6HBun5Sf708YSvU&sz=s4000",
        "https://drive.google.com/thumbnail?id=1jnk1yrq7z2bXfKHa9i9cQACCXD-fw1Z0&sz=s4000",
        "https://drive.google.com/thumbnail?id=1kS33uoFHlV8WGhK3QShSGobuF1rosEOU&sz=s4000",
        "https://drive.google.com/thumbnail?id=1lCaDjduJqQ9ZGw6UW8VM4Jv_1PNTt6vf&sz=s4000",
        "https://drive.google.com/thumbnail?id=1mqBwDjpqcfFKa7DwX2KvccyMBBokG1Tq&sz=s4000",
        "https://drive.google.com/thumbnail?id=1nIzAuDqLcw2ZSON7ULc8elr6momd2Zv5&sz=s4000",
        "https://drive.google.com/thumbnail?id=1nkw6eFelGWGAIhRvxlWFbxXbCjjZGkWB&sz=s4000",
        "https://drive.google.com/thumbnail?id=1o2tFzN_2HjZ2k82InFqqiMyHfjtk302-&sz=s4000",
        "https://drive.google.com/thumbnail?id=1pJN8G7a68GypBv1ujh5A46b7cSkSsPB6&sz=s4000",
        "https://drive.google.com/thumbnail?id=1qOH4eKvdtELrxzmxp8DE9d_FkLHu8lyK&sz=s4000",
        "https://drive.google.com/thumbnail?id=1rBzeqcyrLmBmV11i0y-DDOTbFmpEx0LB&sz=s4000",
        "https://drive.google.com/thumbnail?id=1s6_Id8M5QKQ7fEWjnkWVS-s0_qONLnLb&sz=s4000",
        "https://drive.google.com/thumbnail?id=1skQH791kQbe3qH2Vwuc36G2FYrZ0r1yy&sz=s4000",
        "https://drive.google.com/thumbnail?id=1tKiVm2yj-JhemME_M7MJHrymSQUNiykL&sz=s4000",
        "https://drive.google.com/thumbnail?id=1tVYWihkPsKRPWNAyRgPNVgGxl7Bd-dVe&sz=s4000",
        "https://drive.google.com/thumbnail?id=1u17FcnCkcLqWoxq5zwZX_N0uJsLy7l9r&sz=s4000",
        "https://drive.google.com/thumbnail?id=1u1ynzKuwf8WGQrD0a2s_9ZP73FVHs0z7&sz=s4000",
        "https://drive.google.com/thumbnail?id=1vkwrF1i-ERdb7dbTzrVCyxAQ7iXQLBbt&sz=s4000",
        "https://drive.google.com/thumbnail?id=1wUrstFcTrkASBCWZ3r3fwgRcULhb4Bl6&sz=s4000",
        "https://drive.google.com/thumbnail?id=1w_61iagleOxUd50aLW8Sdn5Jqxr9JD2h&sz=s4000",
        "https://drive.google.com/thumbnail?id=1w_nD94qUCZ6jGCI4YPzuwCyZJXwhbllK&sz=s4000",
        "https://drive.google.com/thumbnail?id=1xMD__68R7IUTsP66_Um8Pnl7H2hiZCFV&sz=s4000",
        "https://drive.google.com/thumbnail?id=1xbbJ8xhBDt4K14ce1kgea59Mpo8Ff-LC&sz=s4000",
        "https://drive.google.com/thumbnail?id=1y9YFn7twpXRr_2oLmAKO4XlhDGPYFhaJ&sz=s4000",
        "https://drive.google.com/thumbnail?id=1ybO5SsUUkUDIgobH-iCtqwR0gYNCUDJE&sz=s4000",
        "https://drive.google.com/thumbnail?id=1z_B5dcWamcNMmCCHPxLr0fjzAdoUZEwZ&sz=s4000",
        "https://drive.google.com/thumbnail?id=1A6PM6Gnj3zR_HA5FXPM-lbsM0-icsIPw&sz=s4000",
        "https://drive.google.com/thumbnail?id=1gdNVlTLjJzIRJxXFhoPw50PSKj_374mB&sz=s4000",
        "https://drive.google.com/thumbnail?id=1naCIbMdOmake8CKlB1Q9y-llHxOm7Waa&sz=s4000",
        "https://drive.google.com/thumbnail?id=1tJViL-fIHvlzf-E9DV1uK-stMfgeJgnh&sz=s4000",
        "https://drive.google.com/thumbnail?id=1uyfTdvzEHt_zY7HS6zz65UTasROChC9q&sz=s4000",
    ]

    # Directorio donde está el script
    script_dir = Path(__file__).resolve().parent
    # Carpeta de imágenes un nivel arriba: ../img
    images_dir = (script_dir.parent / folder_name).resolve()

    if not images_dir.exists():
        return []

    decorative_images: list = []

    # Caminamos solo esta carpeta (no recursivo; si quieres recursivo usa rglob)
    for path in images_dir.iterdir():
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            # Queremos la ruta relativa al cwd actual:
            try:
                rel_path = path.relative_to(Path.cwd())
            except ValueError:
                # Si no es subruta del cwd, construimos una ruta relativa manualmente
                rel_path = os.path.relpath(path, Path.cwd())
            decorative_images.append(str(rel_path))

    return decorative_images


# Poblar lista global con rutas relativas
DECORATIVE_IMAGES = load_decorative_images_from_parent("img")


# DECORATIVE_IMAGES = [
#     # Cambia estas URLs por tu propio repositorio o carpeta
#     "https://source.unsplash.com/featured/800x600?team,work",
#     "https://juan-alvarado-uk.github.io/UAM/img/3912976.jpg"
# ]


class MarkdownToRevealJS:
    def __init__(
            self,
            max_sentences_per_slide: int = 4,
            max_table_rows: int = 8,
            debug: bool = False,
            use_images: bool = True,
    ):
        self.max_sentences_per_slide = max_sentences_per_slide
        self.max_table_rows = max_table_rows
        self.debug = debug
        self.use_images = use_images

        self.current_h1 = ""
        self.current_h2 = ""
        self.current_h3 = ""
        self.slides: List[Dict[str, Any]] = []

        self.in_code_block = False
        self.code_block_language = ""
        self.current_block_lines: List[str] = []
        self.in_table = False
        self.current_table_lines: List[str] = []

        self.current_text_buffer: List[str] = []

    # ===================== PARSEO LINEA A LINEA =====================

    def parse_markdown(self, content: str) -> List[dict]:
        lines = content.split("\n")
        if self.debug:
            print(f"Total de líneas a procesar: {len(lines)}")

        i = 0
        while i < len(lines):
            line = lines[i]

            # Bloques de código
            if line.strip().startswith("```"):
                self._handle_code_fence(line)
                i += 1
                continue

            if self.in_code_block:
                self.current_block_lines.append(line)
                i += 1
                continue

            # Tablas
            if self._is_table_line(line):
                self._handle_table_line(line)
                i += 1
                continue
            else:
                if self.in_table:
                    self._flush_table()
                    # seguimos procesando esta línea como texto normal

            # NUEVO: separadores manuales de slide (--- o *** en una línea)
            if re.match(r'^\s*(---|\*\*\*)\s*$', line):
                # Vaciar cualquier texto acumulado en slides
                self._flush_text_buffer()
                # Avanzar a la siguiente línea y seguir
                i += 1
                continue

            # Encabezados
            heading_match = re.match(r"^(#{1,3})\s+(.+)$", line)
            if heading_match:
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()

                # Antes de cambiar de título, vaciar texto pendiente
                self._flush_text_buffer()

                if level == 1:
                    self.current_h1 = title
                    self.current_h2 = ""
                    self.current_h3 = ""
                    self._add_title_slide(title)
                elif level == 2:
                    self.current_h2 = title
                    self.current_h3 = ""
                elif level == 3:
                    self.current_h3 = title

                if self.debug:
                    print(f"[Línea {i}] Encabezado H{level}: {title}")

                i += 1
                continue

            # Línea normal
            if line.strip():
                self.current_text_buffer.append(line)
            else:
                self.current_text_buffer.append("")
            i += 1

        # Fin del archivo
        if self.in_code_block:
            self.current_block_lines.append("```")
            self._flush_code_block()

        if self.in_table:
            self._flush_table()

        self._flush_text_buffer()

        if self.debug:
            print("\n=== RESUMEN ===")
            print(f"Total de diapositivas generadas: {len(self.slides)}")
            for idx, slide in enumerate(self.slides, 1):
                print(f"  {idx}: {slide['type']} - {slide['title']}")

        return self.slides

    # ===================== MANEJO DE CÓDIGO, TABLAS, TEXTO =====================

    def _handle_code_fence(self, line: str):
        fence = line.strip()[3:].strip()
        if not self.in_code_block:
            # Inicio
            self._flush_text_buffer()
            self.in_code_block = True
            self.code_block_language = fence
            self.current_block_lines = []
        else:
            # Fin
            self.in_code_block = False
            self._flush_code_block()

    def _flush_code_block(self):
        if not self.current_block_lines:
            return
        slide = {
            "type": "content",
            "title": self._current_title(),
            "content_blocks": [
                {"kind": "code", "language": self.code_block_language, "lines": self.current_block_lines}
            ],
            # Sin imágenes en slides de código
            "image": None,
            "image_side": None,
        }
        self.slides.append(slide)
        self.current_block_lines = []
        self.code_block_language = ""

    def _is_table_line(self, line: str) -> bool:
        return line.strip().startswith("|") and "|" in line.strip()[1:]

    def _handle_table_line(self, line: str):
        if not self.in_table:
            self._flush_text_buffer()
            self.in_table = True
            self.current_table_lines = []
        self.current_table_lines.append(line)

    def _flush_table(self):
        if not self.current_table_lines:
            self.in_table = False
            return

        header_line = None
        separator_line = None
        data_rows: List[str] = []

        for ln in self.current_table_lines:
            if not ln.strip():
                continue
            if header_line is None:
                header_line = ln
            elif separator_line is None and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]+\|?\s*$", ln):
                separator_line = ln
            else:
                data_rows.append(ln)

        if not header_line or not separator_line:
            # No es tabla válida: lo tratamos como texto normal
            self.current_text_buffer.extend(self.current_table_lines)
            self.current_table_lines = []
            self.in_table = False
            return

        for i in range(0, len(data_rows), self.max_table_rows):
            chunk = data_rows[i: i + self.max_table_rows]
            table_lines = [header_line, separator_line] + chunk
            slide = {
                "type": "content",
                "title": self._current_title(),
                "content_blocks": [
                    {"kind": "table", "lines": table_lines}
                ],
                # Sin imágenes en slides de tabla
                "image": None,
                "image_side": None,
            }
            self.slides.append(slide)

        self.current_table_lines = []
        self.in_table = False

    def _flush_text_buffer(self):
        """
        Convierte el buffer de texto en slides mezclando párrafos y listas,
        respetando límites de caracteres y número de ítems de lista por slide.
        """
        if not self.current_text_buffer or not any(l.strip() for l in self.current_text_buffer):
            self.current_text_buffer = []
            return

        blocks = self._split_text_buffer_into_blocks()

        max_chars_per_slide = 300  # límite visual aproximado
        max_list_items_per_slide = 9

        # Estado acumulado de la slide actual
        current_blocks: List[Dict[str, Any]] = []
        current_chars = 0
        current_list_items_count = 0

        def append_content_slide(content_blocks: List[Dict[str, Any]]):
            img = self._pick_image()
            side = random.choice(["left", "right"]) if img else None
            self.slides.append({
                "type": "content",
                "title": self._current_title(),
                "content_blocks": content_blocks,
                "image": img,
                "image_side": side,
            })

        def flush_slide():
            nonlocal current_blocks, current_chars, current_list_items_count
            if not current_blocks:
                return
            append_content_slide(current_blocks)
            current_blocks = []
            current_chars = 0
            current_list_items_count = 0

        for block in blocks:
            kind = block["kind"]

            if kind == "paragraph":
                paragraph = self._join_lines_to_paragraph(block["lines"])
                sentences = self._split_into_sentences(paragraph)

                for sent in sentences:
                    if not isinstance(sent, str):
                        continue
                    s = sent.strip()
                    if not s:
                        continue
                    s_len = len(s)

                    if s_len > max_chars_per_slide:
                        flush_slide()
                        current_blocks.append({"kind": "text", "sentences": [s]})
                        flush_slide()
                        continue

                    if current_chars + (1 if current_chars > 0 else 0) + s_len > max_chars_per_slide:
                        flush_slide()

                    if current_blocks and current_blocks[-1]["kind"] == "text":
                        current_blocks[-1]["sentences"].append(s)
                    else:
                        current_blocks.append({"kind": "text", "sentences": [s]})
                    current_chars += (1 if current_chars > 0 else 0) + s_len

            elif kind == "list":
                list_size = self._count_list_text_chars(block)
                list_items = self._count_list_items(block)

                if current_blocks and (
                        current_list_items_count + list_items > max_list_items_per_slide or
                        current_chars + (1 if current_chars > 0 else 0) + list_size > max_chars_per_slide
                ):
                    flush_slide()

                if list_items <= max_list_items_per_slide and list_size <= max_chars_per_slide:
                    current_blocks.append(block)
                    current_chars += (1 if current_chars > 0 else 0) + list_size
                    current_list_items_count += list_items
                else:
                    flush_slide()
                    for split_block in self._split_list_block_for_slides(
                            block,
                            max_items=max_list_items_per_slide,
                            max_chars=max_chars_per_slide,
                    ):
                        append_content_slide([split_block])

        flush_slide()
        self.current_text_buffer = []

    def _add_list_slide(self, items: List[str], ordered: bool):
        img = self._pick_image()
        side = None
        if img:
            side = random.choice(["left", "right"])
        slide = {
            "type": "content",
            "title": self._current_title(),
            "content_blocks": [
                {"kind": "list", "ordered": ordered, "items": items}
            ],
            "image": img,
            "image_side": side,
        }
        self.slides.append(slide)

    # ===================== UTILIDADES DE TEXTO =====================

    def _join_lines_to_paragraph(self, lines: List[str]) -> str:
        parts: List[str] = []
        current_paragraph: List[str] = []

        for ln in lines:
            if ln.strip():
                current_paragraph.append(ln.strip())
            else:
                if current_paragraph:
                    parts.append(" ".join(current_paragraph))
                    current_paragraph = []
        if current_paragraph:
            parts.append(" ".join(current_paragraph))

        return "\n\n".join(parts)

    def _split_into_sentences(self, text: str) -> List[str]:
        if not text.strip():
            return []

        paragraphs = text.split("\n\n")
        sentences: List[str] = []

        # Explicación:
        # (?<!(\d)) asegura que justo antes del punto NO haya un dígito.
        # Es decir, no corta en "1. Texto", pero sí en "Texto final."
        sentence_re = re.compile(r"(?<!(\d))(?<=[\.!?])\s+")
        # sentence_re = re.compile(r"(?<=[\.!?])\s+")

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            parts = sentence_re.split(para)
            # Filtrar y asegurar que todo sea str no vacío
            for p in parts:
                if isinstance(p, str) and p.strip():
                    sentences.append(p.strip())
            # sentences.extend(parts)

        return sentences

    def _split_text_buffer_into_blocks(self) -> List[Dict[str, Any]]:
        """
        Separa self.current_text_buffer en bloques:
        - {"kind": "list", "ordered": bool, "items": [item, ...]}
          donde item = {"text": str, "children": [list_block, ...]}
        - {"kind": "paragraph", "lines": [str, ...]}
        """
        lines = self.current_text_buffer
        blocks: List[Dict[str, Any]] = []

        numbered_re = re.compile(r"^(\s*)(\d+)\.\s+(.*)$")
        bullet_re = re.compile(r"^(\s*)[-*+]\s+(.*)$")

        current_para: List[str] = []
        root_list = None
        list_stack: List[Dict[str, Any]] = []

        def normalize_indent(ws: str) -> int:
            return len(ws.replace("\t", "    "))

        def flush_para():
            nonlocal current_para
            if current_para and any(l.strip() for l in current_para):
                blocks.append({"kind": "paragraph", "lines": current_para[:]})
            current_para = []

        def flush_list_tree():
            nonlocal root_list, list_stack
            if root_list:
                cleaned = self._normalize_list_block(root_list)
                if cleaned and cleaned.get("items"):
                    blocks.append(cleaned)
            root_list = None
            list_stack = []

        def ensure_list_container(indent: int, ordered: bool) -> Dict[str, Any]:
            nonlocal root_list, list_stack

            while list_stack and indent < list_stack[-1]["indent"]:
                list_stack.pop()

            if not list_stack:
                root_list = {
                    "kind": "list",
                    "ordered": ordered,
                    "indent": indent,
                    "items": []
                }
                list_stack.append(root_list)
                return root_list

            top = list_stack[-1]

            if indent > top["indent"]:
                parent_items = top["items"]
                if not parent_items:
                    parent_items.append({"text": "", "children": []})
                last_item = parent_items[-1]
                child_list = {
                    "kind": "list",
                    "ordered": ordered,
                    "indent": indent,
                    "items": []
                }
                last_item.setdefault("children", []).append(child_list)
                list_stack.append(child_list)
                return child_list

            if indent == top["indent"]:
                if top["ordered"] != ordered:
                    list_stack.pop()
                    return ensure_list_container(indent, ordered)
                return top

            top = list_stack[-1]
            if top["ordered"] != ordered:
                list_stack.pop()
                return ensure_list_container(indent, ordered)
            return top

        for ln in lines:
            if not ln.strip():
                flush_para()
                flush_list_tree()
                continue

            m_num = numbered_re.match(ln)
            m_bul = bullet_re.match(ln)

            if m_num:
                flush_para()
                indent = normalize_indent(m_num.group(1))
                text = m_num.group(3).strip()
                target = ensure_list_container(indent, True)
                target["items"].append({
                    "text": text,
                    "children": []
                })
            elif m_bul:
                flush_para()
                indent = normalize_indent(m_bul.group(1))
                text = m_bul.group(2).strip()
                target = ensure_list_container(indent, False)
                target["items"].append({
                    "text": text,
                    "children": []
                })
            else:
                flush_list_tree()
                current_para.append(ln)

        flush_para()
        flush_list_tree()

        return blocks

    def _normalize_list_block(self, block: Dict[str, Any]) -> Dict[str, Any]:
        normalized_items = []
        for item in block.get("items", []):
            text = item.get("text", "").strip()
            children = [
                self._normalize_list_block(child)
                for child in item.get("children", [])
                if child
            ]
            children = [child for child in children if child.get("items")]
            if text or children:
                normalized_items.append({
                    "text": text,
                    "children": children
                })
        return {
            "kind": "list",
            "ordered": block.get("ordered", False),
            "items": normalized_items
        }

    def _count_list_items(self, block: Dict[str, Any]) -> int:
        total = 0
        for item in block.get("items", []):
            total += 1
            for child in item.get("children", []):
                total += self._count_list_items(child)
        return total

    def _count_list_text_chars(self, block: Dict[str, Any]) -> int:
        total = 0
        for item in block.get("items", []):
            total += len(item.get("text", "").strip())
            for child in item.get("children", []):
                total += self._count_list_text_chars(child)
        return total

    def _clone_list_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "text": item.get("text", ""),
            "children": [self._clone_list_block(child) for child in item.get("children", [])]
        }

    def _clone_list_block(self, block: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "kind": "list",
            "ordered": block.get("ordered", False),
            "items": [self._clone_list_item(item) for item in block.get("items", [])]
        }

    def _split_list_block_for_slides(self, block: Dict[str, Any], max_items: int, max_chars: int) -> List[
        Dict[str, Any]]:
        items = block.get("items", [])
        if not items:
            return []

        chunks: List[Dict[str, Any]] = []
        current_items: List[Dict[str, Any]] = []
        current_chars = 0
        current_count = 0
        start_number = 1
        current_start = 1

        for idx, item in enumerate(items, start=1):
            cloned = self._clone_list_item(item)
            item_chars = len(cloned.get("text", "").strip())
            for child in cloned.get("children", []):
                item_chars += self._count_list_text_chars(child)
            item_count = 1
            for child in cloned.get("children", []):
                item_count += self._count_list_items(child)

            if current_items and (current_count + item_count > max_items or current_chars + item_chars > max_chars):
                chunk = {
                    "kind": "list",
                    "ordered": block.get("ordered", False),
                    "items": current_items,
                }
                if chunk["ordered"]:
                    chunk["start"] = current_start
                chunks.append(chunk)
                current_items = []
                current_chars = 0
                current_count = 0
                current_start = idx

            current_items.append(cloned)
            current_chars += item_chars
            current_count += item_count
            start_number = idx + 1

        if current_items:
            chunk = {
                "kind": "list",
                "ordered": block.get("ordered", False),
                "items": current_items,
            }
            if chunk["ordered"]:
                chunk["start"] = current_start
            chunks.append(chunk)

        return chunks

    # ===================== CREACIÓN DE SLIDES =====================

    def _current_title(self) -> str:
        return self.current_h3 or self.current_h2 or self.current_h1 or "Sin título"

    def _add_title_slide(self, title: str):
        self.slides.append({
            "type": "title",
            "title": title,
            "image": None,
            "image_side": None,
        })

    def _add_text_slide(self, sentences: List[str]):
        img = self._pick_image()
        side = None
        if img:
            side = random.choice(["left", "right"])
        slide = {
            "type": "content",
            "title": self._current_title(),
            "content_blocks": [
                {"kind": "text", "sentences": sentences}
            ],
            "image": img,
            "image_side": side,
        }
        self.slides.append(slide)

    def _pick_image(self):
        if not self.use_images or not DECORATIVE_IMAGES:
            return None
        return random.choice(DECORATIVE_IMAGES)

    # ===================== HTML =====================

    def generate_html(self, theme: str = "solarized") -> str:
        slide_html_parts: List[str] = []

        for slide in self.slides:
            if slide["type"] == "title":
                slide_html_parts.append(self._render_title_slide(slide))
            elif slide["type"] == "cover":
                slide_html_parts.append(self._render_full_image_slide(slide, kind="cover"))
            elif slide["type"] == "closing":
                slide_html_parts.append(self._render_full_image_slide(slide, kind="closing"))
            else:
                slide_html_parts.append(self._render_content_slide(slide))

        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Presentación</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/{theme}.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/monokai.css">
    <style>

        /* Usar más ancho de pantalla */
        .reveal .slides {{
            width: 95%;
            margin: 0 auto;
        }}
        .reveal section {{
            padding: 0.5em 0.5em;
            text-align: left;
        }}
        .reveal section h1,
        .reveal section h2,
        .reveal section h3,
        .reveal section p,
        .reveal section li,
        .reveal section ol,
        .reveal section ul,
        .reveal section div {{
            text-align: left;
        }}

        /* Slides de portada/cierre con imagen casi a pantalla completa */
        .full-image-slide {{
            text-align: center;
        }}
        .full-image-slide .full-slide-image {{
            max-width: 100%;
            max-height: 90vh;
            width: 100%;
            height: auto;
            object-fit: contain; /* o 'cover' si prefieres recorte estilizado */
            border-radius: 12px;
        }}
        .full-image-slide h1,
        .full-image-slide h2 {{
            position: absolute;
            bottom: 5%;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            text-shadow: 0 0 10px rgba(0,0,0,0.8);
        }}

        /* Layout dos columnas cuando hay imagen */
      .slide-two-col {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
        gap: 1.5rem;
        align-items: start;
        width: 100%;
        box-sizing: border-box;
      }}

      .slide-two-col .text-col {{
        font-size: 0.9em;
        text-align: left !important;
        align-self: start;
        justify-self: stretch;
        max-height: 100%;
        overflow: auto;
      }}

      .text-col {{
        text-align: left !important;
        width: 100%;
      }}

      .slide-two-col .image-col {{
        display: flex;
        align-items: center;   /* centrar verticalmente la imagen dentro de su mitad */
        justify-content: center;
        max-height: 100%;
        box-sizing: border-box;
      }}

      .slide-two-col .image-col img {{
        /* que NUNCA exceda la mitad de la slide ni en ancho ni en alto */
        max-width: 100%;
        max-height: 100%;
        width: auto;
        height: auto;
        object-fit: contain;
        border-radius: 8px;
        /* quitar márgenes globales de reveal en imágenes dentro de este layout */
        margin: 0 !important;
      }}

      /* Opcional: limitar cualquier imagen genérica de reveal aún más */
      .reveal section img {{
        max-width: 100%;
        max-height: 100%;
      }}

        /* Ajuste general */
        .reveal table {{
            font-size: 0.7em;
            border-collapse: collapse;
            width: 100%;
            margin-top: 0.5em;
        }}
        .reveal table th,
        .reveal table td {{
            border: 1px solid #ddd;
            padding: 0.3em 0.5em;
        }}
        .reveal table th {{
            background-color: rgba(100,100,100,0.2);
        }}
        .reveal pre {{
            font-size: 0.6em;
            text-align: left;
        }}
    </style>
</head>
<body>
<div class="reveal">
    <div>
      <img src="https://drive.google.com/thumbnail?id=1Uj4iU7mPDXGuy91UEBl6ivpz1l_oS9Dk&sz=s4000"  width = "100" alt="Logo">
    </div>
  <div class="slides">
{chr(10).join(slide_html_parts)}
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/notes/notes.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/math/math.js"></script>
<script>
  Reveal.initialize({{
    hash: true,
    slideNumber: true,
    transition: 'slide',
    margin: 0.10,
    width: 1280,
    height: 720,
    plugins: [ RevealHighlight, RevealNotes, RevealMath.KaTeX ]
  }});
</script>
</body>
</html>"""
        return html

    def _render_title_slide(self, slide: Dict[str, Any]) -> str:
        title = self._escape_html(slide["title"])
        return f"""    <section>
      <h1>{title}</h1>
    </section>"""

    def _render_full_image_slide(self, slide: Dict[str, Any], kind: str = "cover") -> str:
        img = slide.get("image")
        if not img:
            return '    <section></section>'
        title_overlay = ""
        if kind == "cover":
            # Si quieres poner un título general aquí, puedes hacerlo:
            # title_overlay = '<h1>Integración de Sistemas</h1>'
            title_overlay = ""
            full_src = "https://drive.google.com/thumbnail?id=1ZDN6IQnMFUPReow1lgaWOqs2Li6z1cXe&sz=s4000"
        elif kind == "closing":
            title_overlay = '<h2>Gracias</h2>'
            full_src = "https://drive.google.com/thumbnail?id=1COyl09OXvJDnmEoddkLLaEQsoMTYz5Ub&sz=s4000"

        img_html = f'<img class="full-slide-image" src="{full_src}" alt="slide image" />'

        return f"""    <section class="full-image-slide">
              {img_html}
              {title_overlay}
            </section>"""

    def _render_content_slide(self, slide: Dict[str, Any]) -> str:
        """Genera HTML para una diapositiva de contenido (texto, listas, código, tablas, imagen)."""
        title = self._escape_html(slide["title"])
        blocks_html: List[str] = []

        # Slides con imagen decorativa → layout dos columnas
        if slide.get("image") and slide.get("image_side") in ("left", "right"):
            full_src = slide["image"]
            img_html = f'<img src="{full_src}" alt="image" />'
            text_html = self._render_blocks_as_text(slide.get("content_blocks", []))

            if slide["image_side"] == "left":
                left = f'<div class="image-col">{img_html}</div>'
                right = f'<div class="text-col">{text_html}</div>'
            else:
                left = f'<div class="text-col">{text_html}</div>'
                right = f'<div class="image-col">{img_html}</div>'

            body = f"""      <div class="slide-two-col">
        {left}
        {right}
      </div>"""
        else:
            # Sin imagen decorativa: todo el contenido ocupa el ancho
            body = self._render_blocks_fullwidth(slide.get("content_blocks", []))

        return f"""    <section>
      <h2>{title}</h2>
{body}
    </section>"""

    def _render_blocks_fullwidth(self, blocks: List[Dict[str, Any]]) -> str:
        """Renderiza todos los tipos de bloques ocupando el ancho completo de la slide."""
        parts: List[str] = []
        for block in blocks:
            kind = block["kind"]

            if kind == "text":
                paragraphs = "".join(
                    f"<p>{self._process_inline_markdown(s)}</p>"
                    for s in block["sentences"]
                )
                parts.append(f"""      <div class="text-col">
{paragraphs}
      </div>""")

            elif kind == "list":
                parts.append(f"""      <div class="text-col">
{self._render_nested_list(block)}
      </div>""")

            elif kind == "code":
                code = "\n".join(block["lines"])
                code = self._escape_html(code)
                lang_class = f"language-{block['language']}" if block["language"] else ""
                parts.append(
                    f"""      <pre><code class="{lang_class}">{code}</code></pre>"""
                )

            elif kind == "table":
                parts.append(self._render_table(block["lines"]))

        return "\n".join(parts)

    def _render_blocks_as_text(self, blocks: List[Dict[str, Any]]) -> str:
        """Renderiza solo bloques de texto y listas como HTML (para la columna de texto)."""
        parts: List[str] = []
        for block in blocks:
            kind = block["kind"]
            if kind == "text":
                paragraphs = "".join(
                    f"<p>{self._process_inline_markdown(s)}</p>"
                    for s in block["sentences"]
                )
                parts.append(paragraphs)
            elif kind == "list":
                parts.append(self._render_nested_list(block))
        return "\n".join(parts)

    def _render_nested_list(self, block: Dict[str, Any]) -> str:
        tag = "ol" if block.get("ordered") else "ul"
        attrs = ""
        if tag == "ol" and block.get("start", 1) not in (None, 1):
            attrs = f' start="{int(block["start"])}"'
        parts = [f"<{tag}{attrs}>"]
        for item in block.get("items", []):
            item_text = self._process_inline_markdown(item.get("text", ""))
            parts.append(f"<li>{item_text}")
            for child in item.get("children", []):
                parts.append(self._render_nested_list(child))
            parts.append("</li>")
        parts.append(f"</{tag}>")
        return "".join(parts)

    def _render_table(self, lines: List[str]) -> str:
        if not lines:
            return ""
        header = [c.strip() for c in lines[0].split("|")[1:-1]]
        rows = []
        for ln in lines[2:]:
            cells = [c.strip() for c in ln.split("|")[1:-1]]
            rows.append(cells)

        thead = "".join(f"<th>{self._escape_html(h)}</th>" for h in header)
        body_rows = []
        for r in rows:
            tds = "".join(f"<td>{self._escape_html(c)}</td>" for c in r)
            body_rows.append(f"<tr>{tds}</tr>")

        return f"""      <table>
        <thead><tr>{thead}</tr></thead>
        <tbody>
          {chr(10).join(body_rows)}
        </tbody>
      </table>"""

    def _process_inline_markdown(self, text: str) -> str:
        """Aplica formato inline básico de Markdown (negritas, itálicas, código, enlaces e imágenes)."""
        text = self._escape_html(text)
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
        text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
        # text = re.sub(r'_([^_]+)_', r'<em>\1</em>', text)
        text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" />', text)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        return text

    def _escape_html(self, text: str) -> str:
        return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))

    # ===================== SLIDES ESPECIALES (PORTADA / CIERRE) =====================
    def _add_cover_slide(self, image: str):
        """Diapositiva de portada con imagen a pantalla casi completa."""
        self.slides.insert(0, {
            "type": "cover",
            "title": "",
            "image": image,
        })

    def _add_closing_slide(self, image: str):
        """Diapositiva final de cierre con imagen a pantalla casi completa."""
        self.slides.append({
            "type": "closing",
            "title": "",
            "image": image,
        })


# ===================== CLI =====================

def main():
    # El siguiente comando se ejecuta desde el directorio de md_to_revealjs.py
    # python md_to_revealjs.py ../src/IntegracionSistemas/Clases/04_SOAP_REST/slides/02_Analisis_diseno.md -o ../slides/integracion/04_02_Analisis_diseno.html -t solarized
    # el anterior es la forma standar para convertir l entrada en src en el reveal en slides
    parser = argparse.ArgumentParser(description="Convierte Markdown a Reveal.js")
    parser.add_argument("input", help="Archivo Markdown de entrada")
    parser.add_argument("-o", "--output", default=None,
                        help="Archivo HTML de salida")
    parser.add_argument("-t", "--theme", default="solarized",
                        help="Tema Reveal.js (black, white, league, beige, sky, night, serif, simple, solarized)")
    parser.add_argument("-s", "--sentences", type=int, default=1,
                        help="Máximo de frases por slide de texto (por defecto: 4)")
    parser.add_argument("-r", "--rows", type=int, default=8,
                        help="Máximo de filas de tabla por slide (por defecto: 8)")
    parser.add_argument("--no-images", action="store_true",
                        help="No insertar imágenes decorativas")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Modo debug")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: no existe {args.input}")
        return

    markdown = input_path.read_text(encoding="utf-8")

    converter = MarkdownToRevealJS(
        max_sentences_per_slide=args.sentences,
        max_table_rows=args.rows,
        debug=args.debug,
        use_images=not args.no_images,
    )
    converter.parse_markdown(markdown)

    # Elegir imágenes para portada y cierre (pueden ser fijas o aleatorias)
    cover_img = None
    closing_img = None
    if not args.no_images:  #and DECORATIVE_IMAGES:
        cover_img = "../logos/cua_05.jpg"  # random.choice(DECORATIVE_IMAGES)
        closing_img = "../logos/cua_01.jpg"  # random.choice(DECORATIVE_IMAGES)

    if cover_img:
        converter._add_cover_slide(cover_img)
    if closing_img:
        converter._add_closing_slide(closing_img)

    html = converter.generate_html(theme=args.theme)

    if args.output is None:
        output_path = input_path.parent / f"{input_path.stem}.html"
    else:
        output_path = Path(args.output)

    output_path.write_text(html, encoding="utf-8")

    print(f"✓ Presentación generada en {output_path}")
    print(f"  - Diapositivas: {len(converter.slides)}")


if __name__ == "__main__":
    main()
