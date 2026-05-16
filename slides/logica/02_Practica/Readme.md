# Instrucciones

Para cuando se usa latex en una página una solución sencilla es que después de que se genera o convierte el markdown a html se agregue al html lo siguiente:


<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js"></script>
<script>
window.onload = () => {
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "$", right: "$", display: false}
    ]
  });
};
</script>

todo esto justo antes del style

Para que el contenido se muestre bien las formulas deben estar entre $ $ o $$ $$

