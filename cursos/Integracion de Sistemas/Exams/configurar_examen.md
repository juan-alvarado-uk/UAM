<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# como instalar sublime en mx linux?

En MX Linux (basado en Debian) lo más limpio es usar el repositorio oficial de Sublime Text.

### 1. Añadir la llave GPG

Abre una terminal y ejecuta:

```bash
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

Esto agrega la llave del repositorio de Sublime Text para que APT lo considere confiable.[^1_1][^1_2][^1_3]

### 2. Asegurar soporte para HTTPS en APT

```bash
sudo apt install apt-transport-https
```

Este paquete permite que APT use repositorios sobre HTTPS.[^1_3][^1_1]

### 3. Agregar el repositorio estable de Sublime

```bash
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

Esto registra el canal estable de Sublime Text en tu sistema.[^1_2][^1_1][^1_3]

### 4. Actualizar e instalar

```bash
sudo apt update
sudo apt install sublime-text
```

Con esto se descarga e instala Sublime Text desde el repositorio oficial.[^1_1][^1_2][^1_3]

### 5. Ejecutar Sublime

Luego podrás abrirlo desde el menú de MX Linux (programación / desarrollo) o con:

```bash
subl
```

en la terminal.[^1_2]
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_4][^1_5][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://www.linuxmadesimple.info/2023/05/how-to-install-sublime-text-on-mx-linux.html

[^1_2]: https://www.linuxeros.org/2021/09/como-instalar-sublime-text-en-debian-11-bullseye.html

[^1_3]: https://www.youtube.com/watch?v=4zc0dxkKPlU

[^1_4]: https://translate.google.com/translate?u=https%3A%2F%2Fwww.sublimetext.com%2Fdocs%2Flinux_repositories.html\&hl=es\&sl=en\&tl=es\&client=srp

[^1_5]: https://www.youtube.com/watch?v=RXlm83cpIvA

[^1_6]: https://proyectotictac.com/2022/07/04/vlog-como-instalar-sublime-text-3-linux-mx-milagros-mundo-mancilla/

[^1_7]: https://noticias.compudemano.com/discusion/sublime-text-4-como-instalarlo-en-gnu-linux-basados-en-debian-y-mx.333243/

[^1_8]: https://www.youtube.com/watch?v=z7Fz7bn_bcc

[^1_9]: https://ubuntuhandbook.org/index.php/2022/05/install-sublime-text-ubuntu-22-04/

[^1_10]: https://www.sublimetext.com/docs/linux_repositories.html

[^1_11]: https://devcamp.com/trails/40/campsites/271/guides/how-to-install-work-sublime-text-linux-2f296dd4-601c-4c34-ad60-ae638bdbb032

[^1_12]: https://www.geeksforgeeks.org/linux-unix/install-sublime-text-editor-debian/

[^1_13]: https://jan.krutisch.de/en/2024/03/04/sublime-text-on-ubuntu-the-right-way.html

[^1_14]: https://blog.desdelinux.net/it/testo-sublime-4/

[^1_15]: https://es.scribd.com/document/629434703/Instalar-Sublime-Text


---

# con el prier comando esto fue lo que salió: sudo: apt-key: command not found

En MX Linux nuevo ya no viene `apt-key`, por eso te sale ese error. Hay que usar el método moderno con keyrings.

En la misma terminal, prueba estos pasos:

### 1. Crear carpeta de keyrings (si no existe)

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

Esto crea el directorio donde guardaremos la llave GPG de Sublime.[^2_1][^2_2]

### 2. Descargar la llave GPG de Sublime

```bash
curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/sublimehq-pub.gpg
```

Con esto guardas la llave en `/etc/apt/keyrings/sublimehq-pub.gpg` para que APT pueda verificar los paquetes.[^2_3][^2_1]

(Si te dice que `curl` no existe, instala antes: `sudo apt install curl gnupg`.)[^2_1]

### 3. Agregar el repositorio estable (formato nuevo)

```bash
echo "deb [signed-by=/etc/apt/keyrings/sublimehq-pub.gpg] https://download.sublimetext.com/ apt/stable/" \
  | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

Esto le dice a APT que use ese repositorio y lo firme con esa llave.[^2_3][^2_1]

### 4. Actualizar e instalar

```bash
sudo apt update
sudo apt install sublime-text
```

Con esto ya deberías tener Sublime Text instalado y aparecerte en el menú, además de poder lanzarlo con `subl` en la terminal.[^2_4][^2_1]

Si te sale algún otro error (por ejemplo de llave o de arquitectura), pégalo tal cual y lo revisamos.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_5][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://www.interserver.net/tips/kb/use-sublime-text-linux-complete-guide/

[^2_2]: https://jan.krutisch.de/en/2024/03/04/sublime-text-on-ubuntu-the-right-way.html

[^2_3]: https://github.com/sublimehq/sublime_text/issues/5278

[^2_4]: https://www.sublimetext.com/docs/linux_repositories.html

[^2_5]: https://forum.sublimetext.com/t/solved-debian-apt-get-download-process-failed-sublime-not-released-yet-for-raspberry-pi/55518

[^2_6]: https://forum.sublimetext.com/t/apt-key-is-deprecated-how-to-install-without-apt-key/62535

[^2_7]: https://forum.sublimetext.com/t/problem-with-install/49804

[^2_8]: https://www.reddit.com/r/Ubuntu/comments/nhr3rn/error_when_installing_sublime_text/

[^2_9]: https://forum.sublimetext.com/t/install-error-on-ubuntu-21-04/58917

[^2_10]: https://www.reddit.com/r/linuxquestions/comments/pz5mip/unable_to_download_sublime/

[^2_11]: https://www.sublimemerge.com/docs/linux_repositories

[^2_12]: https://www.reddit.com/r/SublimeText/comments/akxl8p/sudo_aptget_update_is_not_working_for_sublimetext/

[^2_13]: https://forum.sublimetext.com/t/linux-install-add-the-gpg-key-fingerprint-at-least-on-https-www-sublimetext-com-docs-3-linux-repositories-html/32147

[^2_14]: https://www.reddit.com/r/linuxquestions/comments/5hwp6w/how_to_install_sublime_text_on_linux/


---

# Como instalar Brave?

En MX Linux (Debian‑based) la forma recomendada hoy es usando el repositorio oficial con keyring, similar a lo que hicimos con Sublime.

### 1. Instalar herramientas necesarias

```bash
sudo apt update
sudo apt install curl ca-certificates -y
```

`curl` y los certificados son necesarios para descargar y usar el repo de Brave.[^3_1]

### 2. Importar la llave GPG de Brave

```bash
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg \
  https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
```

Esto guarda la llave en `/usr/share/keyrings/brave-browser-archive-keyring.gpg` para que APT pueda verificar los paquetes de Brave.[^3_2][^3_1]

### 3. Añadir el repositorio estable

```bash
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] \
https://brave-browser-apt-release.s3.brave.com/ stable main" \
| sudo tee /etc/apt/sources.list.d/brave-browser-release.list
```

Con esto agregas el repo estable de Brave que usará esa llave para firmas.[^3_3][^3_2]

### 4. Actualizar e instalar Brave

```bash
sudo apt update
sudo apt install brave-browser
```

Esto instala la versión estable de Brave desde el repositorio oficial y se actualizará junto con el sistema.[^3_4][^3_1]

### 5. Ejecutar Brave

Luego puedes lanzarlo desde el menú (Internet / Web) o vía terminal con:

```bash
brave-browser
```

para abrir el navegador.[^3_1]
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_5][^3_6][^3_7][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://linuxcapable.com/how-to-install-brave-browser-on-ubuntu-linux/

[^3_2]: https://github.com/brave/brave-browser/issues/35657

[^3_3]: https://linuxiac.com/how-to-install-brave-browser-on-linux/

[^3_4]: https://brave.com/linux/

[^3_5]: https://brave.com/es/linux/

[^3_6]: https://www.youtube.com/watch?v=SCM84nUVtok

[^3_7]: https://www.reddit.com/r/brave_browser/comments/c3ci2a/brave_on_mx_linux/

[^3_8]: https://www.youtube.com/watch?v=Jb0nVlUBKsY

[^3_9]: https://www.youtube.com/watch?v=LUddO-hy-zI

[^3_10]: https://itsfoss.com/brave-web-browser/

[^3_11]: https://community.brave.app/t/running-into-errors-when-installing-brave-on-debian-public-key-is-not-available/524631

[^3_12]: https://www.youtube.com/watch?v=sTKFzzrli0w

[^3_13]: https://www.youtube.com/watch?v=WSN59qjd9iE

[^3_14]: https://github.com/brave/brave-browser/issues/48853

[^3_15]: https://www.youtube.com/watch?v=6yonPU1j5Cw


---

# hay alguna forma de automatizar la captura de preguntas en un examen de google classroom, es decir en un google form que va a ser un examen. Además sería bueno que las preguntas no fueran texto, sino imagenes, para evitar copiarlas directamente para pegarlas en algun LLM para obtener las respuestas inmediatamente. yo actualmente tengo las preguntas, las claves de las respuestas y el feedback en texto en archivos md separados. Cómo sería más fácil hacer esta automatización?

Sí, se puede automatizar bastante, pero hay varias piezas: generar las imágenes, subirlas a Drive y crear el Form/quiz (idealmente vía Apps Script + Forms API). Te propongo un flujo que aprovecha que ya tienes todo en Markdown.

***

## Idea general del flujo

1. Convertir tus `.md` a JSON estructurado (pregunta, opciones, clave, feedback).
2. Renderizar cada pregunta a imagen (p. ej. con un script que use pandoc + wkhtmltoimage o un headless browser tipo Puppeteer/Playwright).
3. Subir imágenes a Google Drive (script en Python o Apps Script).
4. Crear el Google Form tipo examen, insertando cada pregunta como imagen y configurando claves/feedback con Apps Script + Forms API.[^4_1][^4_2]
5. Enlazar ese Form como “tarea de cuestionario” en Classroom (que ya lo hace nativo).[^4_3][^4_4]

***

## ¿Se pueden poner preguntas solo como imagen?

Google Forms permite:

- Preguntas de texto con imagen asociada (la imagen se muestra arriba del enunciado).[^4_5][^4_6]
- Opciones de respuesta con imagen (para opción múltiple de imágenes).[^4_6][^4_5]

Esto encaja perfecto con la idea de que el enunciado esté como imagen (aunque técnicamente el campo de texto no se puede “vaciar” del todo, puedes poner un texto mínimo tipo “Pregunta 1”).[^4_7][^4_8]

***

## Automatización técnica recomendada

Dado tu perfil, lo más flexible es:

### 1. Normalizar tus `.md` a un formato intermedio

Ejemplo de JSON por pregunta:

```json
{
  "id": "P01",
  "texto": "Explica brevemente el algoritmo k-NN...",
  "tipo": "opcion_multiple",
  "opciones": [
    "Respuesta A",
    "Respuesta B",
    "Respuesta C",
    "Respuesta D"
  ],
  "correcta": 1,
  "feedback_correcta": "Justificación de la respuesta correcta...",
  "feedback_incorrecta": "Pista / explicación cuando se equivoca..."
}
```

Puedes escribir un script en Python que lea tus `.md` y genere un JSON por examen.

### 2. Generar las imágenes de las preguntas

Opciones:

- Python + headless browser (Playwright/Selenium) que renderice HTML generado desde el JSON y saque screenshots.
- `pandoc` + `wkhtmltoimage` (o `weasyprint`) para pasar de Markdown/HTML a PNG.

Salida: una imagen por pregunta, con nombre alineado a tu ID (`P01.png`, etc.).

### 3. Subir imágenes a Drive programáticamente

- Usar la API de Google Drive desde Python para subir los PNG y guardar los IDs públicos.
- O hacer esta parte con Google Apps Script: subir a una carpeta, y leer desde un script que cree el Form.[^4_2][^4_1]

El objetivo: tener un mapa `id_pregunta -> URL/ID de archivo de Drive`.

### 4. Crear el Form tipo quiz desde script

Con **Google Apps Script + Forms API** puedes:

- Crear un Form vacío y marcarlo como quiz.[^4_1][^4_2]
- Para cada pregunta:
    - Insertar un `ImageItem` con la imagen de Drive (enunciado).[^4_7][^4_1]
    - Insertar la pregunta de opción múltiple / respuesta corta debajo.
    - Configurar la clave, puntos y feedback usando la API de Forms (AnswerKey + feedback).[^4_2][^4_1]

Hay ejemplos completos de creación de quizzes con Apps Script + Forms API que podrías adaptar para leer tu JSON en lugar de hardcodear.[^4_1][^4_2]

### 5. Integración con Classroom

Una vez creado el Form, en Classroom creas una tarea tipo “quiz assignment”: Classroom genera o enlaza el Form y las calificaciones se pueden importar automáticamente.[^4_9][^4_4]

***

## Sobre la protección contra LLMs

- Usar solo imágenes dificulta el copy‑paste, pero no lo impide (pueden usar OCR o extensiones de captura).
- Otras capas que ayudan:
    - Banco grande de preguntas y selección aleatoria por script (Forms API permite barajar y agrupar).[^4_1]
    - Variantes paramétricas de la misma pregunta (tu pipeline de generación podría randomizar números o contextos).
    - Límite de tiempo y “lock mode” en Chromebooks si tu institución lo soporta.[^4_4]

***

## ¿Qué sería “lo más fácil” para ti?

Con tu perfil, diría:

- Mantener el **source of truth en Markdown/JSON** en Git.
- Un pequeño **CLI en Python** que:

1. Parse `.md` → JSON.
2. Genera HTML y screenshots.
3. Sube imágenes a Drive (API).
4. Llama a un Apps Script (o directamente Forms API) para crear/actualizar el Form.

Si quieres, en el siguiente mensaje puedo esbozar una estructura concreta de:

- formato `.md` recomendado,
- esquema JSON,
- y un boceto de Apps Script mínimo que cree un quiz con imágenes y clave/feedback.
<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15]</span>

<div align="center">⁂</div>

[^4_1]: https://developers.google.com/workspace/forms/api/guides/create-form-quiz

[^4_2]: https://gist.github.com/tanaikech/eebcb2d71eed1aab5decff64287bcc9a?permalink_comment_id=4390509

[^4_3]: https://support.google.com/edu/classroom/answer/9095575?hl=id%2F

[^4_4]: https://support.google.com/edu/classroom/answer/9095575?hl=en

[^4_5]: https://support.google.com/a/users/answer/13344425?hl=en

[^4_6]: https://www.youtube.com/watch?v=6YWIw45lkNE

[^4_7]: https://stackoverflow.com/questions/67881474/is-it-possible-to-programmatically-create-a-google-form-with-images-added-to-mul

[^4_8]: https://www.youtube.com/watch?v=Pdt8Vv7-3Xk

[^4_9]: https://stackoverflow.com/questions/64626420/automatically-import-google-forms-quiz-results-to-google-classroom

[^4_10]: https://www.edcafe.ai/blog/how-to-make-a-quiz-in-google-forms

[^4_11]: https://formswrite.com/blog/google-form-import-questions-a-step-by-step-guide

[^4_12]: https://www.youtube.com/watch?v=1y9pxHQRMp0

[^4_13]: https://www.jotform.com/google-forms/how-to-import-questions-into-google-forms/

[^4_14]: https://www.layerpath.com/learn/how-to-import-questions-into-google-forms

[^4_15]: https://www.youtube.com/watch?v=OLhV-t3ExDg


---

# Sí, dame la estructura concreta para el formto .md, el equema json, y un boceto de Apps Script mínimo

Va un diseño concreto pensando en que luego lo proceses con Python y un solo script de Apps Script.

***

## 1. Formato propuesto para cada `.md`

Un archivo `.md` por examen, con bloques por pregunta. Ejemplo:

```markdown
# Examen Unidad 1

::: question
ID: P01
TIPO: opcion_multiple
PUNTOS: 2

ENUNCIADO:
Explica brevemente el algoritmo k-NN y selecciona la opción más adecuada.

OPCIONES:
- Compara un punto con sus k vecinos más cercanos en el espacio de características.
- Entrena una red neuronal profunda para clasificar los datos.
- Ajusta un modelo lineal minimizando el error cuadrático.
- Genera árboles de decisión en forma secuencial.

CORRECTA: 1

FEEDBACK_CORRECTA:
Correcto: k-NN clasifica según la mayoría entre los vecinos más cercanos.

FEEDBACK_INCORRECTA:
Revisa la definición de k-NN: se basa en la distancia a ejemplos de entrenamiento.
:::

::: question
ID: P02
TIPO: verdadero_falso
PUNTOS: 1

ENUNCIADO:
En k-NN, un valor de k muy grande tiende a suavizar demasiado la frontera de decisión.

OPCIONES:
- Verdadero
- Falso

CORRECTA: 1

FEEDBACK_CORRECTA:
Correcto: un k grande reduce el sobreajuste pero puede infraajustar.

FEEDBACK_INCORRECTA:
Piensa en qué pasa cuando cada nueva instancia se clasifica mirando a casi todo el dataset.
:::
```

Notas:

- Marcador `::: question` / `:::` para separar preguntas.
- Campos clave en mayúsculas al inicio de línea (`ID:`, `TIPO:`, etc.) fáciles de parsear.
- `TIPO` restringido a valores que manejarás en el script, p. ej.: `opcion_multiple`, `checkbox`, `verdadero_falso`, `respuesta_corta`.
- `ENUNCIADO`, `OPCIONES`, `FEEDBACK_*` pueden tener varias líneas hasta el siguiente campo o fin de bloque.

***

## 2. Esquema JSON intermedio

A partir del `.md` anterior, un JSON por examen podría ser:

```json
{
  "titulo": "Examen Unidad 1",
  "preguntas": [
    {
      "id": "P01",
      "tipo": "opcion_multiple",
      "puntos": 2,
      "enunciado": "Explica brevemente el algoritmo k-NN y selecciona la opción más adecuada.",
      "opciones": [
        "Compara un punto con sus k vecinos más cercanos en el espacio de características.",
        "Entrena una red neuronal profunda para clasificar los datos.",
        "Ajusta un modelo lineal minimizando el error cuadrático.",
        "Genera árboles de decisión en forma secuencial."
      ],
      "correcta": [^5_1],
      "feedback_correcta": "Correcto: k-NN clasifica según la mayoría entre los vecinos más cercanos.",
      "feedback_incorrecta": "Revisa la definición de k-NN: se basa en la distancia a ejemplos de entrenamiento."
    },
    {
      "id": "P02",
      "tipo": "verdadero_falso",
      "puntos": 1,
      "enunciado": "En k-NN, un valor de k muy grande tiende a suavizar demasiado la frontera de decisión.",
      "opciones": [
        "Verdadero",
        "Falso"
      ],
      "correcta": [^5_1],
      "feedback_correcta": "Correcto: un k grande reduce el sobreajuste pero puede infraajustar.",
      "feedback_incorrecta": "Piensa en qué pasa cuando cada nueva instancia se clasifica mirando a casi todo el dataset."
    }
  ]
}
```

Detalles:

- `correcta` siempre es arreglo de índices base 1 (`[^5_1]`, `[2,3]` para checkbox).
- `tipo` lo usarás para decidir si creas `MultipleChoiceItem` o `CheckboxItem` en Apps Script.
- Puedes añadir campos como `imagenPreguntaId` cuando generes/subas las imágenes a Drive (ID o URL del archivo) para vincularlas al Form.

***

## 3. Boceto mínimo de Apps Script

Este ejemplo asume:

- Ya tienes un archivo JSON en Drive (o puedes pegarlo como string en el script).
- Ya tienes las imágenes subidas a Drive y guardas `imagenPreguntaId` en el JSON.
- Usas solo Apps Script clásico (`FormApp`), sin Forms API REST, para simplificar.[^5_1][^5_2]

```javascript
function crearQuizDesdeJson() {
  // 1. Cargar JSON (ejemplo: desde un archivo en Drive)
  const fileId = 'JSON_FILE_ID_AQUI'; // ID del archivo .json en Drive
  const contenido = DriveApp.getFileById(fileId).getBlob().getDataAsString('UTF-8');
  const examen = JSON.parse(contenido);

  // 2. Crear Form y marcar como quiz
  const form = FormApp.create(examen.titulo || 'Examen sin título');
  form.setIsQuiz(true);
  form.setShuffleQuestions(true);
  form.setProgressBar(true);

  // 3. Recorrer preguntas
  examen.preguntas.forEach((p) => {
    // 3.1. Opcional: añadir imagen de la pregunta si existe
    if (p.imagenPreguntaId) {
      const imgBlob = DriveApp.getFileById(p.imagenPreguntaId).getBlob();
      form.addImageItem()
        .setTitle(p.id) // o vacío, o texto mínimo
        .setImage(imgBlob);
    }

    // 3.2. Crear la pregunta según tipo
    let item;
    if (p.tipo === 'opcion_multiple' || p.tipo === 'verdadero_falso') {
      item = form.addMultipleChoiceItem();
    } else if (p.tipo === 'checkbox') {
      item = form.addCheckboxItem();
    } else if (p.tipo === 'respuesta_corta') {
      item = form.addTextItem();
    } else {
      // tipo no soportado
      return;
    }

    item.setTitle(p.enunciado || p.id)
        .setRequired(true);

    // 3.3. Asignar puntos y opciones + clave (para choice/checkbox)
    if (p.tipo === 'opcion_multiple' || p.tipo === 'verdadero_falso' || p.tipo === 'checkbox') {
      const choices = p.opciones.map((texto, idx) => {
        const esCorrecta = (p.correcta || []).includes(idx + 1);
        return item.createChoice(texto, esCorrecta);
      });
      item.setChoices(choices);
      if (typeof p.puntos === 'number') {
        item.setPoints(p.puntos);
      }
    }

    // Para respuesta corta con autocorrección, Forms API REST da más control,
    // pero aquí dejamos solo puntos si quieres.
    if (p.tipo === 'respuesta_corta' && typeof p.puntos === 'number') {
      item.setPoints(p.puntos);
    }

    // 3.4. Añadir feedback correcta / incorrecta si aplica (choice/checkbox)
    if (p.tipo === 'opcion_multiple' || p.tipo === 'verdadero_falso' || p.tipo === 'checkbox') {
      if (p.feedback_correcta) {
        const fbCorrecta = FormApp.createFeedback()
          .setDisplayText(p.feedback_correcta)
          .build();
        item.setFeedbackForCorrect(fbCorrecta);
      }

      if (p.feedback_incorrecta) {
        const fbIncorrecta = FormApp.createFeedback()
          .setDisplayText(p.feedback_incorrecta)
          .build();
        item.setFeedbackForIncorrect(fbIncorrecta);
      }
    }
  });

  Logger.log('Formulario creado: ' + form.getEditUrl());
}
```

Este patrón de creación de quizzes vía `FormApp` está alineado con ejemplos públicos que crean preguntas, definen choice items y setean feedback con `setFeedbackForCorrect` / `setFeedbackForIncorrect`.[^5_3][^5_4][^5_5][^5_1]

***

Si quieres, en el siguiente paso podemos:

- Ajustar el parser `.md → JSON` (pseudocódigo o Python),
- o extender el JSON para incluir también IDs de imagen de opciones (p. ej. opciones como imagen).
<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_6][^5_7][^5_8][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://gist.github.com/tanaikech/3e131b55c7947ced19a3dd99410367eb

[^5_2]: https://tanaikech.github.io/2022/04/05/creating-quizzes-in-google-form-using-google-forms-service-with-google-apps-script/

[^5_3]: https://developers.google.com/apps-script/reference/forms/quiz-feedback-builder

[^5_4]: https://developers.google.com/apps-script/reference/forms/quiz-feedback

[^5_5]: https://www.youtube.com/watch?v=tpDnPy-MRQ0

[^5_6]: https://developers.google.com/workspace/forms/api/guides

[^5_7]: https://stackoverflow.com/questions/78088555/google-forms-correct-incorrect-feedback

[^5_8]: https://developers.google.com/workspace/forms/api/guides/setup-grading

[^5_9]: https://gist.github.com/GaetanoPiazzolla/ef74f09136946cf9cbd5806f1cbf1d0b

[^5_10]: https://gist.github.com/tanaikech/eebcb2d71eed1aab5decff64287bcc9a

[^5_11]: https://www.jotform.com/google-forms/how-to-create-a-google-form-quiz-with-scoring/

[^5_12]: https://gist.github.com/tanaikech/eebcb2d71eed1aab5decff64287bcc9a?permalink_comment_id=4390509

[^5_13]: https://support.google.com/docs/thread/9867097/different-feedback-for-different-multiple-choice-answers?hl=en

[^5_14]: https://developers.google.com/workspace/forms/api/guides/create-form-quiz

[^5_15]: https://www.youtube.com/watch?v=sAO799ZEZ9s


---

# Dame el json. Es en dos partes porque son dos examenes.Usa el primero de los siguientes textos para extraer las preguntas, el segunde de los textos para marcar la respuesta correcta y el tercero pra definir el feedback, redacta el feedback no como sí se dirigiera a alguien, sino más bien impersonal. Dames un id de pregunta a cada pregunta y el tipo en todas es de opción múltiple. "A continuación tienes dos exámenes pensados para resolverse en 2 horas cada uno, en formato compatible con Google Forms (Google Classroom). Cada reactivo es de opción múltiple e incluye tanto conceptos teóricos (tomados de los .md del espacio) como situaciones prácticas alineadas con las prácticas indicadas. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5fa752c0-54f2-4f21-a4e8-72b916623d66/Practica_Construccion_de_SOAP.md)


***

## Examen 1 – SOAP, XML/XSD, WSDL y monolito mínimo Node.js

### Sección A: Conceptos teóricos (SOAP, XML, XSD, WSDL)

1. ¿Cuál es el propósito principal de usar XML en servicios web SOAP?

- A) Reducir el tamaño de los mensajes de red
- B) Representar datos estructurados de forma jerárquica y validable mediante esquemas
- C) Asegurar que todos los mensajes sean binarios
- D) Evitar el uso de HTTP como transporte

2. ¿Qué característica define a un documento XML “bien formado”?

- A) Tener solo elementos de tipo string
- B) Usar siempre el mismo prefijo de espacio de nombres
- C) Tener un único elemento raíz y etiquetas correctamente anidadas y cerradas
- D) Incluir al menos un atributo en cada elemento

3. En un esquema XSD, ¿qué diferencia hay entre un tipo simple y un tipo complejo?

- A) El tipo simple solo se usa para atributos, el complejo solo para elementos
- B) El tipo simple describe valores atómicos; el complejo agrupa elementos y atributos anidados
- C) El tipo complejo solo se usa en WSDL, el simple solo en XML
- D) No hay diferencia; ambos se usan indistintamente

4. ¿Cuál es el rol de XSD en el contexto de WSDL y servicios SOAP?

- A) Optimizar el rendimiento del servidor HTTP
- B) Describir la estructura y tipos de los mensajes XML que intercambia el servicio
- C) Registrar servicios en directorios públicos
- D) Gestionar la seguridad y el cifrado de los mensajes

5. ¿Cuál de las siguientes opciones describe mejor a WSDL?

- A) Un formato ligero de datos alternativo a JSON
- B) Un protocolo de transporte para servicios web
- C) Un lenguaje basado en XML que describe operaciones, mensajes, tipos de datos y endpoints de un servicio
- D) Una base de datos de servicios web en la nube

6. En un mensaje SOAP típico, ¿qué elemento es obligatorio?

- A) soap:Header
- B) soap:Body
- C) soap:Fault
- D) soap:Security

7. ¿Qué ventaja clave ofrece el uso de WSDL con contratos estrictos?

- A) Permite cambiar la estructura de los mensajes sin coordinar con los consumidores
- B) Facilita la generación de código cliente/servidor y la validación automática de mensajes
- C) Elimina la necesidad de usar XML
- D) Permite que el servicio sea completamente stateless sin esfuerzo

8. ¿Qué componente de la “pila clásica” SOAP se diseñó para publicar y descubrir servicios?

- A) SOAP
- B) WSDL
- C) UDDI
- D) WS-Security

9. ¿Cuál de las siguientes afirmaciones sobre SOAP y REST es correcta?

- A) SOAP usa típicamente XML y contratos formales; REST suele usar JSON y contratos más ligeros
- B) SOAP y REST siempre usan JSON
- C) REST requiere UDDI para descubrir servicios
- D) SOAP no puede usar HTTP como transporte

10. ¿En qué contexto suele seguir siendo razonable usar SOAP en lugar de solo APIs REST?

- A) Aplicaciones móviles sin requisitos de seguridad
- B) Prototipos rápidos con cambios frecuentes de contrato
- C) Integraciones reguladas de largo plazo con contratos muy estructurados y WS-Security
- D) Sitios estáticos de contenido público


### Sección B: Práctica SOAP/XML y WSDL (opción múltiple sobre casos)

11. Te dan el siguiente JSON de respuesta de un producto:
```json
{ "id": 1, "name": "Laptop", "price": 25000.0 }
```

¿Cuál sería el elemento principal más adecuado en el Body de un mensaje SOAP de respuesta?

- A) `<GetProductRequest>`
- B) `<ProductResponse>` o equivalente que agrupe los datos del producto
- C) `<ErrorResponse>`
- D) `<EnvelopeProduct>`

12. En un mensaje SOAP bien formado que representa una respuesta de producto, ¿qué combinación es la más adecuada?

- A) Un único `<soap:Envelope>` con `<soap:Header>` y `<soap:Body>` internos
- B) Varios `<soap:Envelope>` anidados para cada elemento del producto
- C) Un `<soap:Body>` sin `<soap:Envelope>`
- D) Un XML sin namespaces para simplificar

13. Si validas un XML de mensaje SOAP contra un XSD y el validador indica que el elemento `<price>` no es numérico, ¿qué significa?

- A) El WSDL está mal escrito
- B) El XML no es bien formado
- C) El valor del elemento no cumple el tipo de dato definido en el XSD
- D) El servidor HTTP está caído

14. Tienes un WSDL con tipos XSD embebidos en la sección `<types>`. ¿Qué necesitas hacer para validar un mensaje de ejemplo contra esos tipos?

- A) Ignorar la sección `<types>` y validar solo con el navegador
- B) Extraer o referenciar el XSD de la sección `<types>` y usarlo como esquema en un validador XML/XSD
- C) Convertir el WSDL a JSON y validarlo con OpenAPI
- D) No es posible validar mensajes usando un WSDL

15. Un `<soap:Fault>` en un mensaje SOAP se utiliza principalmente para:

- A) Enviar datos de negocio adicionales
- B) Configurar la autenticación del servicio
- C) Establecer una conexión persistente
- D) Comunicar errores de procesamiento con código, motivo y detalles


### Sección C: Teórico/práctico Node.js – Monolito mínimo

16. En el laboratorio de “Monolito mínimo con Node.js y Express”, ¿qué característica distingue a las rutas iniciales implementadas?

- A) Solo exponen métodos GET y POST para recursos como productos y pedidos en memoria
- B) Incluyen persistencia en base de datos relacional
- C) Exponen exclusivamente métodos PUT y DELETE
- D) Usan colas de mensajes en lugar de HTTP

17. ¿Cuál es el propósito de usar `app.use(express.json())` en una API Express?

- A) Permitir que Express sirva archivos estáticos
- B) Habilitar el parseo automático de cuerpos JSON en las peticiones
- C) Configurar el motor de plantillas HTML
- D) Asegurar la conexión HTTPS

18. En una ruta `GET /productos/:id`, el segmento `:id` en Express se conoce como:

- A) Query string
- B) Middleware
- C) Parámetro de ruta
- D) Header obligatorio

19. Para extender la API del monolito mínimo y permitir eliminar un producto específico, ¿cuál de las siguientes rutas es más apropiada?

- A) `DELETE /productos`
- B) `DELETE /productos/:id`
- C) `GET /productos/delete`
- D) `POST /productos/remove/:id`

20. Si una petición intenta obtener un producto por `id` que no existe, ¿qué código HTTP es más apropiado regresar?

- A) 200 OK con un cuerpo vacío
- B) 201 Created
- C) 404 Not Found
- D) 500 Internal Server Error

21. En la práctica de “monolito mínimo extendido”, al implementar `PUT /productos/:id`, ¿cuál es el comportamiento esperado?

- A) Crear siempre un producto nuevo sin importar si existe
- B) Actualizar los campos del producto existente identificado por `id`
- C) Reiniciar el servidor
- D) Devolver siempre 204 sin contenido y sin cambios

22. ¿Qué ventaja tiene mantener los datos de productos y pedidos en estructuras en memoria durante el laboratorio?

- A) Permite simular la lógica de negocio sin configurar una base de datos real
- B) Asegura durabilidad de datos entre reinicios
- C) Mejora la seguridad ante ataques externos
- D) Obliga a usar transacciones distribuidas

23. En pruebas con `curl` o Postman sobre el monolito mínimo, ¿cuál de estas opciones representa correctamente una petición POST para crear un producto?

- A) `POST /products` sin cuerpo, esperando que el servidor genere los datos
- B) `POST /productos` con encabezado `Content-Type: application/json` y un cuerpo JSON con los campos del producto
- C) `GET /productos/new` con parámetros en la URL
- D) `PUT /productos` con un cuerpo vacío

24. Cuando se extiende el monolito mínimo para manejar recursos “pedidos” además de “productos”, ¿qué principio se refuerza?

- A) Que todas las rutas deben compartir el mismo prefijo
- B) La separación de responsabilidades por tipo de recurso en la API
- C) Que solo se puede definir un recurso por servidor
- D) Que los métodos HTTP son intercambiables

25. ¿Cuál es una diferencia clave entre la API monolítica mínima y una arquitectura de microservicios?

- A) En el monolito, todo el código corre en un mismo despliegue; en microservicios se distribuye en servicios independientes
- B) En un monolito no se pueden usar rutas HTTP
- C) Los microservicios no pueden comunicarse vía HTTP
- D) El monolito siempre es más escalable que cualquier microservicio

***

## Examen 2 – Tipos de integración, SOAP vs REST, WSDL vs REST, prácticas de integración

### Sección A: Tipos de integración y panorama histórico

1. En integración de sistemas, la integración “punto a punto” se caracteriza por:

- A) Un bus central que conecta todos los sistemas
- B) Conexiones directas específicas entre cada par de aplicaciones, generando “spaghetti” al crecer
- C) El uso exclusivo de colas de mensajes
- D) La obligación de usar solo SOAP/XML

2. ¿Qué objetivo principal tiene la arquitectura SOA frente al “spaghetti” punto a punto?

- A) Aumentar el número de conexiones
- B) Agrupar la lógica en servicios de negocio con contratos claros y reutilizables
- C) Eliminar la necesidad de contratos
- D) Obligar a usar microservicios

3. ¿Cuál de las siguientes afirmaciones describe mejor a REST en el contexto de integración?

- A) Es un protocolo binario para redes locales
- B) Es un estilo arquitectónico que aprovecha HTTP y trata recursos mediante métodos estándar como GET, POST, PUT, DELETE
- C) Es un lenguaje de programación orientado a objetos
- D) Es un reemplazo obligatorio de SOAP en todos los contextos

4. ¿Qué ventaja principal aportó REST+JSON en comparación con SOAP/XML para muchas APIs modernas?

- A) Mayores requisitos de herramientas especializadas
- B) Contratos más rígidos e inflexibles
- C) Mensajes más ligeros y fáciles de consumir desde navegadores y apps móviles
- D) Imposibilidad de usar HTTPS

5. En el contexto actual, ¿qué es común encontrar en organizaciones grandes?

- A) Solo monolitos puros sin integración
- B) Solo microservicios sin legado
- C) La convivencia de monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos
- D) Exclusivamente colas de mensajes sin APIs

6. ¿Qué tipo de integración se centra principalmente en compartir y sincronizar información (por ejemplo, tablas de clientes) entre sistemas?

- A) Integración de datos
- B) Integración funcional
- C) Integración semántica
- D) Integración física

7. ¿Qué tipo de integración implica consumir capacidades o funciones remotas, como “consultar saldo” o “crear pedido”?

- A) Integración de datos
- B) Integración funcional
- C) Integración semántica
- D) Integración de red

8. ¿A qué se refiere la integración semántica?

- A) A compartir archivos de texto sin estructura
- B) A alinear el significado de los datos y conceptos entre sistemas, evitando ambigüedades
- C) A comprimir mensajes para ahorrar ancho de banda
- D) A usar siempre el mismo tipo de base de datos

9. En un ejercicio donde mapeas sistemas de una organización y clasificas sus conexiones, ¿qué criterio usarías para etiquetar una integración como “crítica”?

- A) Que use JSON
- B) Que sea la que más ancho de banda consume
- C) Que, si falla, afecta procesos de negocio esenciales como facturación o pagos
- D) Que sea la más nueva

10. ¿Qué efecto tiene agregar muchas integraciones punto a punto a lo largo del tiempo?

- A) Facilita el mantenimiento porque todas son similares
- B) Disminuye la dependencia entre sistemas
- C) Aumenta la complejidad, la duplicación de lógica y el acoplamiento
- D) Elimina la necesidad de documentación


### Sección B: SOAP vs REST, pila SOAP y vigencia de SOAP

11. ¿Cuál de las siguientes es una característica típica de SOAP en la era SOA?

- A) Uso exclusivo de JSON

```
- B) Mensajes con sobre `<Envelope>`, `<Header>` y `<Body>` en XML
```

- C) Eliminación de contratos formales
- D) Comunicación solo dentro de un mismo proceso

12. ¿Qué elemento de la pila SOAP describe las operaciones disponibles y los tipos de mensajes?

- A) SOAP Envelope
- B) WSDL
- C) UDDI
- D) WS-Security

13. ¿Qué rol jugaron las especificaciones WS-* (como WS-Security, WS-Policy) en el ecosistema SOAP?

- A) Definir formatos de imagen
- B) Extender SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones
- C) Reemplazar completamente a WSDL
- D) Hacer innecesario el uso de XML

14. ¿En qué sectores se menciona que SOAP sigue siendo comúnmente utilizado?

- A) Redes sociales y aplicaciones de mensajería instantánea
- B) Videojuegos móviles informales
- C) Banca, gobierno y salud con fuertes requisitos regulatorios
- D) Sitios web estáticos

15. ¿Cuál de las siguientes situaciones favorece seguir usando un servicio SOAP existente en lugar de migrarlo inmediatamente a REST?

- A) El proveedor solo ofrece WSDL y WS-* y la integración es estable y de largo plazo
- B) La API se usa solo para pruebas internas temporales
- C) Se requiere una interfaz gráfica rica
- D) No hay requisitos de seguridad

16. ¿Cuál es una diferencia conceptual clave entre mensajes SOAP y mensajes REST/JSON?

- A) REST/JSON obliga a usar WS-Security
- B) SOAP incluye un sobre estandarizado y namespaces; REST/JSON suele enviar directamente los datos sin esa envoltura
- C) SOAP no permite tipos de datos complejos
- D) REST requiere UDDI

17. ¿Qué describe mejor a una API REST bien diseñada?

- A) Operaciones definidas por verbos arbitrarios en la URL
- B) Recursos identificados por URIs y manipulados con métodos HTTP estándar y códigos de estado apropiados
- C) Mensajes exclusivamente XML
- D) Ausencia total de contrato o documentación

18. ¿En qué caso es especialmente importante decidir “cuándo convivir con SOAP y encapsularlo, y cuándo migrar a APIs más ligeras”?

- A) Cuando solo hay un sistema aislado sin integraciones
- B) Cuando no hay restricciones regulatorias ni de seguridad
- C) Cuando se integran sistemas legacy SOAP con nuevas aplicaciones y microservicios
- D) Cuando todos los servicios ya son REST


### Sección C: Prácticas – Tipos de integración, comparación WSDL vs REST

19. En la práctica de “tipos de integración”, un equipo dibuja varios sistemas y marca una integración entre el ERP y el sistema de facturación donde solo se replica la tabla de clientes cada noche. ¿Qué tipo de integración es la más adecuada?

- A) Funcional
- B) Semántica
- C) De datos
- D) De red

20. En esa misma práctica, otra integración permite que una app móvil invoque “consultar saldo” en un sistema bancario remoto. ¿Qué tipo de integración representa mejor esta situación?

- A) De datos, porque solo importa la tabla de saldos
- B) Funcional, porque se consume una capacidad remota de negocio
- C) Semántica, porque solo se alinea el significado
- D) Física, porque usa redes móviles

21. En el ejercicio de comparación WSDL vs REST, ¿cuál de estos elementos es más natural encontrar en un WSDL?

- A) Definiciones de `paths` y `responses` en JSON

```
- B) Elementos `<portType>`, `<operation>` y `<message>` que describen el contrato
```

- C) Documentación en formato Markdown
- D) Solo ejemplos de llamadas con `curl`

22. En la documentación de una API REST equivalente, ¿qué preguntas se suelen responder de forma explícita?

- A) Qué URIs existen, qué métodos HTTP soportan, qué estructura de JSON esperan y devuelven
- B) Cómo generar código a partir de WSDL
- C) Cómo registrar el servicio en UDDI
- D) Cómo usar WS-Security

23. Cuando en la práctica se pide comparar un WSDL con una API REST, ¿qué objetivo conceptual se busca?

- A) Convertir siempre el WSDL en REST
- B) Identificar elementos de contrato en ambos enfoques y discutir ventajas/desventajas
- C) Demostrar que uno de los dos está obsoleto
- D) Medir solo el tamaño de los mensajes

24. En un escenario donde un servicio SOAP y una API REST exponen la misma funcionalidad de “consultar saldo”, ¿qué diferencia práctica suele encontrarse?

- A) El SOAP se consume solo desde navegadores
- B) El WSDL describe tipos y operaciones en XML, mientras que la API REST suele usar JSON y documentación tipo OpenAPI o similar
- C) El SOAP es siempre más rápido
- D) La API REST no puede usar HTTPS

25. En un ejercicio grupal, se identifica una integración donde dos sistemas usan el mismo campo “balance” con significados distintos (uno es saldo disponible, otro saldo contable total). ¿Qué tipo de problema se ilustra?

- A) Problema de sintaxis XML
- B) Problema de transporte HTTP
- C) Problema de integración semántica
- D) Problema exclusivo de rendimiento

***

Si quieres, en el siguiente paso puedo proponerte claves sugeridas de respuesta para ambos exámenes, o ajustar el número de preguntas/dificultad para que se ajusten mejor al tiempo de 2 horas.", "Aquí tienes la clave de ambos exámenes y textos de feedback listos para copiar en Google Forms. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5c230302-fc47-4a58-8b04-4b086818c350/01_Diff_SOAP_REST.md)

***

## Examen 1 – Clave y feedback

### Sección A (1–10)

1. B
2. C
3. B
4. B
5. C
6. B
7. B
8. C
9. A
10. C

### Sección B (11–15)

11. B
12. A
13. C
14. B
15. D

### Sección C (16–25)

16. A
17. B
18. C
19. B
20. C
21. B
22. A
23. B
24. B
25. A

## Examen 2 – Clave y feedback

### Sección A (1–10)

1. B
2. B
3. B
4. C
5. C
6. A
7. B
8. B
9. C
10. C

### Sección B (11–18)

11. B
12. B
13. B
14. C
15. A
16. B
17. B
18. C

### Sección C (19–25)

19. C
20. B
21. B
22. A
23. B
24. B
25. C

", "A continuación tienes un feedback específico por pregunta para ambos exámenes, con una frase para respuesta correcta y otra para respuesta incorrecta. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5c230302-fc47-4a58-8b04-4b086818c350/01_Diff_SOAP_REST.md)

***

## Examen 1 – Feedback por pregunta

1. 

- Correcta: Entendido: XML se usa para representar datos jerárquicos y validables, lo que es clave en mensajes SOAP.
- Incorrecta: Revisa que XML en servicios web se valora por su estructura jerárquica y validación con XSD, no por tamaño reducido ni por ser binario.

2. 

- Correcta: Bien: identificas que un XML bien formado tiene un solo elemento raíz y etiquetas bien anidadas y cerradas.
- Incorrecta: Vuelve a revisar las reglas de “bien formado”: un único root y etiquetas correctamente anidadas son esenciales.

3. 

- Correcta: Correcto: distingues que tipos simples son valores atómicos y los complejos agrupan elementos y atributos.
- Incorrecta: Revisa la diferencia entre tipo simple (valor atómico) y tipo complejo (estructura con elementos/atributos).

4. 

- Correcta: Bien: reconoces que XSD describe la estructura y tipos de los mensajes XML usados por el servicio.
- Incorrecta: Recuerda que XSD no optimiza HTTP ni seguridad; su foco es definir estructura y tipos de datos de los mensajes.

5. 

- Correcta: Correcto: WSDL es un lenguaje XML para describir operaciones, mensajes, tipos y endpoints de un servicio.
- Incorrecta: Revisa que WSDL no es ni un formato de datos ni un protocolo: es un contrato descriptivo basado en XML.

6. 

- Correcta: Bien: identificas que el Body es obligatorio en un mensaje SOAP, el Header y Fault son opcionales.
- Incorrecta: Recuerda que el elemento obligatorio en SOAP es el Body; el Header y Fault aparecen solo cuando se requieren.

7. 

- Correcta: Correcto: ves que WSDL permite generar código y validar mensajes de forma automática gracias al contrato estricto.
- Incorrecta: Revisa la ventaja de contratos estrictos: facilitan generación de código y validación, pero exigen disciplina al evolucionar.

8. 

- Correcta: Bien: UDDI se diseñó como registro para publicar y descubrir servicios web.
- Incorrecta: Recuerda que SOAP es protocolo de mensajería, WSDL describe el contrato, y UDDI es el registro/catalogo.

9. 

- Correcta: Correcto: SOAP típicamente usa XML y contratos formales; REST suele usar JSON y contratos más ligeros.
- Incorrecta: Revisa la comparación: REST no requiere UDDI ni SOAP JSON; se caracteriza por mensajes ligeros y menor rigidez.

10. 

- Correcta: Bien: identificas que SOAP sigue siendo razonable en integraciones reguladas y de largo plazo con contratos muy estructurados.
- Incorrecta: Recuerda que SOAP encaja mejor donde hay requisitos fuertes de seguridad, contratos estables y WS-Security.

11. 

- Correcta: Correcto: el Body suele contener un elemento que agrupa los datos del producto, como ProductResponse.
- Incorrecta: Revisa la estructura del Body: no se envuelven datos en EnvelopeProduct ni en elementos de petición si es respuesta.

12. 

- Correcta: Bien: reconoces que debe existir un único Envelope con Header opcional y Body obligatorio.
- Incorrecta: Recuerda que no se anidan múltiples Envelopes y siempre debe existir un Envelope que contenga Header y Body.

13. 

- Correcta: Correcto: el error indica que el valor no cumple el tipo definido en el XSD, aunque el XML pueda ser bien formado.
- Incorrecta: Diferencia “bien formado” (sintaxis XML) de “válido” contra XSD; aquí el problema es de tipo de dato, no de sintaxis.

14. 

- Correcta: Bien: sabes que puedes extraer el XSD de `<types>` y usarlo en un validador XML/XSD.
- Incorrecta: Recuerda que el WSDL sí permite validar mensajes extrayendo o referenciando sus XSD, no se ignoran los `<types>`.

15. 

- Correcta: Correcto: el Fault sirve para comunicar errores de procesamiento con código, motivo y detalles.
- Incorrecta: Revisa que Fault no transmite datos de negocio ni configuraciones, sino información de error estándar.

16. 

- Correcta: Bien: identificas que el monolito mínimo arranca con rutas GET/POST en memoria para productos y pedidos.
- Incorrecta: Revisa que inicialmente no hay base de datos ni solo PUT/DELETE; el foco es un CRUD simple en memoria.

17. 

- Correcta: Correcto: `express.json()` permite parsear automáticamente JSON en el cuerpo de la petición.
- Incorrecta: Recuerda que `express.json()` no es para estáticos ni HTTPS; su función es procesar cuerpos JSON.

18. 

- Correcta: Bien: reconoces que `:id` es un parámetro de ruta en Express.
- Incorrecta: Diferencia parámetros de ruta (`/recurso/:id`) de query string (`?id=…`) y headers.

19. 

- Correcta: Correcto: `DELETE /productos/:id` es la forma típica de eliminar un recurso específico.
- Incorrecta: Revisa la convención REST: DELETE sobre la URI del recurso concreto, no sobre rutas genéricas o GETs “borradores”.

20. 

- Correcta: Bien: 404 Not Found es apropiado cuando el recurso solicitado por id no existe.
- Incorrecta: Recuerda: 200 implica éxito con recurso; 404 es el código estándar cuando el recurso no se encuentra.

21. 

- Correcta: Correcto: PUT `/productos/:id` se usa para actualizar el recurso existente identificado por ese id.
- Incorrecta: Revisa la semántica de PUT: típicamente actualiza o reemplaza el recurso, no solo “crear siempre” ni retornar sin cambios.

22. 

- Correcta: Bien: usar estructuras en memoria simplifica el laboratorio al evitar configurar una base de datos real.
- Incorrecta: Recuerda que el objetivo es practicar lógica y rutas, no garantizar persistencia ni transacciones reales.

23. 

- Correcta: Correcto: POST `/productos` con `Content-Type: application/json` y cuerpo JSON es el patrón adecuado.
- Incorrecta: Revisa que POST sin cuerpo o GET/PUT para crear recurso no son el patrón principal practicado.

24. 

- Correcta: Bien: reconoces la separación de recursos (productos, pedidos) como principio de diseño de la API.
- Incorrecta: Recuerda que no se trata de tener un solo recurso, sino de tener rutas claras y separadas por tipo de entidad.

25. 

- Correcta: Correcto: en un monolito todo corre en un despliegue; en microservicios se fragmenta en servicios independientes.
- Incorrecta: Revisa la diferencia de despliegue: monolito un solo artefacto, microservicios varios servicios autónomos.

***

## Examen 2 – Feedback por pregunta

1. 

- Correcta: Bien: identificas la integración punto a punto como conexiones directas que generan “spaghetti” al crecer.
- Incorrecta: Revisa que en punto a punto no hay bus central; cada par de sistemas construye su propia integración.

2. 

- Correcta: Correcto: SOA agrupa lógica en servicios de negocio con contratos claros, reduciendo spaghetti.
- Incorrecta: Recuerda que SOA no busca más conexiones, sino servicios reutilizables y contratos bien definidos.

3. 

- Correcta: Bien: REST es un estilo que usa HTTP y trata recursos con métodos GET, POST, PUT, DELETE, etc.
- Incorrecta: Revisa que REST no es un protocolo binario ni un lenguaje de programación.

4. 

- Correcta: Correcto: REST+JSON aporta mensajes más ligeros y fáciles de consumir que SOAP/XML en muchos casos.
- Incorrecta: Recuerda que la ventaja típica de REST+JSON es simplicidad y ligereza, no mayor rigidez ni más herramientas pesadas.

5. 

- Correcta: Bien: reconoces la coexistencia de monolitos, SOAP legacy, REST y eventos en organizaciones reales.
- Incorrecta: Revisa que el mundo real suele mezclar estilos, no eliminar por completo monolitos o SOAP.

6. 

- Correcta: Correcto: cuando se comparte/sincroniza información (como tablas de clientes), se trata de integración de datos.
- Incorrecta: Recuerda que la integración de datos se enfoca en replicar y sincronizar información, no tanto en invocar funciones.

7. 

- Correcta: Bien: consumir “consultar saldo” remoto es integración funcional, porque usas capacidades de otro sistema.
- Incorrecta: Diferencia integrar datos (tablas) de integrar funciones (operaciones como consultar o crear).

8. 

- Correcta: Correcto: integración semántica alinea significado de datos y conceptos entre sistemas.
- Incorrecta: Revisa que el problema semántico es que “balance”, “cliente”, etc., signifiquen lo mismo en todos los sistemas.

9. 

- Correcta: Bien: una integración es crítica si, al fallar, afecta procesos esenciales como pagos o facturación.
- Incorrecta: Recuerda que lo crítico se define por impacto al negocio, no por ancho de banda ni novedad.

10. 

- Correcta: Correcto: muchas integraciones punto a punto terminan en mayor complejidad, duplicación y acoplamiento.
- Incorrecta: Revisa que más conexiones punto a punto aumentan el “spaghetti” y hacen el mantenimiento más difícil.

11. 

- Correcta: Bien: SOAP se caracteriza por mensajes XML con Envelope, Header y Body.
- Incorrecta: Recuerda que SOAP no es JSON; su estructura estándar en XML es una de sus señas de identidad.

12. 

- Correcta: Correcto: WSDL describe operaciones, mensajes y tipos de datos del servicio.
- Incorrecta: Revisa que WSDL es el contrato; SOAP es el protocolo de mensaje y UDDI es el registro.

13. 

- Correcta: Bien: las especificaciones WS-* extienden SOAP con seguridad, políticas, confianza, transacciones, etc.
- Incorrecta: Recuerda que WS-* no reemplaza WSDL ni define imágenes; amplía capacidades de la pila SOAP empresarial.

14. 

- Correcta: Correcto: SOAP sigue siendo común en banca, gobierno y salud con requisitos fuertes.
- Incorrecta: Revisa que estos sectores valoran los contratos formales y WS-Security; no se trata de redes sociales o juegos.

15. 

- Correcta: Bien: si solo hay WSDL/WS-* y el contrato es estable de largo plazo, tiene sentido seguir usando SOAP.
- Incorrecta: Recuerda que migrar a REST no siempre es prioritario si la integración SOAP es estable y regulada.

16. 

- Correcta: Correcto: SOAP incluye sobre estándar y namespaces; REST/JSON suele enviar directamente datos sin esa envoltura.
- Incorrecta: Revisa que REST no obliga WS-Security ni UDDI; su formato típico es JSON sin Envelope estándar.

17. 

- Correcta: Bien: una API REST bien diseñada usa URIs de recursos, métodos HTTP y códigos de estado coherentes.
- Incorrecta: Recuerda que REST no es solo “sin contrato”; debería documentar recursos, métodos y respuestas.

18. 

- Correcta: Correcto: el dilema SOAP vs APIs ligeras se vuelve crítico cuando integras legacy SOAP con nuevos servicios.
- Incorrecta: Revisa que cuando todo es REST el problema es menor; el reto es convivir con sistemas SOAP existentes.

19. 

- Correcta: Bien: replicar la tabla de clientes cada noche es integración de datos.
- Incorrecta: Recuerda que aquí no se invoca una función de negocio; solo se copian datos entre sistemas.

20. 

- Correcta: Correcto: la app que invoca “consultar saldo” realiza integración funcional.
- Incorrecta: Diferencia compartir tablas (datos) de exponer operaciones como “consultar saldo” (funcional).

21. 
```
- Correcta: Bien: en un WSDL verás elementos como `<portType>`, `<operation>` y `<message>`.  
```

- Incorrecta: Revisa que JSON y `paths` son típicos de OpenAPI/REST, no de WSDL.

22. 

- Correcta: Correcto: la documentación REST detalla URIs, métodos, estructura de JSON de entrada/salida, etc.
- Incorrecta: Recuerda que registrar en UDDI y WS-Security pertenecen más al mundo SOAP/WS-*.

23. 

- Correcta: Bien: el objetivo es identificar elementos de contrato en WSDL y REST y discutir ventajas/desventajas.
- Incorrecta: Revisa que la práctica no busca declarar obsoleto a uno, sino entender ambos enfoques.

24. 

- Correcta: Correcto: el WSDL describe tipos/operaciones en XML; la API REST usa JSON y normalmente OpenAPI u otra doc.
- Incorrecta: Recuerda que ambos pueden usar HTTPS; la diferencia está en formato y forma de documentar el contrato.

25. 

- Correcta: Bien: el uso distinto de “balance” ilustra un problema de integración semántica.
- Incorrecta: Revisa que aquí el problema no es de transporte ni sintaxis, sino de significado de los datos.

***

Si quieres, puedo condensar estos textos en versiones aún más cortas pensadas para el límite de caracteres del feedback en Google Forms."

Aquí tienes el JSON con los dos exámenes, incluyendo ids, tipo (todas opción múltiple), clave correcta y feedback reescrito en forma impersonal.

```json
{
  "examenes": [
    {
      "titulo": "Examen 1 – SOAP, XML/XSD, WSDL y monolito mínimo Node.js",
      "preguntas": [
        {
          "id": "E1_P01",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál es el propósito principal de usar XML en servicios web SOAP?",
          "opciones": [
            "Reducir el tamaño de los mensajes de red",
            "Representar datos estructurados de forma jerárquica y validable mediante esquemas",
            "Asegurar que todos los mensajes sean binarios",
            "Evitar el uso de HTTP como transporte"
          ],
          "correcta": [2],
          "feedback_correcta": "XML se utiliza para representar datos jerárquicos y validables, lo cual resulta fundamental en mensajes SOAP.",
          "feedback_incorrecta": "XML en servicios web se valora por su estructura jerárquica y la posibilidad de validación mediante XSD, no por reducción de tamaño ni por ser binario."
        },
        {
          "id": "E1_P02",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué característica define a un documento XML “bien formado”?",
          "opciones": [
            "Tener solo elementos de tipo string",
            "Usar siempre el mismo prefijo de espacio de nombres",
            "Tener un único elemento raíz y etiquetas correctamente anidadas y cerradas",
            "Incluir al menos un atributo en cada elemento"
          ],
          "correcta": [3],
          "feedback_correcta": "Un XML bien formado se caracteriza por tener un único elemento raíz y etiquetas bien anidadas y cerradas.",
          "feedback_incorrecta": "Las reglas de documento XML bien formado exigen un único elemento raíz y etiquetas correctamente anidadas y cerradas."
        },
        {
          "id": "E1_P03",
          "tipo": "opcion_multiple",
          "enunciado": "En un esquema XSD, ¿qué diferencia hay entre un tipo simple y un tipo complejo?",
          "opciones": [
            "El tipo simple solo se usa para atributos, el complejo solo para elementos",
            "El tipo simple describe valores atómicos; el complejo agrupa elementos y atributos anidados",
            "El tipo complejo solo se usa en WSDL, el simple solo en XML",
            "No hay diferencia; ambos se usan indistintamente"
          ],
          "correcta": [2],
          "feedback_correcta": "Los tipos simples describen valores atómicos y los tipos complejos agrupan elementos y atributos.",
          "feedback_incorrecta": "La diferencia clave es que el tipo simple representa un valor atómico y el tipo complejo define estructuras con elementos y/o atributos."
        },
        {
          "id": "E1_P04",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál es el rol de XSD en el contexto de WSDL y servicios SOAP?",
          "opciones": [
            "Optimizar el rendimiento del servidor HTTP",
            "Describir la estructura y tipos de los mensajes XML que intercambia el servicio",
            "Registrar servicios en directorios públicos",
            "Gestionar la seguridad y el cifrado de los mensajes"
          ],
          "correcta": [2],
          "feedback_correcta": "XSD se utiliza para describir la estructura y los tipos de datos de los mensajes XML de un servicio.",
          "feedback_incorrecta": "XSD no se orienta a rendimiento HTTP ni a seguridad; su finalidad es definir estructura y tipos de datos de los mensajes."
        },
        {
          "id": "E1_P05",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál de las siguientes opciones describe mejor a WSDL?",
          "opciones": [
            "Un formato ligero de datos alternativo a JSON",
            "Un protocolo de transporte para servicios web",
            "Un lenguaje basado en XML que describe operaciones, mensajes, tipos de datos y endpoints de un servicio",
            "Una base de datos de servicios web en la nube"
          ],
          "correcta": [3],
          "feedback_correcta": "WSDL es un lenguaje basado en XML para describir operaciones, mensajes, tipos y endpoints de un servicio.",
          "feedback_incorrecta": "WSDL no es un formato de datos ni un protocolo; es un contrato descriptivo basado en XML."
        },
        {
          "id": "E1_P06",
          "tipo": "opcion_multiple",
          "enunciado": "En un mensaje SOAP típico, ¿qué elemento es obligatorio?",
          "opciones": [
            "soap:Header",
            "soap:Body",
            "soap:Fault",
            "soap:Security"
          ],
          "correcta": [2],
          "feedback_correcta": "En un mensaje SOAP, el elemento Body es obligatorio, mientras que Header y Fault son opcionales.",
          "feedback_incorrecta": "El elemento obligatorio en SOAP es el Body; Header y Fault solo aparecen cuando se requieren."
        },
        {
          "id": "E1_P07",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué ventaja clave ofrece el uso de WSDL con contratos estrictos?",
          "opciones": [
            "Permite cambiar la estructura de los mensajes sin coordinar con los consumidores",
            "Facilita la generación de código cliente/servidor y la validación automática de mensajes",
            "Elimina la necesidad de usar XML",
            "Permite que el servicio sea completamente stateless sin esfuerzo"
          ],
          "correcta": [2],
          "feedback_correcta": "Los contratos estrictos en WSDL facilitan la generación de código y la validación automática de mensajes.",
          "feedback_incorrecta": "La principal ventaja de contratos estrictos en WSDL es la generación de código y la validación automática, aunque exigen disciplina al evolucionar."
        },
        {
          "id": "E1_P08",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué componente de la “pila clásica” SOAP se diseñó para publicar y descubrir servicios?",
          "opciones": [
            "SOAP",
            "WSDL",
            "UDDI",
            "WS-Security"
          ],
          "correcta": [3],
          "feedback_correcta": "UDDI se diseñó como registro para publicar y descubrir servicios web.",
          "feedback_incorrecta": "En la pila SOAP, SOAP es el protocolo de mensajería, WSDL describe el contrato y UDDI actúa como registro o catálogo."
        },
        {
          "id": "E1_P09",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál de las siguientes afirmaciones sobre SOAP y REST es correcta?",
          "opciones": [
            "SOAP usa típicamente XML y contratos formales; REST suele usar JSON y contratos más ligeros",
            "SOAP y REST siempre usan JSON",
            "REST requiere UDDI para descubrir servicios",
            "SOAP no puede usar HTTP como transporte"
          ],
          "correcta": [1],
          "feedback_correcta": "SOAP suele usar XML y contratos formales, mientras que REST tiende a emplear JSON y contratos más ligeros.",
          "feedback_incorrecta": "REST no requiere UDDI y SOAP no se limita en absoluto a JSON; REST se caracteriza por mensajes ligeros y menor rigidez contractual."
        },
        {
          "id": "E1_P10",
          "tipo": "opcion_multiple",
          "enunciado": "¿En qué contexto suele seguir siendo razonable usar SOAP en lugar de solo APIs REST?",
          "opciones": [
            "Aplicaciones móviles sin requisitos de seguridad",
            "Prototipos rápidos con cambios frecuentes de contrato",
            "Integraciones reguladas de largo plazo con contratos muy estructurados y WS-Security",
            "Sitios estáticos de contenido público"
          ],
          "correcta": [3],
          "feedback_correcta": "SOAP resulta razonable en integraciones reguladas y de largo plazo con contratos muy estructurados y uso de WS-Security.",
          "feedback_incorrecta": "SOAP encaja mejor en escenarios con requisitos fuertes de seguridad, contratos estables y uso de WS-Security que en prototipos cambiantes."
        },
        {
          "id": "E1_P11",
          "tipo": "opcion_multiple",
          "enunciado": "Te dan el siguiente JSON de respuesta de un producto: { \"id\": 1, \"name\": \"Laptop\", \"price\": 25000.0 }. ¿Cuál sería el elemento principal más adecuado en el Body de un mensaje SOAP de respuesta?",
          "opciones": [
            "<GetProductRequest>",
            "<ProductResponse> o equivalente que agrupe los datos del producto",
            "<ErrorResponse>",
            "<EnvelopeProduct>"
          ],
          "correcta": [2],
          "feedback_correcta": "El Body suele contener un elemento que agrupa los datos del producto, como ProductResponse o equivalente.",
          "feedback_incorrecta": "En el Body no se usan elementos de petición cuando se trata de una respuesta; tampoco se emplea un envoltorio como EnvelopeProduct para los datos."
        },
        {
          "id": "E1_P12",
          "tipo": "opcion_multiple",
          "enunciado": "En un mensaje SOAP bien formado que representa una respuesta de producto, ¿qué combinación es la más adecuada?",
          "opciones": [
            "Un único <soap:Envelope> con <soap:Header> y <soap:Body> internos",
            "Varios <soap:Envelope> anidados para cada elemento del producto",
            "Un <soap:Body> sin <soap:Envelope>",
            "Un XML sin namespaces para simplificar"
          ],
          "correcta": [1],
          "feedback_correcta": "Un mensaje SOAP bien formado tiene un único Envelope que contiene Header opcional y Body obligatorio.",
          "feedback_incorrecta": "En SOAP no se anidan múltiples Envelopes y siempre debe existir un Envelope que encapsule Header y Body."
        },
        {
          "id": "E1_P13",
          "tipo": "opcion_multiple",
          "enunciado": "Si se valida un XML de mensaje SOAP contra un XSD y el validador indica que el elemento <price> no es numérico, ¿qué significa?",
          "opciones": [
            "El WSDL está mal escrito",
            "El XML no es bien formado",
            "El valor del elemento no cumple el tipo de dato definido en el XSD",
            "El servidor HTTP está caído"
          ],
          "correcta": [3],
          "feedback_correcta": "El mensaje indica que el valor del elemento no cumple el tipo de dato definido en el XSD, aunque el XML pueda ser bien formado.",
          "feedback_incorrecta": "Es necesario distinguir entre XML bien formado y XML válido frente a XSD; en este caso el problema es de tipo de dato, no de sintaxis."
        },
        {
          "id": "E1_P14",
          "tipo": "opcion_multiple",
          "enunciado": "Tienes un WSDL con tipos XSD embebidos en la sección <types>. ¿Qué se necesita para validar un mensaje de ejemplo contra esos tipos?",
          "opciones": [
            "Ignorar la sección <types> y validar solo con el navegador",
            "Extraer o referenciar el XSD de la sección <types> y usarlo como esquema en un validador XML/XSD",
            "Convertir el WSDL a JSON y validarlo con OpenAPI",
            "No es posible validar mensajes usando un WSDL"
          ],
          "correcta": [2],
          "feedback_correcta": "El XSD embebido en la sección types puede extraerse o referenciarse y usarse en un validador XML/XSD.",
          "feedback_incorrecta": "El WSDL sí permite validar mensajes, extrayendo o referenciando sus XSD; la sección types no debe ignorarse."
        },
        {
          "id": "E1_P15",
          "tipo": "opcion_multiple",
          "enunciado": "Un <soap:Fault> en un mensaje SOAP se utiliza principalmente para:",
          "opciones": [
            "Enviar datos de negocio adicionales",
            "Configurar la autenticación del servicio",
            "Establecer una conexión persistente",
            "Comunicar errores de procesamiento con código, motivo y detalles"
          ],
          "correcta": [4],
          "feedback_correcta": "La estructura Fault se emplea para comunicar errores de procesamiento con código, motivo y detalles.",
          "feedback_incorrecta": "Fault no transmite datos de negocio ni configuraciones; su propósito es estandarizar la información de error."
        },
        {
          "id": "E1_P16",
          "tipo": "opcion_multiple",
          "enunciado": "En el laboratorio de “Monolito mínimo con Node.js y Express”, ¿qué caracteriza a las rutas iniciales implementadas?",
          "opciones": [
            "Solo exponen métodos GET y POST para recursos como productos y pedidos en memoria",
            "Incluyen persistencia en base de datos relacional",
            "Exponen exclusivamente métodos PUT y DELETE",
            "Usan colas de mensajes en lugar de HTTP"
          ],
          "correcta": [1],
          "feedback_correcta": "El monolito mínimo inicia con rutas GET y POST en memoria para recursos como productos y pedidos.",
          "feedback_incorrecta": "En la configuración inicial no se usa base de datos ni únicamente PUT/DELETE; el enfoque es un CRUD simple en memoria."
        },
        {
          "id": "E1_P17",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál es el propósito de usar app.use(express.json()) en una API Express?",
          "opciones": [
            "Permitir que Express sirva archivos estáticos",
            "Habilitar el parseo automático de cuerpos JSON en las peticiones",
            "Configurar el motor de plantillas HTML",
            "Asegurar la conexión HTTPS"
          ],
          "correcta": [2],
          "feedback_correcta": "La función express.json() permite parsear automáticamente cuerpos JSON en las solicitudes.",
          "feedback_incorrecta": "express.json() no se relaciona con archivos estáticos ni con HTTPS; su función es procesar cuerpos JSON."
        },
        {
          "id": "E1_P18",
          "tipo": "opcion_multiple",
          "enunciado": "En una ruta GET /productos/:id, ¿cómo se denomina el segmento :id en Express?",
          "opciones": [
            "Query string",
            "Middleware",
            "Parámetro de ruta",
            "Header obligatorio"
          ],
          "correcta": [3],
          "feedback_correcta": "El segmento :id se conoce como parámetro de ruta en Express.",
          "feedback_incorrecta": "Es importante diferenciar los parámetros de ruta (/recurso/:id) de la query string (?id=...) y de los encabezados."
        },
        {
          "id": "E1_P19",
          "tipo": "opcion_multiple",
          "enunciado": "Para extender la API del monolito mínimo y permitir eliminar un producto específico, ¿cuál de las siguientes rutas es más apropiada?",
          "opciones": [
            "DELETE /productos",
            "DELETE /productos/:id",
            "GET /productos/delete",
            "POST /productos/remove/:id"
          ],
          "correcta": [2],
          "feedback_correcta": "La convención REST indica que DELETE /productos/:id es la forma adecuada de eliminar un recurso específico.",
          "feedback_incorrecta": "El patrón habitual es enviar DELETE sobre la URI del recurso concreto, no sobre rutas genéricas ni sobre GETs simulando borrado."
        },
        {
          "id": "E1_P20",
          "tipo": "opcion_multiple",
          "enunciado": "Si una petición intenta obtener un producto por id que no existe, ¿qué código HTTP es más apropiado regresar?",
          "opciones": [
            "200 OK con un cuerpo vacío",
            "201 Created",
            "404 Not Found",
            "500 Internal Server Error"
          ],
          "correcta": [3],
          "feedback_correcta": "El código 404 Not Found es el más adecuado cuando el recurso solicitado por id no existe.",
          "feedback_incorrecta": "El código 200 implica éxito con un recurso; cuando el recurso no se encuentra, el código estándar es 404."
        },
        {
          "id": "E1_P21",
          "tipo": "opcion_multiple",
          "enunciado": "En la práctica de “monolito mínimo extendido”, al implementar PUT /productos/:id, ¿cuál es el comportamiento esperado?",
          "opciones": [
            "Crear siempre un producto nuevo sin importar si existe",
            "Actualizar los campos del producto existente identificado por id",
            "Reiniciar el servidor",
            "Devolver siempre 204 sin contenido y sin cambios"
          ],
          "correcta": [2],
          "feedback_correcta": "La ruta PUT /productos/:id se emplea para actualizar los campos del producto existente identificado por ese id.",
          "feedback_incorrecta": "La semántica habitual de PUT es actualizar o reemplazar el recurso, no crear siempre ni responder sin cambios."
        },
        {
          "id": "E1_P22",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué ventaja tiene mantener los datos de productos y pedidos en estructuras en memoria durante el laboratorio?",
          "opciones": [
            "Permite simular la lógica de negocio sin configurar una base de datos real",
            "Asegura durabilidad de datos entre reinicios",
            "Mejora la seguridad ante ataques externos",
            "Obliga a usar transacciones distribuidas"
          ],
          "correcta": [1],
          "feedback_correcta": "Las estructuras en memoria permiten practicar la lógica y las rutas sin necesidad de configurar una base de datos real.",
          "feedback_incorrecta": "El objetivo de usar estructuras en memoria es simplificar la práctica de lógica y rutas, no garantizar persistencia ni transacciones."
        },
        {
          "id": "E1_P23",
          "tipo": "opcion_multiple",
          "enunciado": "En pruebas con curl o Postman sobre el monolito mínimo, ¿qué opción representa correctamente una petición POST para crear un producto?",
          "opciones": [
            "POST /products sin cuerpo, esperando que el servidor genere los datos",
            "POST /productos con encabezado Content-Type: application/json y un cuerpo JSON con los campos del producto",
            "GET /productos/new con parámetros en la URL",
            "PUT /productos con un cuerpo vacío"
          ],
          "correcta": [2],
          "feedback_correcta": "El patrón adecuado es POST /productos con Content-Type: application/json y un cuerpo JSON con los campos del producto.",
          "feedback_incorrecta": "POST sin cuerpo, GET para crear recursos o PUT vacío no corresponden al patrón principal utilizado para creación en la práctica."
        },
        {
          "id": "E1_P24",
          "tipo": "opcion_multiple",
          "enunciado": "Cuando se extiende el monolito mínimo para manejar recursos “pedidos” además de “productos”, ¿qué principio se refuerza?",
          "opciones": [
            "Que todas las rutas deben compartir el mismo prefijo",
            "La separación de responsabilidades por tipo de recurso en la API",
            "Que solo se puede definir un recurso por servidor",
            "Que los métodos HTTP son intercambiables"
          ],
          "correcta": [2],
          "feedback_correcta": "La extensión a productos y pedidos refuerza la separación de responsabilidades por tipo de recurso en la API.",
          "feedback_incorrecta": "El objetivo no es limitar a un solo recurso por servidor, sino definir rutas claras y separadas para cada tipo de entidad."
        },
        {
          "id": "E1_P25",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál es una diferencia clave entre la API monolítica mínima y una arquitectura de microservicios?",
          "opciones": [
            "En el monolito, todo el código corre en un mismo despliegue; en microservicios se distribuye en servicios independientes",
            "En un monolito no se pueden usar rutas HTTP",
            "Los microservicios no pueden comunicarse vía HTTP",
            "El monolito siempre es más escalable que cualquier microservicio"
          ],
          "correcta": [1],
          "feedback_correcta": "En un monolito el código se despliega como un solo artefacto, mientras que en microservicios se distribuye en servicios independientes.",
          "feedback_incorrecta": "La diferencia central radica en el modelo de despliegue: un artefacto único en el monolito frente a varios servicios autónomos en microservicios."
        }
      ]
    },
    {
      "titulo": "Examen 2 – Tipos de integración, SOAP vs REST, WSDL vs REST, prácticas de integración",
      "preguntas": [
        {
          "id": "E2_P01",
          "tipo": "opcion_multiple",
          "enunciado": "En integración de sistemas, la integración “punto a punto” se caracteriza por:",
          "opciones": [
            "Un bus central que conecta todos los sistemas",
            "Conexiones directas específicas entre cada par de aplicaciones, generando “spaghetti” al crecer",
            "El uso exclusivo de colas de mensajes",
            "La obligación de usar solo SOAP/XML"
          ],
          "correcta": [2],
          "feedback_correcta": "La integración punto a punto se basa en conexiones directas entre pares de sistemas y tiende a generar un esquema tipo “spaghetti” al crecer.",
          "feedback_incorrecta": "En la integración punto a punto no existe un bus central; cada par de sistemas establece su propia integración específica."
        },
        {
          "id": "E2_P02",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué objetivo principal tiene la arquitectura SOA frente al “spaghetti” punto a punto?",
          "opciones": [
            "Aumentar el número de conexiones",
            "Agrupar la lógica en servicios de negocio con contratos claros y reutilizables",
            "Eliminar la necesidad de contratos",
            "Obligar a usar microservicios"
          ],
          "correcta": [2],
          "feedback_correcta": "SOA busca agrupar la lógica en servicios de negocio con contratos claros y reutilizables para reducir el “spaghetti”.",
          "feedback_incorrecta": "El objetivo de SOA no es incrementar conexiones, sino definir servicios reutilizables con contratos bien especificados."
        },
        {
          "id": "E2_P03",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál de las siguientes afirmaciones describe mejor a REST en el contexto de integración?",
          "opciones": [
            "Es un protocolo binario para redes locales",
            "Es un estilo arquitectónico que aprovecha HTTP y trata recursos mediante métodos estándar como GET, POST, PUT, DELETE",
            "Es un lenguaje de programación orientado a objetos",
            "Es un reemplazo obligatorio de SOAP en todos los contextos"
          ],
          "correcta": [2],
          "feedback_correcta": "REST se considera un estilo arquitectónico que utiliza HTTP y trata recursos con métodos como GET, POST, PUT y DELETE.",
          "feedback_incorrecta": "REST no es un protocolo binario ni un lenguaje de programación; se trata de un estilo arquitectónico para APIs."
        },
        {
          "id": "E2_P04",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué ventaja principal aportó REST+JSON en comparación con SOAP/XML para muchas APIs modernas?",
          "opciones": [
            "Mayores requisitos de herramientas especializadas",
            "Contratos más rígidos e inflexibles",
            "Mensajes más ligeros y fáciles de consumir desde navegadores y apps móviles",
            "Imposibilidad de usar HTTPS"
          ],
          "correcta": [3],
          "feedback_correcta": "REST con JSON suele producir mensajes más ligeros y sencillos de consumir en navegadores y aplicaciones móviles.",
          "feedback_incorrecta": "La ventaja típica de REST+JSON es la simplicidad y ligereza de los mensajes, no una mayor rigidez ni requisitos de herramientas pesadas."
        },
        {
          "id": "E2_P05",
          "tipo": "opcion_multiple",
          "enunciado": "En el contexto actual, ¿qué es común encontrar en organizaciones grandes?",
          "opciones": [
            "Solo monolitos puros sin integración",
            "Solo microservicios sin legado",
            "La convivencia de monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos",
            "Exclusivamente colas de mensajes sin APIs"
          ],
          "correcta": [3],
          "feedback_correcta": "En muchas organizaciones grandes coexisten monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos.",
          "feedback_incorrecta": "El panorama real suele mezclar estilos de integración; rara vez se eliminan por completo monolitos o servicios SOAP."
        },
        {
          "id": "E2_P06",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué tipo de integración se centra principalmente en compartir y sincronizar información (por ejemplo, tablas de clientes) entre sistemas?",
          "opciones": [
            "Integración de datos",
            "Integración funcional",
            "Integración semántica",
            "Integración física"
          ],
          "correcta": [1],
          "feedback_correcta": "Cuando se comparten o sincronizan tablas e información entre sistemas se habla de integración de datos.",
          "feedback_incorrecta": "La integración de datos se orienta a replicar y sincronizar información, a diferencia de la integración funcional que consume capacidades remotas."
        },
        {
          "id": "E2_P07",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué tipo de integración implica consumir capacidades o funciones remotas, como “consultar saldo” o “crear pedido”?",
          "opciones": [
            "Integración de datos",
            "Integración funcional",
            "Integración semántica",
            "Integración de red"
          ],
          "correcta": [2],
          "feedback_correcta": "La integración funcional se refiere al consumo de capacidades de negocio remotas, como operaciones de consulta o creación.",
          "feedback_incorrecta": "La integración de datos se centra en tablas e información, mientras que la funcional se enfoca en invocar operaciones de negocio remotas."
        },
        {
          "id": "E2_P08",
          "tipo": "opcion_multiple",
          "enunciado": "¿A qué se refiere la integración semántica?",
          "opciones": [
            "A compartir archivos de texto sin estructura",
            "A alinear el significado de los datos y conceptos entre sistemas, evitando ambigüedades",
            "A comprimir mensajes para ahorrar ancho de banda",
            "A usar siempre el mismo tipo de base de datos"
          ],
          "correcta": [2],
          "feedback_correcta": "La integración semántica se centra en alinear el significado de datos y conceptos entre sistemas para evitar ambigüedades.",
          "feedback_incorrecta": "El problema semántico radica en que términos como “cliente” o “balance” tengan el mismo significado en todos los sistemas involucrados."
        },
        {
          "id": "E2_P09",
          "tipo": "opcion_multiple",
          "enunciado": "En un ejercicio donde se mapean sistemas de una organización y se clasifican sus conexiones, ¿qué criterio se usaría para etiquetar una integración como “crítica”?",
          "opciones": [
            "Que use JSON",
            "Que sea la que más ancho de banda consume",
            "Que, si falla, afecta procesos de negocio esenciales como facturación o pagos",
            "Que sea la más nueva"
          ],
          "correcta": [3],
          "feedback_correcta": "Una integración se considera crítica cuando su fallo impacta procesos esenciales del negocio, como facturación o pagos.",
          "feedback_incorrecta": "El carácter crítico se define por el impacto sobre procesos de negocio clave, no por el formato de mensaje ni por el ancho de banda."
        },
        {
          "id": "E2_P10",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué efecto tiene agregar muchas integraciones punto a punto a lo largo del tiempo?",
          "opciones": [
            "Facilita el mantenimiento porque todas son similares",
            "Disminuye la dependencia entre sistemas",
            "Aumenta la complejidad, la duplicación de lógica y el acoplamiento",
            "Elimina la necesidad de documentación"
          ],
          "correcta": [3],
          "feedback_correcta": "La acumulación de integraciones punto a punto incrementa la complejidad, la duplicación de lógica y el acoplamiento.",
          "feedback_incorrecta": "Un número creciente de integraciones punto a punto suele generar un panorama de “spaghetti” difícil de mantener."
        },
        {
          "id": "E2_P11",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál de las siguientes es una característica típica de SOAP en la era SOA?",
          "opciones": [
            "Uso exclusivo de JSON",
            "Mensajes con sobre <Envelope>, <Header> y <Body> en XML",
            "Eliminación de contratos formales",
            "Comunicación solo dentro de un mismo proceso"
          ],
          "correcta": [2],
          "feedback_correcta": "SOAP se caracteriza por mensajes en XML con elementos Envelope, Header y Body.",
          "feedback_incorrecta": "SOAP no se basa en JSON; su estructura estándar en XML con Envelope, Header y Body es una de sus características distintivas."
        },
        {
          "id": "E2_P12",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué elemento de la pila SOAP describe las operaciones disponibles y los tipos de mensajes?",
          "opciones": [
            "SOAP Envelope",
            "WSDL",
            "UDDI",
            "WS-Security"
          ],
          "correcta": [2],
          "feedback_correcta": "WSDL es el componente que describe operaciones, mensajes y tipos de datos del servicio.",
          "feedback_incorrecta": "En la pila SOAP, WSDL actúa como contrato; SOAP define el protocolo de mensaje y UDDI ofrece un registro de servicios."
        },
        {
          "id": "E2_P13",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué rol jugaron las especificaciones WS-* (como WS-Security, WS-Policy) en el ecosistema SOAP?",
          "opciones": [
            "Definir formatos de imagen",
            "Extender SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones",
            "Reemplazar completamente a WSDL",
            "Hacer innecesario el uso de XML"
          ],
          "correcta": [2],
          "feedback_correcta": "Las especificaciones WS-* extendieron SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones.",
          "feedback_incorrecta": "WS-* no reemplaza WSDL ni define formatos gráficos; añade capacidades empresariales a la pila SOAP."
        },
        {
          "id": "E2_P14",
          "tipo": "opcion_multiple",
          "enunciado": "¿En qué sectores se menciona que SOAP sigue siendo comúnmente utilizado?",
          "opciones": [
            "Redes sociales y aplicaciones de mensajería instantánea",
            "Videojuegos móviles informales",
            "Banca, gobierno y salud con fuertes requisitos regulatorios",
            "Sitios web estáticos"
          ],
          "correcta": [3],
          "feedback_correcta": "SOAP sigue siendo frecuente en banca, gobierno y salud, donde existen requisitos regulatorios y de seguridad estrictos.",
          "feedback_incorrecta": "Estos sectores valoran contratos formales y WS-Security; SOAP no se asocia principalmente con redes sociales o juegos casuales."
        },
        {
          "id": "E2_P15",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál de las siguientes situaciones favorece seguir usando un servicio SOAP existente en lugar de migrarlo inmediatamente a REST?",
          "opciones": [
            "El proveedor solo ofrece WSDL y WS-* y la integración es estable y de largo plazo",
            "La API se usa solo para pruebas internas temporales",
            "Se requiere una interfaz gráfica rica",
            "No hay requisitos de seguridad"
          ],
          "correcta": [1],
          "feedback_correcta": "Cuando el proveedor solo dispone de WSDL y WS-* y la integración es estable y de largo plazo, tiene sentido mantener SOAP.",
          "feedback_incorrecta": "Migrar a REST no siempre es prioritario si la integración SOAP es estable, regulada y responde a necesidades de largo plazo."
        },
        {
          "id": "E2_P16",
          "tipo": "opcion_multiple",
          "enunciado": "¿Cuál es una diferencia conceptual clave entre mensajes SOAP y mensajes REST/JSON?",
          "opciones": [
            "REST/JSON obliga a usar WS-Security",
            "SOAP incluye un sobre estandarizado y namespaces; REST/JSON suele enviar directamente los datos sin esa envoltura",
            "SOAP no permite tipos de datos complejos",
            "REST requiere UDDI"
          ],
          "correcta": [2],
          "feedback_correcta": "SOAP incorpora un sobre estandarizado y namespaces, mientras que REST/JSON suele transmitir directamente los datos sin esa envoltura.",
          "feedback_incorrecta": "REST no obliga al uso de WS-Security ni de UDDI; su formato típico es JSON sin un Envelope estándar como en SOAP."
        },
        {
          "id": "E2_P17",
          "tipo": "opcion_multiple",
          "enunciado": "¿Qué describe mejor a una API REST bien diseñada?",
          "opciones": [
            "Operaciones definidas por verbos arbitrarios en la URL",
            "Recursos identificados por URIs y manipulados con métodos HTTP estándar y códigos de estado apropiados",
            "Mensajes exclusivamente XML",
            "Ausencia total de contrato o documentación"
          ],
          "correcta": [2],
          "feedback_correcta": "Una API REST bien diseñada identifica recursos por URIs y los manipula usando métodos HTTP estándar y códigos de estado coherentes.",
          "feedback_incorrecta": "REST no se limita a la ausencia de contrato; se recomienda documentar recursos, métodos y respuestas de forma explícita."
        },
        {
          "id": "E2_P18",
          "tipo": "opcion_multiple",
          "enunciado": "¿En qué caso es especialmente importante decidir “cuándo convivir con SOAP y encapsularlo, y cuándo migrar a APIs más ligeras”?",
          "opciones": [
            "Cuando solo hay un sistema aislado sin integraciones",
            "Cuando no hay restricciones regulatorias ni de seguridad",
            "Cuando se integran sistemas legacy SOAP con nuevas aplicaciones y microservicios",
            "Cuando todos los servicios ya son REST"
          ],
          "correcta": [3],
          "feedback_correcta": "El dilema entre convivir con SOAP y encapsularlo o migrar a APIs ligeras es especialmente relevante al integrar sistemas SOAP heredados con nuevas aplicaciones y microservicios.",
          "feedback_incorrecta": "Cuando todo el entorno es REST el problema se reduce; la decisión es crítica al coexistir con sistemas SOAP legacy."
        },
        {
          "id": "E2_P19",
          "tipo": "opcion_multiple",
          "enunciado": "En la práctica de “tipos de integración”, un equipo dibuja varios sistemas y marca una integración entre el ERP y el sistema de facturación donde solo se replica la tabla de clientes cada noche. ¿Qué tipo de integración es la más adecuada?",
          "opciones": [
            "Funcional",
            "Semántica",
            "De datos",
            "De red"
          ],
          "correcta": [3],
          "feedback_correcta": "La réplica nocturna de la tabla de clientes corresponde a un caso de integración de datos.",
          "feedback_incorrecta": "En este escenario no se invoca una función de negocio; se copian datos entre sistemas, lo cual encaja con integración de datos."
        },
        {
          "id": "E2_P20",
          "tipo": "opcion_multiple",
          "enunciado": "En esa misma práctica, otra integración permite que una app móvil invoque “consultar saldo” en un sistema bancario remoto. ¿Qué tipo de integración representa mejor esta situación?",
          "opciones": [
            "De datos, porque solo importa la tabla de saldos",
            "Funcional, porque se consume una capacidad remota de negocio",
            "Semántica, porque solo se alinea el significado",
            "Física, porque usa redes móviles"
          ],
          "correcta": [2],
          "feedback_correcta": "La invocación de la operación “consultar saldo” representa un ejemplo de integración funcional.",
          "feedback_incorrecta": "Aquí no se comparten tablas directamente, sino una capacidad de negocio remota; por ello se trata de integración funcional."
        },
        {
          "id": "E2_P21",
          "tipo": "opcion_multiple",
          "enunciado": "En el ejercicio de comparación WSDL vs REST, ¿cuál de estos elementos es más natural encontrar en un WSDL?",
          "opciones": [
            "Definiciones de paths y responses en JSON",
            "Elementos <portType>, <operation> y <message> que describen el contrato",
            "Documentación en formato Markdown",
            "Solo ejemplos de llamadas con curl"
          ],
          "correcta": [2],
          "feedback_correcta": "En un documento WSDL es habitual encontrar elementos como portType, operation y message que describen el contrato.",
          "feedback_incorrecta": "Las definiciones de paths y responses en JSON son propias de OpenAPI y REST, no de WSDL."
        },
        {
          "id": "E2_P22",
          "tipo": "opcion_multiple",
          "enunciado": "En la documentación de una API REST equivalente, ¿qué preguntas se suelen responder de forma explícita?",
          "opciones": [
            "Qué URIs existen, qué métodos HTTP soportan, qué estructura de JSON esperan y devuelven",
            "Cómo generar código a partir de WSDL",
            "Cómo registrar el servicio en UDDI",
            "Cómo usar WS-Security"
          ],
          "correcta": [1],
          "feedback_correcta": "La documentación de una API REST suele precisar qué URIs existen, qué métodos HTTP soportan y qué estructura JSON se espera en solicitudes y respuestas.",
          "feedback_incorrecta": "La generación de código a partir de WSDL y el registro en UDDI pertenecen al ámbito SOAP/WS-*, no a la documentación típica de REST."
        },
        {
          "id": "E2_P23",
          "tipo": "opcion_multiple",
          "enunciado": "Cuando en la práctica se pide comparar un WSDL con una API REST, ¿qué objetivo conceptual se busca?",
          "opciones": [
            "Convertir siempre el WSDL en REST",
            "Identificar elementos de contrato en ambos enfoques y discutir ventajas/desventajas",
            "Demostrar que uno de los dos está obsoleto",
            "Medir solo el tamaño de los mensajes"
          ],
          "correcta": [2],
          "feedback_correcta": "El objetivo consiste en identificar los elementos de contrato en WSDL y REST y reflexionar sobre sus ventajas y desventajas.",
          "feedback_incorrecta": "La intención no es declarar obsoleto a uno de los enfoques, sino comprender cómo cada uno expresa su contrato."
        },
        {
          "id": "E2_P24",
          "tipo": "opcion_multiple",
          "enunciado": "En un escenario donde un servicio SOAP y una API REST exponen la misma funcionalidad de “consultar saldo”, ¿qué diferencia práctica suele encontrarse?",
          "opciones": [
            "El SOAP se consume solo desde navegadores",
            "El WSDL describe tipos y operaciones en XML, mientras que la API REST suele usar JSON y documentación tipo OpenAPI o similar",
            "El SOAP es siempre más rápido",
            "La API REST no puede usar HTTPS"
          ],
          "correcta": [2],
          "feedback_correcta": "En un servicio SOAP la funcionalidad se describe en WSDL mediante XML, mientras que en REST suele documentarse con JSON y especificaciones como OpenAPI.",
          "feedback_incorrecta": "Ambos pueden usar HTTPS; la diferencia suele estar en el formato del contrato (WSDL en XML frente a documentación JSON en REST)."
        },
        {
          "id": "E2_P25",
          "tipo": "opcion_multiple",
          "enunciado": "En un ejercicio grupal, se identifica una integración donde dos sistemas usan el mismo campo “balance” con significados distintos (uno es saldo disponible, otro saldo contable total). ¿Qué tipo de problema se ilustra?",
          "opciones": [
            "Problema de sintaxis XML",
            "Problema de transporte HTTP",
            "Problema de integración semántica",
            "Problema exclusivo de rendimiento"
          ],
          "correcta": [3],
          "feedback_correcta": "El uso distinto del campo “balance” ilustra un problema de integración semántica.",
          "feedback_incorrecta": "En este caso el conflicto no reside en transporte ni en sintaxis, sino en el significado diferente que cada sistema asigna al mismo dato."
        }
      ]
    }
  ]
}
```


---

# <q>2. Generar las imágenes de las preguntas

Opciones:

Python + headless browser (Playwright/Selenium) que renderice HTML generado desde el JSON y saque screenshots.

pandoc + wkhtmltoimage (o weasyprint) para pasar de Markdown/HTML a PNG.

Salida: una imagen por pregunta, con nombre alineado a tu ID (P01.png, etc.).
3. Subir imágenes a Drive programáticamente

Usar la API de Google Drive desde Python para subir los PNG y guardar los IDs públicos.

O hacer esta parte con Google Apps Script: subir a una carpeta, y leer desde un script que cree el Form.

El objetivo: tener un mapa id_pregunta -> URL/ID de archivo de Drive.</q> Cómo hago esto?

Te propongo un flujo concreto en Python “de punta a punta”: JSON → HTML → PNG por pregunta → subir a Drive y devolver un mapa `id_pregunta -> fileId`.

Abajo va todo en modo receta (puedes modularizarlo luego).

***

## 1. Supuestos previos

- Tienes un JSON como el que generamos (`examenes[^7_0].preguntas[*].id/enunciado/opciones/...`).
- Tienes un proyecto de Google Cloud con OAuth habilitado para Drive y un `credentials.json` descargado.
- Tienes Python 3.10+.

Instala dependencias:

```bash
pip install playwright weasyprint google-api-python-client google-auth-httplib2 google-auth-oauthlib
playwright install chromium
```

Puedes usar **Playwright** o **WeasyPrint**; aquí te dejo un ejemplo con WeasyPrint (no necesita navegador) y otro corto con Playwright, para que elijas.

***

## 2. Renderizar cada pregunta a HTML simple

Ejemplo mínimo de función para generar HTML a partir de una pregunta:

```python
def pregunta_a_html(p):
    # p es un dict con id, enunciado, opciones, etc.
    opciones_html = "".join(
        f"<li>{op}</li>" for op in p["opciones"]
    )
    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <style>
          body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 16px;
            margin: 16px;
            max-width: 800px;
          }}
          .id {{ color: #666; font-size: 12px; margin-bottom: 4px; }}
          .enunciado {{ font-weight: 600; margin-bottom: 8px; }}
          ol {{ padding-left: 24px; }}
        </style>
      </head>
      <body>
        <div class="id">{p["id"]}</div>
        <div class="enunciado">{p["enunciado"]}</div>
        <ol type="A">
          {opciones_html}
        </ol>
      </body>
    </html>
    """
    return html
```


***

## 3A. Opción WeasyPrint: HTML → PNG sin navegador

WeasyPrint permite convertir HTML a PNG directamente.[^7_1][^7_2]

```python
import json
import os
from weasyprint import HTML

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
```

Esto te deja, por ejemplo, `outs_imgs/E1_P01.png`, etc.

***

## 3B. Opción Playwright: HTML → PNG con navegador headless

Si prefieres Playwright (más control visual).[^7_3][^7_4]

```python
from playwright.sync_api import sync_playwright
import tempfile
import pathlib

def generar_imagenes_playwright(ruta_json, carpeta_salida="outs_imgs"):
    os.makedirs(carpeta_salida, exist_ok=True)
    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    mapas = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 900, "height": 600})

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
```


***

## 4. Subir PNGs a Google Drive con la API

La guía oficial recomienda usar `google-api-python-client` y OAuth.[^7_5][^7_6]

### 4.1 Autenticación Drive

Crea `credentials.json` en la carpeta del script (desde Google Cloud Console → OAuth client).

```python
from __future__ import print_function
import os.path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

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
```

La primera vez se abre un navegador para autorizar la app; luego se usa `token.json`.

### 4.2 Subir archivos a una carpeta específica

Crea una carpeta en Drive (p. ej. “Preguntas_Examenes”) y copia su ID de la URL.

```python
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
```


***

## 5. Pipeline completo y salida `id_pregunta -> fileId`

Juntas todo en un main:

```python
def main():
    ruta_json = "examenes.json"          # el JSON que ya tienes
    carpeta_png = "outs_imgs"
    folder_drive_id = "TU_FOLDER_ID"     # carpeta en Drive

    # 1) JSON -> PNG por pregunta
    mapa_local = generar_imagenes_desde_json(ruta_json, carpeta_png)
    # o: mapa_local = generar_imagenes_playwright(ruta_json, carpeta_png)

    # 2) PNG -> Drive
    mapa_drive = subir_imagenes_a_drive(mapa_local, folder_drive_id)

    # 3) Guardar el mapa para luego usarlo desde Apps Script / Forms
    with open("mapa_pregunta_drive.json", "w", encoding="utf-8") as f:
        json.dump(mapa_drive, f, ensure_ascii=False, indent=2)

    print("Listo. Mapa id_pregunta -> fileId guardado en mapa_pregunta_drive.json")

if __name__ == "__main__":
    main()
```

`mapa_pregunta_drive.json` se verá algo así:

```json
{
  "E1_P01": "1AbCDEfgHiJKlmNoPqr",
  "E1_P02": "1ZyxWVutsRQPonMLkjh",
  ...
}
```

Ese mapa lo puedes:

- Leer desde tu **Apps Script** y asignar `imagenPreguntaId` en el JSON antes de crear el Form, o
- Incorporarlo directamente en tu JSON fuente (por ejemplo, enriqueciendo cada pregunta con ese `imagenPreguntaId` y volviendo a subir el JSON a Drive para que lo lea el script que te generé.

Si quieres, en el siguiente mensaje puedo darte un pequeño script en Apps Script que:

1. Lee `mapa_pregunta_drive.json` desde Drive.
2. Enriquecería tu JSON de preguntas con `imagenPreguntaId`.
3. Llama a `crearQuizDesdeJson()` con las imágenes ya enlazadas.
<span style="display:none">[^7_10][^7_11][^7_12][^7_13][^7_14][^7_15][^7_7][^7_8][^7_9]</span>

<div align="center">⁂</div>

[^7_1]: https://stackoverflow.com/questions/61155743/weasyprint-html-to-image-conversion-how-to-adapt-image-size-to-content

[^7_2]: https://doc.courtbouillon.org/weasyprint/v0.42.3/tutorial.html

[^7_3]: https://playwright.dev/python/docs/screenshots

[^7_4]: https://www.scrapingbee.com/webscraping-questions/playwright/how-to-take-screenshot-with-playwright/

[^7_5]: https://developers.google.com/workspace/drive/api/guides/manage-uploads

[^7_6]: https://thepythoncode.com/article/using-google-drive--api-in-python

[^7_7]: https://playwright.dev/docs/screenshots

[^7_8]: https://www.htmltoimage.com/python/playwright

[^7_9]: https://playwright.help/python/docs/screenshots

[^7_10]: https://www.youtube.com/watch?v=NfQw_JxIDQg

[^7_11]: https://stackoverflow.com/questions/60182791/how-to-upload-a-file-to-google-drive-using-python-and-the-drive-api-v3

[^7_12]: https://www.youtube.com/watch?v=NfQw_JxIDQg\&vl=en

[^7_13]: https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python

[^7_14]: https://www.youtube.com/watch?v=oxYrUPoEcG8

[^7_15]: https://urlbox.com/html-to-png-with-python


---

# <q>Tienes un proyecto de Google Cloud con OAuth habilitado para Drive y un credentials.json descargado.</q> Que significa esto?

Significa “darle permiso oficial a tu script para usar la API de Drive en tu cuenta de Google”. En la práctica son estos pasos, una sola vez:

### 1. Crear un proyecto en Google Cloud

1. Entra a https://console.cloud.google.com (con tu cuenta de Google).
2. Arriba, selecciona “Seleccionar proyecto” → “Nuevo proyecto”.
3. Ponle un nombre (por ejemplo, `ExamenesDrive`) y crea el proyecto.

### 2. Habilitar la API de Google Drive

1. Dentro de ese proyecto, ve a “APIs y servicios” → “Biblioteca”.
2. Busca “Google Drive API”.
3. Entra y haz clic en “Habilitar”.

### 3. Configurar la pantalla de consentimiento OAuth

1. En “APIs y servicios” → “Pantalla de consentimiento OAuth”.
2. Tipo de usuario: “Externa” (aunque solo la uses tú) y sigue el asistente:
    - Nombre de la app (por ejemplo, `Script Examenes`).
    - Correo de soporte y desarrollador (tu correo).
3. Guarda hasta terminar (no hace falta publicar la app para uso personal).

### 4. Crear credenciales OAuth y bajar `credentials.json`

1. Ve a “APIs y servicios” → “Credenciales”.
2. “+ Crear credenciales” → “ID de cliente de OAuth”.
3. Tipo de aplicación: **Aplicación de escritorio** (ideal para tu script local).
4. Pon un nombre (por ejemplo, `Desktop Examenes`) y crea.
5. En la lista de credenciales, en esa que acabas de crear:
    - Haz clic en el ícono de descarga (JSON).
    - Guarda el archivo y renómbralo a `credentials.json` en la carpeta de tu script de Python.

Ese archivo `credentials.json` contiene el `client_id` y `client_secret` de tu app. Tu script lo usa para abrir una ventana de autorización la primera vez; tú haces login con tu cuenta de Google, aceptas el permiso de Drive, y luego el script guarda un `token.json` para no pedirte permiso cada vez.

Con eso, ya está cumplido el requisito de “tener un proyecto de Google Cloud con OAuth habilitado para Drive y un credentials.json descargado”.
<span style="display:none">[^8_1][^8_10][^8_2][^8_3][^8_4][^8_5][^8_6][^8_7][^8_8][^8_9]</span>

<div align="center">⁂</div>

[^8_1]: https://developers.google.com/workspace/drive/api/guides/api-specific-auth?hl=es-419

[^8_2]: https://developers.google.com/identity/protocols/oauth2/web-server?hl=es-419

[^8_3]: https://www.youtube.com/watch?v=muDL3hkcgaY

[^8_4]: https://www.youtube.com/watch?v=P-jlIVq8DhQ

[^8_5]: https://docs.globant.ai/es/wiki?212%2CHerramientas+de+Google+Drive+–+Flujo+de+autorización+OAuth+(OAuth+Authorization+Flow)

[^8_6]: https://es.stackoverflow.com/questions/4246/como-autorizar-el-acceso-a-google-drive-con-oauth2

[^8_7]: https://automatizatutrabajo.com/manual-credenciales-google-drive/

[^8_8]: https://help.scriptcase.net/portal/es/kb/articles/habilitacion-de-la-api-de-google-drive-en-google-console

[^8_9]: https://ai.google.dev/palm_docs/oauth_quickstart?hl=es-419

[^8_10]: https://docs.logicaldoc.com/es/google-drive/configuring-google-api


---

# <q>tener un proyecto de Google Cloud con OAuth habilitado para Drive y un credentials.json descargado</q> Esto tiene costo?

No, para lo que quieres, en la práctica es **gratis**.

- La **API de Google Drive** no tiene costo adicional por uso; trabajar con ella está incluido en tu cuenta de Google.[^9_1]
- Sí existen **límites de cuota** (número de peticiones por día), pero son muy altos para un uso como “subir imágenes de exámenes” y si alguna vez los superaras, no se te cobra, simplemente se limita temporalmente.[^9_2][^9_1]
- Lo único que podría tener costo es:
    - Si usas **Google Cloud Storage** (producto diferente de Drive) o servicios de cómputo de Google Cloud a gran escala, que sí tienen precios propios.[^9_3][^9_4]
    - Si tu Drive personal/Workspace se queda sin espacio de almacenamiento (lo mismo que al subir archivos manualmente).
<span style="display:none">[^9_10][^9_11][^9_12][^9_13][^9_14][^9_15][^9_5][^9_6][^9_7][^9_8][^9_9]</span>

<div align="center">⁂</div>

[^9_1]: https://developers.google.com/workspace/drive/api/guides/limits?hl=es-419

[^9_2]: https://developers.google.com/workspace/drive/api/guides/limits

[^9_3]: https://cloud.google.com/pricing/list?hl=es

[^9_4]: https://cloud.google.com/storage/pricing

[^9_5]: https://cloud.google.com/api-gateway/pricing?hl=es-419

[^9_6]: https://translate.google.com/translate?u=https%3A%2F%2Fdocs.cloud.google.com%2Fbilling%2Fdocs%2Freference%2Fpricing-api%2Frest\&hl=es\&sl=en\&tl=es\&client=srp

[^9_7]: https://console.cloud.google.com/apis/library/drive.googleapis.com?hl=es-419

[^9_8]: https://stackoverflow.com/questions/14156781/where-can-i-find-the-price-list-for-google-drive-api

[^9_9]: https://ai.google.dev/gemini-api/docs/pricing

[^9_10]: https://stackoverflow.com/questions/67098285/what-is-the-difference-between-google-cloud-storage-api-and-google-drive-api

[^9_11]: https://cloud.google.com/billing/docs/reference/pricing-api/rest

[^9_12]: https://docs.cloud.google.com/api-keys/docs/quotas

[^9_13]: https://www.youtube.com/watch?v=_Y_0uHJI_xU

[^9_14]: https://developers.google.com/workspace/sheets/api/limits

[^9_15]: https://www.googlecloudcommunity.com/gc/Cloud-Hub/Costs-of-using-drive-and-docs-api-in-my-company/m-p/651040


---

# estoy usando generar_imagenes_desde_json y da como resultado o siguiente: OSError: cannot load library 'libgobject-2.0-0': dlopen(libgobject-2.0-0, 0x0002): tried: 'libgobject-2.0-0' (no such file), '/System/Volumes/Preboot/Cryptexes/OSlibgobject-2.0-0' (no such file), '/Users/juanalvarado/opt/miniconda3/envs/examenesDrive/bin/../lib/libgobject-2.0-0' (no such file), '/usr/lib/libgobject-2.0-0' (no such file, not in dyld cache), 'libgobject-2.0-0' (no such file).  Additionally, ctypes.util.find_library() did not manage to locate a library called 'libgobject-2.0-0'

Ese error es típico de WeasyPrint en macOS: le faltan librerías de GTK/GLib (gobject). Solución rápida: en vez de pelear con eso, te conviene cambiar a la opción Playwright para generar las imágenes.

### Opción recomendada: usar Playwright (evitas gobject/WeasyPrint)

1. Instala Playwright (si no lo hiciste):
```bash
pip install playwright
playwright install chromium
```

2. Usa esta versión de `generar_imagenes_playwright` en lugar de `generar_imagenes_desde_json`:
```python
import json
import os
import tempfile
import pathlib
from playwright.sync_api import sync_playwright

def pregunta_a_html(p):
    opciones_html = "".join(
        f"<li>{op}</li>" for op in p["opciones"]
    )
    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <style>
          body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 16px;
            margin: 16px;
            max-width: 800px;
          }}
          .id {{ color: #666; font-size: 12px; margin-bottom: 4px; }}
          .enunciado {{ font-weight: 600; margin-bottom: 8px; }}
          ol {{ padding-left: 24px; }}
        </style>
      </head>
      <body>
        <div class="id">{p["id"]}</div>
        <div class="enunciado">{p["enunciado"]}</div>
        <ol type="A">
          {opciones_html}
        </ol>
      </body>
    </html>
    """
    return html

def generar_imagenes_playwright(ruta_json, carpeta_salida="outs_imgs"):
    os.makedirs(carpeta_salida, exist_ok=True)
    with open(ruta_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    mapas = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 900, "height": 600})

        for examen in data["examenes"]:
            for p_ in examen["preguntas"]:
                html = pregunta_a_html(p_)
                tmp_html = pathlib.Path(tempfile.gettempdir()) / f"{p_['id']}.html"
                tmp_html.write_text(html, encoding="utf-8")

                page.goto(tmp_html.as_uri())
                file_name = f"{p_['id']}.png"
                path = os.path.join(carpeta_salida, file_name)
                page.screenshot(path=path, full_page=True)
                mapas.append({"id_pregunta": p_["id"], "path": path})

        browser.close()
    return mapas
```

Y en tu `main` reemplaza:

```python
mapa_local = generar_imagenes_desde_json(ruta_json, carpeta_png)
```

por:

```python
mapa_local = generar_imagenes_playwright(ruta_json, carpeta_png)
```

Con eso evitas completamente la dependencia `libgobject-2.0-0` y el error desaparece.[^10_1][^10_2][^10_3]

***

### Si aun así quieres insistir con WeasyPrint

En macOS tendrías que:

- Instalar dependencias con Homebrew (cairo, pango, gobject, etc.).[^10_4][^10_5][^10_6]
- Asegurarte de exportar `DYLD_FALLBACK_LIBRARY_PATH` apuntando a la carpeta de libs de Homebrew cuando ejecutas Python.[^10_7][^10_8]

Pero para tu objetivo (renderizar HTML sencillo a PNG para exámenes) Playwright es mucho menos dolor.
<span style="display:none">[^10_10][^10_11][^10_12][^10_13][^10_14][^10_15][^10_16][^10_17][^10_18][^10_9]</span>

<div align="center">⁂</div>

[^10_1]: https://playwright.dev/python/docs/screenshots

[^10_2]: https://www.htmltoimage.com/python/playwright

[^10_3]: https://www.scrapingbee.com/webscraping-questions/playwright/how-to-take-screenshot-with-playwright/

[^10_4]: https://www.pythontutorials.net/blog/gobject-2-0-0-not-able-to-load-on-macbook/

[^10_5]: https://macappstore.org/gobject-introspection/

[^10_6]: https://formulae.brew.sh/formula/gobject-introspection

[^10_7]: https://github.com/Kozea/WeasyPrint/issues/2427

[^10_8]: https://stackoverflow.com/questions/69097224/gobject-2-0-0-not-able-to-load-on-macbook/69295303

[^10_9]: https://github.com/Kozea/WeasyPrint/issues/1448

[^10_10]: https://www.youtube.com/watch?v=dYR75vxY1ho

[^10_11]: https://stackoverflow.com/questions/69067530/how-to-solve-weasyprint-error-message-gobject-2-0-0-error-0x7e-message

[^10_12]: https://stackoverflow.com/questions/71352437/cannot-load-library-gobject-2-0-0

[^10_13]: https://github.com/Kozea/WeasyPrint/issues/1556

[^10_14]: https://github.com/Kozea/WeasyPrint/issues/971

[^10_15]: https://www.youtube.com/watch?v=VS6mxHAwweE

[^10_16]: https://macappstore.org/pygobject/

[^10_17]: https://www.youtube.com/watch?v=uz1igVVp8vY

[^10_18]: https://github.com/Kozea/WeasyPrint/issues/1600


---

```
# <q>Aquí tienes el JSON con los dos exámenes, incluyendo ids, tipo (todas opción múltiple), clave correcta y feedback reescrito en forma impersonal.</q> dame el json reestructurado de la siguiente manera, el formato está bien, pero las preguntas no deben tener relación entre ellas ni con contenidos/prácticas especificos del curso, por ejemplo,  E2_P19, habla de la "practica de tipos de integración", eso fue especifico de una clase, la pregunta E2_P20, empieza diciendo "En la misma práctica", pero las preguntas se presentarán aleatoriamente, con lo que este enunciado pierde sentido, en la pregunta E2_P21 dice ""En el ejercicio de comparación WSDL vs REST,", otra vez muy expecifico de la clase. Las preguntas deben estar relacionadas con lo visto en clase, pero no deben preguntar cosas de clase sobre todo no las practicas ni actividades, los conceptos teóricos sí, pero no las actividades. En lugar de reusar las actividades de clase y para hacer cada pregunta independiente genera las preguntas con un breve contexto.
```

Aquí está el JSON reestructurado con todas las preguntas independientes, sin referencias a actividades/prácticas/“en este ejercicio”, pero manteniendo los mismos conceptos teóricos. Cada pregunta incluye un contexto breve cuando hace falta.

```json
{
  "examenes": [
    {
      "titulo": "Examen 1 – SOAP, XML/XSD, WSDL y monolito mínimo Node.js",
      "preguntas": [
        {
          "id": "E1_P01",
          "tipo": "opcion_multiple",
          "enunciado": "En un servicio bancario basado en SOAP, se requiere enviar información de cuentas y transacciones entre sistemas heterogéneos. ¿Cuál es el propósito principal de usar XML en este tipo de servicios web?",
          "opciones": [
            "Reducir el tamaño de los mensajes de red",
            "Representar datos estructurados de forma jerárquica y validable mediante esquemas",
            "Asegurar que todos los mensajes sean binarios",
            "Evitar el uso de HTTP como transporte"
          ],
          "correcta": [2],
          "feedback_correcta": "XML se utiliza para representar datos jerárquicos y validables, lo cual resulta fundamental en mensajes SOAP.",
          "feedback_incorrecta": "XML en servicios web se valora por su estructura jerárquica y la posibilidad de validación mediante XSD, no por reducción de tamaño ni por ser binario."
        },
        {
          "id": "E1_P02",
          "tipo": "opcion_multiple",
          "enunciado": "Una compañía de seguros intercambia pólizas en formato XML entre aplicaciones internas. Antes de validar el contenido con XSD, se verifica que el XML esté bien formado. ¿Qué característica define que el documento XML esté bien formado?",
          "opciones": [
            "Tener solo elementos de tipo string",
            "Usar siempre el mismo prefijo de espacio de nombres",
            "Tener un único elemento raíz y etiquetas correctamente anidadas y cerradas",
            "Incluir al menos un atributo en cada elemento"
          ],
          "correcta": [3],
          "feedback_correcta": "Un XML bien formado se caracteriza por tener un único elemento raíz y etiquetas bien anidadas y cerradas.",
          "feedback_incorrecta": "Las reglas de documento XML bien formado exigen un único elemento raíz y etiquetas correctamente anidadas y cerradas."
        },
        {
          "id": "E1_P03",
          "tipo": "opcion_multiple",
          "enunciado": "En el XSD que describe los mensajes de un servicio de pedidos, algunos campos representan valores simples (como cantidades o precios) y otros representan estructuras completas (como dirección de envío con calle, ciudad y código postal). ¿Qué diferencia hay entre un tipo simple y un tipo complejo en XSD en este contexto?",
          "opciones": [
            "El tipo simple solo se usa para atributos, el complejo solo para elementos",
            "El tipo simple describe valores atómicos; el complejo agrupa elementos y atributos anidados",
            "El tipo complejo solo se usa en WSDL, el simple solo en XML",
            "No hay diferencia; ambos se usan indistintamente"
          ],
          "correcta": [2],
          "feedback_correcta": "Los tipos simples describen valores atómicos y los tipos complejos agrupan elementos y atributos.",
          "feedback_incorrecta": "La diferencia clave es que el tipo simple representa un valor atómico y el tipo complejo define estructuras con elementos y/o atributos."
        },
        {
          "id": "E1_P04",
          "tipo": "opcion_multiple",
          "enunciado": "Una empresa define un contrato formal para su servicio SOAP de facturación y necesita asegurarse de que todos los mensajes cumplan la misma estructura. ¿Cuál es el rol de XSD en el contexto de WSDL y servicios SOAP en este escenario?",
          "opciones": [
            "Optimizar el rendimiento del servidor HTTP",
            "Describir la estructura y tipos de los mensajes XML que intercambia el servicio",
            "Registrar servicios en directorios públicos",
            "Gestionar la seguridad y el cifrado de los mensajes"
          ],
          "correcta": [2],
          "feedback_correcta": "XSD se utiliza para describir la estructura y los tipos de datos de los mensajes XML de un servicio.",
          "feedback_incorrecta": "XSD no se orienta a rendimiento HTTP ni a seguridad; su finalidad es definir estructura y tipos de datos de los mensajes."
        },
        {
          "id": "E1_P05",
          "tipo": "opcion_multiple",
          "enunciado": "Un equipo de integración recibe un archivo que describe las operaciones disponibles de un servicio SOAP de inventarios, los mensajes que usa y los endpoints a los que puede conectarse. El archivo está definido en XML. ¿Qué describe mejor a este archivo?",
          "opciones": [
            "Un formato ligero de datos alternativo a JSON",
            "Un protocolo de transporte para servicios web",
            "Un lenguaje basado en XML que describe operaciones, mensajes, tipos de datos y endpoints de un servicio",
            "Una base de datos de servicios web en la nube"
          ],
          "correcta": [3],
          "feedback_correcta": "WSDL es un lenguaje basado en XML para describir operaciones, mensajes, tipos y endpoints de un servicio.",
          "feedback_incorrecta": "WSDL no es un formato de datos ni un protocolo; es un contrato descriptivo basado en XML."
        },
        {
          "id": "E1_P06",
          "tipo": "opcion_multiple",
          "enunciado": "En un mensaje SOAP que devuelve el resultado de una consulta de cliente, se define un sobre con espacios de nombres y se agregan secciones opcionales según sea necesario. ¿Qué elemento es obligatorio en ese mensaje SOAP?",
          "opciones": [
            "soap:Header",
            "soap:Body",
            "soap:Fault",
            "soap:Security"
          ],
          "correcta": [2],
          "feedback_correcta": "En un mensaje SOAP, el elemento Body es obligatorio, mientras que Header y Fault son opcionales.",
          "feedback_incorrecta": "El elemento obligatorio en SOAP es el Body; Header y Fault solo aparecen cuando se requieren."
        },
        {
          "id": "E1_P07",
          "tipo": "opcion_multiple",
          "enunciado": "Una organización desea que sus clientes internos puedan generar clientes SOAP y stubs de servidor automáticamente a partir de un contrato centralizado, reduciendo errores de integración. ¿Qué ventaja clave ofrece el uso de WSDL con contratos estrictos para este fin?",
          "opciones": [
            "Permite cambiar la estructura de los mensajes sin coordinar con los consumidores",
            "Facilita la generación de código cliente/servidor y la validación automática de mensajes",
            "Elimina la necesidad de usar XML",
            "Permite que el servicio sea completamente stateless sin esfuerzo"
          ],
          "correcta": [2],
          "feedback_correcta": "Los contratos estrictos en WSDL facilitan la generación de código y la validación automática de mensajes.",
          "feedback_incorrecta": "La principal ventaja de contratos estrictos en WSDL es la generación de código y la validación automática, aunque exigen disciplina al evolucionar."
        },
        {
          "id": "E1_P08",
          "tipo": "opcion_multiple",
          "enunciado": "Un proveedor de servicios expone varios servicios SOAP y desea que sus consumidores externos puedan encontrarlos y consultarlos a través de un catálogo público. En la pila clásica basada en SOAP, ¿qué componente se diseñó con este propósito?",
          "opciones": [
            "SOAP",
            "WSDL",
            "UDDI",
            "WS-Security"
          ],
          "correcta": [3],
          "feedback_correcta": "UDDI se diseñó como registro para publicar y descubrir servicios web.",
          "feedback_incorrecta": "En la pila SOAP, SOAP es el protocolo de mensajería, WSDL describe el contrato y UDDI actúa como registro o catálogo."
        },
        {
          "id": "E1_P09",
          "tipo": "opcion_multiple",
          "enunciado": "Un arquitecto compara el diseño de una integración basada en SOAP con otra basada en REST para exponer un catálogo de productos. ¿Cuál de las siguientes afirmaciones describe mejor la diferencia típica entre ambos enfoques?",
          "opciones": [
            "SOAP usa típicamente XML y contratos formales; REST suele usar JSON y contratos más ligeros",
            "SOAP y REST siempre usan JSON",
            "REST requiere UDDI para descubrir servicios",
            "SOAP no puede usar HTTP como transporte"
          ],
          "correcta": [1],
          "feedback_correcta": "SOAP suele usar XML y contratos formales, mientras que REST tiende a emplear JSON y contratos más ligeros.",
          "feedback_incorrecta": "REST no requiere UDDI y SOAP no se limita en absoluto a JSON; REST se caracteriza por mensajes ligeros y menor rigidez contractual."
        },
        {
          "id": "E1_P10",
          "tipo": "opcion_multiple",
          "enunciado": "Una institución financiera evalúa exponer una operación de pagos a largo plazo con fuertes requisitos de auditoría y seguridad basada en WS-Security. ¿En qué contexto sigue siendo razonable preferir SOAP en lugar de solo APIs REST?",
          "opciones": [
            "Aplicaciones móviles sin requisitos de seguridad",
            "Prototipos rápidos con cambios frecuentes de contrato",
            "Integraciones reguladas de largo plazo con contratos muy estructurados y WS-Security",
            "Sitios estáticos de contenido público"
          ],
          "correcta": [3],
          "feedback_correcta": "SOAP resulta razonable en integraciones reguladas y de largo plazo con contratos muy estructurados y uso de WS-Security.",
          "feedback_incorrecta": "SOAP encaja mejor en escenarios con requisitos fuertes de seguridad, contratos estables y uso de WS-Security que en prototipos cambiantes."
        },
        {
          "id": "E1_P11",
          "tipo": "opcion_multiple",
          "enunciado": "Un servicio SOAP devuelve la información de un producto en respuesta a una consulta por su identificador. El modelo de datos del producto en JSON es { \"id\": 1, \"name\": \"Laptop\", \"price\": 25000.0 }. ¿Cuál sería el elemento principal más adecuado en el Body del mensaje SOAP de respuesta?",
          "opciones": [
            "<GetProductRequest>",
            "<ProductResponse> o equivalente que agrupe los datos del producto",
            "<ErrorResponse>",
            "<EnvelopeProduct>"
          ],
          "correcta": [2],
          "feedback_correcta": "El Body suele contener un elemento que agrupa los datos del producto, como ProductResponse o equivalente.",
          "feedback_incorrecta": "En el Body no se usan elementos de petición cuando se trata de una respuesta; tampoco se emplea un envoltorio como EnvelopeProduct para los datos."
        },
        {
          "id": "E1_P12",
          "tipo": "opcion_multiple",
          "enunciado": "Una integración revisa la estructura de los mensajes SOAP que intercambia un sistema de reservas. Se observa que cada mensaje tiene un sobre con un cuerpo y, en algunos casos, un encabezado adicional. ¿Qué combinación describe mejor un mensaje SOAP bien formado en este contexto?",
          "opciones": [
            "Un único <soap:Envelope> con <soap:Header> y <soap:Body> internos",
            "Varios <soap:Envelope> anidados para cada elemento del producto",
            "Un <soap:Body> sin <soap:Envelope>",
            "Un XML sin namespaces para simplificar"
          ],
          "correcta": [1],
          "feedback_correcta": "Un mensaje SOAP bien formado tiene un único Envelope que contiene Header opcional y Body obligatorio.",
          "feedback_incorrecta": "En SOAP no se anidan múltiples Envelopes y siempre debe existir un Envelope que encapsule Header y Body."
        },
        {
          "id": "E1_P13",
          "tipo": "opcion_multiple",
          "enunciado": "En un sistema de facturación, se valida un mensaje SOAP de factura contra el XSD correspondiente. El validador indica que el elemento <price> no es numérico. ¿Qué significa este resultado?",
          "opciones": [
            "El WSDL está mal escrito",
            "El XML no es bien formado",
            "El valor del elemento no cumple el tipo de dato definido en el XSD",
            "El servidor HTTP está caído"
          ],
          "correcta": [3],
          "feedback_correcta": "El mensaje indica que el valor del elemento no cumple el tipo de dato definido en el XSD, aunque el XML pueda ser bien formado.",
          "feedback_incorrecta": "Es necesario distinguir entre XML bien formado y XML válido frente a XSD; en este caso el problema es de tipo de dato, no de sintaxis."
        },
        {
          "id": "E1_P14",
          "tipo": "opcion_multiple",
          "enunciado": "Un integrador recibe un WSDL de un servicio de clientes que incluye los tipos XSD embebidos en la sección <types>. Se desea validar ejemplos de mensajes antes de poner el sistema en producción. ¿Qué se debe hacer para validar un mensaje XML contra esos tipos?",
          "opciones": [
            "Ignorar la sección <types> y validar solo con el navegador",
            "Extraer o referenciar el XSD de la sección <types> y usarlo como esquema en un validador XML/XSD",
            "Convertir el WSDL a JSON y validarlo con OpenAPI",
            "No es posible validar mensajes usando un WSDL"
          ],
          "correcta": [2],
          "feedback_correcta": "El XSD embebido en la sección types puede extraerse o referenciarse y usarse en un validador XML/XSD.",
          "feedback_incorrecta": "El WSDL sí permite validar mensajes, extrayendo o referenciando sus XSD; la sección types no debe ignorarse."
        },
        {
          "id": "E1_P15",
          "tipo": "opcion_multiple",
          "enunciado": "Durante la integración de un sistema de pagos, se recibe un mensaje SOAP con una estructura <soap:Fault> que incluye un código y una descripción de error. ¿Para qué se utiliza principalmente un elemento Fault en un mensaje SOAP?",
          "opciones": [
            "Enviar datos de negocio adicionales",
            "Configurar la autenticación del servicio",
            "Establecer una conexión persistente",
            "Comunicar errores de procesamiento con código, motivo y detalles"
          ],
          "correcta": [4],
          "feedback_correcta": "La estructura Fault se emplea para comunicar errores de procesamiento con código, motivo y detalles.",
          "feedback_incorrecta": "Fault no transmite datos de negocio ni configuraciones; su propósito es estandarizar la información de error."
        },
        {
          "id": "E1_P16",
          "tipo": "opcion_multiple",
          "enunciado": "Se construye una API sencilla con Node.js y Express para gestionar productos y pedidos en memoria durante el desarrollo. ¿Qué característica describe mejor las rutas iniciales de este monolito mínimo?",
          "opciones": [
            "Solo exponen métodos GET y POST para recursos como productos y pedidos en memoria",
            "Incluyen persistencia en base de datos relacional",
            "Exponen exclusivamente métodos PUT y DELETE",
            "Usan colas de mensajes en lugar de HTTP"
          ],
          "correcta": [1],
          "feedback_correcta": "El monolito mínimo inicia con rutas GET y POST en memoria para recursos como productos y pedidos.",
          "feedback_incorrecta": "En la configuración inicial no se usa base de datos ni únicamente PUT/DELETE; el enfoque es un CRUD simple en memoria."
        },
        {
          "id": "E1_P17",
          "tipo": "opcion_multiple",
          "enunciado": "En una API REST construida con Express, se configura middleware para procesar el cuerpo de las solicitudes que llegan en formato JSON. ¿Cuál es el propósito de usar app.use(express.json()) en este contexto?",
          "opciones": [
            "Permitir que Express sirva archivos estáticos",
            "Habilitar el parseo automático de cuerpos JSON en las peticiones",
            "Configurar el motor de plantillas HTML",
            "Asegurar la conexión HTTPS"
          ],
          "correcta": [2],
          "feedback_correcta": "La función express.json() permite parsear automáticamente cuerpos JSON en las solicitudes.",
          "feedback_incorrecta": "express.json() no se relaciona con archivos estáticos ni con HTTPS; su función es procesar cuerpos JSON."
        },
        {
          "id": "E1_P18",
          "tipo": "opcion_multiple",
          "enunciado": "Una API expone la ruta GET /productos/:id para recuperar un producto específico a partir de su identificador. En Express, ¿cómo se denomina el segmento :id en esta ruta?",
          "opciones": [
            "Query string",
            "Middleware",
            "Parámetro de ruta",
            "Header obligatorio"
          ],
          "correcta": [3],
          "feedback_correcta": "El segmento :id se conoce como parámetro de ruta en Express.",
          "feedback_incorrecta": "Es importante diferenciar los parámetros de ruta (/recurso/:id) de la query string (?id=...) y de los encabezados."
        },
        {
          "id": "E1_P19",
          "tipo": "opcion_multiple",
          "enunciado": "Se desea permitir que un cliente elimine un producto específico a través de una API REST. ¿Cuál de las siguientes rutas HTTP es más apropiada para implementar esta operación en un diseño basado en recursos?",
          "opciones": [
            "DELETE /productos",
            "DELETE /productos/:id",
            "GET /productos/delete",
            "POST /productos/remove/:id"
          ],
          "correcta": [2],
          "feedback_correcta": "La convención REST indica que DELETE /productos/:id es la forma adecuada de eliminar un recurso específico.",
          "feedback_incorrecta": "El patrón habitual es enviar DELETE sobre la URI del recurso concreto, no sobre rutas genéricas ni sobre GETs simulando borrado."
        },
        {
          "id": "E1_P20",
          "tipo": "opcion_multiple",
          "enunciado": "Una solicitud GET /productos/999 intenta recuperar un producto que no existe en la colección gestionada por la API. ¿Qué código de estado HTTP es más apropiado devolver en este caso?",
          "opciones": [
            "200 OK con un cuerpo vacío",
            "201 Created",
            "404 Not Found",
            "500 Internal Server Error"
          ],
          "correcta": [3],
          "feedback_correcta": "El código 404 Not Found es el más adecuado cuando el recurso solicitado por id no existe.",
          "feedback_incorrecta": "El código 200 implica éxito con un recurso; cuando el recurso no se encuentra, el código estándar es 404."
        },
        {
          "id": "E1_P21",
          "tipo": "opcion_multiple",
          "enunciado": "Una API REST para productos ofrece la ruta PUT /productos/:id. El cliente envía un cuerpo JSON con los campos actualizados de un producto existente. ¿Cuál es el comportamiento esperado de esta operación según las prácticas habituales?",
          "opciones": [
            "Crear siempre un producto nuevo sin importar si existe",
            "Actualizar los campos del producto existente identificado por id",
            "Reiniciar el servidor",
            "Devolver siempre 204 sin contenido y sin cambios"
          ],
          "correcta": [2],
          "feedback_correcta": "La ruta PUT /productos/:id se emplea para actualizar los campos del producto existente identificado por ese id.",
          "feedback_incorrecta": "La semántica habitual de PUT es actualizar o reemplazar el recurso, no crear siempre ni responder sin cambios."
        },
        {
          "id": "E1_P22",
          "tipo": "opcion_multiple",
          "enunciado": "Durante el desarrollo de una API de ejemplo, se decide mantener los datos de productos y pedidos en estructuras de memoria en lugar de una base de datos. ¿Qué ventaja principal ofrece este enfoque en un entorno de laboratorio?",
          "opciones": [
            "Permite simular la lógica de negocio sin configurar una base de datos real",
            "Asegura durabilidad de datos entre reinicios",
            "Mejora la seguridad ante ataques externos",
            "Obliga a usar transacciones distribuidas"
          ],
          "correcta": [1],
          "feedback_correcta": "Las estructuras en memoria permiten practicar la lógica y las rutas sin necesidad de configurar una base de datos real.",
          "feedback_incorrecta": "El objetivo de usar estructuras en memoria es simplificar la práctica de lógica y rutas, no garantizar persistencia ni transacciones."
        },
        {
          "id": "E1_P23",
          "tipo": "opcion_multiple",
          "enunciado": "Un cliente HTTP utiliza curl o Postman para crear un nuevo producto en una API REST. ¿Qué configuración representa correctamente una petición POST adecuada para este propósito?",
          "opciones": [
            "POST /products sin cuerpo, esperando que el servidor genere los datos",
            "POST /productos con encabezado Content-Type: application/json y un cuerpo JSON con los campos del producto",
            "GET /productos/new con parámetros en la URL",
            "PUT /productos con un cuerpo vacío"
          ],
          "correcta": [2],
          "feedback_correcta": "El patrón adecuado es POST /productos con Content-Type: application/json y un cuerpo JSON con los campos del producto.",
          "feedback_incorrecta": "POST sin cuerpo, GET para crear recursos o PUT vacío no corresponden al patrón principal utilizado para creación en la práctica."
        },
        {
          "id": "E1_P24",
          "tipo": "opcion_multiple",
          "enunciado": "Una API REST de una tienda en línea expone recursos como /productos y /pedidos, cada uno con sus propias rutas y lógica. ¿Qué principio de diseño se refuerza al separar las rutas por tipo de recurso?",
          "opciones": [
            "Que todas las rutas deben compartir el mismo prefijo",
            "La separación de responsabilidades por tipo de recurso en la API",
            "Que solo se puede definir un recurso por servidor",
            "Que los métodos HTTP son intercambiables"
          ],
          "correcta": [2],
          "feedback_correcta": "La extensión a productos y pedidos refuerza la separación de responsabilidades por tipo de recurso en la API.",
          "feedback_incorrecta": "El objetivo no es limitar a un solo recurso por servidor, sino definir rutas claras y separadas para cada tipo de entidad."
        },
        {
          "id": "E1_P25",
          "tipo": "opcion_multiple",
          "enunciado": "Una empresa evalúa migrar una aplicación monolítica de comercio electrónico a una arquitectura de microservicios. ¿Cuál es una diferencia clave entre la API monolítica mínima y una arquitectura de microservicios en este escenario?",
          "opciones": [
            "En el monolito, todo el código corre en un mismo despliegue; en microservicios se distribuye en servicios independientes",
            "En un monolito no se pueden usar rutas HTTP",
            "Los microservicios no pueden comunicarse vía HTTP",
            "El monolito siempre es más escalable que cualquier microservicio"
          ],
          "correcta": [1],
          "feedback_correcta": "En un monolito el código se despliega como un solo artefacto, mientras que en microservicios se distribuye en servicios independientes.",
          "feedback_incorrecta": "La diferencia central radica en el modelo de despliegue: un artefacto único en el monolito frente a varios servicios autónomos en microservicios."
        }
      ]
    },
    {
      "titulo": "Examen 2 – Tipos de integración, SOAP vs REST, WSDL vs REST, prácticas de integración",
      "preguntas": [
        {
          "id": "E2_P01",
          "tipo": "opcion_multiple",
          "enunciado": "En una empresa mediana, los sistemas de ventas, inventarios y facturación se han conectado progresivamente mediante enlaces directos entre pares de aplicaciones. ¿Cómo se caracteriza este estilo de integración “punto a punto” cuando el número de sistemas crece?",
          "opciones": [
            "Un bus central que conecta todos los sistemas",
            "Conexiones directas específicas entre cada par de aplicaciones, generando “spaghetti” al crecer",
            "El uso exclusivo de colas de mensajes",
            "La obligación de usar solo SOAP/XML"
          ],
          "correcta": [2],
          "feedback_correcta": "La integración punto a punto se basa en conexiones directas entre pares de sistemas y tiende a generar un esquema tipo “spaghetti” al crecer.",
          "feedback_incorrecta": "En la integración punto a punto no existe un bus central; cada par de sistemas establece su propia integración específica."
        },
        {
          "id": "E2_P02",
          "tipo": "opcion_multiple",
          "enunciado": "Una organización que sufría alta complejidad por integraciones punto a punto decide reorganizar su arquitectura hacia servicios de negocio bien definidos. ¿Qué objetivo principal tiene la arquitectura SOA en comparación con ese “spaghetti” de integraciones?",
          "opciones": [
            "Aumentar el número de conexiones",
            "Agrupar la lógica en servicios de negocio con contratos claros y reutilizables",
            "Eliminar la necesidad de contratos",
            "Obligar a usar microservicios"
          ],
          "correcta": [2],
          "feedback_correcta": "SOA busca agrupar la lógica en servicios de negocio con contratos claros y reutilizables para reducir el “spaghetti”.",
          "feedback_incorrecta": "El objetivo de SOA no es incrementar conexiones, sino definir servicios reutilizables con contratos bien especificados."
        },
        {
          "id": "E2_P03",
          "tipo": "opcion_multiple",
          "enunciado": "Un equipo diseña una API pública para consulta de productos accesible desde navegadores y aplicaciones móviles, siguiendo principios REST. ¿Cuál de las siguientes afirmaciones describe mejor a REST en este contexto?",
          "opciones": [
            "Es un protocolo binario para redes locales",
            "Es un estilo arquitectónico que aprovecha HTTP y trata recursos mediante métodos estándar como GET, POST, PUT, DELETE",
            "Es un lenguaje de programación orientado a objetos",
            "Es un reemplazo obligatorio de SOAP en todos los contextos"
          ],
          "correcta": [2],
          "feedback_correcta": "REST se considera un estilo arquitectónico que utiliza HTTP y trata recursos con métodos como GET, POST, PUT y DELETE.",
          "feedback_incorrecta": "REST no es un protocolo binario ni un lenguaje de programación; se trata de un estilo arquitectónico para APIs."
        },
        {
          "id": "E2_P04",
          "tipo": "opcion_multiple",
          "enunciado": "Una startup expone sus servicios mediante una API para terceros. Decide usar REST con JSON en lugar de SOAP con XML para facilitar el consumo desde clientes ligeros. ¿Qué ventaja principal aporta REST+JSON en este caso?",
          "opciones": [
            "Mayores requisitos de herramientas especializadas",
            "Contratos más rígidos e inflexibles",
            "Mensajes más ligeros y fáciles de consumir desde navegadores y apps móviles",
            "Imposibilidad de usar HTTPS"
          ],
          "correcta": [3],
          "feedback_correcta": "REST con JSON suele producir mensajes más ligeros y sencillos de consumir en navegadores y aplicaciones móviles.",
          "feedback_incorrecta": "La ventaja típica de REST+JSON es la simplicidad y ligereza de los mensajes, no una mayor rigidez ni requisitos de herramientas pesadas."
        },
        {
          "id": "E2_P05",
          "tipo": "opcion_multiple",
          "enunciado": "En una organización grande con varios años de historia tecnológica, se hace un inventario de sistemas. Se encuentran aplicaciones monolíticas, servicios SOAP heredados, APIs REST recientes y algunos componentes por eventos. ¿Qué situación describe mejor este panorama?",
          "opciones": [
            "Solo monolitos puros sin integración",
            "Solo microservicios sin legado",
            "La convivencia de monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos",
            "Exclusivamente colas de mensajes sin APIs"
          ],
          "correcta": [3],
          "feedback_correcta": "En muchas organizaciones grandes coexisten monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos.",
          "feedback_incorrecta": "El panorama real suele mezclar estilos de integración; rara vez se eliminan por completo monolitos o servicios SOAP."
        },
        {
          "id": "E2_P06",
          "tipo": "opcion_multiple",
          "enunciado": "Dos sistemas comparten información de clientes mediante procesos nocturnos que replican tablas completas de datos. No se invocan operaciones remotas; solo se copian registros. ¿Qué tipo de integración se está realizando principalmente?",
          "opciones": [
            "Integración de datos",
            "Integración funcional",
            "Integración semántica",
            "Integración física"
          ],
          "correcta": [1],
          "feedback_correcta": "Cuando se comparten o sincronizan tablas e información entre sistemas se habla de integración de datos.",
          "feedback_incorrecta": "La integración de datos se orienta a replicar y sincronizar información, a diferencia de la integración funcional que consume capacidades remotas."
        },
        {
          "id": "E2_P07",
          "tipo": "opcion_multiple",
          "enunciado": "Una aplicación móvil invoca un servicio remoto para ejecutar la operación \"consultar saldo\" en un sistema bancario central. ¿Qué tipo de integración representa mejor esta situación?",
          "opciones": [
            "Integración de datos",
            "Integración funcional",
            "Integración semántica",
            "Integración de red"
          ],
          "correcta": [2],
          "feedback_correcta": "La integración funcional se refiere al consumo de capacidades de negocio remotas, como operaciones de consulta o creación.",
          "feedback_incorrecta": "La integración de datos se centra en tablas e información, mientras que la funcional se enfoca en invocar operaciones de negocio remotas."
        },
        {
          "id": "E2_P08",
          "tipo": "opcion_multiple",
          "enunciado": "En una empresa, dos sistemas utilizan el campo \"cliente\" pero con significados distintos: en uno incluye personas físicas y morales, y en otro solo personas físicas. Se busca que ambos sistemas manejen el mismo concepto. ¿A qué se refiere este tipo de esfuerzo de integración?",
          "opciones": [
            "A compartir archivos de texto sin estructura",
            "A alinear el significado de los datos y conceptos entre sistemas, evitando ambigüedades",
            "A comprimir mensajes para ahorrar ancho de banda",
            "A usar siempre el mismo tipo de base de datos"
          ],
          "correcta": [2],
          "feedback_correcta": "La integración semántica se centra en alinear el significado de datos y conceptos entre sistemas para evitar ambigüedades.",
          "feedback_incorrecta": "El problema semántico radica en que términos como “cliente” o “balance” tengan el mismo significado en todos los sistemas involucrados."
        },
        {
          "id": "E2_P09",
          "tipo": "opcion_multiple",
          "enunciado": "En un análisis de riesgos de integración, se identifican conexiones entre sistemas de nómina, facturación y reporteo. ¿Qué criterio es más adecuado para etiquetar una integración como crítica en este contexto?",
          "opciones": [
            "Que use JSON",
            "Que sea la que más ancho de banda consume",
            "Que, si falla, afecta procesos de negocio esenciales como facturación o pagos",
            "Que sea la más nueva"
          ],
          "correcta": [3],
          "feedback_correcta": "Una integración se considera crítica cuando su fallo impacta procesos esenciales del negocio, como facturación o pagos.",
          "feedback_incorrecta": "El carácter crítico se define por el impacto sobre procesos de negocio clave, no por el formato de mensaje ni por el ancho de banda."
        },
        {
          "id": "E2_P10",
          "tipo": "opcion_multiple",
          "enunciado": "Una empresa ha ido agregando integraciones directas entre aplicaciones a lo largo de varios años sin un diseño centralizado. Hoy tiene decenas de enlaces específicos entre pares de sistemas. ¿Qué efecto típico tiene esta acumulación de integraciones punto a punto?",
          "opciones": [
            "Facilita el mantenimiento porque todas son similares",
            "Disminuye la dependencia entre sistemas",
            "Aumenta la complejidad, la duplicación de lógica y el acoplamiento",
            "Elimina la necesidad de documentación"
          ],
          "correcta": [3],
          "feedback_correcta": "La acumulación de integraciones punto a punto incrementa la complejidad, la duplicación de lógica y el acoplamiento.",
          "feedback_incorrecta": "Un número creciente de integraciones punto a punto suele generar un panorama de “spaghetti” difícil de mantener."
        },
        {
          "id": "E2_P11",
          "tipo": "opcion_multiple",
          "enunciado": "Un sistema de salud expone servicios SOAP para registrar citas y consultar expedientes. Los mensajes intercambiados se basan en XML y siguen una estructura estándar con sobre, encabezado y cuerpo. ¿Cuál de las siguientes es una característica típica de SOAP en este entorno?",
          "opciones": [
            "Uso exclusivo de JSON",
            "Mensajes con sobre <Envelope>, <Header> y <Body> en XML",
            "Eliminación de contratos formales",
            "Comunicación solo dentro de un mismo proceso"
          ],
          "correcta": [2],
          "feedback_correcta": "SOAP se caracteriza por mensajes en XML con elementos Envelope, Header y Body.",
          "feedback_incorrecta": "SOAP no se basa en JSON; su estructura estándar en XML con Envelope, Header y Body es una de sus características distintivas."
        },
        {
          "id": "E2_P12",
          "tipo": "opcion_multiple",
          "enunciado": "Un integrador recibe la descripción de un servicio SOAP que incluye operaciones como \"consultarCuenta\" y \"pagarServicio\". La descripción está en un archivo XML que documenta qué mensajes se envían y reciben. ¿Qué componente de la pila SOAP corresponde a este archivo?",
          "opciones": [
            "SOAP Envelope",
            "WSDL",
            "UDDI",
            "WS-Security"
          ],
          "correcta": [2],
          "feedback_correcta": "WSDL es el componente que describe operaciones, mensajes y tipos de datos del servicio.",
          "feedback_incorrecta": "En la pila SOAP, WSDL actúa como contrato; SOAP define el protocolo de mensaje y UDDI ofrece un registro de servicios."
        },
        {
          "id": "E2_P13",
          "tipo": "opcion_multiple",
          "enunciado": "En un entorno empresarial, se adoptan especificaciones adicionales sobre SOAP para cubrir requisitos avanzados, como cifrado de mensajes, políticas de seguridad y transacciones distribuidas. ¿Qué rol jugaron las especificaciones WS-* en este ecosistema?",
          "opciones": [
            "Definir formatos de imagen",
            "Extender SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones",
            "Reemplazar completamente a WSDL",
            "Hacer innecesario el uso de XML"
          ],
          "correcta": [2],
          "feedback_correcta": "Las especificaciones WS-* extendieron SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones.",
          "feedback_incorrecta": "WS-* no reemplaza WSDL ni define formatos gráficos; añade capacidades empresariales a la pila SOAP."
        },
        {
          "id": "E2_P14",
          "tipo": "opcion_multiple",
          "enunciado": "En una integración entre un banco, una entidad gubernamental y un proveedor de salud, se observa que la mayoría de los servicios siguen siendo SOAP con contratos formales y WS-Security. ¿En qué sectores se considera que SOAP sigue siendo comúnmente utilizado?",
          "opciones": [
            "Redes sociales y aplicaciones de mensajería instantánea",
            "Videojuegos móviles informales",
            "Banca, gobierno y salud con fuertes requisitos regulatorios",
            "Sitios web estáticos"
          ],
          "correcta": [3],
          "feedback_correcta": "SOAP sigue siendo frecuente en banca, gobierno y salud, donde existen requisitos regulatorios y de seguridad estrictos.",
          "feedback_incorrecta": "Estos sectores valoran contratos formales y WS-Security; SOAP no se asocia principalmente con redes sociales o juegos casuales."
        },
        {
          "id": "E2_P15",
          "tipo": "opcion_multiple",
          "enunciado": "Un integrador externo se conecta a un proveedor de servicios que documenta su interfaz mediante WSDL y especificaciones WS-Security. La integración ha sido estable durante años y cumple con regulaciones estrictas. ¿Cuál de las siguientes situaciones favorece seguir usando este servicio SOAP en lugar de migrarlo de inmediato a REST?",
          "opciones": [
            "El proveedor solo ofrece WSDL y WS-* y la integración es estable y de largo plazo",
            "La API se usa solo para pruebas internas temporales",
            "Se requiere una interfaz gráfica rica",
            "No hay requisitos de seguridad"
          ],
          "correcta": [1],
          "feedback_correcta": "Cuando el proveedor solo dispone de WSDL y WS-* y la integración es estable y de largo plazo, tiene sentido mantener SOAP.",
          "feedback_incorrecta": "Migrar a REST no siempre es prioritario si la integración SOAP es estable, regulada y responde a necesidades de largo plazo."
        },
        {
          "id": "E2_P16",
          "tipo": "opcion_multiple",
          "enunciado": "En una arquitectura híbrida, un servicio de cuentas se expone tanto como SOAP/XML como a través de una API REST/JSON. Al comparar los mensajes intercambiados, se nota que en SOAP siempre aparece un sobre con espacios de nombres, mientras que en REST no. ¿Cuál es una diferencia conceptual clave entre mensajes SOAP y mensajes REST/JSON en este escenario?",
          "opciones": [
            "REST/JSON obliga a usar WS-Security",
            "SOAP incluye un sobre estandarizado y namespaces; REST/JSON suele enviar directamente los datos sin esa envoltura",
            "SOAP no permite tipos de datos complejos",
            "REST requiere UDDI"
          ],
          "correcta": [2],
          "feedback_correcta": "SOAP incorpora un sobre estandarizado y namespaces, mientras que REST/JSON suele transmitir directamente los datos sin esa envoltura.",
          "feedback_incorrecta": "REST no obliga al uso de WS-Security ni de UDDI; su formato típico es JSON sin un Envelope estándar como en SOAP."
        },
        {
          "id": "E2_P17",
          "tipo": "opcion_multiple",
          "enunciado": "Al diseñar una API REST para gestión de pedidos, se buscan buenas prácticas para que otros equipos puedan consumirla fácilmente. ¿Qué descripción se ajusta mejor a una API REST bien diseñada?",
          "opciones": [
            "Operaciones definidas por verbos arbitrarios en la URL",
            "Recursos identificados por URIs y manipulados con métodos HTTP estándar y códigos de estado apropiados",
            "Mensajes exclusivamente XML",
            "Ausencia total de contrato o documentación"
          ],
          "correcta": [2],
          "feedback_correcta": "Una API REST bien diseñada identifica recursos por URIs y los manipula usando métodos HTTP estándar y códigos de estado coherentes.",
          "feedback_incorrecta": "REST no se limita a la ausencia de contrato; se recomienda documentar recursos, métodos y respuestas de forma explícita."
        },
        {
          "id": "E2_P18",
          "tipo": "opcion_multiple",
          "enunciado": "Una organización planea modernizar su plataforma. Algunos sistemas críticos siguen exponiendo servicios SOAP, mientras que los nuevos desarrollos se plantean como microservicios REST. ¿En qué caso es especialmente importante decidir cuándo convivir con SOAP y encapsularlo y cuándo migrar a APIs más ligeras?",
          "opciones": [
            "Cuando solo hay un sistema aislado sin integraciones",
            "Cuando no hay restricciones regulatorias ni de seguridad",
            "Cuando se integran sistemas legacy SOAP con nuevas aplicaciones y microservicios",
            "Cuando todos los servicios ya son REST"
          ],
          "correcta": [3],
          "feedback_correcta": "El dilema entre convivir con SOAP y encapsularlo o migrar a APIs ligeras es especialmente relevante al integrar sistemas SOAP heredados con nuevas aplicaciones y microservicios.",
          "feedback_incorrecta": "Cuando todo el entorno es REST el problema se reduce; la decisión es crítica al coexistir con sistemas SOAP legacy."
        },
        {
          "id": "E2_P19",
          "tipo": "opcion_multiple",
          "enunciado": "Un área de TI describe una integración en la que el sistema de contabilidad copia cada noche la información de clientes desde el sistema de CRM para tener una copia local de esos datos. No se invocan funciones de negocio remotas, solo se replican registros. ¿Qué tipo de integración describe mejor esta situación?",
          "opciones": [
            "Funcional",
            "Semántica",
            "De datos",
            "De red"
          ],
          "correcta": [3],
          "feedback_correcta": "La réplica nocturna de la tabla de clientes corresponde a un caso de integración de datos.",
          "feedback_incorrecta": "En este escenario no se invoca una función de negocio; se copian datos entre sistemas, lo cual encaja con integración de datos."
        },
        {
          "id": "E2_P20",
          "tipo": "opcion_multiple",
          "enunciado": "En otro escenario, una aplicación web permite consultar en tiempo real el saldo de un cliente llamando a una operación expuesta por un sistema de núcleo bancario remoto. ¿Qué tipo de integración representa mejor esta situación?",
          "opciones": [
            "De datos, porque solo importa la tabla de saldos",
            "Funcional, porque se consume una capacidad remota de negocio",
            "Semántica, porque solo se alinea el significado",
            "Física, porque usa redes móviles"
          ],
          "correcta": [2],
          "feedback_correcta": "La invocación de la operación “consultar saldo” representa un ejemplo de integración funcional.",
          "feedback_incorrecta": "Aquí no se comparten tablas directamente, sino una capacidad de negocio remota; por ello se trata de integración funcional."
        },
        {
          "id": "E2_P21",
          "tipo": "opcion_multiple",
          "enunciado": "Al revisar la especificación de un servicio basado en SOAP, se observa un documento en XML que define tipos de datos, mensajes y operaciones mediante elementos como <portType>, <operation> y <message>. ¿Cuál de las siguientes opciones describe mejor este tipo de documento?",
          "opciones": [
            "Definiciones de paths y responses en JSON",
            "Elementos <portType>, <operation> y <message> que describen el contrato",
            "Documentación en formato Markdown",
            "Solo ejemplos de llamadas con curl"
          ],
          "correcta": [2],
          "feedback_correcta": "En un documento WSDL es habitual encontrar elementos como portType, operation y message que describen el contrato.",
          "feedback_incorrecta": "Las definiciones de paths y responses en JSON son propias de OpenAPI y REST, no de WSDL."
        },
        {
          "id": "E2_P22",
          "tipo": "opcion_multiple",
          "enunciado": "Una API REST pública para consulta de pedidos se publica junto con documentación accesible para desarrolladores externos. ¿Qué tipo de información suele incluir esta documentación para que otros puedan consumir la API correctamente?",
          "opciones": [
            "Qué URIs existen, qué métodos HTTP soportan, qué estructura de JSON esperan y devuelven",
            "Cómo generar código a partir de WSDL",
            "Cómo registrar el servicio en UDDI",
            "Cómo usar WS-Security"
          ],
          "correcta": [1],
          "feedback_correcta": "La documentación de una API REST suele precisar qué URIs existen, qué métodos HTTP soportan y qué estructura JSON se espera en solicitudes y respuestas.",
          "feedback_incorrecta": "La generación de código a partir de WSDL y el registro en UDDI pertenecen al ámbito SOAP/WS-*, no a la documentación típica de REST."
        },
        {
          "id": "E2_P23",
          "tipo": "opcion_multiple",
          "enunciado": "Un arquitecto compara el contrato de un servicio SOAP descrito con WSDL y el contrato de una API REST documentado con OpenAPI. El objetivo es decidir qué estilo usar en un nuevo proyecto. ¿Qué objetivo conceptual se persigue al realizar esta comparación?",
          "opciones": [
            "Convertir siempre el WSDL en REST",
            "Identificar elementos de contrato en ambos enfoques y discutir ventajas/desventajas",
            "Demostrar que uno de los dos está obsoleto",
            "Medir solo el tamaño de los mensajes"
          ],
          "correcta": [2],
          "feedback_correcta": "El objetivo consiste en identificar los elementos de contrato en WSDL y REST y reflexionar sobre sus ventajas y desventajas.",
          "feedback_incorrecta": "La intención no es declarar obsoleto a uno de los enfoques, sino comprender cómo cada uno expresa su contrato."
        },
        {
          "id": "E2_P24",
          "tipo": "opcion_multiple",
          "enunciado": "Un servicio de consulta de saldo se expone simultáneamente como SOAP y como API REST. Para SOAP se entrega un WSDL; para REST, se proporciona una especificación OpenAPI en formato JSON. ¿Qué diferencia práctica suele encontrarse entre ambos contratos?",
          "opciones": [
            "El SOAP se consume solo desde navegadores",
            "El WSDL describe tipos y operaciones en XML, mientras que la API REST suele usar JSON y documentación tipo OpenAPI o similar",
            "El SOAP es siempre más rápido",
            "La API REST no puede usar HTTPS"
          ],
          "correcta": [2],
          "feedback_correcta": "En un servicio SOAP la funcionalidad se describe en WSDL mediante XML, mientras que en REST suele documentarse con JSON y especificaciones como OpenAPI.",
          "feedback_incorrecta": "Ambos pueden usar HTTPS; la diferencia suele estar en el formato del contrato (WSDL en XML frente a documentación JSON en REST)."
        },
        {
          "id": "E2_P25",
          "tipo": "opcion_multiple",
          "enunciado": "En la integración entre dos sistemas financieros, ambos intercambian un campo llamado \"balance\". En un sistema, representa saldo disponible; en el otro, saldo contable total. Esta diferencia genera inconsistencias en los reportes consolidados. ¿Qué tipo de problema se está ilustrando?",
          "opciones": [
            "Problema de sintaxis XML",
            "Problema de transporte HTTP",
            "Problema de integración semántica",
            "Problema exclusivo de rendimiento"
          ],
          "correcta": [3],
          "feedback_correcta": "El uso distinto del campo “balance” ilustra un problema de integración semántica.",
          "feedback_incorrecta": "En este caso el conflicto no reside en transporte ni en sintaxis, sino en el significado diferente que cada sistema asigna al mismo dato."
        }
      ]
    }
  ]
}
```


---

# cuando estaba probando subir las imagenes a drive aparecio esto: Acceso bloqueado: Script Examenes no completó el proceso de verificación de Google, qué debo hacer para corregirlo?

Para tu caso (script personal que sube imágenes a tu propio Drive) no necesitas pasar por el proceso de verificación completo; basta con ajustar la configuración de OAuth para que Google te deje usarlo en modo “testing”.

Lo que suele estar pasando es una de estas dos cosas:

1) La app está en “Testing” pero tu correo no está como tester
2) La pantalla de consentimiento no está bien configurada (no agregaste el scope de Drive)

### Paso 1: Revisa la pantalla de consentimiento OAuth

1. Ve a https://console.cloud.google.com
2. Selecciona tu proyecto (el que usaste para crear `credentials.json`).
3. En el menú: “APIs y servicios” → “Pantalla de consentimiento OAuth”.
4. Verifica:
    - Tipo de usuario: “Externa” (correcto para cuentas personales).
    - En el paso de **Permisos / Scopes**, asegúrate de haber añadido el scope de Drive que estás usando (por ejemplo `https://www.googleapis.com/auth/drive.file`).[^12_1][^12_2]
    - Guarda los cambios.

### Paso 2: Añádete como “usuario de prueba” (test user)

Mientras la app está en modo “Prueba” (Testing), solo los correos listados pueden autorizarla.[^12_3][^12_4]

1. En la misma pantalla de consentimiento, baja a la sección **Usuarios de prueba (Test users)**.
2. Agrega el correo con el que intentas autorizar el script (tu cuenta de Google).
3. Guarda.

Vuelve a ejecutar tu script; la primera vez te mostrará el flujo de OAuth, pero ahora debería dejarte continuar (a veces con la pantalla de “app no verificada”, donde puedes hacer clic en “Avanzado” → “Ir a Script Examenes (no seguro)”).

### Paso 3 (opcional): regenerar `credentials.json` si cambiaste de proyecto

Si por error creaste las credenciales en un proyecto distinto al que estás configurando:

- Crea las credenciales de aplicación de escritorio de nuevo en el proyecto correcto.
- Descarga el JSON y reemplaza tu `credentials.json`.
- Borra `token.json` para que el flujo de autorización se rehaga con la nueva config.

Con eso, para uso personal/limitado, no hace falta solicitar verificación formal a Google; solo necesitas tener la pantalla de consentimiento bien configurada y tu correo añadido como tester.[^12_2][^12_5]
<span style="display:none">[^12_10][^12_11][^12_12][^12_13][^12_14][^12_15][^12_6][^12_7][^12_8][^12_9]</span>

<div align="center">⁂</div>

[^12_1]: https://es.stackoverflow.com/questions/560117/acceso-bloqueado-my-project-no-completó-el-proceso-de-verificación-de-google

[^12_2]: https://developers.google.com/workspace/drive/api/troubleshoot-authentication-authorization?hl=es-419

[^12_3]: https://community.zappysys.com/t/how-to-fix-the-this-app-is-blocked-error-in-google-oauth/509

[^12_4]: https://github.com/MarkEdmondson1234/googleCloudRunner/issues/102

[^12_5]: https://support.google.com/cloud/answer/7454865?hl=en

[^12_6]: https://developers.google.com/workspace/tasks/troubleshoot-authentication-authorization?hl=es-419

[^12_7]: https://support.google.com/a/answer/9352843?hl=es

[^12_8]: https://docs.cloud.google.com/chrome-enterprise-premium/docs/policy-remediator?hl=es-419

[^12_9]: https://www.youtube.com/watch?v=bkZns_VOB6I

[^12_10]: https://stackoverflow.com/questions/68876081/google-app-is-blocked-while-its-being-verified-in-production

[^12_11]: https://discuss.google.dev/t/cannot-access-oauth-consent-screen-or-add-test-users-for-gmail-api-project/295811

[^12_12]: https://support.google.com/drive/answer/9279980?hl=es-419

[^12_13]: https://developers.google.com/apps-script/guides/client-verification

[^12_14]: https://www.reddit.com/r/googlecloud/comments/11vm96q/how_do_i_secure_a_production_external_oauth/

[^12_15]: https://www.reddit.com/r/googlecloud/comments/194lxvm/app_has_not_completed_the_google_verification/


---

# Ahora esto: Google hasn’t verified this app

You’ve been given access to an app that’s currently being tested. You should only continue if you know the developer that invited you.

Ese mensaje es normal en el modo “testing” y, dado que tú eres el desarrollador, puedes continuar sin problema.

Haz esto en la ventana del navegador donde salió:

1. Verifica que arriba aparezca el nombre de tu app (por ejemplo, “Script Examenes”) y tu cuenta de Google.
2. Haz clic en el botón **“Continue” / “Continuar”** (o “Allow” en los pasos siguientes) para aceptar los permisos de Drive que pide tu script.
3. Al finalizar, te devolverá un código al script (o cerrará la ventana si usas `flow.run_local_server`); se generará el `token.json` y ya no tendrás que pasar por este aviso en las siguientes ejecuciones.

En resumen:

- No es un error, es solo la advertencia estándar de “app no verificada” en modo prueba.
- Como tú controlas el código y el proyecto, es seguro darle continuar y aceptar los permisos para tu propia cuenta.

---

# y ahora en el script: googleapiclient.errors.HttpError: <HttpError 403 when requesting [https://www.googleapis.com/upload/drive/v3/files?fields=id\&alt=json\&uploadType=multipart](https://www.googleapis.com/upload/drive/v3/files?fields=id&alt=json&uploadType=multipart) returned "Google Drive API has not been used in project 1006706292695 before or it is disabled. Enable it by visiting [https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=1006706292695](https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=1006706292695) then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.". Details: "[{'message': 'Google Drive API has not been used in project 1006706292695 before or it is disabled. Enable it by visiting [https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=1006706292695](https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=1006706292695) then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.', 'domain': 'usageLimits', 'reason': 'accessNotConfigured', 'extendedHelp': 'https://console.developers.google.com'}]">

El mensaje es claro: estás usando credenciales de un proyecto de Google Cloud donde **la Google Drive API no está habilitada** (o se acaba de habilitar y aún no propaga).

Haz esto (una sola vez por proyecto):

### 1. Habilitar la Google Drive API en el proyecto correcto

1. Abre el enlace que sale en el error (ajustado a español):
https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=1006706292695[^14_1]
2. Verifica que arriba, en el selector de proyecto, esté el mismo ID/proyecto que usaste para crear `credentials.json` (el número 1006706292695 debe coincidir).
3. Si ves un botón **“Habilitar” / “Enable”**, haz clic y espera a que quede como **“Deshabilitar”** (eso significa que ya está activa).[^14_1]

Si ya aparecía habilitada, espera 1–2 minutos y prueba de nuevo: a veces tarda un poco en propagarse.[^14_1]

### 2. Confirmar que el script usa ese proyecto

- El `credentials.json` que está junto a tu script debe ser el descargado de **ese mismo proyecto** (el que tiene la Drive API habilitada).
- Si en algún momento creaste otro proyecto y otro `credentials.json`, asegúrate de borrar `token.json` y dejar solo el `credentials.json` correcto, para obligar al script a re-autenticar con el proyecto adecuado.

Después de habilitar la API y, si hace falta, borrar `token.json` y ejecutar el script de nuevo, el error 403 `accessNotConfigured` debería desaparecer.[^14_2][^14_1]

<div align="center">⁂</div>

[^14_1]: https://developers.google.com/workspace/drive/api/troubleshoot-authentication-authorization?hl=es-419

[^14_2]: https://es.stackoverflow.com/questions/560117/acceso-bloqueado-my-project-no-completó-el-proceso-de-verificación-de-google


---

# Ahora el mensaje es este: googleapiclient.errors.HttpError: <HttpError 404 when requesting [https://www.googleapis.com/upload/drive/v3/files?fields=id\&alt=json\&uploadType=multipart](https://www.googleapis.com/upload/drive/v3/files?fields=id&alt=json&uploadType=multipart) returned "File not found: [https://drive.google.com/drive/folders/15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2](https://drive.google.com/drive/folders/15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2).". Details: "[{'message': 'File not found: [https://drive.google.com/drive/folders/15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2](https://drive.google.com/drive/folders/15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2).', 'domain': 'global', 'reason': 'notFound', 'location': 'fileId', 'locationType': 'parameter'}]"> Copié la url de la carpeta y la puse en el código

En el código de Drive no va la **URL completa**, va solo el **ID** de la carpeta. La API está interpretando la URL como si fuera un `fileId` y por eso responde “File not found”.

De tu ejemplo:

- URL de la carpeta:
`https://drive.google.com/drive/folders/15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2`
- ID de la carpeta:
`15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2`

Corrige en tu script algo así:

```python
folder_drive_id = "15WWnucErMV-4Q3JSy7LbmmW7_8kMKXi2"  # solo el ID, sin la URL
```

Y deja la parte de subida igual:

```python
file_metadata = {
    "name": os.path.basename(item["path"]),
    "parents": [folder_id]  # aquí folder_id debe ser SOLO el ID
}
```

Con eso debería desaparecer el 404 de “File not found”.

---

# <q>3. Boceto mínimo de Apps Script

Este ejemplo asume:

Ya tienes un archivo JSON en Drive (o puedes pegarlo como string en el script).

Ya tienes las imágenes subidas a Drive y guardas imagenPreguntaId en el JSON.

Usas solo Apps Script clásico (FormApp), sin Forms API REST, para simplificar.</q> Ya tengo el Json de preguntas, el mismo que me diste, ya tengo las imagenes en Drive y para cada una, el json incluye el ID del archivo en Drive no entiendo lo de Apps clásico o Forms API REST, el código que me das es javascript, cómo lo ejecuto, yo solo he usado hasta ahora python?

Google Apps Script es un entorno de scripting de Google (tipo “JavaScript en la nube”) que se edita y ejecuta desde el navegador, no desde Python. Lo usas para crear el Form directamente dentro de tu cuenta de Google.

Pasos concretos con lo que ya tienes:

***

### 1. Preparar tu JSON en Drive

1. En Google Drive, sube el archivo JSON de exámenes (el que ya incluye `imagenPreguntaId` por pregunta).
2. Copia su **ID** (lo mismo que con las carpetas: en la URL, la parte larga de letras/números).

***

### 2. Crear el proyecto de Apps Script

1. Ve a https://script.google.com (o en Drive: “Nuevo → Más → Google Apps Script”).
2. Se abre el editor online, con un archivo `Code.gs`.
3. En la parte superior, pon un nombre al proyecto, por ejemplo: `CrearFormExamen`.

***

### 3. Pegar el código de Apps Script

En `Code.gs` borra todo y pega este código, ajustando el `JSON_FILE_ID`:

```javascript
function crearQuizDesdeJson() {
  const JSON_FILE_ID = 'PON_AQUI_EL_ID_DEL_JSON';  // <- cambia esto

  // 1. Cargar JSON desde Drive
  const contenido = DriveApp.getFileById(JSON_FILE_ID)
    .getBlob()
    .getDataAsString('UTF-8');
  const data = JSON.parse(contenido);

  // 2. Crear Form y marcar como quiz
  const form = FormApp.create(data.titulo || 'Examen sin título');
  form.setIsQuiz(true);
  form.setShuffleQuestions(true);
  form.setProgressBar(true);

  // 3. Recorrer preguntas
  data.preguntas.forEach(p => {
    // 3.1. Añadir imagen si existe
    if (p.imagenPreguntaId) {
      const imgBlob = DriveApp.getFileById(p.imagenPreguntaId).getBlob();
      form.addImageItem()
        .setTitle(p.id)  // texto pequeño arriba de la imagen
        .setImage(imgBlob);
    }

    // 3.2. Crear la pregunta (todas son opción múltiple)
    const item = form.addMultipleChoiceItem();
    item.setTitle(p.enunciado || p.id)
        .setRequired(true);

    // 3.3. Opciones y clave
    const choices = p.opciones.map((texto, idx) => {
      const esCorrecta = (p.correcta || []).includes(idx + 1);
      return item.createChoice(texto, esCorrecta);
    });
    item.setChoices(choices);

    // 3.4. Puntos
    if (typeof p.puntos === 'number') {
      item.setPoints(p.puntos);
    } else {
      item.setPoints(1);  // valor por defecto
    }

    // 3.5. Feedback
    if (p.feedback_correcta) {
      const fbCorrecta = FormApp.createFeedback()
        .setDisplayText(p.feedback_correcta)
        .build();
      item.setFeedbackForCorrect(fbCorrecta);
    }

    if (p.feedback_incorrecta) {
      const fbIncorrecta = FormApp.createFeedback()
        .setDisplayText(p.feedback_incorrecta)
        .build();
      item.setFeedbackForIncorrect(fbIncorrecta);
    }
  });

  Logger.log('Formulario creado: ' + form.getEditUrl());
}
```

Notas:

- Tu JSON debe ser del tipo:

```json
{
  "titulo": "Examen 1 ...",
  "preguntas": [
    {
      "id": "E1_P01",
      "tipo": "opcion_multiple",
      "enunciado": "...",
      "opciones": ["A", "B", "C", "D"],
      "correcta": [2],
      "puntos": 1,
      "imagenPreguntaId": "ID_DE_LA_IMAGEN_EN_DRIVE",
      "feedback_correcta": "...",
      "feedback_incorrecta": "..."
    },
    ...
  ]
}
```


***

### 4. Dar permisos y ejecutar

1. En el editor de Apps Script, arriba, abre el desplegable de funciones y elige `crearQuizDesdeJson`.
2. Haz clic en el ícono de “▶ Ejecutar”.
3. La primera vez te pedirá permisos:
    - Elige tu cuenta de Google.
    - Te mostrará advertencia de “app no verificada”; como es tu script, haz clic en “Avanzado” → “Ir a CrearFormExamen (no seguro)” → “Permitir”.
4. Cuando termine, ve a “Ver → Registros” (Logs) y copia la URL que aparece: es la URL de edición del Form creado.

***

### 5. Relación con Python

- Python lo usas para:
    - Generar el JSON.
    - Subir las imágenes y obtener sus IDs para `imagenPreguntaId`.
- Apps Script (JavaScript en la nube) lo usas para:
    - Leer ese JSON desde Drive.
    - Crear el Form/quiz de Google en tu cuenta automáticamente.

No necesitas instalar nada local para Apps Script: todo se corre en la interfaz web de Google; el “runtime” es de Google, no tu Python.

Si quieres, en el siguiente mensaje podemos revisar un ejemplo concreto de tu JSON con `imagenPreguntaId` y ajusto el script para usar también varios exámenes (por ejemplo, `examenes[0]`, `examenes[1]`).

---

# <q>Tu JSON debe ser del tipo:

json{
"titulo": "Examen 1 ...",
"preguntas": [
{
"id": "E1_P01",
"tipo": "opcion_multiple",
"enunciado": "...",
"opciones": ["A", "B", "C", "D"],
"correcta": [2],
"puntos": 1,
"imagenPreguntaId": "ID_DE_LA_IMAGEN_EN_DRIVE",
"feedback_correcta": "...",
"feedback_incorrecta": "..."
},
...
]
}</q> mi json no tiene ese formato, dame el json con ese formato usando como entrada los dos Json adjuntos.

Aquí tienes el JSON ya en el formato que pide el Apps Script, combinando `examenes.json` con los IDs de `mapa_pregunta_drive.json` (añadí `imagenPreguntaId` en cada pregunta).[^17_1][^17_2]

```json
{
  "examenes": [
    {
      "titulo": "Examen 1 – SOAP, XML/XSD, WSDL y monolito mínimo Node.js",
      "preguntas": [
        {
          "id": "E1_P01",
          "tipo": "opcion_multiple",
          "enunciado": "En un servicio bancario basado en SOAP, se requiere enviar información de cuentas y transacciones entre sistemas heterogéneos. ¿Cuál es el propósito principal de usar XML en este tipo de servicios web?",
          "opciones": [
            "Reducir el tamaño de los mensajes de red",
            "Representar datos estructurados de forma jerárquica y validable mediante esquemas",
            "Asegurar que todos los mensajes sean binarios",
            "Evitar el uso de HTTP como transporte"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1if6aGtqXCwVXtrEnX2aTN4As8SCEqx-I",
          "feedback_correcta": "XML se utiliza para representar datos jerárquicos y validables, lo cual resulta fundamental en mensajes SOAP.",
          "feedback_incorrecta": "XML en servicios web se valora por su estructura jerárquica y la posibilidad de validación mediante XSD, no por reducción de tamaño ni por ser binario."
        },
        {
          "id": "E1_P02",
          "tipo": "opcion_multiple",
          "enunciado": "Una compañía de seguros intercambia pólizas en formato XML entre aplicaciones internas. Antes de validar el contenido con XSD, se verifica que el XML esté bien formado. ¿Qué característica define que el documento XML esté bien formado?",
          "opciones": [
            "Tener solo elementos de tipo string",
            "Usar siempre el mismo prefijo de espacio de nombres",
            "Tener un único elemento raíz y etiquetas correctamente anidadas y cerradas",
            "Incluir al menos un atributo en cada elemento"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1XIZXXpV-CdEJTmYfnybhA28y1gwchKU7",
          "feedback_correcta": "Un XML bien formado se caracteriza por tener un único elemento raíz y etiquetas bien anidadas y cerradas.",
          "feedback_incorrecta": "Las reglas de documento XML bien formado exigen un único elemento raíz y etiquetas correctamente anidadas y cerradas."
        },
        {
          "id": "E1_P03",
          "tipo": "opcion_multiple",
          "enunciado": "En el XSD que describe los mensajes de un servicio de pedidos, algunos campos representan valores simples (como cantidades o precios) y otros representan estructuras completas (como dirección de envío con calle, ciudad y código postal). ¿Qué diferencia hay entre un tipo simple y un tipo complejo en XSD en este contexto?",
          "opciones": [
            "El tipo simple solo se usa para atributos, el complejo solo para elementos",
            "El tipo simple describe valores atómicos; el complejo agrupa elementos y atributos anidados",
            "El tipo complejo solo se usa en WSDL, el simple solo en XML",
            "No hay diferencia; ambos se usan indistintamente"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1FRkIpuGsuVlbFpmBMOo-8thhwc2j4O2X",
          "feedback_correcta": "Los tipos simples describen valores atómicos y los tipos complejos agrupan elementos y atributos.",
          "feedback_incorrecta": "La diferencia importante es que el tipo simple representa un valor atómico y el tipo complejo define estructuras con elementos y/o atributos."
        },
        {
          "id": "E1_P04",
          "tipo": "opcion_multiple",
          "enunciado": "Una empresa define un contrato formal para su servicio SOAP de facturación y necesita asegurarse de que todos los mensajes cumplan la misma estructura. ¿Cuál es el rol de XSD en el contexto de WSDL y servicios SOAP en este escenario?",
          "opciones": [
            "Optimizar el rendimiento del servidor HTTP",
            "Describir la estructura y tipos de los mensajes XML que intercambia el servicio",
            "Registrar servicios en directorios públicos",
            "Gestionar la seguridad y el cifrado de los mensajes"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1OWPilsiXq0PUo9fxz4KhDL9axHEqRMez",
          "feedback_correcta": "XSD se utiliza para describir la estructura y los tipos de datos de los mensajes XML de un servicio.",
          "feedback_incorrecta": "XSD no se orienta a rendimiento HTTP ni a seguridad; su finalidad es definir estructura y tipos de datos de los mensajes."
        },
        {
          "id": "E1_P05",
          "tipo": "opcion_multiple",
          "enunciado": "Un equipo de integración recibe un archivo que describe las operaciones disponibles de un servicio SOAP de inventarios, los mensajes que usa y los endpoints a los que puede conectarse. El archivo está definido en XML. ¿Qué describe mejor a este archivo?",
          "opciones": [
            "Un formato ligero de datos alternativo a JSON",
            "Un protocolo de transporte para servicios web",
            "Un lenguaje basado en XML que describe operaciones, mensajes, tipos de datos y endpoints de un servicio",
            "Una base de datos de servicios web en la nube"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "19kqm3nMOxKudwiziJb-gVagAxYl_Gk3a",
          "feedback_correcta": "WSDL es un lenguaje basado en XML para describir operaciones, mensajes, tipos y endpoints de un servicio.",
          "feedback_incorrecta": "WSDL no es un formato de datos ni un protocolo; es un contrato descriptivo basado en XML."
        },
        {
          "id": "E1_P06",
          "tipo": "opcion_multiple",
          "enunciado": "En un mensaje SOAP que devuelve el resultado de una consulta de cliente, se define un sobre con espacios de nombres y se agregan secciones opcionales según sea necesario. ¿Qué elemento es obligatorio en ese mensaje SOAP?",
          "opciones": [
            "soap:Header",
            "soap:Body",
            "soap:Fault",
            "soap:Security"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1VrbghwpwURClI6OFVNm1oOYAfZGnlSvm",
          "feedback_correcta": "En un mensaje SOAP, el elemento Body es obligatorio, mientras que Header y Fault son opcionales.",
          "feedback_incorrecta": "El elemento obligatorio en SOAP es el Body; Header y Fault solo aparecen cuando se requieren."
        },
        {
          "id": "E1_P07",
          "tipo": "opcion_multiple",
          "enunciado": "Una organización desea que sus clientes internos puedan generar clientes SOAP y stubs de servidor automáticamente a partir de un contrato centralizado, reduciendo errores de integración. ¿Qué ventaja clave ofrece el uso de WSDL con contratos estrictos para este fin?",
          "opciones": [
            "Permite cambiar la estructura de los mensajes sin coordinar con los consumidores",
            "Facilita la generación de código cliente/servidor y la validación automática de mensajes",
            "Elimina la necesidad de usar XML",
            "Permite que el servicio sea completamente stateless sin esfuerzo"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1qpxKilEBjtJ3stDGErr0HpDP50EdWlEa",
          "feedback_correcta": "Los contratos estrictos en WSDL facilitan la generación de código y la validación automática de mensajes.",
          "feedback_incorrecta": "La principal ventaja de contratos estrictos en WSDL es la generación de código y la validación automática, aunque exigen disciplina al evolucionar."
        },
        {
          "id": "E1_P08",
          "tipo": "opcion_multiple",
          "enunciado": "Un proveedor de servicios expone varios servicios SOAP y desea que sus consumidores externos puedan encontrarlos y consultarlos a través de un catálogo público. En la pila clásica basada en SOAP, ¿qué componente se diseñó con este propósito?",
          "opciones": [
            "SOAP",
            "WSDL",
            "UDDI",
            "WS-Security"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1vj0bCjUh2uctd-bYe8eWQ9DB_jh3Fqyi",
          "feedback_correcta": "UDDI se diseñó como registro para publicar y descubrir servicios web.",
          "feedback_incorrecta": "En la pila SOAP, SOAP es el protocolo de mensajería, WSDL describe el contrato y UDDI actúa como registro o catálogo."
        },
        {
          "id": "E1_P09",
          "tipo": "opcion_multiple",
          "enunciado": "Un arquitecto compara el diseño de una integración basada en SOAP con otra basada en REST para exponer un catálogo de productos. ¿Cuál de las siguientes afirmaciones describe mejor la diferencia típica entre ambos enfoques?",
          "opciones": [
            "SOAP usa típicamente XML y contratos formales; REST suele usar JSON y contratos más ligeros",
            "SOAP y REST siempre usan JSON",
            "REST requiere UDDI para descubrir servicios",
            "SOAP no puede usar HTTP como transporte"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "1AzRYYw9DlzTaba8rds4W5kDWSHUCaD-m",
          "feedback_correcta": "SOAP suele usar XML y contratos formales, mientras que REST tiende a emplear JSON y contratos más ligeros.",
          "feedback_incorrecta": "REST no requiere UDDI y SOAP no se limita en absoluto a JSON; REST se caracteriza por mensajes ligeros y menor rigidez contractual."
        },
        {
          "id": "E1_P10",
          "tipo": "opcion_multiple",
          "enunciado": "Una institución financiera evalúa exponer una operación de pagos a largo plazo con fuertes requisitos de auditoría y seguridad basada en WS-Security. ¿En qué contexto sigue siendo razonable preferir SOAP en lugar de solo APIs REST?",
          "opciones": [
            "Aplicaciones móviles sin requisitos de seguridad",
            "Prototipos rápidos con cambios frecuentes de contrato",
            "Integraciones reguladas de largo plazo con contratos muy estructurados y WS-Security",
            "Sitios estáticos de contenido público"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1_0LhGjRZMP4_dqG6LcFUTgDgGN5Qx5b1",
          "feedback_correcta": "SOAP resulta razonable en integraciones reguladas y de largo plazo con contratos muy estructurados y uso de WS-Security.",
          "feedback_incorrecta": "SOAP encaja mejor en escenarios con requisitos fuertes de seguridad, contratos estables y uso de WS-Security que en prototipos cambiantes."
        },
        {
          "id": "E1_P11",
          "tipo": "opcion_multiple",
          "enunciado": "Un servicio SOAP devuelve la información de un producto en respuesta a una consulta por su identificador. El modelo de datos del producto en JSON es { \"id\": 1, \"name\": \"Laptop\", \"price\": 25000.0 }. ¿Cuál sería el elemento principal más adecuado en el Body del mensaje SOAP de respuesta?",
          "opciones": [
            "<GetProductRequest>",
            "<ProductResponse> o equivalente que agrupe los datos del producto",
            "<ErrorResponse>",
            "<EnvelopeProduct>"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1WhydZ4AUJTvTFRhaR3BJQmHlwei5A5DB",
          "feedback_correcta": "El Body suele contener un elemento que agrupa los datos del producto, como ProductResponse o equivalente.",
          "feedback_incorrecta": "En el Body no se usan elementos de petición cuando se trata de una respuesta; tampoco se emplea un envoltorio como EnvelopeProduct para los datos."
        },
        {
          "id": "E1_P12",
          "tipo": "opcion_multiple",
          "enunciado": "Una integración revisa la estructura de los mensajes SOAP que intercambia un sistema de reservas. Se observa que cada mensaje tiene un sobre con un cuerpo y, en algunos casos, un encabezado adicional. ¿Qué combinación describe mejor un mensaje SOAP bien formado en este contexto?",
          "opciones": [
            "Un único <soap:Envelope> con <soap:Header> y <soap:Body> internos",
            "Varios <soap:Envelope> anidados para cada elemento del producto",
            "Un <soap:Body> sin <soap:Envelope>",
            "Un XML sin namespaces para simplificar"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "1dF6bg8MFBUD0SGa3OYPvCHO9wtlnHIfF",
          "feedback_correcta": "Un mensaje SOAP bien formado tiene un único Envelope que contiene Header opcional y Body obligatorio.",
          "feedback_incorrecta": "En SOAP no se anidan múltiples Envelopes y siempre debe existir un Envelope que encapsule Header y Body."
        },
        {
          "id": "E1_P13",
          "tipo": "opcion_multiple",
          "enunciado": "En un sistema de facturación, se valida un mensaje SOAP de factura contra el XSD correspondiente. El validador indica que el elemento <price> no es numérico. ¿Qué significa este resultado?",
          "opciones": [
            "El WSDL está mal escrito",
            "El XML no es bien formado",
            "El valor del elemento no cumple el tipo de dato definido en el XSD",
            "El servidor HTTP está caído"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1B-eZiTjXMEC_Tn7GifIFfmq0115GOIQs",
          "feedback_correcta": "El mensaje indica que el valor del elemento no cumple el tipo de dato definido en el XSD, aunque el XML pueda ser bien formado.",
          "feedback_incorrecta": "Es necesario distinguir entre XML bien formado y XML válido frente a XSD; en este caso el problema es de tipo de dato, no de sintaxis."
        },
        {
          "id": "E1_P14",
          "tipo": "opcion_multiple",
          "enunciado": "Un integrador recibe un WSDL de un servicio de clientes que incluye los tipos XSD embebidos en la sección <types>. Se desea validar ejemplos de mensajes antes de poner el sistema en producción. ¿Qué se debe hacer para validar un mensaje XML contra esos tipos?",
          "opciones": [
            "Ignorar la sección <types> y validar solo con el navegador",
            "Extraer o referenciar el XSD de la sección <types> y usarlo como esquema en un validador XML/XSD",
            "Convertir el WSDL a JSON y validarlo con OpenAPI",
            "No es posible validar mensajes usando un WSDL"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1fj4WUZhxo_XbfDQAojBrVO07RKI9Y2b7",
          "feedback_correcta": "El XSD embebido en la sección types puede extraerse o referenciarse y usarse en un validador XML/XSD.",
          "feedback_incorrecta": "El WSDL sí permite validar mensajes, extrayendo o referenciando sus XSD; la sección types no debe ignorarse."
        },
        {
          "id": "E1_P15",
          "tipo": "opcion_multiple",
          "enunciado": "Durante la integración de un sistema de pagos, se recibe un mensaje SOAP con una estructura <soap:Fault> que incluye un código y una descripción de error. ¿Para qué se utiliza principalmente un elemento Fault en un mensaje SOAP?",
          "opciones": [
            "Enviar datos de negocio adicionales",
            "Configurar la autenticación del servicio",
            "Establecer una conexión persistente",
            "Comunicar errores de procesamiento con código, motivo y detalles"
          ],
          "correcta": [^17_4],
          "puntos": 1,
          "imagenPreguntaId": "1D_TnN5l2KAGHstZ8AQIoG5uhkd-rA6I8",
          "feedback_correcta": "La estructura Fault se emplea para comunicar errores de procesamiento con código, motivo y detalles.",
          "feedback_incorrecta": "Fault no transmite datos de negocio ni configuraciones; su propósito es estandarizar la información de error."
        },
        {
          "id": "E1_P16",
          "tipo": "opcion_multiple",
          "enunciado": "Se construye una API sencilla con Node.js y Express para gestionar productos y pedidos en memoria durante el desarrollo. ¿Qué característica describe mejor las rutas iniciales de este monolito mínimo?",
          "opciones": [
            "Solo exponen métodos GET y POST para recursos como productos y pedidos en memoria",
            "Incluyen persistencia en base de datos relacional",
            "Exponen exclusivamente métodos PUT y DELETE",
            "Usan colas de mensajes en lugar de HTTP"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "14uMAa9XrJPHtUGEY-rSHe4lrHOJ-1vSw",
          "feedback_correcta": "El monolito mínimo inicia con rutas GET y POST en memoria para recursos como productos y pedidos.",
          "feedback_incorrecta": "En la configuración inicial no se usa base de datos ni únicamente PUT/DELETE; el enfoque es un CRUD simple en memoria."
        },
        {
          "id": "E1_P17",
          "tipo": "opcion_multiple",
          "enunciado": "En una API REST construida con Express, se configura middleware para procesar el cuerpo de las solicitudes que llegan en formato JSON. ¿Cuál es el propósito de usar app.use(express.json()) en este contexto?",
          "opciones": [
            "Permitir que Express sirva archivos estáticos",
            "Habilitar el parseo automático de cuerpos JSON en las peticiones",
            "Configurar el motor de plantillas HTML",
            "Asegurar la conexión HTTPS"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1xIuyDrokaCwCWPcxdoWsyXLRm3Iiqp6i",
          "feedback_correcta": "La función express.json() permite parsear automáticamente cuerpos JSON en las solicitudes.",
          "feedback_incorrecta": "express.json() no se relaciona con archivos estáticos ni con HTTPS; su función es procesar cuerpos JSON."
        },
        {
          "id": "E1_P18",
          "tipo": "opcion_multiple",
          "enunciado": "Una API expone la ruta GET /productos/:id para recuperar un producto específico a partir de su identificador. En Express, ¿cómo se denomina el segmento :id en esta ruta?",
          "opciones": [
            "Query string",
            "Middleware",
            "Parámetro de ruta",
            "Header obligatorio"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1lJp7-Zf5pXC8zpf7kLR_6eBkuGjswRHS",
          "feedback_correcta": "El segmento :id se conoce como parámetro de ruta en Express.",
          "feedback_incorrecta": "Es importante diferenciar los parámetros de ruta (/recurso/:id) de la query string (?id=...) y de los encabezados."
        },
        {
          "id": "E1_P19",
          "tipo": "opcion_multiple",
          "enunciado": "Se desea permitir que un cliente elimine un producto específico a través de una API REST. ¿Cuál de las siguientes rutas HTTP es más apropiada para implementar esta operación en un diseño basado en recursos?",
          "opciones": [
            "DELETE /productos",
            "DELETE /productos/:id",
            "GET /productos/delete",
            "POST /productos/remove/:id"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "15d_UP7OqoF9TrHd9BrVH6LqwplMd-ip_",
          "feedback_correcta": "La convención REST indica que DELETE /productos/:id es la forma adecuada de eliminar un recurso específico.",
          "feedback_incorrecta": "El patrón habitual es enviar DELETE sobre la URI del recurso concreto, no sobre rutas genéricas ni sobre GETs simulando borrado."
        },
        {
          "id": "E1_P20",
          "tipo": "opcion_multiple",
          "enunciado": "Una solicitud GET /productos/999 intenta recuperar un producto que no existe en la colección gestionada por la API. ¿Qué código de estado HTTP es más apropiado devolver en este caso?",
          "opciones": [
            "200 OK con un cuerpo vacío",
            "201 Created",
            "404 Not Found",
            "500 Internal Server Error"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1n7O4EBGiZ4ou9D4D3iGhXwPenlFk2zdP",
          "feedback_correcta": "El código 404 Not Found es el más adecuado cuando el recurso solicitado por id no existe.",
          "feedback_incorrecta": "El código 200 implica éxito con un recurso; cuando el recurso no se encuentra, el código estándar es 404."
        },
        {
          "id": "E1_P21",
          "tipo": "opcion_multiple",
          "enunciado": "Una API REST para productos ofrece la ruta PUT /productos/:id. El cliente envía un cuerpo JSON con los campos actualizados de un producto existente. ¿Cuál es el comportamiento esperado de esta operación según las prácticas habituales?",
          "opciones": [
            "Crear siempre un producto nuevo sin importar si existe",
            "Actualizar los campos del producto existente identificado por id",
            "Reiniciar el servidor",
            "Devolver siempre 204 sin contenido y sin cambios"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1hTUVkMsP9Bhb_Jpnd9GnTTc932H3fcHZ",
          "feedback_correcta": "La ruta PUT /productos/:id se emplea para actualizar los campos del producto existente identificado por ese id.",
          "feedback_incorrecta": "La semántica habitual de PUT es actualizar o reemplazar el recurso, no crear siempre ni responder sin cambios."
        },
        {
          "id": "E1_P22",
          "tipo": "opcion_multiple",
          "enunciado": "Durante el desarrollo de una API de ejemplo, se decide mantener los datos de productos y pedidos en estructuras de memoria en lugar de una base de datos. ¿Qué ventaja principal ofrece este enfoque en un entorno de laboratorio?",
          "opciones": [
            "Permite simular la lógica de negocio sin configurar una base de datos real",
            "Asegura durabilidad de datos entre reinicios",
            "Mejora la seguridad ante ataques externos",
            "Obliga a usar transacciones distribuidas"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "1bzogTOaCd-kI7BcdrBV-dkYEsO47J_on",
          "feedback_correcta": "Las estructuras en memoria permiten practicar la lógica y las rutas sin necesidad de configurar una base de datos real.",
          "feedback_incorrecta": "El objetivo de usar estructuras en memoria es simplificar la práctica de lógica y rutas, no garantizar persistencia ni transacciones."
        },
        {
          "id": "E1_P23",
          "tipo": "opcion_multiple",
          "enunciado": "Un cliente HTTP utiliza curl o Postman para crear un nuevo producto en una API REST. ¿Qué configuración representa correctamente una petición POST adecuada para este propósito?",
          "opciones": [
            "POST /products sin cuerpo, esperando que el servidor genere los datos",
            "POST /productos con encabezado Content-Type: application/json y un cuerpo JSON con los campos del producto",
            "GET /productos/new con parámetros en la URL",
            "PUT /productos con un cuerpo vacío"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "11af5mBSrI4npizQGToySf-caslqRyS-c",
          "feedback_correcta": "El patrón adecuado es POST /productos con Content-Type: application/json y un cuerpo JSON con los campos del producto.",
          "feedback_incorrecta": "POST sin cuerpo, GET para crear recursos o PUT vacío no corresponden al patrón principal utilizado para creación en la práctica."
        },
        {
          "id": "E1_P24",
          "tipo": "opcion_multiple",
          "enunciado": "Una API REST de una tienda en línea expone recursos como /productos y /pedidos, cada uno con sus propias rutas y lógica. ¿Qué principio de diseño se refuerza al separar las rutas por tipo de recurso?",
          "opciones": [
            "Que todas las rutas deben compartir el mismo prefijo",
            "La separación de responsabilidades por tipo de recurso en la API",
            "Que solo se puede definir un recurso por servidor",
            "Que los métodos HTTP son intercambiables"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1sSO1cZ7oHZUI84Ej6-gAuiJ7W8Z-txQZ",
          "feedback_correcta": "La extensión a productos y pedidos refuerza la separación de responsabilidades por tipo de recurso en la API.",
          "feedback_incorrecta": "El objetivo no es limitar a un solo recurso por servidor, sino definir rutas claras y separadas para cada tipo de entidad."
        },
        {
          "id": "E1_P25",
          "tipo": "opcion_multiple",
          "enunciado": "Una empresa evalúa migrar una aplicación monolítica de comercio electrónico a una arquitectura de microservicios. ¿Cuál es una diferencia clave entre la API monolítica mínima y una arquitectura de microservicios en este escenario?",
          "opciones": [
            "En el monolito, todo el código corre en un mismo despliegue; en microservicios se distribuye en servicios independientes",
            "En un monolito no se pueden usar rutas HTTP",
            "Los microservicios no pueden comunicarse vía HTTP",
            "El monolito siempre es más escalable que cualquier microservicio"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "15gNqPHspzCCByVfdkBK-W9WsY3XcGo3a",
          "feedback_correcta": "En un monolito el código se despliega como un solo artefacto, mientras que en microservicios se distribuye en servicios independientes.",
          "feedback_incorrecta": "La diferencia central radica en el modelo de despliegue: un artefacto único en el monolito frente a varios servicios autónomos en microservicios."
        }
      ]
    },
    {
      "titulo": "Examen 2 – Tipos de integración, SOAP vs REST, WSDL vs REST, prácticas de integración",
      "preguntas": [
        {
          "id": "E2_P01",
          "tipo": "opcion_multiple",
          "enunciado": "En una empresa mediana, los sistemas de ventas, inventarios y facturación se han conectado progresivamente mediante enlaces directos entre pares de aplicaciones. ¿Cómo se caracteriza este estilo de integración “punto a punto” cuando el número de sistemas crece?",
          "opciones": [
            "Un bus central que conecta todos los sistemas",
            "Conexiones directas específicas entre cada par de aplicaciones, generando “spaghetti” al crecer",
            "El uso exclusivo de colas de mensajes",
            "La obligación de usar solo SOAP/XML"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1OgUVgWAqP0-T08zjp5LvNozvOFHaknLz",
          "feedback_correcta": "La integración punto a punto se basa en conexiones directas entre pares de sistemas y tiende a generar un esquema tipo “spaghetti” al crecer.",
          "feedback_incorrecta": "En la integración punto a punto no existe un bus central; cada par de sistemas establece su propia integración específica."
        },
        {
          "id": "E2_P02",
          "tipo": "opcion_multiple",
          "enunciado": "Una organización que sufría alta complejidad por integraciones punto a punto decide reorganizar su arquitectura hacia servicios de negocio bien definidos. ¿Qué objetivo principal tiene la arquitectura SOA en comparación con ese “spaghetti” de integraciones?",
          "opciones": [
            "Aumentar el número de conexiones",
            "Agrupar la lógica en servicios de negocio con contratos claros y reutilizables",
            "Eliminar la necesidad de contratos",
            "Obligar a usar microservicios"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1uX4cVDs_JsyunugNXJ11-EOoXFSLan1v",
          "feedback_correcta": "SOA busca agrupar la lógica en servicios de negocio con contratos claros y reutilizables para reducir el “spaghetti”.",
          "feedback_incorrecta": "El objetivo de SOA no es incrementar conexiones, sino definir servicios reutilizables con contratos bien especificados."
        },
        {
          "id": "E2_P03",
          "tipo": "opcion_multiple",
          "enunciado": "Un equipo diseña una API pública para consulta de productos accesible desde navegadores y aplicaciones móviles, siguiendo principios REST. ¿Cuál de las siguientes afirmaciones describe mejor a REST en este contexto?",
          "opciones": [
            "Es un protocolo binario para redes locales",
            "Es un estilo arquitectónico que aprovecha HTTP y trata recursos mediante métodos estándar como GET, POST, PUT, DELETE",
            "Es un lenguaje de programación orientado a objetos",
            "Es un reemplazo obligatorio de SOAP en todos los contextos"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1VXNX18oxxZsfA9CZvW-dtd6ccJkKYLfm",
          "feedback_correcta": "REST se considera un estilo arquitectónico que utiliza HTTP y trata recursos con métodos como GET, POST, PUT y DELETE.",
          "feedback_incorrecta": "REST no es un protocolo binario ni un lenguaje de programación; se trata de un estilo arquitectónico para APIs."
        },
        {
          "id": "E2_P04",
          "tipo": "opcion_multiple",
          "enunciado": "Una startup expone sus servicios mediante una API para terceros. Decide usar REST con JSON en lugar de SOAP con XML para facilitar el consumo desde clientes ligeros. ¿Qué ventaja principal aporta REST+JSON en este caso?",
          "opciones": [
            "Mayores requisitos de herramientas especializadas",
            "Contratos más rígidos e inflexibles",
            "Mensajes más ligeros y fáciles de consumir desde navegadores y apps móviles",
            "Imposibilidad de usar HTTPS"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1c33znoKL-aKUGGYYkDMRdUSo2MAB0cXv",
          "feedback_correcta": "REST con JSON suele producir mensajes más ligeros y sencillos de consumir en navegadores y aplicaciones móviles.",
          "feedback_incorrecta": "La ventaja típica de REST+JSON es la simplicidad y ligereza de los mensajes, no una mayor rigidez ni requisitos de herramientas pesadas."
        },
        {
          "id": "E2_P05",
          "tipo": "opcion_multiple",
          "enunciado": "En una organización grande con varios años de historia tecnológica, se hace un inventario de sistemas. Se encuentran aplicaciones monolíticas, servicios SOAP heredados, APIs REST recientes y algunos componentes por eventos. ¿Qué situación describe mejor este panorama?",
          "opciones": [
            "Solo monolitos puros sin integración",
            "Solo microservicios sin legado",
            "La convivencia de monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos",
            "Exclusivamente colas de mensajes sin APIs"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "13QEofL_oVFICzKxIj_m90vqb-75zUPKH",
          "feedback_correcta": "En muchas organizaciones grandes coexisten monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos.",
          "feedback_incorrecta": "El panorama real suele mezclar estilos de integración; rara vez se eliminan por completo monolitos o servicios SOAP."
        },
        {
          "id": "E2_P06",
          "tipo": "opcion_multiple",
          "enunciado": "Dos sistemas comparten información de clientes mediante procesos nocturnos que replican tablas completas de datos. No se invocan operaciones remotas; solo se copian registros. ¿Qué tipo de integración se está realizando principalmente?",
          "opciones": [
            "Integración de datos",
            "Integración funcional",
            "Integración semántica",
            "Integración física"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "19_dQvJ3Sc_fo35gIWs_oajnSv9v8a-oi",
          "feedback_correcta": "Cuando se comparten o sincronizan tablas e información entre sistemas se habla de integración de datos.",
          "feedback_incorrecta": "La integración de datos se orienta a replicar y sincronizar información, a diferencia de la integración funcional que consume capacidades remotas."
        },
        {
          "id": "E2_P07",
          "tipo": "opcion_multiple",
          "enunciado": "Una aplicación móvil invoca un servicio remoto para ejecutar la operación \"consultar saldo\" en un sistema bancario central. ¿Qué tipo de integración representa mejor esta situación?",
          "opciones": [
            "Integración de datos",
            "Integración funcional",
            "Integración semántica",
            "Integración de red"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1ADt6MMLFKZoRNyjjINxfg9VRKieq5z2t",
          "feedback_correcta": "La integración funcional se refiere al consumo de capacidades de negocio remotas, como operaciones de consulta o creación.",
          "feedback_incorrecta": "La integración de datos se centra en tablas e información, mientras que la funcional se enfoca en invocar operaciones de negocio remotas."
        },
        {
          "id": "E2_P08",
          "tipo": "opcion_multiple",
          "enunciado": "En una empresa, dos sistemas utilizan el campo \"cliente\" pero con significados distintos: en uno incluye personas físicas y morales, y en otro solo personas físicas. Se busca que ambos sistemas manejen el mismo concepto. ¿A qué se refiere este tipo de esfuerzo de integración?",
          "opciones": [
            "A compartir archivos de texto sin estructura",
            "A alinear el significado de los datos y conceptos entre sistemas, evitando ambigüedades",
            "A comprimir mensajes para ahorrar ancho de banda",
            "A usar siempre el mismo tipo de base de datos"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1zvD07Fus2O_7F9eUQuhEBb8L8G3BWFQN",
          "feedback_correcta": "La integración semántica se centra en alinear el significado de datos y conceptos entre sistemas para evitar ambigüedades.",
          "feedback_incorrecta": "El problema semántico radica en que términos como “cliente” o “balance” tengan el mismo significado en todos los sistemas involucrados."
        },
        {
          "id": "E2_P09",
          "tipo": "opcion_multiple",
          "enunciado": "En un análisis de riesgos de integración, se identifican conexiones entre sistemas de nómina, facturación y reporteo. ¿Qué criterio es más adecuado para etiquetar una integración como crítica en este contexto?",
          "opciones": [
            "Que use JSON",
            "Que sea la que más ancho de banda consume",
            "Que, si falla, afecta procesos de negocio esenciales como facturación o pagos",
            "Que sea la más nueva"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "19ex8Wi_hrJV6lV9fJNwABsf3io85ZXR1",
          "feedback_correcta": "Una integración se considera crítica cuando su fallo impacta procesos esenciales del negocio, como facturación o pagos.",
          "feedback_incorrecta": "El carácter crítico se define por el impacto sobre procesos de negocio clave, no por el formato de mensaje ni por el ancho de banda."
        },
        {
          "id": "E2_P10",
          "tipo": "opcion_multiple",
          "enunciado": "Una empresa ha ido agregando integraciones directas entre aplicaciones a lo largo de varios años sin un diseño centralizado. Hoy tiene decenas de enlaces específicos entre pares de sistemas. ¿Qué efecto típico tiene esta acumulación de integraciones punto a punto?",
          "opciones": [
            "Facilita el mantenimiento porque todas son similares",
            "Disminuye la dependencia entre sistemas",
            "Aumenta la complejidad, la duplicación de lógica y el acoplamiento",
            "Elimina la necesidad de documentación"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1n8j0UdrKD86c2qIF-CmEauVl5niF-RBE",
          "feedback_correcta": "La acumulación de integraciones punto a punto incrementa la complejidad, la duplicación de lógica y el acoplamiento.",
          "feedback_incorrecta": "Un número creciente de integraciones punto a punto suele generar un panorama de “spaghetti” difícil de mantener."
        },
        {
          "id": "E2_P11",
          "tipo": "opcion_multiple",
          "enunciado": "Un sistema de salud expone servicios SOAP para registrar citas y consultar expedientes. Los mensajes intercambiados se basan en XML y siguen una estructura estándar con sobre, encabezado y cuerpo. ¿Cuál de las siguientes es una característica típica de SOAP en este entorno?",
          "opciones": [
            "Uso exclusivo de JSON",
            "Mensajes con sobre <Envelope>, <Header> y <Body> en XML",
            "Eliminación de contratos formales",
            "Comunicación solo dentro de un mismo proceso"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1FM47n53c7CP2dd8zz5FSkBkDpWbl1RBS",
          "feedback_correcta": "SOAP se caracteriza por mensajes en XML con elementos Envelope, Header y Body.",
          "feedback_incorrecta": "SOAP no se basa en JSON; su estructura estándar en XML con Envelope, Header y Body es una de sus características distintivas."
        },
        {
          "id": "E2_P12",
          "tipo": "opcion_multiple",
          "enunciado": "Un integrador recibe la descripción de un servicio SOAP que incluye operaciones como \"consultarCuenta\" y \"pagarServicio\". La descripción está en un archivo XML que documenta qué mensajes se envían y reciben. ¿Qué componente de la pila SOAP corresponde a este archivo?",
          "opciones": [
            "SOAP Envelope",
            "WSDL",
            "UDDI",
            "WS-Security"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1Ly6PrWAaVntVZhRiG7FkiDngSLFuH54u",
          "feedback_correcta": "WSDL es el componente que describe operaciones, mensajes y tipos de datos del servicio.",
          "feedback_incorrecta": "En la pila SOAP, WSDL actúa como contrato; SOAP define el protocolo de mensaje y UDDI ofrece un registro de servicios."
        },
        {
          "id": "E2_P13",
          "tipo": "opcion_multiple",
          "enunciado": "En un entorno empresarial, se adoptan especificaciones adicionales sobre SOAP para cubrir requisitos avanzados, como cifrado de mensajes, políticas de seguridad y transacciones distribuidas. ¿Qué rol jugaron las especificaciones WS-* en este ecosistema?",
          "opciones": [
            "Definir formatos de imagen",
            "Extender SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones",
            "Reemplazar completamente a WSDL",
            "Hacer innecesario el uso de XML"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1APVFFwf6vOeVYkzwhBY1InXqZHs7DDsZ",
          "feedback_correcta": "Las especificaciones WS-* extendieron SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones.",
          "feedback_incorrecta": "WS-* no reemplaza WSDL ni define formatos gráficos; añade capacidades empresariales a la pila SOAP."
        },
        {
          "id": "E2_P14",
          "tipo": "opcion_multiple",
          "enunciado": "En una integración entre un banco, una entidad gubernamental y un proveedor de salud, se observa que la mayoría de los servicios siguen siendo SOAP con contratos formales y WS-Security. ¿En qué sectores se considera que SOAP sigue siendo comúnmente utilizado?",
          "opciones": [
            "Redes sociales y aplicaciones de mensajería instantánea",
            "Videojuegos móviles informales",
            "Banca, gobierno y salud con fuertes requisitos regulatorios",
            "Sitios web estáticos"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1TMqz0vM228QUb1GG23yQymnFW4GdrcZg",
          "feedback_correcta": "SOAP sigue siendo frecuente en banca, gobierno y salud, donde existen requisitos regulatorios y de seguridad estrictos.",
          "feedback_incorrecta": "Estos sectores valoran contratos formales y WS-Security; SOAP no se asocia principalmente con redes sociales o juegos casuales."
        },
        {
          "id": "E2_P15",
          "tipo": "opcion_multiple",
          "enunciado": "Un integrador externo se conecta a un proveedor de servicios que documenta su interfaz mediante WSDL y especificaciones WS-Security. La integración ha sido estable durante años y cumple con regulaciones estrictas. ¿Cuál de las siguientes situaciones favorece seguir usando este servicio SOAP en lugar de migrarlo de inmediato a REST?",
          "opciones": [
            "El proveedor solo ofrece WSDL y WS-* y la integración es estable y de largo plazo",
            "La API se usa solo para pruebas internas temporales",
            "Se requiere una interfaz gráfica rica",
            "No hay requisitos de seguridad"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "12O_mANPHLZAhgDCWv_-eguBPJZiYE0Fg",
          "feedback_correcta": "Cuando el proveedor solo dispone de WSDL y WS-* y la integración es estable y de largo plazo, tiene sentido mantener SOAP.",
          "feedback_incorrecta": "Migrar a REST no siempre es prioritario si la integración SOAP es estable, regulada y responde a necesidades de largo plazo."
        },
        {
          "id": "E2_P16",
          "tipo": "opcion_multiple",
          "enunciado": "En una arquitectura híbrida, un servicio de cuentas se expone tanto como SOAP/XML como a través de una API REST/JSON. Al comparar los mensajes intercambiados, se nota que en SOAP siempre aparece un sobre con espacios de nombres, mientras que en REST no. ¿Cuál es una diferencia conceptual clave entre mensajes SOAP y mensajes REST/JSON en este escenario?",
          "opciones": [
            "REST/JSON obliga a usar WS-Security",
            "SOAP incluye un sobre estandarizado y namespaces; REST/JSON suele enviar directamente los datos sin esa envoltura",
            "SOAP no permite tipos de datos complejos",
            "REST requiere UDDI"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1w5p88DcwuhwfcIbNjWSwBEJ9yjXNj__-",
          "feedback_correcta": "SOAP incorpora un sobre estandarizado y namespaces, mientras que REST/JSON suele transmitir directamente los datos sin esa envoltura.",
          "feedback_incorrecta": "REST no obliga al uso de WS-Security ni de UDDI; su formato típico es JSON sin un Envelope estándar como en SOAP."
        },
        {
          "id": "E2_P17",
          "tipo": "opcion_multiple",
          "enunciado": "Al diseñar una API REST para gestión de pedidos, se buscan buenas prácticas para que otros equipos puedan consumirla fácilmente. ¿Qué descripción se ajusta mejor a una API REST bien diseñada?",
          "opciones": [
            "Operaciones definidas por verbos arbitrarios en la URL",
            "Recursos identificados por URIs y manipulados con métodos HTTP estándar y códigos de estado apropiados",
            "Mensajes exclusivamente XML",
            "Ausencia total de contrato o documentación"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1W0H8XssOvVhY5hvJFxEnZ2Tg85xXTN1q",
          "feedback_correcta": "Una API REST bien diseñada identifica recursos por URIs y los manipula usando métodos HTTP estándar y códigos de estado coherentes.",
          "feedback_incorrecta": "REST no se limita a la ausencia de contrato; se recomienda documentar recursos, métodos y respuestas de forma explícita."
        },
        {
          "id": "E2_P18",
          "tipo": "opcion_multiple",
          "enunciado": "Una organización planea modernizar su plataforma. Algunos sistemas críticos siguen exponiendo servicios SOAP, mientras que los nuevos desarrollos se plantean como microservicios REST. ¿En qué caso es especialmente importante decidir cuándo convivir con SOAP y encapsularlo y cuándo migrar a APIs más ligeras?",
          "opciones": [
            "Cuando solo hay un sistema aislado sin integraciones",
            "Cuando no hay restricciones regulatorias ni de seguridad",
            "Cuando se integran sistemas legacy SOAP con nuevas aplicaciones y microservicios",
            "Cuando todos los servicios ya son REST"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1apVzPHrJUXpG1SNXJCYsu0wy2yX7A_vT",
          "feedback_correcta": "El dilema entre convivir con SOAP y encapsularlo o migrar a APIs ligeras es especialmente relevante al integrar sistemas SOAP heredados con nuevas aplicaciones y microservicios.",
          "feedback_incorrecta": "Cuando todo el entorno es REST el problema se reduce; la decisión es crítica al coexistir con sistemas SOAP legacy."
        },
        {
          "id": "E2_P19",
          "tipo": "opcion_multiple",
          "enunciado": "Un área de TI describe una integración en la que el sistema de contabilidad copia cada noche la información de clientes desde el sistema de CRM para tener una copia local de esos datos. No se invocan funciones de negocio remotas, solo se replican registros. ¿Qué tipo de integración describe mejor esta situación?",
          "opciones": [
            "Funcional",
            "Semántica",
            "De datos",
            "De red"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1-Ixtt_pHWO1a-lCSYNfGoZQ82AwBsOZ-",
          "feedback_correcta": "La réplica nocturna de la tabla de clientes corresponde a un caso de integración de datos.",
          "feedback_incorrecta": "En este escenario no se invoca una función de negocio; se copian datos entre sistemas, lo cual encaja con integración de datos."
        },
        {
          "id": "E2_P20",
          "tipo": "opcion_multiple",
          "enunciado": "En otro escenario, una aplicación web permite consultar en tiempo real el saldo de un cliente llamando a una operación expuesta por un sistema de núcleo bancario remoto. ¿Qué tipo de integración representa mejor esta situación?",
          "opciones": [
            "De datos, porque solo importa la tabla de saldos",
            "Funcional, porque se consume una capacidad remota de negocio",
            "Semántica, porque solo se alinea el significado",
            "Física, porque usa redes móviles"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1gTD9Bu3IDYYxdvjOx2xWzzL62IUDK8gA",
          "feedback_correcta": "La invocación de la operación “consultar saldo” representa un ejemplo de integración funcional.",
          "feedback_incorrecta": "Aquí no se comparten tablas directamente, sino una capacidad de negocio remota; por ello se trata de integración funcional."
        },
        {
          "id": "E2_P21",
          "tipo": "opcion_multiple",
          "enunciado": "Al revisar la especificación de un servicio basado en SOAP, se observa un documento en XML que define tipos de datos, mensajes y operaciones mediante elementos como <portType>, <operation> y <message>. ¿Cuál de las siguientes opciones describe mejor este tipo de documento?",
          "opciones": [
            "Definiciones de paths y responses en JSON",
            "Elementos <portType>, <operation> y <message> que describen el contrato",
            "Documentación en formato Markdown",
            "Solo ejemplos de llamadas con curl"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1r4UGQJaB8N6RrlhdLSByDcFAf33jOZma",
          "feedback_correcta": "En un documento WSDL es habitual encontrar elementos como portType, operation y message que describen el contrato.",
          "feedback_incorrecta": "Las definiciones de paths y responses en JSON son propias de OpenAPI y REST, no de WSDL."
        },
        {
          "id": "E2_P22",
          "tipo": "opcion_multiple",
          "enunciado": "Una API REST pública para consulta de pedidos se publica junto con documentación accesible para desarrolladores externos. ¿Qué tipo de información suele incluir esta documentación para que otros puedan consumir la API correctamente?",
          "opciones": [
            "Qué URIs existen, qué métodos HTTP soportan, qué estructura de JSON esperan y devuelven",
            "Cómo generar código a partir de WSDL",
            "Cómo registrar el servicio en UDDI",
            "Cómo usar WS-Security"
          ],
          "correcta": [^17_1],
          "puntos": 1,
          "imagenPreguntaId": "15oKjqg8QMTO-iWOcGVCABj0NdOMXqVf3",
          "feedback_correcta": "La documentación de una API REST suele precisar qué URIs existen, qué métodos HTTP soportan y qué estructura JSON se espera en solicitudes y respuestas.",
          "feedback_incorrecta": "La generación de código a partir de WSDL y el registro en UDDI pertenecen al ámbito SOAP/WS-*, no a la documentación típica de REST."
        },
        {
          "id": "E2_P23",
          "tipo": "opcion_multiple",
          "enunciado": "Un arquitecto compara el contrato de un servicio SOAP descrito con WSDL y el contrato de una API REST documentado con OpenAPI. El objetivo es decidir qué estilo usar en un nuevo proyecto. ¿Qué objetivo conceptual se persigue al realizar esta comparación?",
          "opciones": [
            "Convertir siempre el WSDL en REST",
            "Identificar elementos de contrato en ambos enfoques y discutir ventajas/desventajas",
            "Demostrar que uno de los dos está obsoleto",
            "Medir solo el tamaño de los mensajes"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1n8uACVYclviYPopwsI2fKXVOPBWlYuaK",
          "feedback_correcta": "El objetivo consiste en identificar los elementos de contrato en WSDL y REST y reflexionar sobre sus ventajas y desventajas.",
          "feedback_incorrecta": "La intención no es declarar obsoleto a uno de los enfoques, sino comprender cómo cada uno expresa su contrato."
        },
        {
          "id": "E2_P24",
          "tipo": "opcion_multiple",
          "enunciado": "Un servicio de consulta de saldo se expone simultáneamente como SOAP y como API REST. Para SOAP se entrega un WSDL; para REST, se proporciona una especificación OpenAPI en formato JSON. ¿Qué diferencia práctica suele encontrarse entre ambos contratos?",
          "opciones": [
            "El SOAP se consume solo desde navegadores",
            "El WSDL describe tipos y operaciones en XML, mientras que la API REST suele usar JSON y documentación tipo OpenAPI o similar",
            "El SOAP es siempre más rápido",
            "La API REST no puede usar HTTPS"
          ],
          "correcta": [^17_2],
          "puntos": 1,
          "imagenPreguntaId": "1mxqb0333l-k8BiXEMrnV9lmFmkaqQNAI",
          "feedback_correcta": "En un servicio SOAP la funcionalidad se describe en WSDL mediante XML, mientras que en REST suele documentarse con JSON y especificaciones como OpenAPI.",
          "feedback_incorrecta": "Ambos pueden usar HTTPS; la diferencia suele estar en el formato del contrato (WSDL en XML frente a documentación JSON en REST)."
        },
        {
          "id": "E2_P25",
          "tipo": "opcion_multiple",
          "enunciado": "En la integración entre dos sistemas financieros, ambos intercambian un campo llamado \"balance\". En un sistema, representa saldo disponible; en el otro, saldo contable total. Esta diferencia genera inconsistencias en los reportes consolidados. ¿Qué tipo de problema se está ilustrando?",
          "opciones": [
            "Problema de sintaxis XML",
            "Problema de transporte HTTP",
            "Problema de integración semántica",
            "Problema exclusivo de rendimiento"
          ],
          "correcta": [^17_3],
          "puntos": 1,
          "imagenPreguntaId": "1NQHnMKsU6HVlprT689EAYYtIlJWtYyjI",
          "feedback_correcta": "El uso distinto del campo “balance” ilustra un problema de integración semántica.",
          "feedback_incorrecta": "En este caso el conflicto no reside en transporte ni en sintaxis, sino en el significado diferente que cada sistema asigna al mismo dato."
        }
      ]
    }
  ]
}
```

<div align="center">⁂</div>

[^17_1]: examenes.json

[^17_2]: mapa_pregunta_drive.json


---

```
# <q>const JSON_FILE_ID = 'PON_AQUI_EL_ID_DEL_JSON';  // <- cambia esto</q> Mi json está en mi Drive y para obtener el ID he usando "share" -> "copy link" esto es correcto?
```

Sí, usar “Compartir → Copiar enlace” sirve, pero de ese enlace debes extraer solo el ID.

Si el enlace que copias es algo como:

- `https://drive.google.com/file/d/1AbCdEfGhIjKlMnOpQrStUvWxYz123456/view?usp=sharing`

Entonces el **ID** es la parte entre `/d/` y `/view`:

- `1AbCdEfGhIjKlMnOpQrStUvWxYz123456`

En tu Apps Script debe quedar así:

```javascript
const JSON_FILE_ID = '1AbCdEfGhIjKlMnOpQrStUvWxYz123456';
```

No pongas la URL completa, solo ese ID.

---

# he revisado el script y genere un form tipo examen, pero el json que yo tengo contiene dos examenes, debo separarlos en dos json?

No hace falta separarlos; puedes:

- O bien subir **dos JSON** (uno por examen) y reutilizar la misma función.
- O adaptar el script para elegir qué examen del array usar.

Con tu estructura actual (`{ "examenes": [ {..}, {..} ] }`), puedes ajustar Apps Script así:

```javascript
function crearQuizDesdeJson() {
  const JSON_FILE_ID = 'ID_DEL_JSON';
  const INDICE_EXAMEN = 0;  // 0 para examen 1, 1 para examen 2

  const contenido = DriveApp.getFileById(JSON_FILE_ID)
    .getBlob()
    .getDataAsString('UTF-8');
  const data = JSON.parse(contenido);

  const examen = data.examenes[INDICE_EXAMEN];

  const form = FormApp.create(examen.titulo || 'Examen sin título');
  form.setIsQuiz(true);
  form.setShuffleQuestions(true);
  form.setProgressBar(true);

  examen.preguntas.forEach(p => {
    if (p.imagenPreguntaId) {
      const imgBlob = DriveApp.getFileById(p.imagenPreguntaId).getBlob();
      form.addImageItem()
        .setTitle(p.id)
        .setImage(imgBlob);
    }

    const item = form.addMultipleChoiceItem();
    item.setTitle(p.enunciado || p.id)
        .setRequired(true);

    const choices = p.opciones.map((texto, idx) => {
      const esCorrecta = (p.correcta || []).includes(idx + 1);
      return item.createChoice(texto, esCorrecta);
    });
    item.setChoices(choices);

    item.setPoints(typeof p.puntos === 'number' ? p.puntos : 1);

    if (p.feedback_correcta) {
      const fbCorrecta = FormApp.createFeedback()
        .setDisplayText(p.feedback_correcta)
        .build();
      item.setFeedbackForCorrect(fbCorrecta);
    }
    if (p.feedback_incorrecta) {
      const fbIncorrecta = FormApp.createFeedback()
        .setDisplayText(p.feedback_incorrecta)
        .build();
      item.setFeedbackForIncorrect(fbIncorrecta);
    }
  });

  Logger.log('Formulario creado: ' + form.getEditUrl());
}
```

Para crear el segundo examen, cambias solo:

```javascript
const INDICE_EXAMEN = 1;
```

y ejecutas de nuevo la función.

---

# Obtuve esto: cuando el script ponia el feedback para respuestas correctas: TypeError: FormApp.createFeedback(...).setDisplayText is not a function

En la API actual de Apps Script la forma correcta es usar **`setText()`**, no `setDisplayText()`; la documentación está medio inconsistente y por eso sale ese TypeError.[^20_1][^20_2][^20_3]

Solo cambia esas líneas del script:

De:

```javascript
const fbCorrecta = FormApp.createFeedback()
  .setDisplayText(p.feedback_correcta)
  .build();
item.setFeedbackForCorrect(fbCorrecta);

const fbIncorrecta = FormApp.createFeedback()
  .setDisplayText(p.feedback_incorrecta)
  .build();
item.setFeedbackForIncorrect(fbIncorrecta);
```

A:

```javascript
if (p.feedback_correcta) {
  const fbCorrecta = FormApp.createFeedback()
    .setText(p.feedback_correcta)
    .build();
  item.setFeedbackForCorrect(fbCorrecta);
}

if (p.feedback_incorrecta) {
  const fbIncorrecta = FormApp.createFeedback()
    .setText(p.feedback_incorrecta)
    .build();
  item.setFeedbackForIncorrect(fbIncorrecta);
}
```

`setText()` es el método soportado por `QuizFeedbackBuilder` y funciona bien con `setFeedbackForCorrect` / `setFeedbackForIncorrect` en items de opción múltiple.[^20_2][^20_4][^20_3]
<span style="display:none">[^20_10][^20_11][^20_12][^20_13][^20_14][^20_15][^20_5][^20_6][^20_7][^20_8][^20_9]</span>

<div align="center">⁂</div>

[^20_1]: https://stackoverflow.com/questions/79576722/how-to-set-feedback-for-multiple-choice-questions-using-google-script

[^20_2]: https://developers.google.com/apps-script/reference/forms/quiz-feedback-builder

[^20_3]: https://www.bazroberts.com/2017/11/21/apps-script-basics-17-making-quizzes-in-google-forms/

[^20_4]: https://developers.google.com/apps-script/reference/forms/multiple-choice-item

[^20_5]: https://developers.google.com/apps-script/reference/forms/quiz-feedback

[^20_6]: https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/google-apps-script/google-apps-script.forms.d.ts

[^20_7]: https://support.google.com/docs/thread/109483950/script-that-adds-new-responses-to-the-form?hl=en

[^20_8]: https://stackoverflow.com/questions/58517291/how-to-setting-feedback-which-should-be-automatically-shown-when-a-user-responds/58519772

[^20_9]: https://gist.github.com/indatawetrust/68505be60f5601ffff1d7948b9327fe0

[^20_10]: https://cloud.tencent.com/developer/ask/sof/108462199

[^20_11]: https://developers.google.com/apps-script/reference/forms/quiz-feedback-builder?hl=id

[^20_12]: https://groups.google.com/g/google-apps-script-community/c/V1Vw-DmO9PI

[^20_13]: https://developers.google.com/apps-script/reference/forms/feedback-type

[^20_14]: https://developers.google.com/apps-script/reference/forms/quiz-feedback?hl=ja

[^20_15]: https://www.youtube.com/watch?v=OQBpVRhJdQ8


---

# Con los siguientes dos bloques lo que sucede es que agraga la pregunta dos veces, una como imagen y otra como texto. yo necesito que solo ponga la pregunta como imagen en donde hace la form.addMultipleChoiceItem(),  en item settitle debe usarse la imagen.   "if (p.imagenPreguntaId) {

      const imgBlob = DriveApp.getFileById(p.imagenPreguntaId).getBlob();
      form.addImageItem()
        .setTitle(" ")  // texto pequeño arriba de la imagen
        .setImage(imgBlob);
    }
    
    
    // 3.2. Crear la pregunta (todas son opción múltiple)
    const item = form.addMultipleChoiceItem();
    item.setTitle(p.enunciado || p.id)
        .setRequired(true);"
    En Google Forms no puedes “poner una imagen como título” directamente en el `MultipleChoiceItem`; la imagen siempre es un `ImageItem` separado, y el `MultipleChoiceItem` necesita algún texto. La forma de ocultar la pregunta en texto es dejar un título mínimo neutro.

Puedes solucionar así:

1. **No uses el enunciado como título del ítem**, solo un marcador neutro (por ejemplo, un espacio o “Pregunta”).
2. Mantén la imagen inmediatamente antes, que es lo que el alumno verá como enunciado.

Quedaría:

```javascript
// 3.1. Añadir imagen si existe (enunciado visual)
if (p.imagenPreguntaId) {
  const imgBlob = DriveApp.getFileById(p.imagenPreguntaId).getBlob();
  form.addImageItem()
    .setTitle(" ")  // o "Pregunta", algo mínimo
    .setImage(imgBlob);
}

// 3.2. Crear la pregunta (todas son opción múltiple)
const item = form.addMultipleChoiceItem();
// título mínimo, sin enunciado real
item.setTitle(" ")  // o "Selecciona una opción", si quieres algo genérico
    .setRequired(true);
```

De esa forma:

- La **imagen** es lo que contiene la pregunta completa.
- El `MultipleChoiceItem` sólo muestra las opciones, con un título vacío/genérico que no revela el enunciado en texto.

---

# No, lo que yo quiero es que la imagen de la pregunta se agregue aquí "// 3.2. Crear la pregunta (todas son opción múltiple)

    const item = form.addMultipleChoiceItem();
    item.setTitle(p.enunciado || p.id)
        .setRequired(true);", de otra forma, cuando creas un form.addImageItem, el form genera un elemento separado de la pregunta. Lo que yo quiero es que la imagen aparazca ccuando se genera form.addMultipleChoiceItem(), y a ese item agregarle imagen a la pregunta con texto de pregunta Mínimo, como "Responde..."
    No se puede hacer exactamente lo que quieres solo con `FormApp`: la API clásica de Apps Script **no permite** adjuntar una imagen al título de un `MultipleChoiceItem`; solo permite:

- `addImageItem()` como ítem separado, o
- imágenes en opciones/preguntas creadas a mano en la UI, pero eso no está expuesto en `FormApp`.[^22_1][^22_2][^22_3]

Con `FormApp` puro, las opciones reales son:

1. **Imagen como ítem separado + título mínimo en la pregunta** (lo que ya tenías, ajustado):

```javascript
if (p.imagenPreguntaId) {
  const imgBlob = DriveApp.getFileById(p.imagenPreguntaId).getBlob();
  form.addImageItem()
    .setTitle("Pregunta")  // o "Responde..."
    .setImage(imgBlob);
}

const item = form.addMultipleChoiceItem();
item.setTitle("Responde...")
    .setRequired(true);
```

Aquí la imagen va justo encima y el texto del ítem es genérico; el enunciado real solo existe en la imagen.
2. **Pasar al Forms API REST**, que sí permite imagen dentro de la pregunta (no como ítem separado).
Esto implica:
    - Activar la **Google Forms API** en tu proyecto.
    - Usar `UrlFetchApp` o Python para llamar a `forms.batchUpdate` y añadir `imageItem` dentro de un `questionItem`.[^22_3][^22_4]

Si quieres mantener todo dentro de Apps Script sencillo y ya te está funcionando el resto (claves, feedback, etc.), la opción práctica es la 1: aceptar que la imagen será un `ImageItem` inmediatamente antes, y el `MultipleChoiceItem` tendrá solo un título genérico tipo “Selecciona la respuesta correcta”.
<span style="display:none">[^22_10][^22_11][^22_12][^22_13][^22_14][^22_15][^22_16][^22_5][^22_6][^22_7][^22_8][^22_9]</span>

<div align="center">⁂</div>

[^22_1]: https://stackoverflow.com/questions/51427821/insert-image-in-multiplechoiceitem-in-google-forms-with-google-apps-script

[^22_2]: https://stackoverflow.com/questions/67480686/how-to-get-image-inside-a-form-item-in-google-apps-scripts

[^22_3]: https://gist.github.com/tanaikech/bac38226e863a398f55b5c3d817d86ed

[^22_4]: https://developers.google.com/workspace/forms/api/guides/create-form-quiz

[^22_5]: https://developers.google.com/apps-script/reference/forms/multiple-choice-item

[^22_6]: https://issuetracker.google.com/issues/215967255

[^22_7]: https://support.google.com/docs/thread/90759117/how-to-add-image-in-paragraphtextitem-multiplechoiceitem-in-google-form?hl=en

[^22_8]: https://developers.google.com/apps-script/reference/forms/image-item

[^22_9]: https://support.google.com/docs/thread/57322909/i-can-t-set-images-to-choice-items-in-google-forms-with-apps-script-gas?hl=en

[^22_10]: https://stackoverflow.com/questions/41210292/inserting-images-to-a-multiple-choice-field-in-google-forms-using-apps-script

[^22_11]: https://developers.google.com/apps-script/reference/forms

[^22_12]: https://gist.github.com/ttsukagoshi/d9fad5b8865066ddefa64be9cff208d0

[^22_13]: https://www.reddit.com/r/googlesheets/comments/1amaxl1/apps_script_to_add_multiple_choice_questions_to/

[^22_14]: https://stackoverflow.com/questions/71038070/adding-image-to-the-sectionheaderitem-in-google-forms-apps-script

[^22_15]: https://www.youtube.com/watch?v=_r17AsOEYKw

[^22_16]: https://developers.google.com/apps-script/reference/forms/multiple-choice-item?hl=hi


---

# No me sirve la solución actual, pues el motivo de tener preguntas como imagen es que no las tuvieran en texto para poder copiar facilmente y en segundo porque el examen presenta las preguntas en orden aleatorio y al estar separadas se desconectan las preguntas de sus opciones de respuesta

Con la API clásica (`FormApp`) **no se puede** adjuntar la imagen al `MultipleChoiceItem`: siempre será un `ImageItem` separado, y si activas “barajar preguntas”, se separan. Eso rompe justo tus dos requisitos (sin texto y pegado a la pregunta).

Para lograr:

- pregunta = solo imagen
- opciones ligadas a esa imagen aunque el examen baraje

necesitas usar la **Google Forms API REST**, que sí permite un `questionItem` con campo `image` dentro.[^23_1][^23_2]

### Qué cambia en la solución

En vez de:

- `FormApp.addMultipleChoiceItem()` + `addImageItem()`

tienes que:

1) Crear el Form (puedes hacerlo una vez a mano o con Apps Script).
2) Usar un script (Apps Script o Python) que llame a `forms.batchUpdate` con requests tipo:
```json
{
  "createItem": {
    "item": {
      "title": "Responde...",
      "questionItem": {
        "image": {
          "sourceUri": "https://drive.google.com/uc?export=view&id=ID_DE_LA_IMAGEN"
        },
        "question": {
          "required": true,
          "grading": {
            "pointValue": 1,
            "correctAnswers": {
              "answers": [{ "value": "B" }]
            },
            "whenRight": { "text": "feedback correcta..." },
            "whenWrong": { "text": "feedback incorrecta..." }
          },
          "choiceQuestion": {
            "type": "RADIO",
            "options": [
              { "value": "A" },
              { "value": "B" },
              { "value": "C" },
              { "value": "D" }
            ],
            "shuffle": false
          }
        }
      }
    },
    "location": { "index": 0 }
  }
}
```

La clave es el bloque `questionItem.image.sourceUri`: ahí va la URL pública de tu PNG en Drive.[^23_3][^23_1]

### Sugerencia práctica

Dado todo lo que ya tienes montado, el siguiente paso razonable sería:

- Seguir usando Python (donde ya manejas IDs de imágenes) para:
    - Crear el Form vacío vía Forms API.
    - Hacer un `batchUpdate` por cada pregunta usando el JSON que ya generaste.

Si quieres, en el siguiente mensaje puedo darte:

- Un ejemplo completo de `batchUpdate` en Python para **una** pregunta con imagen, opciones, clave y feedback, usando tu estructura actual (`imagenPreguntaId`, etc.).
<span style="display:none">[^23_10][^23_11][^23_12][^23_13][^23_14][^23_15][^23_4][^23_5][^23_6][^23_7][^23_8][^23_9]</span>

<div align="center">⁂</div>

[^23_1]: https://stackoverflow.com/questions/72284995/adding-image-to-question-item-in-the-new-google-form-rest-api

[^23_2]: https://developers.google.com/workspace/forms/api/reference/rest/v1/forms

[^23_3]: https://developers.google.com/workspace/forms/api/reference/rest/v1beta/forms

[^23_4]: https://developers.google.com/workspace/forms/api/reference/rest/v1beta/forms?hl=it

[^23_5]: https://googleapis.dev/dotnet/Google.Apis.Forms.v1/latest/api/Google.Apis.Forms.v1.Data.QuestionItem.html

[^23_6]: https://www.sharonstutorials.com/how-to-add-images-to-questions-in-google-forms/

[^23_7]: https://www.youtube.com/watch?v=eszbh2OZj7U

[^23_8]: https://googleapis.dev/dotnet/Google.Apis.Forms.v1/latest/api/Google.Apis.Forms.v1.Data.QuestionGroupItem.html

[^23_9]: https://www.youtube.com/watch?v=_cCPydccqMQ

[^23_10]: https://support.microsoft.com/en-us/office/add-a-picture-to-a-question-72ffc881-c22e-4069-8468-400d1c580871

[^23_11]: https://developers.google.com/apps-script/reference/forms/image-item

[^23_12]: https://www.youtube.com/watch?v=O3D8ufuOctQ

[^23_13]: https://support.microsoft.com/vi-vn/office/thêm-ảnh-vào-câu-hỏi-72ffc881-c22e-4069-8468-400d1c580871

[^23_14]: https://developers.google.com/workspace/forms/api/guides

[^23_15]: https://stackoverflow.com/questions/76479192/adding-alt-text-to-an-image-in-google-forms-api


---

# Sí, dame ese batchupdate

Te dejo un ejemplo mínimo en **Python** que hace un `forms.batchUpdate` para crear **una pregunta** de opción múltiple con:

- Imagen incrustada en la pregunta.
- Opciones de texto.
- Clave correcta.
- Feedback correcto/incorrecto.
- Puntos.

Lo puedes adaptar a tu JSON y repetir por todas las preguntas.

***

## 1. Preparar entorno Forms API

Sigue primero el quickstart oficial (es parecido al de Drive, pero usando la Forms API): habilitar Forms API y crear credenciales de escritorio.[^24_1][^24_2]

Instala:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Y usa un `SCOPES` que incluya Forms y Drive (para leer imágenes si las necesitas por URL), por ejemplo:

```python
SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/forms.body.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]
```

(Para solo crear el formulario no necesitas drive.readonly, pero no estorba.)

***

## 2. Crear el Form vacío

```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os, json

SCOPES = [
    "https://www.googleapis.com/auth/forms.body"
]

def get_forms_service():
    creds = None
    if os.path.exists("token_forms.json"):
        creds = Credentials.from_authorized_user_file("token_forms.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials_forms.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token_forms.json", "w") as token:
            token.write(creds.to_json())
    return build("forms", "v1", credentials=creds)

def crear_form_vacio(titulo):
    service = get_forms_service()
    body = {
        "info": {
            "title": titulo,
            "documentTitle": titulo
        }
    }
    form = service.forms().create(body=body).execute()
    return form["formId"]
```

Llama una vez:

```python
form_id = crear_form_vacio("Examen 1 – SOAP / REST")
print(form_id)
```

Ese `form_id` lo usarás en `batchUpdate`.

***

## 3. `batchUpdate` para UNA pregunta con imagen

Supongamos que ya tienes:

```python
p = {
  "id": "E1_P01",
  "enunciado": "…texto…",
  "opciones": ["A", "B", "C", "D"],
  "correcta": [^24_2],
  "puntos": 1,
  "imagenPreguntaId": "1if6aGtqXCwVXtrEnX2aTN4As8SCEqx-I",
  "feedback_correcta": "XML se utiliza para representar datos jerárquicos…",
  "feedback_incorrecta": "XML en servicios web se valora por su estructura jerárquica…"
}
```

Necesitas una URL pública de la imagen. Lo más simple: construirla como:

```python
def drive_id_a_url(id_):
    # versión simple, asumiendo que ya diste permiso "cualquiera con el enlace"
    return f"https://drive.google.com/uc?export=view&id={id_}"
```

Ejemplo de `batchUpdate`:

```python
def agregar_pregunta_con_imagen(form_id, p, index):
    service = get_forms_service()

    # construimos opciones
    opciones = [{"value": texto} for texto in p["opciones"]]

    # valor correcto: aquí uso la letra (A, B, C, D) como value
    idx_correcta = p["correcta"][^24_0] - 1
    valor_correcto = p["opciones"][idx_correcta]

    req = {
        "requests": [
            {
                "createItem": {
                    "item": {
                        "title": "Responde...",  # texto mínimo que verá el alumno
                        "description": p["id"],  # opcional, por si quieres dejar rastro interno
                        "questionItem": {
                            "image": {
                                "sourceUri": drive_id_a_url(p["imagenPreguntaId"]),
                                "altText": p["enunciado"][:100]  # opcional
                            },
                            "question": {
                                "required": True,
                                "grading": {
                                    "pointValue": p.get("puntos", 1),
                                    "correctAnswers": {
                                        "answers": [
                                            {"value": valor_correcto}
                                        ]
                                    },
                                    "whenRight": {
                                        "text": p.get("feedback_correcta", "")
                                    },
                                    "whenWrong": {
                                        "text": p.get("feedback_incorrecta", "")
                                    }
                                },
                                "choiceQuestion": {
                                    "type": "RADIO",
                                    "options": opciones,
                                    "shuffle": False
                                }
                            }
                        }
                    },
                    "location": {
                        "index": index
                    }
                }
            }
        ]
    }

    service.forms().batchUpdate(formId=form_id, body=req).execute()
```

Uso:

```python
# Cargar tu JSON de examenes (el que ya te generé con imagenPreguntaId)
with open("examenes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

examen = data["examenes"][^24_0]  # 0 = Examen 1
form_id = "EL_ID_DEL_FORM_QUE_CREASTE_ANTES"

for i, p in enumerate(examen["preguntas"]):
    agregar_pregunta_con_imagen(form_id, p, index=i)
```

Puntos clave:

- `questionItem.image.sourceUri` recibe una URL accesible públicamente; si las imágenes no están compartidas, tendrás que darles permiso “cualquiera con el enlace” o servirlas desde otro lado.[^24_3][^24_4]
- En `correctAnswers.answers[].value` debe ir exactamente el mismo texto que en la opción (`"value": texto`), por eso uso `valor_correcto = p["opciones"][idx_correcta]`.[^24_2][^24_5]
- `location.index` controla el orden; luego en el Form puedes activar “Barajar preguntas” y la imagen sigue pegada a la pregunta porque está dentro del `questionItem`, no como ítem separado.[^24_6][^24_2]

Si quieres, después afinamos:

- Soporte para varias respuestas correctas (checkbox).
- Crear el form como **quiz** (`settings.quiz = true`) vía otro `batchUpdate`.
<span style="display:none">[^24_10][^24_11][^24_12][^24_13][^24_14][^24_15][^24_16][^24_7][^24_8][^24_9]</span>

<div align="center">⁂</div>

[^24_1]: https://developers.google.com/workspace/forms/api/quickstart/python

[^24_2]: https://developers.google.com/workspace/forms/api/guides/update-form-quiz

[^24_3]: https://7ed28yqx0a.apidog.io/api-3506496

[^24_4]: https://stackoverflow.com/questions/72284995/adding-image-to-question-item-in-the-new-google-form-rest-api

[^24_5]: https://developers.google.com/workspace/forms/api/guides/setup-grading

[^24_6]: https://developers.google.com/forms/api/reference/rest/v1beta/forms/batchUpdate

[^24_7]: https://stackoverflow.com/questions/74681379/i-have-a-question-about-multiple-choice-grid-in-google-forms-api

[^24_8]: https://github.com/fguogufe2/GoogleFormsAPITutorial/blob/main/readMe.md

[^24_9]: https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate

[^24_10]: https://stackoverflow.com/questions/74848206/how-do-i-use-the-google-forms-api-with-python-to-update-the-correct-answers-of-a

[^24_11]: https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/create

[^24_12]: https://googleapis.github.io/google-api-python-client/docs/dyn/forms_v1.forms.html

[^24_13]: https://github.com/JacobNoahGlik/GradeAssistant_PoC

[^24_14]: https://stackoverflow.com/questions/71714110/can-you-submit-a-restful-request-to-a-google-forms-api

[^24_15]: https://docs.cloud.google.com/workflows/docs/reference/googleapis/forms/Overview

[^24_16]: https://developers.google.com/workspace/forms/api/reference/rest/v1beta/forms

