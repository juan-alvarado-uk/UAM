# De Herbrand a programas lógicos

En temas previos se ha mostrado cómo una fórmula de lógica de primer orden puede transformarse en un conjunto de cláusulas, pasando por eliminación de implicaciones, movimiento de negaciones, usando la forma prenexa y skolemización. 

***

Ahora, esas cláusulas se leen como piezas cercanas a un programa lógico: los literales positivos se interpretan como conclusiones y los literales negativos como condiciones que deben cumplirse para que la conclusión sea verdadera. Esta lectura aproxima el método de Herbrand a un lenguaje tipo Prolog, donde las cláusulas se convierten en hechos y reglas. 

***

Es importante notar que:

- un conjunto de cláusulas universales puede entenderse como base de conocimiento;
- el universo y la base de Herbrand describen los “casos posibles” dentro del lenguaje;
- los mecanismos de prueba se pueden leer como respuesta a consultas sobre esa base. 

***

# Cláusulas de tipo Horn y su lectura

Una **cláusula de Horn** es una disyunción de literales con a lo más un literal positivo. En notación cercana a la forma clausular, una cláusula de Horn típica se ve como:

\[
A \lor \neg B_1 \lor \cdots \lor \neg B_n
\]

---
y puede reescribirse como una implicación:

\[
(B_1 \land \cdots \land B_n) \to A
\]

***

Esta forma se alinea con la manera en que se escriben reglas en un lenguaje de programación lógica:

```prolog
A :- B1, ..., Bn.
```

donde el lado izquierdo representa la cabeza (conclusión) y el lado derecho representa el cuerpo (condiciones). 

***

Dos casos particulares de cláusulas de Horn se reconocen fácilmente:

- Si no hay literales negativos (n = 0), la cláusula es simplemente un **hecho**.
- Si no hay literal positivo, se obtiene una cláusula puramente negativa que puede leerse como una restricción (no usaremos restricciones, nos concentraremos en hechos y reglas). 


# Del conjunto de cláusulas a base de conocimiento

Retomamos el concepto de universo de Herbrand: el conjunto de todos los términos cerrados construibles con las constantes y funciones del lenguaje. A partir de ahí, la base de Herbrand reúne todos los átomos cerrados que se pueden formar con los predicados del lenguaje y esos términos. 

***

Cuando un conjunto de cláusulas está libre de cuantificadores existenciales (gracias a la skolemización) y los cuantificadores universales se dejan implícitos, estas cláusulas se pueden entender como una descripción declarativa de un dominio. Esa descripción, a su vez, puede interpretarse como un “programa lógico” que responde preguntas sobre el dominio. 

***

:::fullwidth
Así, el puente entre lógica y programación lógica se construye así:

1. Fórmulas de LPO.
2. Transformación hacia forma clausular (prenexa).
3. Eliminación de existenciales (skolemización).
4. Conjunto de cláusulas universales.
5. Lectura de esas cláusulas como hechos y reglas de un programa lógico. 

***

# Introducción a un lenguaje de programación lógica

## Programación lógica

Un lenguaje de programación lógica se basa en tres componentes fundamentales:

- hechos,
- reglas,
- consultas.

Estos componentes se conectan con las cláusulas, instancias y satisfacibilidad desarrolladas con el método de Herbrand. 

***

En este paradigma, el énfasis está en describir qué relaciones se cumplen en un dominio, no en especificar paso a paso cómo obtener el resultado. El sistema de programación lógica intenta encontrar demostraciones de las consultas a partir de los hechos y reglas disponibles, de manera similar a como una prueba formal explora instancias de fórmulas universales. 

***

## Hechos

Un hecho expresa que un átomo particular es verdadero. En una lectura clausular, un hecho corresponde a una cláusula con un único literal positivo. En programación lógica se escribe simplemente como un predicado aplicado a términos concretos, terminado en punto. 

***

### Ejemplos:

```prolog
usuario(ana).
usuario(luis).
servidor(web1).
servidor(db1).
activo(web1).
```

Cada una de estas líneas afirma algo sobre individuos particulares, igual que una cláusula como \(Usuario(ana)\) o \(Servidor(db1)\) dentro de una base de Herbrand. 

***

```prolog
padre(juan, ana).
padre(juan, luis).
madre(elena, ana).
madre(elena, luis).
```

Aquí se describen relaciones familiares básicas, y cada hecho aporta un átomo cerrado a la base de conocimiento. 

***

## Reglas

Una regla expresa que un enunciado es verdadero si se satisfacen otras condiciones. En forma clausular, una regla con un literal positivo y varios negativos equivale a una cláusula de Horn. En programación lógica, se escribe con el símbolo `:-`, que separa la cabeza del cuerpo. 

***

### Ejemplos

```prolog
autenticado(X) :- usuario(X), credencial_valida(X).
acceso(X) :- autenticado(X), permiso(X).
```

:::fullwidth
Que corresponden, respectivamente, a cláusulas del tipo:

\[
\neg Usuario(x) \lor \neg CredencialValida(x) \lor Autenticado(x)
\]

\[
\neg Autenticado(x) \lor \neg Permiso(x) \lor Acceso(x)
\]

donde cada literal positivo actúa como cabeza de una regla, y el conjunto de literales negativos conforma el cuerpo. 

---

```prolog
puede_entrar(X) :- tiene_boleto(X), llega_a_tiempo(X).
```
:::fullwidth
Lectura: 

“X puede entrar si tiene boleto y llega a tiempo”. Su forma clausular se ajusta a la misma plantilla de cláusula de Horn. 

***

## Consultas

Una consulta es una pregunta al sistema acerca de si cierto átomo o combinación de átomos puede derivarse de la base de conocimiento. En términos de Herbrand, **cada consulta corresponde a preguntar si existe una interpretación de Herbrand que haga verdadera la cláusula asociada, dada la información del programa**. 

***

En sintaxis tipo Prolog, una consulta se escribe así:

```prolog
?- usuario(ana).
?- disponible(web1).
?- acceso(X).
```

- Una consulta cerrada, como `?- usuario(ana).`, pregunta si el átomo `usuario(ana)` puede derivarse.
- Una consulta con variables, como `?- acceso(X).`, pregunta por qué valores de X el átomo `acceso(X)` podría ser demostrado. 

***

### Ejemplos

```prolog
?- servidor(db1).
?- disponible(db1).
?- disponible(X).
```

Si se tienen los hechos y reglas adecuados, el sistema responde cuáles átomos de la base de Herbrand quedan justificados. 

***

```prolog
?- padre(juan, ana).
?- progenitor(X, ana).
?- hermano(ana, Y).
```

Estas consultas exploran derivaciones posibles a partir de la base sobre relaciones familiares. 

***

# Universo y base de Herbrand en lectura declarativa

## Universo y base de Herbrand


En el contexto de programación lógica, estos conceptos se pueden ver así:

- el universo de Herbrand enumera los “datos posibles” nombrables dentro del lenguaje;
- la base de Herbrand lista todas las afirmaciones posibles sobre esos datos;
- el programa lógico escoge algunas de esas afirmaciones como verdaderas (hechos) y establece reglas que relacionan unas con otras. 

***

Ejemplo con funciones:

Lenguaje con constante \(a\) y función unaria \(f\). Universo de Herbrand:

- profundidad 0: \(a\)
- profundidad 1: \(f(a)\)
- profundidad 2: \(f(f(a))\)
- …

Con un predicado unario \(P\) y uno binario \(R\), la base de Herbrand incluye átomos como \(P(a)\), \(P(f(a))\), \(R(a,f(a))\), \(R(f(a),f(f(a)))\), etcétera. 

***

Si se tiene una cláusula de Horn como:

\[
\neg P(x) \lor R(x,f(x))
\]

su lectura como regla es:

```prolog
r(X, f(X)) :- p(X).
```

y las instancias de Herbrand, para \[x := a\] o \[x := f(a)\] muestran cómo se van particularizando estas reglas sobre términos concretos. 

***

# Interpretaciones de Herbrand y programas

Una interpretación de Herbrand asigna valores de verdad a los átomos de la base de Herbrand tomando como dominio el universo de Herbrand. En ejercicios previos se vio cómo, con unos cuantos átomos, se puede enumerar las posibles interpretaciones y decidir si un conjunto de cláusulas es satisfacible. 

***

En programación lógica, el conjunto de hechos fija parte de esa interpretación: cada hecho declara un átomo que se considera verdadero. Las reglas imponen condiciones adicionales que deben cumplirse para que otros átomos sean verdaderos, de modo que la interpretación resultante respete todas las cláusulas de Horn del programa. 


***

# Ejemplo: autenticación y acceso

Se construye una base de conocimiento sobre autenticación y acceso usando hechos y reglas que se ajustan a la forma clausular trabajada antes. 

***

### Base

```prolog
usuario(ana).
usuario(luis).
credencial_valida(ana).
permiso(ana).
permiso(luis).

autenticado(X) :- usuario(X), credencial_valida(X).
acceso(X) :- autenticado(X), permiso(X).
```

### Universo

El universo de Herbrand (en este fragmento) incluye al menos `ana` y `luis`. La base de Herbrand contiene átomos como `usuario(ana)`, `credencial_valida(ana)`, `autenticado(ana)`, `acceso(ana)`, `usuario(luis)`, `permiso(luis)`, `autenticado(luis)`, `acceso(luis)`. 

### Consultas


:::fullwidth
- `?- autenticado(ana).`  
  Se verifica `usuario(ana)` y `credencial_valida(ana)`, por lo que la regla `autenticado/1` se satisface y la consulta responde afirmativamente.

- `?- autenticado(luis).`  
  Falta `credencial_valida(luis)` en los hechos, por lo que la regla no se puede activar.

:::fullwidth
- `?- acceso(ana).`  
  Como `autenticado(ana)` y `permiso(ana)` se sostienen, la regla `acceso/1` se cumple para `ana`.

- `?- acceso(luis).`  
  Aunque `permiso(luis)` es verdadero, `autenticado(luis)` no se ha demostrado. 

***

Esta situación ilustra la lectura declarativa: el programa describe quiénes son usuarios, qué credenciales son válidas y bajo qué condiciones se concede acceso. También muestra la lectura operacional: el sistema genera instancias de Herbrand de las reglas y verifica si las condiciones se cumplen para los individuos concretos. 

***

# Ejemplo: familias y hermanos

### Base

```prolog
padre(juan, ana).
padre(juan, luis).
madre(elena, ana).
madre(elena, luis).

progenitor(X, Y) :- padre(X, Y).
progenitor(X, Y) :- madre(X, Y).
hermano(X, Y) :- padre(P, X), padre(P, Y).
```

En esta definición, `hermano(X, Y)` se lee: “X y Y son hermanos si hay un padre P que es padre de X y de Y”. 

***

### Consultas 

:::fullwidth
- `?- progenitor(juan, ana).`  
  Afirmativa, porque `padre(juan, ana)` está en la base y la regla `progenitor(X, Y) :- padre(X, Y).` se cumple.

- `?- progenitor(elena, luis).`  
  Afirmativa, porque `madre(elena, luis)` está en la base y la regla `progenitor(X, Y) :- madre(X, Y).` se cumple.

:::fullwidth
- `?- hermano(ana, luis).`  
  Afirmativa, porque existe `P = juan` tal que `padre(juan, ana)` y `padre(juan, luis)` se sostienen.

:::fullwidth
- `?- hermano(ana, ana).`  
  También se justificaría con la regla dada, porque si `X = ana` y `Y = ana`, entonces `P = juan` satisface `padre(juan, ana)` dos veces; la regla no impide que X y Y sean iguales. 

***

Ese último resultado muestra un fenómeno importante: el programa, tal como está escrito, responde correctamente según su forma lógica, aunque la respuesta choque con la expectativa informal de que nadie es hermano de sí mismo. La base de conocimiento refleja exactamente lo que las reglas dicen, no lo que se “tenía en mente”. 

***

Para corregir esta situación, se puede enriquecer la regla de `hermano/2` con una condición adicional que exija que X y Y sean distintos:

```prolog
hermano(X, Y) :- padre(P, X), padre(P, Y), X \= Y.
```

Con esta versión, `hermano(ana, ana)` queda descartado porque la condición `X \= Y` falla cuando X e Y son la misma persona, mientras que `hermano(ana, luis)` continúa siendo derivable. 

***


# Ejercicios de lectura declarativa y predicción

Se proponen ahora fragmentos cortos de programas lógicos para practicar la lectura declarativa y la predicción de consultas, en línea con el trabajo previo sobre instancias de Herbrand y conjuntos de cláusulas. 

***

## Ejercicio 1: dispositivos y red

```prolog
dispositivo(pc1).
dispositivo(pc2).
en_red(pc1).

visible(X) :- dispositivo(X), en_red(X).
```

Consultas a analizar:

- `?- visible(pc1).`
- `?- visible(pc2).`
- `?- dispositivo(pc2).`

***

:::fullwidth
Lectura declarativa:

- `dispositivo/1` indica qué elementos son dispositivos.
- `en_red/1` indica cuáles están conectados a la red.
- `visible/1` indica dispositivos visibles desde la red, es decir, que son dispositivos y están en red. 

***

:::fullwidth
- `visible(pc1)` se justifica porque `dispositivo(pc1)` y `en_red(pc1)` aparecen como hechos; la instancia de la regla para `X = pc1` se cumple.
- `visible(pc2)` no se justifica porque, aunque `dispositivo(pc2)` es verdadero, falta `en_red(pc2)`.
- `dispositivo(pc2)` es afirmativa porque aparece directamente como hecho. 

***



## Ejercicio 2: prerequisitos adicionales

```prolog
curso(bases_datos).
curso(ia1).

prerrequisito(ia1, logica).

puede_inscribirse(X, Y) :- curso(Y), prerrequisito(Y, X).
```

:::fullwidth
Consultas:

- `?- puede_inscribirse(logica, ia1).`
- `?- puede_inscribirse(ia1, bases_datos).`
- `?- curso(ia1).`

***

:::fullwidth
- `puede_inscribirse(logica, ia1)` afirmativa, porque `curso(ia1)` y `prerrequisito(ia1, logica)` son verdaderos.
- `puede_inscribirse(ia1, bases_datos)` no se justifica con la base dada, dado que no se declaró `prerrequisito(bases_datos, ia1)`.
- `curso(ia1)` afirmativa, porque se declara directamente en el programa. 

***

# para llevar...

Esta sesión enlaza tres niveles:

- el nivel de fórmulas de LPO transformadas hacia cláusulas, 
- el nivel de universos y bases de Herbrand, 
- y el nivel de programas lógicos escritos con hechos, reglas y consultas.

Gracias a este enlace, un conjunto de cláusulas de Horn puede verse simultáneamente como objeto lógico y como programa en un lenguaje de programación lógica. 

***

El trabajo con bases y universos de Herbrand deja de ser solamente un ejercicio abstracto y se convierte en la base semántica para entender cómo funciona la programación lógica. 

Respone a: Qué significado tienen los hechos, cómo operan las reglas y por qué las consultas reflejan la búsqueda de interpretaciones que satisfacen las cláusulas del programa. 
