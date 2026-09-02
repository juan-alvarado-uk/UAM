## Práctica - Herbrand, prenexa, clausular, satisfactibilidad

En esta práctica vamos a trabajar con un sistema de cursos universitarios. El sistema representa información sobre alumnos, cursos, profesores, inscripciones, calificaciones y aprobaciones de cursos.

En el sistema hay distintos alumnos y distintos cursos. Cada curso tiene asignado un profesor que lo imparte. Los alumnos pueden estar inscritos o no en cada curso, pueden obtener una calificación en el curso y, dependiendo de esa calificación, pueden aprobar o no el curso.

Las condiciones de especificación que queremos capturar son las siguientes:

1. Todo alumno que está inscrito en un curso y obtiene una calificación aprobatoria en ese curso, aprueba ese curso. Es decir, si un alumno está inscrito en un curso y la calificación que obtiene en ese curso es una calificación aprobatoria, entonces el alumno aprueba ese curso.

2. Alicia es alumna y está inscrita en el curso de Lógica.

3. El curso de Lógica es un curso del sistema y tiene asignado al menos un profesor que lo imparte.

4. Ningún alumno aprueba un curso si no está inscrito en él. Para cualquier alumno y cualquier curso, si el alumno no está inscrito en el curso, entonces no aprueba ese curso.

Toda la práctica se desarrolla a partir de esta especificación.

***

## 1. Lenguaje y formalización

### Símbolos del lenguaje

Usaremos el siguiente lenguaje de primer orden:

- Constantes:
  - $a$: Alicia (alumna).
  - $c_1$: curso de Lógica.
  - $p_0$: un profesor concreto (introducido después por Skolemización).
  - $z_0$: una calificación aprobatoria.
  - $z_1$: una calificación reprobatoria.
- Funciones:
  - $prof(x)$: el profesor asignado al curso $x$.
- Predicados:
  - $Alumno(x)$: “$x$ es alumno”.
  - $Curso(x)$: “$x$ es curso”.
  - $Inscrito(x,y)$: “el alumno $x$ está inscrito en el curso $y$”.
  - $Aprueba(x,y)$: “el alumno $x$ aprueba el curso $y$”.
  - $DaClase(p,c)$: “$p$ da clase en el curso $c$”.
  - $Calificacion(x,y,z)$: “el alumno $x$ obtiene calificación $z$ en el curso $y$”.
  - $Aprobatoria(z)$: “$z$ es una calificación aprobatoria”.

### Formalización de la especificación

1. “Todo alumno inscrito en un curso que tiene calificación aprobatoria en ese curso, aprueba el curso”:

$$
\forall x \forall y \forall z\big((Alumno(x) \land Curso(y) \land Inscrito(x,y) \land Calificacion(x,y,z) \land Aprobatoria(z)) \rightarrow Aprueba(x,y)\big)
$$

2. “Alicia es alumna y está inscrita en el curso de Lógica”:

$$
Alumno(a)
$$
$$
Inscrito(a,c_1)
$$

3. “El curso de Lógica es curso y tiene profesor”:

$$
Curso(c_1) \land \exists p(DaClase(p,c_1))
$$

4. “Ningún alumno aprueba un curso si no está inscrito en él”:

$$
\forall x \forall y\big(Alumno(x) \land Curso(y) \land \neg Inscrito(x,y) \rightarrow \neg Aprueba(x,y)\big)
$$

En la práctica trabajaremos además con los hechos de calificación:

- $Calificacion(a,c_1,z_0)$ (Alicia obtuvo calificación $z_0$).
- $Aprobatoria(z_0)$.
- $Calificacion(a,c_1,z_1)$ puede considerarse falsa o verdadera según la interpretación que queramos usar para ejemplos; $z_1$ será reprobatoria (no aprobatoria).

***

## 2. Forma prenexa

Recordaremos las transformaciones principales:

- Eliminar implicaciones: $A \rightarrow B$ se sustituye por $\neg A \lor B$.
- Usar reglas de De Morgan para empujar negaciones hacia átomos.
- Mover todos los cuantificadores al frente (prefijo); la parte sin cuantificadores se llama matriz. 

### 2.1. Prenexa de la fórmula (1)

Fórmula:

$$
\forall x \forall y \forall z\big((Alumno(x) \land Curso(y) \land Inscrito(x,y) \land Calificacion(x,y,z) \land Aprobatoria(z)) \rightarrow Aprueba(x,y)\big)
$$

1. Eliminar implicación:

$$
\forall x \forall y \forall z\big(\neg(Alumno(x) \land Curso(y) \land Inscrito(x,y) \land Calificacion(x,y,z) \land Aprobatoria(z)) \lor Aprueba(x,y)\big)
$$

2. De Morgan:

$$
\neg Alumno(x) \lor \neg Curso(y) \lor \neg Inscrito(x,y) \lor \neg Calificacion(x,y,z) \lor \neg Aprobatoria(z)
$$

Por tanto:

$$
\forall x \forall y \forall z\big(\neg Alumno(x) \lor \neg Curso(y) \lor \neg Inscrito(x,y) \lor \neg Calificacion(x,y,z) \lor \neg Aprobatoria(z) \lor Aprueba(x,y)\big)
$$

Esta ya es forma prenexa: prefijo $\forall x \forall y \forall z$, matriz disyuntiva.

### 2.2. Prenexa de la fórmula (3)

Fórmula:

$$
Curso(c_1) \land \exists p(DaClase(p,c_1))
$$

Forma prenexa:

$$
\exists p\big(Curso(c_1) \land DaClase(p,c_1)\big)
$$

### 2.3. Prenexa de la fórmula (4)

Fórmula:

$$
\forall x \forall y\big(Alumno(x) \land Curso(y) \land \neg Inscrito(x,y) \rightarrow \neg Aprueba(x,y)\big)
$$

1. Eliminar implicación:

$$
\forall x \forall y\big(\neg(Alumno(x) \land Curso(y) \land \neg Inscrito(x,y)) \lor \neg Aprueba(x,y)\big)
$$

2. De Morgan:

$$
\neg Alumno(x) \lor \neg Curso(y) \lor Inscrito(x,y)
$$

Entonces:

$$
\forall x \forall y\big(\neg Alumno(x) \lor \neg Curso(y) \lor Inscrito(x,y) \lor \neg Aprueba(x,y)\big)
$$

Forma prenexa: prefijo $\forall x \forall y$, matriz disyuntiva.

***

## 3. Skolemización y forma clausular

### 3.1. Skolemización de la fórmula (3)

Partimos de:

$$
\exists p\big(Curso(c_1) \land DaClase(p,c_1)\big)
$$

Como no hay cuantificadores universales fuera, $\exists p$ se skolemiza con una nueva constante $p_0$:

$$
Curso(c_1) \land DaClase(p_0,c_1)
$$

De aquí obtenemos dos cláusulas unitarias:

- $\{Curso(c_1)\}$
- $\{DaClase(p_0,c_1)\}$

### 3.2. Conjunto de cláusulas

Con las fórmulas ya en forma prenexa y skolemizada, eliminamos los cuantificadores universales y obtenemos las siguientes cláusulas:

1. De la fórmula (1):

$$
C_1:\quad \neg Alumno(x) \lor \neg Curso(y) \lor \neg Inscrito(x,y) \lor \neg Calificacion(x,y,z) \lor \neg Aprobatoria(z) \lor Aprueba(x,y)
$$

2. De la fórmula (4):

$$
C_2:\quad \neg Alumno(x) \lor \neg Curso(y) \lor Inscrito(x,y) \lor \neg Aprueba(x,y)
$$

3. De los hechos y la skolemización:

$$
C_3:\quad \{Alumno(a)\}
$$
$$
C_4:\quad \{Inscrito(a,c_1)\}
$$
$$
C_5:\quad \{Curso(c_1)\}
$$
$$
C_6:\quad \{DaClase(p_0,c_1)\}
$$
$$
C_7:\quad \{Calificacion(a,c_1,z_0)\}
$$
$$
C_8:\quad \{Aprobatoria(z_0)\}
$$

Asumiremos además que:

$$
C_9:\quad \neg Aprobatoria(z_1)
$$

es verdadera (es decir, $Aprobatoria(z_1)$ es falsa) para reflejar que $z_1$ es reprobatoria.

***

## 4. Universo y base de Herbrand

### 4.1. Universo de Herbrand

Con el lenguaje definido:

- Constantes: $a, c_1, p_0, z_0, z_1$.
- Funciones: $prof(x)$.

El universo de Herbrand $U_H$ es el conjunto de todos los términos cerrados construidos con estas constantes y la función $prof$:

- Nivel 0 (términos básicos): $a, c_1, p_0, z_0, z_1$.
- Nivel 1: $prof(a), prof(c_1), prof(p_0), prof(z_0), prof(z_1)$.
- Nivel 2: $prof(prof(a)), prof(prof(c_1)), \ldots$

Y así sucesivamente. Debido a la función $prof$, el universo es infinito, ya que se puede aplicar $prof$ indefinidamente. 

### 4.2. Base de Herbrand

La base de Herbrand es el conjunto de todos los átomos posibles formados con los predicados del lenguaje y términos de $U_H$.

Si nos restringimos a términos de nivel 0 ($a, c_1, p_0, z_0, z_1$), algunos átomos de la base son:

- Con $Alumno$ y $Curso$:
  - $Alumno(a)$, $Alumno(c_1)$, $Alumno(p_0)$, $Alumno(z_0)$, $Alumno(z_1)$.
  - $Curso(a)$, $Curso(c_1)$, $Curso(p_0)$, $Curso(z_0)$, $Curso(z_1)$.
- Con $Inscrito$ y $Aprueba$:
  - $Inscrito(a,c_1)$, $Inscrito(a,a)$, $Inscrito(c_1,a)$, $Inscrito(p_0,c_1)$, etc.
  - $Aprueba(a,c_1)$, $Aprueba(a,a)$, $Aprueba(c_1,a)$, $Aprueba(p_0,c_1)$, etc.
- Con $DaClase$:
  - $DaClase(p_0,c_1)$, $DaClase(a,c_1)$, $DaClase(p_0,a)$, etc.
- Con $Calificacion$:
  - $Calificacion(a,c_1,z_0)$, $Calificacion(a,c_1,z_1)$.
  - $Calificacion(a,a,z_0)$, $Calificacion(c_1,a,z_1)$, etc.
- Con $Aprobatoria$:
  - $Aprobatoria(z_0)$, $Aprobatoria(z_1)$, $Aprobatoria(a)$, etc.

En las cláusulas de nuestra práctica aparecen específicamente los átomos:

- $Alumno(a)$, $Curso(c_1)$, $Inscrito(a,c_1)$, $DaClase(p_0,c_1)$, $Calificacion(a,c_1,z_0)$, $Aprobatoria(z_0)$, $Aprueba(a,c_1)$.

***

## 5. Interpretaciones de Herbrand y satisfactibilidad

Una interpretación de Herbrand usa:

- Universo $U_H$.
- Las funciones interpretadas de manera estándar (sobre términos).
- Un conjunto de átomos de la base que se consideran verdaderos; los demás son falsos.

Trabajaremos con tres interpretaciones:

- $\mathcal{I}_1$: satisface todas las cláusulas.
- $\mathcal{I}_2$: no satisface la cláusula $C_1$.
- $\mathcal{I}_3$: permite que un alumno apruebe un curso sin estar inscrito, violando la cláusula $C_2$.

### 5.1. Interpretación $\mathcal{I}_1$ (satisfactible)

En $\mathcal{I}_1$ consideramos verdaderos los siguientes átomos:

- $Alumno(a)$.
- $Curso(c_1)$.
- $DaClase(p_0,c_1)$.
- $Inscrito(a,c_1)$.
- $Calificacion(a,c_1,z_0)$.
- $Aprobatoria(z_0)$.
- $Aprueba(a,c_1)$.

Y consideramos falsos todos los demás átomos, incluyendo $Aprobatoria(z_1)$ y cualquier otro que no esté en la lista.

#### Verificación de la cláusula $C_1$

Cláusula:

$$
C_1:\quad \neg Alumno(x) \lor \neg Curso(y) \lor \neg Inscrito(x,y) \lor \neg Calificacion(x,y,z) \lor \neg Aprobatoria(z) \lor Aprueba(x,y)
$$

Tomamos la instancia $x=a, y=c_1, z=z_0$. Sustituimos:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor \neg Inscrito(a,c_1) \lor \neg Calificacion(a,c_1,z_0) \lor \neg Aprobatoria(z_0) \lor Aprueba(a,c_1)
$$

En $\mathcal{I}_1$:

- $Alumno(a)$ es verdadero → $\neg Alumno(a)$ es falso.
- $Curso(c_1)$ es verdadero → $\neg Curso(c_1)$ es falso.
- $Inscrito(a,c_1)$ es verdadero → $\neg Inscrito(a,c_1)$ es falso.
- $Calificacion(a,c_1,z_0)$ es verdadera → $\neg Calificacion(a,c_1,z_0)$ es falsa.
- $Aprobatoria(z_0)$ es verdadera → $\neg Aprobatoria(z_0)$ es falsa.
- $Aprueba(a,c_1)$ es verdadera.

Sustituimos valores:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor \neg Inscrito(a,c_1) \lor \neg Calificacion(a,c_1,z_0) \lor \neg Aprobatoria(z_0) \lor Aprueba(a,c_1)
$$

$$
= \text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{True}
$$

La disyunción:

$$
\text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{True} = \text{True}
$$

Por tanto, la instancia de $C_1$ para $x=a,y=c_1,z=z_0$ es verdadera en $\mathcal{I}_1$.

#### Verificación de la cláusula $C_2$

Cláusula:

$$
C_2:\quad \neg Alumno(x) \lor \neg Curso(y) \lor Inscrito(x,y) \lor \neg Aprueba(x,y)
$$

Tomamos la instancia $x=a,y=c_1$. Sustituimos:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor Inscrito(a,c_1) \lor \neg Aprueba(a,c_1)
$$

En $\mathcal{I}_1$:

- $Alumno(a)$ es verdadero → $\neg Alumno(a)$ es falso.
- $Curso(c_1)$ es verdadero → $\neg Curso(c_1)$ es falso.
- $Inscrito(a,c_1)$ es verdadero.
- $Aprueba(a,c_1)$ es verdadero → $\neg Aprueba(a,c_1)$ es falso.

Sustituimos valores:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor Inscrito(a,c_1) \lor \neg Aprueba(a,c_1)
$$

$$
= \text{False} \lor \text{False} \lor \text{True} \lor \text{False}
$$

La disyunción:

$$
\text{False} \lor \text{False} \lor \text{True} \lor \text{False} = \text{True}
$$

Por tanto, la instancia de $C_2$ para $x=a,y=c_1$ es verdadera en $\mathcal{I}_1$.

En $\mathcal{I}_1$, todas las cláusulas $C_1$–$C_9$ se satisfacen para las instancias relevantes, por lo que el conjunto es satisfactible.

***

### 5.2. Interpretación $\mathcal{I}_2$ (no satisface $C_1$)

En $\mathcal{I}_2$ tomamos como verdaderos:

- $Alumno(a)$.
- $Curso(c_1)$.
- $DaClase(p_0,c_1)$.
- $Inscrito(a,c_1)$.
- $Calificacion(a,c_1,z_0)$.
- $Aprobatoria(z_0)$.

Pero ahora **consideramos falso**:

- $Aprueba(a,c_1)$.

Todos los demás átomos, falsos (incluyendo $Aprobatoria(z_1)$).

#### Verificación de la cláusula $C_1$ en $\mathcal{I}_2$

Cláusula:

$$
C_1:\quad \neg Alumno(x) \lor \neg Curso(y) \lor \neg Inscrito(x,y) \lor \neg Calificacion(x,y,z) \lor \neg Aprobatoria(z) \lor Aprueba(x,y)
$$

Instancia $x=a,y=c_1,z=z_0$:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor \neg Inscrito(a,c_1) \lor \neg Calificacion(a,c_1,z_0) \lor \neg Aprobatoria(z_0) \lor Aprueba(a,c_1)
$$

En $\mathcal{I}_2$:

- $Alumno(a)$ es verdadero → $\neg Alumno(a)$ es falso.
- $Curso(c_1)$ es verdadero → $\neg Curso(c_1)$ es falso.
- $Inscrito(a,c_1)$ es verdadero → $\neg Inscrito(a,c_1)$ es falso.
- $Calificacion(a,c_1,z_0)$ es verdadera → $\neg Calificacion(a,c_1,z_0)$ es falsa.
- $Aprobatoria(z_0)$ es verdadera → $\neg Aprobatoria(z_0)$ es falsa.
- $Aprueba(a,c_1)$ es falso.

Sustituimos valores:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor \neg Inscrito(a,c_1) \lor \neg Calificacion(a,c_1,z_0) \lor \neg Aprobatoria(z_0) \lor Aprueba(a,c_1)
$$

$$
= \text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{False}
$$

La disyunción:

$$
\text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{False} \lor \text{False} = \text{False}
$$

Por tanto, la instancia de $C_1$ para $x=a,y=c_1,z=z_0$ es falsa en $\mathcal{I}_2$. Esto muestra que el conjunto de cláusulas no es satisfactible en $\mathcal{I}_2$.

#### Verificación de la cláusula $C_2$ en $\mathcal{I}_2$

Cláusula:

$$
C_2:\quad \neg Alumno(x) \lor \neg Curso(y) \lor Inscrito(x,y) \lor \neg Aprueba(x,y)
$$

Instancia $x=a,y=c_1$:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor Inscrito(a,c_1) \lor \neg Aprueba(a,c_1)
$$

En $\mathcal{I}_2$:

- $Alumno(a)$ verdadero → $\neg Alumno(a)$ falso.
- $Curso(c_1)$ verdadero → $\neg Curso(c_1)$ falso.
- $Inscrito(a,c_1)$ verdadero.
- $Aprueba(a,c_1)$ falso → $\neg Aprueba(a,c_1)$ verdadero.

Sustituimos valores:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor Inscrito(a,c_1) \lor \neg Aprueba(a,c_1)
$$

$$
= \text{False} \lor \text{False} \lor \text{True} \lor \text{True}
$$

La disyunción:

$$
\text{False} \lor \text{False} \lor \text{True} \lor \text{True} = \text{True}
$$

La cláusula $C_2$ sigue siendo verdadera en $\mathcal{I}_2$; la violación se produce sólo en $C_1$.

***

### 5.3. Interpretación $\mathcal{I}_3$ (aprueba sin estar inscrito, viola $C_2$)

En $\mathcal{I}_3$ queremos un caso donde un alumno apruebe un curso sin estar inscrito, contradiciendo la regla de la cláusula $C_2$.

Tomamos como verdaderos:

- $Alumno(a)$.
- $Curso(c_1)$.
- $DaClase(p_0,c_1)$.
- $Calificacion(a,c_1,z_0)$.
- $Aprobatoria(z_0)$.
- $Aprueba(a,c_1)$.

Consideramos falsos:

- $Inscrito(a,c_1)$ (clave para violar $C_2$).
- $Aprobatoria(z_1)$.
- Todos los demás átomos no mencionados.

#### Verificación de la cláusula $C_1$ en $\mathcal{I}_3$

Cláusula:

$$
C_1:\quad \neg Alumno(x) \lor \neg Curso(y) \lor \neg Inscrito(x,y) \lor \neg Calificacion(x,y,z) \lor \neg Aprobatoria(z) \lor Aprueba(x,y)
$$

Instancia $x=a,y=c_1,z=z_0$:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor \neg Inscrito(a,c_1) \lor \neg Calificacion(a,c_1,z_0) \lor \neg Aprobatoria(z_0) \lor Aprueba(a,c_1)
$$

En $\mathcal{I}_3$:

- $Alumno(a)$ es verdadero → $\neg Alumno(a)$ falso.
- $Curso(c_1)$ es verdadero → $\neg Curso(c_1)$ falso.
- $Inscrito(a,c_1)$ es falso → $\neg Inscrito(a,c_1)$ verdadero.
- $Calificacion(a,c_1,z_0)$ verdadera → $\neg Calificacion(a,c_1,z_0)$ falsa.
- $Aprobatoria(z_0)$ verdadera → $\neg Aprobatoria(z_0)$ falsa.
- $Aprueba(a,c_1)$ verdadera.

Sustituimos:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor \neg Inscrito(a,c_1) \lor \neg Calificacion(a,c_1,z_0) \lor \neg Aprobatoria(z_0) \lor Aprueba(a,c_1)
$$

$$
= \text{False} \lor \text{False} \lor \text{True} \lor \text{False} \lor \text{False} \lor \text{True}
$$

La disyunción:

$$
\text{False} \lor \text{False} \lor \text{True} \lor \text{False} \lor \text{False} \lor \text{True} = \text{True}
$$

Así, la instancia de $C_1$ para $x=a,y=c_1,z=z_0$ sigue siendo verdadera en $\mathcal{I}_3$.

#### Verificación de la cláusula $C_2$ en $\mathcal{I}_3$

Cláusula:

$$
C_2:\quad \neg Alumno(x) \lor \neg Curso(y) \lor Inscrito(x,y) \lor \neg Aprueba(x,y)
$$

Instancia $x=a,y=c_1$:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor Inscrito(a,c_1) \lor \neg Aprueba(a,c_1)
$$

En $\mathcal{I}_3$:

- $Alumno(a)$ verdadero → $\neg Alumno(a)$ falso.
- $Curso(c_1)$ verdadero → $\neg Curso(c_1)$ falso.
- $Inscrito(a,c_1)$ falso.
- $Aprueba(a,c_1)$ verdadero → $\neg Aprueba(a,c_1)$ falso.

Sustituimos valores:

$$
\neg Alumno(a) \lor \neg Curso(c_1) \lor Inscrito(a,c_1) \lor \neg Aprueba(a,c_1)
$$

$$
= \text{False} \lor \text{False} \lor \text{False} \lor \text{False}
$$

La disyunción:

$$
\text{False} \lor \text{False} \lor \text{False} \lor \text{False} = \text{False}
$$

La cláusula $C_2$ es falsa en $\mathcal{I}_3$, lo que muestra que esta interpretación viola la condición “si no está inscrito, entonces no aprueba”.
