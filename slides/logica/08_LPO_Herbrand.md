# Transformación hacia cláusulas y preparación de Herbrand

# Alcance

El foco ahora va de las reglas con cuantificadores a la transformación sistemática de fórmulas hacia formas cercanas a cláusulas. Con esas formas, el análisis de satisfacibilidad se puede plantear usando universos, bases e interpretaciones de Herbrand, que viven completamente en el plano sintáctico del lenguaje. 

***
El objetivo práctico consiste en entender por qué se eliminan implicaciones, cómo se empujan negaciones, para qué sirve la forma prenexa y qué papel juega la skolemización. A partir de ahí, se introducen las nociones de universo y base de Herbrand, así como interpretaciones sencillas para decidir satisfacibilidad de conjuntos pequeños de cláusulas. 

***

# Hacia formas cercanas a cláusulas

Una **cláusula** es una disyunción de literales, donde un **literal** es un átomo o la negación de un átomo. Trabajar con conjuntos de cláusulas conviene porque la representación se vuelve uniforme y facilita el análisis de satisfacibilidad mediante procedimientos sistemáticos. 

***
Si cada fórmula tuviera una forma arbitraria, el razonamiento mecánico sería desordenado. 

Al llevarlas a una forma cercana a cláusulas, se reduce la variedad superficial y se hace visible la estructura lógica relevante. 

***
El punto central es entender por qué se eliminan implicaciones, por qué las negaciones se empujan hacia adentro y por qué las existencias se reemplazan mediante términos especiales: todo eso acerca la fórmula a un conjunto de cláusulas sobre el cual puede trabajarse de manera más sistemática. 

***

# Eliminar implicaciones y bicondicionales

La eliminación de implicaciones reemplaza conectivos como \(\rightarrow\) y \(\leftrightarrow\) por combinaciones de negación, conjunción y disyunción. Este paso es importante porque las cláusulas se construyen más fácilmente cuando la fórmula ya no depende de conectivos derivados. 

***
Las equivalencias básicas que interesan son:

- \(A \to B \equiv \neg A \lor B\)  
- \(A \leftrightarrow B \equiv (A \to B) \land (B \to A)\)  

:::fullwidth
Ejemplo:
\[
\forall x \, (Servidor(x) \rightarrow Disponible(x))
\]
se reescribe como
\[
\forall x \, (\neg Servidor(x) \lor Disponible(x))
\]
Esta forma ya se parece mucho más a una cláusula, porque dentro del alcance del cuantificador aparece una disyunción de literales. 

:::fullwidth
Ejemplo fuera del ámbito tecnológico:
\[
\forall x \, (Estudiante(x) \rightarrow UsaBiblioteca(x))
\]
pasa a
\[
\forall x \, (\neg Estudiante(x) \lor UsaBiblioteca(x))
\]
La información semántica es la misma; lo que cambia es la forma de presentación para facilitar pasos posteriores. 

***

# Mover negaciones hacia adentro

Mover negaciones hacia adentro significa usar leyes como De Morgan y las reglas para cuantificadores negados, con el fin de dejar la negación lo más cerca posible de los átomos. La meta es evitar negaciones aplicadas a fórmulas grandes, porque una cláusula trabaja con literales simples. 

***
Las transformaciones más importantes son:

- \(\neg (A \land B) \equiv \neg A \lor \neg B\)  
- \(\neg (A \lor B) \equiv \neg A \land \neg B\)  
- \(\neg \forall x \, A(x) \equiv \exists x \, \neg A(x)\)  
- \(\neg \exists x \, A(x) \equiv \forall x \, \neg A(x)\)  

:::fullwidth
Ejemplo:
\[
\neg \forall x \, (Usuario(x) \rightarrow Autorizado(x))
\]
primero se transforma en
\[
\exists x \, \neg (Usuario(x) \rightarrow Autorizado(x))
\]
y luego, al eliminar la implicación, queda
\[
\exists x \, \neg (\neg Usuario(x) \lor Autorizado(x))
\]

:::fullwidth
por De Morgan se obtiene
\[
\exists x \, (Usuario(x) \land \neg Autorizado(x))
\]
La negación ya quedó pegada al átomo \(Autorizado(x)\), que es el tipo de forma que nos interesa conservar. 

***
Este proceso es, digamos... despejar la expresión hasta dejarla compuesta por piezas manejables. 

***

# Forma prenexa

La forma prenexa es una presentación de la fórmula donde todos los cuantificadores quedan al frente y, después de ellos, aparece una parte libre de cuantificadores llamada matriz. Esta forma resulta útil porque separa el “patrón de cuantificación” de la estructura proposicional interna. 

***
Ejemplo:
\[
(\forall x \, P(x)) \lor (\forall y \, Q(y))
\]
bajo condiciones de variables adecuadas puede reacomodarse como una fórmula con cuantificador al frente. Conviene ordenar primero quiénes son los objetos sobre los que se habla y después qué condición se afirma sobre ellos. 

***
Para la preparación de Herbrand, la forma prenexa ayuda porque pone los cuantificadores en una zona visible y permite identificar con claridad cuáles son universales y cuáles existenciales antes del paso de skolemización. 

***

# Skolemización

La skolemización elimina cuantificadores existenciales reemplazando las variables existenciales por términos especiales llamados términos de Skolem. La idea es introducir un “testigo simbólico” que represente al objeto cuya existencia estaba garantizada por la fórmula. 

***
Si la existencia no depende de variables universales anteriores, el testigo puede ser una constante nueva. 

:::fullwidth 
Por ejemplo, de una forma como \[\exists x \, ServidorRespaldo(x)\] se pasa a \[ServidorRespaldo(c)\] 
donde \(c\) es una nueva constante de Skolem que nombra a algún servidor de respaldo garantizado por la existencia. 

***
Si la existencia sí depende de variables universales previas, el testigo ya no es una constante sino una función. 

:::fullwidth
Por ejemplo, en
\[
\forall x \, \exists y \, Atiende(y,x)
\]
el objeto \(y\) puede depender de \(x\), así que se reemplaza por \(f(x)\), obteniendo una forma como
\[
\forall x \, Atiende(f(x),x)
\]
donde \(f\) representa “el atendiente asociado a \(x\)”. 

:::fullwidth
Ejemplo fuera de tecnología:
\[
\forall x \, (Persona(x) \rightarrow \exists y \, MadreDe(y,x))
\]
puede esbozarse como
\[
\forall x \, (Persona(x) \rightarrow MadreDe(m(x),x))
\]
donde \(m(x)\) funciona como “la madre de \(x\)” dentro del lenguaje formal. No se está diciendo que se conozca el nombre real de esa persona, sino que se introduce un símbolo que garantiza el papel lógico del testigo. 

***
La skolemización convierte existencias en términos concretos del lenguaje, y eso permite construir instancias y cláusulas sin cargar con el cuantificador existencial original. 

***

# Paso final hacia cláusulas

Después de eliminar implicaciones, mover negaciones, llevar la fórmula a forma prenexa y skolemizar, la expresión queda muy cerca de una forma normal conjuntiva de primer orden. En esa etapa, los cuantificadores universales suelen omitirse por convención y la matriz se interpreta como un conjunto de cláusulas. 

:::fullwidth
Ejemplo:

Fórmula inicial:
\[
\forall x \, (Usuario(x) \rightarrow \exists y \, Recurso(y) \land PuedeUsar(x,y))
\]

Esbozo de transformación:
- Eliminar implicación:
\[
\forall x \, (\neg Usuario(x) \lor \exists y \, (Recurso(y) \land PuedeUsar(x,y)))
\]

:::fullwidth
- Llevar a forma apta para skolemizar:
\[
\forall x \, \exists y \, (\neg Usuario(x) \lor (Recurso(y) \land PuedeUsar(x,y)))
\]

- Skolemizar \(y\) como \(f(x)\):
\[
\forall x \, (\neg Usuario(x) \lor (Recurso(f(x)) \land PuedeUsar(x,f(x))))
\]

:::fullwidth
- Distribuir para hacer cláusulas:
- \(\neg Usuario(x) \lor Recurso(f(x))\)
- \(\neg Usuario(x) \lor PuedeUsar(x,f(x))\)

***
Ahora ya aparecen dos cláusulas. Esa es la razón práctica de todo el proceso: una fórmula compacta, pero poco operable, se convierte en piezas uniformes que luego pueden analizarse mediante instancias sobre términos del lenguaje. 

***

# Un ejemplo para la forma clausular

:::fullwidth
\[ F = \exists x P(x, c) \lor \forall x P(c, x) \to \forall x \exists y P(x, y) \]

Primer, renombrar variables para no entrar en confusiones. 

Luego, resolver implicaciones y negaciones, incluídas las que queden en cuantificadores (deben llegar al átomo).

Agrupar los cuantificadores y aplicar distribuitividad.

:::fullwidth
\[ F = \exists x P(x, c) \lor \forall x P(c, x) \to \forall x \exists y P(x, y) \]
\[ F = \exists x P(x, c) \lor \forall u P(c, u) \to \forall w \exists y P(w, y) \]
\[ F = \neg (\exists x P(x, c) \lor \forall u P(c, u)) \lor \forall w \exists y P(w, y) \]

:::fullwidth
\[ F = \neg \exists x P(x, c) \land \neg \forall u P(c, u) \lor \forall w \exists y P(w, y) \]
\[ F = \forall x \neg P(x, c) \land \exists u \neg P(c, u) \lor \forall w \exists y P(w, y) \]
\[ F = \forall x \exists u \forall w \exists y (\neg P(x, c) \land \neg P(c, u) \lor P(w, y)) \]

:::fullwidth
Prenexa
\[ F = \forall x \exists u \forall w \exists y (( \neg P(x, c) \lor P(w, y)) \land (\neg P(c, u) \lor P(w, y))) \]

---
Para construir la forma clausular se deben eliminar los cuantificadores existenciales, para ello se debe considerar:

:::fullwidth
- Si la fórmula es de la forma \[ A = \forall y_1 \forall y_2 \ldots \forall y_n \exists x M(x, y_1, y_2, \ldots , y_n )   \]
  - Se define un nuevo símbolo de función de aridad n
  - Se reemplaza toda ocurrencia de x por \( f(y_1, y_2, \ldots, y_n) \)

:::fullwidth
\( A = \forall y_1 \forall y_2 \ldots \forall y_n \exists x M(f(y_1, y_2, \ldots, y_n), y_1, y_2, \ldots , y_n )   \)


---
:::fullwidth
- Si la fórmla es de la forma \[ A = \exists x M(x) \]
  - Se reemplaza toda ocurrencia de x por una nueva constante a

\( A = M(a) \)

:::fullwidth

En el ejemplo que estabamos trabajando:

\[ F = \forall x \exists u \forall w \exists y (( \neg P(x, c) \lor P(w, y)) \land (\neg P(c, u) \lor P(w, y))) \]

- u se reemplaza por g(x)

- y se reemplaza por f(x, w)

:::fullwidth
Clausular
\[ F = \forall x \forall w (( \neg P(x, c) \lor P(w, f(x, w))) \land (\neg P(c, g(x)) \lor P(w, f(x, w)))) \]

# Motivación para Herbrand

El método de Herbrand nace de la necesidad de estudiar satisfacibilidad sin tener que recorrer dominios arbitrarios y potencialmente complicados. La idea es trasladar el problema a un terreno sintáctico, construido con los propios símbolos del lenguaje: términos, átomos e instancias de cláusulas. 

***
Dicho de otra manera, en vez de preguntarse por cualquier dominio imaginable, interesa mirar primero el “mundo generado por el propio lenguaje”. Si el lenguaje tiene constantes y funciones, entonces con ellas se construyen términos; con esos términos se construyen átomos; y con esas piezas se prueban combinaciones que reflejan la satisfacibilidad de los conjuntos de cláusulas. 

***
La idea es similar a probar un sistema a partir de los objetos que su propia especificación puede construir. Si un modelo de red solo usa ciertos nodos, funciones de enrutamiento y relaciones de conexión, resulta natural comenzar por estudiar todas las configuraciones simbólicas que esos mismos componentes permiten describir. 

***
Por eso la preparación hacia cláusulas no es un adorno técnico. Es el paso que hace posible que la atención se centre en instancias concretas de un lenguaje formal, y no en estructuras completamente arbitrarias y difíciles de manipular. 

***

# Universo de Herbrand

El universo de Herbrand es el conjunto de todos los términos cerrados que pueden construirse con las constantes y símbolos de función del lenguaje. “Cerrados” significa que no contienen variables; son expresiones completas que pueden nombrar individuos dentro del mundo sintáctico generado por el propio lenguaje. 

***
Si el lenguaje tiene la constante \(a\) y la función unaria \(f\), el universo de Herbrand comienza así:

- Profundidad 0: \(a\)
- Profundidad 1: \(f(a)\)
- Profundidad 2: \(f(f(a))\)
- Profundidad 3: \(f(f(f(a)))\)

***
Si además hubiera otra constante \(b\), entonces desde profundidad 0 aparecerían \(a, b\), y luego \(f(a), f(b)\), y así sucesivamente. Si existe una función binaria \(g\), el crecimiento es más rápido porque surgen términos como \(g(a,a)\), \(g(a,b)\), \(g(f(a),b)\), entre muchos otros; esto muestra por qué en la práctica se trabaja por niveles de profundidad. 

:::fullwidth
Ejemplo:
Lenguaje con constantes \(a, b\), función unaria \(s\), función binaria \(g\).

- Profundidad 0: \(a, b\)
- Profundidad 1: \(s(a), s(b), g(a,a), g(a,b), g(b,a), g(b,b)\)
- Profundidad 2: aparecen términos como \(s(s(a))\), \(g(s(a),b)\), \(g(g(a,b),s(b))\)

***
La construcción por profundidad funciona como generar cadenas o árboles en estructura de datos: primero se tienen nodos base, luego se aplican funciones para producir objetos más complejos. El universo de Herbrand es, en ese sentido, el inventario de términos posibles del lenguaje. 

***

# Base de Herbrand

La base de Herbrand es el conjunto de todos los átomos cerrados que se pueden formar usando los predicados del lenguaje y los términos del universo de Herbrand. Si el universo aporta los nombres posibles de individuos, la base aporta las afirmaciones atómicas posibles sobre ellos. 

***
Ejemplo:
Si el universo contiene \(a, f(a)\) y hay un predicado unario \(P\) y uno binario \(R\), entonces la base de Herbrand incluye:

- \(P(a)\)
- \(P(f(a))\)
- \(R(a,a)\)
- \(R(a,f(a))\)
- \(R(f(a),a)\)
- \(R(f(a),f(a))\)

***
En un escenario de redes, si el predicado es \(Conectado(x,y)\) y los términos posibles son \(r1, r2\), la base contiene \(Conectado(r1,r1)\), \(Conectado(r1,r2)\), \(Conectado(r2,r1)\) y \(Conectado(r2,r2)\). En un ejemplo de personas, con el predicado \(Amigo(x,y)\) y términos \(ana, luis\), la base contiene las cuatro combinaciones atómicas correspondientes. 

***
La base de Herbrand es importante porque una interpretación de Herbrand puede decidir, para cada átomo de esa base, si se considera verdadero o falso. Así, el problema semántico se vuelve una cuestión sobre asignaciones de verdad a un conjunto de átomos construidos sintácticamente. 

***

# Interpretaciones de Herbrand y satisfacibilidad

Una interpretación de Herbrand toma como dominio el universo de Herbrand y asigna verdad o falsedad a los átomos de la base de Herbrand. Con eso ya puede evaluarse si determinadas cláusulas quedan satisfechas o no bajo esa interpretación. 

***
Ejemplo:
Lenguaje con constante \(a\), predicado unario \(P\).  
Universo de Herbrand: \(\{a\}\).  
Base de Herbrand: \(\{P(a)\}\).

Las interpretaciones de Herbrand posibles son dos:

- \(P(a)\) verdadera  
- \(P(a)\) falsa  

***
Si el conjunto de cláusulas es \(\{P(a)\}\), solo la primera interpretación lo satisface. Si el conjunto es \(\{\neg P(a)\}\), solo la segunda lo satisface. Si el conjunto es \(\{P(a), \neg P(a)\}\), ninguna interpretación lo satisface, porque las dos cláusulas exigen valores incompatibles para el mismo átomo. 

***
Ejemplo con dos átomos:

Base: \(\{P(a), Q(a)\}\)

Conjunto de cláusulas:
- \(P(a) \lor Q(a)\)
- \(\neg P(a)\)

Para satisfacer ambas, la segunda cláusula obliga a que \(P(a)\) sea falsa. Entonces la primera obliga a que \(Q(a)\) sea verdadera. 

:::fullwidth
Una interpretación que funciona es:
- \(P(a)\) falsa
- \(Q(a)\) verdadera


***

# Ejemplo integrado completo

Se considera el lenguaje con:

- Constante: \(a\)
- Función unaria: \(f\)
- Predicados: \(P(x)\), \(R(x,y)\)

***
Universo de Herbrand hasta profundidad 2:

- Profundidad 0: \(a\)
- Profundidad 1: \(f(a)\)
- Profundidad 2: \(f(f(a))\)

Por tanto, hasta esa profundidad:
\[
U_H^{(2)} = \{a, f(a), f(f(a))\}
\]

***
Base de Herbrand correspondiente hasta esa misma profundidad:

- Átomos con \(P\):
  - \(P(a)\)
  - \(P(f(a))\)
  - \(P(f(f(a)))\)

- Átomos con \(R\):
  - \(R(a,a)\)
  - \(R(a,f(a))\)
  - \(R(a,f(f(a)))\)
  - \(R(f(a),a)\)
  - \(R(f(a),f(a))\)
  - \(R(f(a),f(f(a)))\)
  - \(R(f(f(a)),a)\)
  - \(R(f(f(a)),f(a))\)
  - \(R(f(f(a)),f(f(a)))\)

:::fullwidth
Ahora se analizan las cláusulas:

1. \(\neg P(x) \lor R(x,f(x))\)  
2. \(P(a)\)

Instancias relevantes hasta profundidad 1:
- De la cláusula 1 con \(x:=a\): \(\neg P(a) \lor R(a,f(a))\)
- De la cláusula 1 con \(x:=f(a)\): \(\neg P(f(a)) \lor R(f(a),f(f(a)))\)


Si una interpretación hace verdadera \(P(a)\), entonces la primera instancia obliga a que \(R(a,f(a))\) sea verdadera. 

:::fullwidth
En cambio (para \(x:=f(a)\)), nada obliga todavía a que \(P(f(a))\) sea verdadera, así que la segunda instancia puede quedar satisfecha ya sea porque \(P(f(a))\) sea verdadera (o falsa) o porque \(R(f(a),f(f(a)))\) sea verdadera (o falsa). La condición solo sería que alguna sea verdadera. 

***
Una interpretación de Herbrand que satisface esas instancias es:

- \(P(a)\): verdadera
- \(P(f(a))\): falsa
- \(R(a,f(a))\): verdadera
- Los demás átomos: falsos

Con esa asignación, la cláusula 2 se satisface directamente y la cláusula 1 también queda satisfecha con las instancias mostradas. 

***

# Errores que deben evitarse

Un error frecuente consiste en confundir una variable con un término cerrado. El universo de Herbrand no se construye con variables como \(x\) o \(y\), sino con términos sin variables, porque su función es servir como catálogo de individuos sintácticos completos. 

***
Otro error consiste en creer que la base de Herbrand contiene fórmulas complejas. La base contiene solo átomos cerrados; las cláusulas y conjuntos de cláusulas se construyen después usando esos átomos o sus negaciones como literales. 

***
También es común skolemizar de manera apresurada. Si un existencial depende de universales previos, no debe reemplazarse por una constante cualquiera, sino por una función cuyos argumentos reflejen esa dependencia; de lo contrario, se pierde información lógica importante sobre cómo varía el testigo con los valores universales. 

***
Un último error aparece al analizar satisfacibilidad: no basta con ver una cláusula aislada, sino el conjunto completo. Una interpretación puede satisfacer una cláusula y violar otra; por eso se evalúa el comportamiento total del conjunto de cláusulas bajo la misma interpretación. 

***

# Para llevar...

La prueba formal se extiende a cuantificadores mediante reglas como instanciación universal y generalización; las fórmulas se transforman para quedar cerca de cláusulas; y esa forma estándar permite preparar el estudio de universos, bases e interpretaciones de Herbrand. 

***
En lugar de tratar las fórmulas de primer orden como expresiones demasiado amplias para manipularse, se aprende a desarmarlas, normalizarlas y reconstruirlas en un formato más operativo. Esa es la puerta de entrada para trabajar con satisfacibilidad de conjuntos de cláusulas usando objetos que el propio lenguaje puede generar. 

***
Con estas herramientas se pueden construir universos de Herbrand por profundidad, formar bases de Herbrand, producir instancias relevantes y decidir la satisfacibilidad de conjuntos pequeños de cláusulas bajo interpretaciones sencillas. 
