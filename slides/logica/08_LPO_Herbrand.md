## Sesión 2 (1.5 horas): Transformación hacia cláusulas y preparación de Herbrand

### Alcance de la sesión 2

En la segunda sesión el foco se mueve de las reglas con cuantificadores a la transformación sistemática de fórmulas hacia formas cercanas a cláusulas. Con esas formas, el análisis de satisfacibilidad se puede plantear usando universos, bases e interpretaciones de Herbrand, que viven completamente en el plano sintáctico del lenguaje. 

***
El objetivo práctico consiste en entender por qué se eliminan implicaciones, cómo se empujan negaciones, para qué sirve la forma prenexa y qué papel juega la skolemización. A partir de ahí, se introducen las nociones de universo y base de Herbrand, así como interpretaciones sencillas para decidir satisfacibilidad de conjuntos pequeños de cláusulas. 

***

### Hacia formas cercanas a cláusulas

Una cláusula es, de manera intuitiva, una disyunción de literales, donde un literal es un átomo o la negación de un átomo. Trabajar con conjuntos de cláusulas conviene porque la representación se vuelve uniforme y facilita el análisis de satisfacibilidad mediante procedimientos sistemáticos. 

***
La motivación es parecida a la normalización de datos o a convertir distintos formatos de entrada a una estructura estándar antes de procesarlos. Si cada fórmula tuviera una forma arbitraria, el razonamiento mecánico sería desordenado; al llevarlas a una forma cercana a cláusulas, se reduce la variedad superficial y se hace visible la estructura lógica relevante. 

***
En esta sesión no se busca desarrollar el método completo, sino preparar su entrada. El punto central es entender por qué se eliminan implicaciones, por qué las negaciones se empujan hacia adentro y por qué las existencias se reemplazan mediante términos especiales: todo eso acerca la fórmula a un conjunto de cláusulas sobre el cual puede trabajarse de manera más sistemática. 

***

### Eliminar implicaciones y bicondicionales

La eliminación de implicaciones reemplaza conectivos como \(\rightarrow\) y \(\leftrightarrow\) por combinaciones de negación, conjunción y disyunción. Este paso es importante porque las cláusulas se construyen más fácilmente cuando la fórmula ya no depende de conectivos derivados. 

***
Las equivalencias básicas que interesan son:

- \(A \rightarrow B \equiv \neg A \vee B\)  
- \(A \leftrightarrow B \equiv (A \rightarrow B) \wedge (B \rightarrow A)\)  

***
Ejemplo:
\[
\forall x \, (Servidor(x) \rightarrow Disponible(x))
\]
se reescribe como
\[
\forall x \, (\neg Servidor(x) \vee Disponible(x))
\]
Esta forma ya se parece mucho más a una cláusula, porque dentro del alcance del cuantificador aparece una disyunción de literales. 

***
Ejemplo fuera del ámbito tecnológico:
\[
\forall x \, (Estudiante(x) \rightarrow UsaBiblioteca(x))
\]
pasa a
\[
\forall x \, (\neg Estudiante(x) \vee UsaBiblioteca(x))
\]
La información semántica es la misma; lo que cambia es la forma de presentación para facilitar pasos posteriores. 

***

### Mover negaciones hacia adentro

Mover negaciones hacia adentro significa usar leyes como De Morgan y las reglas para cuantificadores negados, con el fin de dejar la negación lo más cerca posible de los átomos. La meta es evitar negaciones aplicadas a fórmulas grandes, porque una cláusula trabaja con literales simples. 

***
Las transformaciones más importantes son:

- \(\neg (A \wedge B) \equiv \neg A \vee \neg B\)  
- \(\neg (A \vee B) \equiv \neg A \wedge \neg B\)  
- \(\neg \forall x \, A \equiv \exists x \, \neg A\)  
- \(\neg \exists x \, A \equiv \forall x \, \neg A\)  

***
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
\exists x \, \neg (\neg Usuario(x) \vee Autorizado(x))
\]
por De Morgan se obtiene
\[
\exists x \, (Usuario(x) \wedge \neg Autorizado(x))
\]
La negación ya quedó pegada al átomo \(Autorizado(x)\), que es el tipo de forma que interesa conservar. 

***
Esa limpieza estructural se parece a desarmar una condición compleja en un programa para dejar solo pruebas simples al nivel más bajo. La lógica hace algo semejante: despeja la expresión hasta dejarla compuesta por piezas manejables. 

***

### Forma prenexa

La forma prenexa es una presentación de la fórmula donde todos los cuantificadores quedan al frente y, después de ellos, aparece una parte libre de cuantificadores llamada matriz. Esta forma resulta útil porque separa el “patrón de cuantificación” de la estructura proposicional interna. 

***
Ejemplo:
\[
(\forall x \, P(x)) \vee Q
\]
bajo condiciones de variables adecuadas puede reacomodarse como una fórmula con cuantificador al frente. La intuición es que conviene ordenar primero quiénes son los objetos sobre los que se habla y después qué condición se afirma sobre ellos, del mismo modo que en una consulta formal primero se delimita el rango y luego se evalúa el predicado. 

***
Para la preparación de Herbrand, la forma prenexa ayuda porque pone los cuantificadores en una zona visible y permite identificar con claridad cuáles son universales y cuáles existenciales antes del paso de skolemización. 

***

### Esbozo de skolemización

La skolemización elimina cuantificadores existenciales reemplazando las variables existenciales por términos especiales llamados términos de Skolem. La idea intuitiva es introducir un “testigo simbólico” que represente al objeto cuya existencia estaba garantizada por la fórmula. 

***
Si la existencia no depende de variables universales anteriores, el testigo puede ser una constante nueva. Por ejemplo, de una forma como \(\exists x \, ServidorRespaldo(x)\) se pasa intuitivamente a \(ServidorRespaldo(c)\), donde \(c\) es una nueva constante de Skolem que nombra a algún servidor de respaldo garantizado por la existencia. 

***
Si la existencia sí depende de variables universales previas, el testigo ya no es una constante sino una función. Por ejemplo, en
\[
\forall x \, \exists y \, Atiende(y,x)
\]
el objeto \(y\) puede depender de \(x\), así que se reemplaza por \(f(x)\), obteniendo una forma como
\[
\forall x \, Atiende(f(x),x)
\]
donde \(f\) representa “el atendiente asociado a \(x\)”. 

***
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
Lo importante en esta sesión no es dominar todos los detalles técnicos, sino captar la motivación: la skolemización convierte existencias en términos concretos del lenguaje, y eso permite construir instancias y cláusulas sin cargar con el cuantificador existencial original. 

***

### Paso final hacia cláusulas

Después de eliminar implicaciones, mover negaciones, llevar la fórmula a forma prenexa y skolemizar, la expresión queda muy cerca de una forma normal conjuntiva de primer orden. En esa etapa, los cuantificadores universales suelen omitirse por convención y la matriz se interpreta como un conjunto de cláusulas. 

***
Ejemplo guiado:

Fórmula inicial:
\[
\forall x \, (Usuario(x) \rightarrow \exists y \, Recurso(y) \wedge PuedeUsar(x,y))
\]

Esbozo de transformación:
1. Eliminar implicación:
\[
\forall x \, (\neg Usuario(x) \vee \exists y \, (Recurso(y) \wedge PuedeUsar(x,y)))
\]

2. Llevar a forma apta para skolemizar:
\[
\forall x \, \exists y \, (\neg Usuario(x) \vee (Recurso(y) \wedge PuedeUsar(x,y)))
\]

3. Skolemizar \(y\) como \(f(x)\):
\[
\forall x \, (\neg Usuario(x) \vee (Recurso(f(x)) \wedge PuedeUsar(x,f(x))))
\]

4. Distribuir para acercarse a cláusulas:
- \(\neg Usuario(x) \vee Recurso(f(x))\)
- \(\neg Usuario(x) \vee PuedeUsar(x,f(x))\)

***
Ahora ya aparecen dos cláusulas. Esa es la razón práctica de todo el proceso: una fórmula compacta, pero poco operable, se convierte en piezas uniformes que luego pueden analizarse mediante instancias sobre términos del lenguaje. 

***

### Motivación para Herbrand

El método de Herbrand nace de la necesidad de estudiar satisfacibilidad sin tener que recorrer dominios arbitrarios y potencialmente complicados. La idea es trasladar el problema a un terreno sintáctico, construido con los propios símbolos del lenguaje: términos, átomos e instancias de cláusulas. 

***
Dicho de otra manera, en vez de preguntarse por cualquier dominio imaginable, interesa mirar primero el “mundo generado por el propio lenguaje”. Si el lenguaje tiene constantes y funciones, entonces con ellas se construyen términos; con esos términos se construyen átomos; y con esas piezas se prueban combinaciones que reflejan la satisfacibilidad de los conjuntos de cláusulas. 

***
La intuición es semejante a probar un sistema a partir de los objetos que su propia especificación puede construir. Si un modelo de red solo usa ciertos nodos, funciones de enrutamiento y relaciones de conexión, resulta natural comenzar por estudiar todas las configuraciones simbólicas que esos mismos componentes permiten describir. 

***
Por eso la preparación hacia cláusulas no es un adorno técnico. Es el paso que hace posible que la atención se centre en instancias concretas de un lenguaje formal, y no en estructuras completamente arbitrarias y difíciles de manipular. 

***

### Universo de Herbrand

El universo de Herbrand es el conjunto de todos los términos cerrados que pueden construirse con las constantes y símbolos de función del lenguaje. “Cerrados” significa que no contienen variables; son expresiones completas que pueden nombrar individuos dentro del mundo sintáctico generado por el propio lenguaje. 

***
Si el lenguaje tiene la constante \(a\) y la función unaria \(f\), el universo de Herbrand comienza así:

- Profundidad 0: \(a\)
- Profundidad 1: \(f(a)\)
- Profundidad 2: \(f(f(a))\)
- Profundidad 3: \(f(f(f(a)))\)

***
Si además hubiera otra constante \(b\), entonces desde profundidad 0 aparecerían \(a, b\), y luego \(f(a), f(b)\), y así sucesivamente. Si existe una función binaria \(g\), el crecimiento es más rápido porque surgen términos como \(g(a,a)\), \(g(a,b)\), \(g(f(a),b)\), entre muchos otros; esto muestra por qué en la práctica se trabaja por niveles de profundidad. 

***
Ejemplo:
Lenguaje con constantes \(a, b\), función unaria \(s\), función binaria \(g\).

- Profundidad 0: \(a, b\)
- Profundidad 1: \(s(a), s(b), g(a,a), g(a,b), g(b,a), g(b,b)\)
- Profundidad 2: aparecen términos como \(s(s(a))\), \(g(s(a),b)\), \(g(g(a,b),s(b))\)

***
La construcción por profundidad funciona como generar cadenas o árboles en estructura de datos: primero se tienen nodos base, luego se aplican funciones para producir objetos más complejos. El universo de Herbrand es, en ese sentido, el inventario de términos posibles del lenguaje. 

***

### Base de Herbrand

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

### Interpretaciones de Herbrand y satisfacibilidad sencilla

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
- \(P(a) \vee Q(a)\)
- \(\neg P(a)\)

Para satisfacer ambas, la segunda cláusula obliga a que \(P(a)\) sea falsa. Entonces la primera obliga a que \(Q(a)\) sea verdadera. Una interpretación que funciona es:
- \(P(a)\) falsa
- \(Q(a)\) verdadera

***
Ese tipo de análisis es justo el que el alumnado necesita dominar para producir evidencias como hojas de ejercicios con universos, bases y respuestas de satisfacibilidad. La clave está en pasar con orden del lenguaje dado a los términos, de los términos a los átomos y de los átomos a la evaluación de cláusulas. 

***

### Ejemplo integrado completo

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

***
Ahora se analizan las cláusulas:

1. \(\neg P(x) \vee R(x,f(x))\)  
2. \(P(a)\)

Instancias relevantes hasta profundidad 1:
- De la cláusula 1 con \(x:=a\): \(\neg P(a) \vee R(a,f(a))\)
- De la cláusula 1 con \(x:=f(a)\): \(\neg P(f(a)) \vee R(f(a),f(f(a)))\)

***
Si una interpretación hace verdadera \(P(a)\), entonces la primera instancia obliga a que \(R(a,f(a))\) sea verdadera. En cambio, nada obliga todavía a que \(P(f(a))\) sea verdadera, así que la segunda instancia puede quedar satisfecha ya sea porque \(P(f(a))\) sea falsa o porque \(R(f(a),f(f(a)))\) sea verdadera. 

***
Una interpretación de Herbrand que satisface esas instancias es:

- \(P(a)\): verdadera
- \(P(f(a))\): falsa
- \(R(a,f(a))\): verdadera
- Los demás átomos: falsos

Con esa asignación, la cláusula 2 se satisface directamente y la cláusula 1 también queda satisfecha en las instancias mostradas. 

***

### Ejercicios insertados en la exposición

Una práctica consiste en construir el universo de Herbrand hasta profundidad 2 para el lenguaje con constante \(c\), función unaria \(s\) y predicado binario \(Conecta(x,y)\). El resultado esperado comienza con \(c\), luego \(s(c)\) y después \(s(s(c))\); a partir de esos términos, la base se forma con todos los átomos \(Conecta(t_1,t_2)\) donde \(t_1\) y \(t_2\) pertenecen al universo truncado. 

***
Otra práctica consiste en tomar el lenguaje con constantes \(ana\) y \(luis\), sin funciones, y predicados \(Alumno(x)\) y \(TrabajaCon(x,y)\). El universo de Herbrand queda formado solo por \(\{ana, luis\}\), mientras que la base incluye \(Alumno(ana)\), \(Alumno(luis)\) y las cuatro combinaciones posibles para \(TrabajaCon\); este caso es útil porque permite ver la construcción completa sin crecimiento explosivo. 

***
Una tercera práctica consiste en analizar satisfacibilidad para el conjunto:
- \(P(a) \vee Q(a)\)
- \(\neg P(a)\)
- \(\neg Q(a)\)

La primera cláusula exige que al menos uno de los dos átomos sea verdadero, pero las otras dos obligan a que ambos sean falsos; por tanto, el conjunto es insatisfacible en cualquier interpretación de Herbrand sobre esa base. 

***
Otra práctica:
- \(\neg Disponible(s1) \vee Responde(s1)\)
- \(Disponible(s1)\)

Aquí cualquier interpretación que satisfaga ambas debe hacer verdadero \(Responde(s1)\). El patrón es exactamente el mismo que en una cláusula proposicional, pero ya expresado como átomo de primer orden cerrado. 

***

### Errores que deben evitarse

Un error frecuente consiste en confundir una variable con un término cerrado. El universo de Herbrand no se construye con variables como \(x\) o \(y\), sino con términos sin variables, porque su función es servir como catálogo de individuos sintácticos completos. 

***
Otro error consiste en creer que la base de Herbrand contiene fórmulas complejas. La base contiene solo átomos cerrados; las cláusulas y conjuntos de cláusulas se construyen después usando esos átomos o sus negaciones como literales. 

***
También es común skolemizar de manera apresurada. Si un existencial depende de universales previos, no debe reemplazarse por una constante cualquiera, sino por una función cuyos argumentos reflejen esa dependencia; de lo contrario, se pierde información lógica importante sobre cómo varía el testigo con los valores universales. 

***
Un último error aparece al analizar satisfacibilidad: no basta con ver una cláusula aislada, sino el conjunto completo. Una interpretación puede satisfacer una cláusula y violar otra; por eso se evalúa el comportamiento total del conjunto de cláusulas bajo la misma interpretación. 

***

### Para llevar (cierre de ambas sesiones)

La prueba formal se extiende a cuantificadores mediante reglas como instanciación universal y generalización; las fórmulas se transforman para quedar cerca de cláusulas; y esa forma estándar permite preparar el estudio de universos, bases e interpretaciones de Herbrand. 

***
En lugar de tratar las fórmulas de primer orden como expresiones demasiado amplias para manipularse, se aprende a desarmarlas, normalizarlas y reconstruirlas en un formato más operativo. Esa es la puerta de entrada para trabajar con satisfacibilidad de conjuntos de cláusulas usando objetos que el propio lenguaje puede generar. 

***
Con estas herramientas se pueden construir universos de Herbrand por profundidad, formar bases de Herbrand, producir instancias relevantes y decidir la satisfacibilidad de conjuntos pequeños de cláusulas bajo interpretaciones sencillas. 

***

## Hoja breve de repaso (para el final de la segunda sesión)

- La instanciación universal pasa de \(\forall x \, A(x)\) a \(A(t)\) para un término \(t\).  
- La generalización universal pasa de un caso arbitrario a \(\forall x \, A(x)\), con restricciones sobre la arbitrariedad del elemento. 

***
- Para acercarse a cláusulas se eliminan implicaciones, se empujan negaciones hacia los átomos, se ordenan cuantificadores y se esboza la skolemización de existenciales. 

***
- El universo de Herbrand contiene términos cerrados; la base de Herbrand contiene átomos cerrados construidos con esos términos y con los predicados del lenguaje. 

***
- Una interpretación de Herbrand asigna verdad a los átomos de la base, y con eso puede evaluarse la satisfacibilidad de conjuntos de cláusulas. 

***
- La razón para trabajar con cláusulas es que permiten un tratamiento más uniforme y más mecánico del problema de satisfacibilidad en lógica de primer orden. 