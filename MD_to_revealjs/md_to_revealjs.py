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

def load_decorative_images_from_parent(folder_name: str = "img") -> list:
    """
    Busca imágenes en ../<folder_name> respecto al directorio del script
    y devuelve rutas RELATIVAS respecto al cwd actual.
    """
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
        if not self.current_text_buffer or not any(l.strip() for l in self.current_text_buffer):
            self.current_text_buffer = []
            return

        paragraph = self._join_lines_to_paragraph(self.current_text_buffer)
        sentences = self._split_into_sentences(paragraph)

        if self.debug:
            print(f"  -> Flush texto: {len(sentences)} frases")

        chunk: List[str] = []
        for sent in sentences:
            if not isinstance(sent, str):
                continue
            if not sent.strip():
                continue
            chunk.append(sent.strip())
            if len(chunk) >= self.max_sentences_per_slide:
                self._add_text_slide(chunk)
                chunk = []
        if chunk:
            self._add_text_slide(chunk)

        self.current_text_buffer = []

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
        <style>
        
        /* Usar más ancho de pantalla */
        .reveal .slides {{
            width: 95%;
            margin: 0 auto;
        }}
        .reveal section {{
            padding: 0.5em 0.5em;
        }}
        
        /* Slides de portada/cierre con imagen casi a pantalla completa */
        .full-image-slide {{
            text-align: center;
        }}
        .full-image-slide .full-slide-image {{
            max-width: 100%;
            max-height: 90vh;
            object-fit: cover;
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
            grid-template-columns: 1fr 1fr;
            grid-gap: 1.5rem;
            align-items: center;
        }}
        .slide-two-col .text-col {{
            font-size: 0.9em;
            text-align: left;
        }}
        .slide-two-col .image-col img {{
            max-width: 100%;
            border-radius: 8px;
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
      <img src="https://juan-alvarado-uk.github.io/UAM/logos/variacion5Cua.png"  width = "200" alt="Logo">
      <p style="color:grey;font-size:18px;">&nbsp;&nbsp;&nbsp;Dr. Juan Alvarado</p>
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
            title_overlay = '<h1>Integración de Sistemas</h1>'
            # title_overlay = ""
        elif kind == "closing":
            title_overlay = '<h2>Gracias</h2>'

        full_src = "https://juan-alvarado-uk.github.io/UAM/" + img[3:]
        img_html = f'<img class="full-slide-image" src="{full_src}" alt="slide image" />'

        return f"""    <section class="full-image-slide">
              {img_html}
              {title_overlay}
            </section>"""

    def _render_content_slide(self, slide: Dict[str, Any]) -> str:
        title = self._escape_html(slide["title"])
        blocks_html: List[str] = []

        # Slides con imagen decorativa → dos columnas
        if slide.get("image") and slide.get("image_side") in ("left", "right"):
            full_src = "https://juan-alvarado-uk.github.io/UAM/" + slide["image"][3:]
            img_html = f'<img src="{full_src}" alt="image" />'
            text_html = self._render_blocks_as_text(blocks=slide.get("content_blocks", []))

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
            # Sin imagen: texto/código/tabla ocupan todo el ancho
            txt = self._render_blocks_fullwidth(slide.get("content_blocks", []))
            body = txt

        return f"""    <section>
      <h2>{title}</h2>
{body}
    </section>"""

    def _render_blocks_as_text(self, blocks: List[Dict[str, Any]]) -> str:
        """Solo renderiza bloques de texto como lista; ignora código/tablas aquí."""
        parts: List[str] = []
        for block in blocks:
            if block["kind"] == "text":
                lis = "".join(f"<li>{self._escape_html(s)}</li>" for s in block["sentences"])
                parts.append(f"<ul>{lis}</ul>")
        return "\n".join(parts)

    def _render_blocks_fullwidth(self, blocks: List[Dict[str, Any]]) -> str:
        parts: List[str] = []
        for block in blocks:
            kind = block["kind"]
            if kind == "text":
                lis = "".join(f"<li>{self._escape_html(s)}</li>" for s in block["sentences"])
                parts.append(f"""      <div class="text-col">
        <ul>
{lis}
        </ul>
      </div>""")
            elif kind == "code":
                code = "\n".join(block["lines"])
                code = self._escape_html(code)
                lang_class = f"language-{block['language']}" if block["language"] else ""
                parts.append(f"""      <pre><code class="{lang_class}">{code}</code></pre>""")
            elif kind == "table":
                parts.append(self._render_table(block["lines"]))
        return "\n".join(parts)

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
    parser = argparse.ArgumentParser(description="Convierte Markdown a Reveal.js")
    parser.add_argument("input", help="Archivo Markdown de entrada")
    parser.add_argument("-o", "--output", default="presentation.html",
                        help="Archivo HTML de salida")
    parser.add_argument("-t", "--theme", default="black",
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
    if not args.no_images: #and DECORATIVE_IMAGES:
        cover_img = "../logos/cua_05.jpg"   # random.choice(DECORATIVE_IMAGES)
        closing_img = "../logos/cua_01.jpg"   # random.choice(DECORATIVE_IMAGES)

    if cover_img:
        converter._add_cover_slide(cover_img)
    if closing_img:
        converter._add_closing_slide(closing_img)

    html = converter.generate_html(theme=args.theme)

    output_path = Path(args.output)
    output_path.write_text(html, encoding="utf-8")

    print(f"✓ Presentación generada en {output_path}")
    print(f"  - Diapositivas: {len(converter.slides)}")


if __name__ == "__main__":
    main()
