# UAM
Para hacer presentaciones Reveal de la UAM

# Por hacer

Hay varias cosas que habrá que remover, pero hay que ir viendo cuales sirven y cuales no.

La versión actual de este proyecto genera presentaciones en revealjs con elementos gráficos para la UAM Cuajimalpa. Esto esta muy bien, pero en caso de querer parametrizar las presentaciones se vuelve complicado. Entre las cosas por hacer están: hacer la versión parametrizada para las presentaciones. El script actual se invoca desde la línea de comandos y recibe parámetros, tal vez hay que agregarle un(os) parámetro(s) más para que utilice los elementos visuales que correspondan. 

Otra cosa que se podría hacer en este caso con **RevealJS** es utilizar las capacidades de transiciones hacia abajo y hacia arriba, como si fueran temas que se desprenden de alguna diapositiva de título, hay que pensar en ello. También se pueden agregar animaciones al código y hacer resatado de código con highlights y también están las animaciones de bullets de diapositiva normal (fragments con toda una variedad de opciones), tiene una opción auto-animate (ver demo: https://revealjs.com/demo/?view=scroll), están también el fit text que pone texto a la diapositiva completa y la exportación a pdf.

También hace falta hacer una página de índice para poder navegar en todas las presentaciones, esta página puede ser más bien privada y personal para saber que hay y poder compartir más facilmente y mantenerla manualmente. 

Algunas ideas anteriores...

Otras cosas que hay que hacer en la versión actual de la aplicación es generar dos versiones de las presentaciones, 

1. para las presentaciones en la clase que usen las rutas relativas y
2. otra que use las rutas absolutas, porque esas son las que usarán los alumnos cuando descarguen el html. Las relativas no les servirán (pues no habrá nada relativo ahí)
3. Hay una tercera opción que es hacer una versión de rutas relativas para github y que usen esas versiones, ahi si funcionará lo relativo y además no tendrán que descargar nada.





