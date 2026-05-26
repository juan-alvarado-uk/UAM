# Las tablas de verdad no son suficientes

Las tablas de verdad permiten verificar si un argumento es válido: se construía la tabla completa y se buscaban contraejemplos. Ese método es sistemático y correcto, pero tiene un problema serio cuando el número de variables crece. Con $n$ variables atómicas, la tabla tiene $2^n$ filas. Con 10 variables — algo perfectamente razonable en la especificación de un sistema real — la tabla tendría 1,024 filas. Con 20 variables, más de un millón.

Existe un camino distinto: en lugar de evaluar todas las combinaciones posibles, se puede derivar la conclusión paso a paso, aplicando en cada paso una regla que preserve la verdad. Ese camino es la **prueba formal** o **deducción**.

La analogía con el trabajo cotidiano en sistemas es directa. Cuando un desarrollador depura un programa, no prueba todas las entradas posibles; razona: "si el módulo de autenticación falló y el log muestra que la conexión a la base de datos fue exitosa, entonces el problema está en la capa de validación de credenciales". Eso es inferencia. Las reglas formales que se estudian en esta sesión son precisamente la versión rigurosa de ese razonamiento.

***

# Argumento Válido y Prueba Formal

Un **argumento** en lógica proposicional es un conjunto finito de fórmulas llamadas **premisas**, acompañado de una fórmula designada llamada **conclusión**. Se escribe habitualmente como:

$$
P_1,\; P_2,\; \ldots,\; P_n \;\vdash\; C
$$

donde $P_1, \ldots, P_n$ son las premisas y $C$ es la conclusión.

Un argumento es **válido** cuando es imposible que todas las premisas sean verdaderas y la conclusión sea falsa al mismo tiempo; es decir, cuando la conclusión es consecuencia lógica de las premisas.

Una **prueba formal** (o **demostración**) es una secuencia finita de fórmulas $F_1, F_2, \ldots, F_k$, donde cada $F_i$ satisface exactamente una de estas dos condiciones:

- Es una de las premisas del argumento, o
- Se obtiene de fórmulas anteriores en la secuencia aplicando una **regla de inferencia**.

La última fórmula de la secuencia es la conclusión que se quería demostrar. Cada línea de la prueba lleva anotada su justificación: el nombre de la premisa o el nombre de la regla aplicada, junto con los números de línea de las que depende.

# Notación de las Pruebas Formales

Cada línea de una prueba tiene el siguiente formato:

| Línea | Fórmula | Justificación                  |
|-------|---------|--------------------------------|
| 1     | $P_1$   | Premisa                        |
| 2     | $P_2$   | Premisa                        |
| 3     | $F_3$   | Nombre de regla, líneas usadas |
| …     | …       | …                              |
| k     | $C$     | Nombre de regla, líneas usadas |

La columna de justificación es obligatoria. Una línea sin justificación no tiene valor en una prueba formal.

***

# Las Reglas de Inferencia Básicas

A continuación se presentan las reglas de inferencia más utilizadas en lógica de proposiciones. Cada regla se expresa indicando las fórmulas que deben estar disponibles (hipótesis de la regla) y la fórmula que se obtiene (conclusión de la regla).

***

## Modus Ponens (MP)

Si se sabe que $p \to q$ es verdadero, y también que $p$ es verdadero, entonces necesariamente $q$ es verdadero.

$$
\frac{p \to q \quad p}{q} \quad \text{Modus Ponens}
$$

**Ejemplo cotidiano:** "Si llueve, la calle se moja" y "está lloviendo"; por lo tanto, "la calle está mojada".

El modus ponens es probablemente la regla más usada en razonamiento cotidiano y en especificación de sistemas basados en reglas.

***

## Modus Tollens (MT)

Si se sabe que $p \to q$ y además que $q$ es falso ($\neg q$), entonces $p$ también es falso ($\neg p$).

$$
\frac{p \to q \quad \neg q}{\neg p} \quad \text{Modus Tollens}
$$

**Ejemplo cotidiano:** "Si el candidato aprobó el examen, recibe la certificación" y "no recibió la certificación"; por lo tanto, "no aprobó el examen".

El modus tollens es la base del razonamiento por descarte: cuando el efecto esperado no ocurre, se concluye que la causa tampoco ocurrió.

***

## Silogismo Hipotético (SH)

Si $p \to q$ y $q \to r$, entonces se puede concluir $p \to r$. La regla encadena condicionales.

$$
\frac{p \to q \quad q \to r}{p \to r} \quad \text{Silogismo Hipotético}
$$

**Ejemplo cotidiano:** "Si estudio, aprendo; si aprendo, apruebo el examen"; por lo tanto, "si estudio, apruebo el examen".

Esta regla aparece con frecuencia cuando se modelan cadenas de dependencias entre módulos.

***

## Silogismo Disyuntivo (SD)

Si se sabe que $p \lor q$ y además que $\neg p$ (es decir, $p$ es falso), entonces necesariamente $q$ es verdadero.

$$
\frac{p \lor q \quad \neg p}{q} \quad \text{Silogismo Disyuntivo}
$$

Simétricamente, si se sabe $p \lor q$ y $\neg q$, se concluye $p$.

**Ejemplo cotidiano:** "La reunión es en línea o en la sala de juntas" y "la reunión no es en línea"; por lo tanto, "la reunión es en la sala de juntas".

## Adición (Ad)

Si se sabe que $p$ es verdadero, entonces $p \lor q$ también es verdadero, para cualquier $q$.

$$
\frac{p}{p \lor q} \quad \text{Adición}
$$

**Justificación intuitiva:** Si una disyunción requiere que al menos uno de sus disyuntos sea verdadero, y ya se sabe que $p$ lo es, la disyunción completa es verdadera sin importar el valor de $q$.

Esta regla parece trivial, pero es indispensable en pruebas donde se necesita construir una disyunción para aplicar después el silogismo disyuntivo.

***

## Simplificación (Simp)

Si se sabe que $p \land q$ es verdadero, entonces en particular $p$ es verdadero, y también $q$ es verdadero. Se pueden extraer los conjuntos por separado.

$$
\frac{p \land q}{p} \qquad \frac{p \land q}{q} \quad \text{Simplificación}
$$

**Ejemplo:** La especificación dice "el sistema es seguro y está disponible". De ahí se puede concluir, por separado, que "el sistema es seguro" o que "el sistema está disponible", según lo que se necesite en el razonamiento.

***

## Conjunción (Conj)

Si se sabe que $p$ es verdadero y que $q$ es verdadero (en líneas separadas de la prueba), se puede combinar para obtener $p \land q$.

$$
\frac{p \quad q}{p \land q} \quad \text{Conjunción}
$$

**Ejemplo en sistemas:** Si se ha demostrado "el respaldo fue exitoso" y "el sistema está en línea", se puede concluir "el respaldo fue exitoso y el sistema está en línea", que podría ser la condición compuesta que se buscaba establecer.

***

## Doble Negación (DN)

Una fórmula y su doble negación son interderivables: de $p$ se puede pasar a $\neg \neg p$ y viceversa.

$$
\frac{p}{\neg \neg p} \qquad \frac{\neg \neg p}{p} \quad \text{Doble Negación}
$$

Esta regla se usa con frecuencia para preparar una fórmula para aplicar modus tollens o para simplificar negaciones acumuladas.

***

## Transposición (Trans)

Un condicional y su contrapositivo son lógicamente equivalentes. Por eso, de $p \to q$ se puede derivar $\neg q \to \neg p$, y viceversa.

$$
\frac{p \to q}{\neg q \to \neg p} \quad \text{Transposición}
$$

**Ejemplo:** "Si el protocolo es seguro, los datos viajan cifrados" equivale a "si los datos no viajan cifrados, el protocolo no es seguro".

La transposición es la contraparte formal del modus tollens: en lugar de aplicar MT directamente, a veces conviene primero transponer y luego aplicar MP.

***

## Exportación / Importación (Exp)

Permite reescribir una conjunción en el antecedente como un condicional anidado, y viceversa.

$$
\frac{(p \land q) \to r}{p \to (q \to r)} \quad \text{Exportación}
$$

$$
\frac{p \to (q \to r)}{(p \land q) \to r} \quad \text{Importación}
$$

**Ejemplo en sistemas:** "Si el usuario está autenticado y tiene permisos de escritura, puede modificar el archivo" equivale a "si el usuario está autenticado, entonces si tiene permisos de escritura, puede modificar el archivo".

***

## Absorción (Abs)

De $p \to q$ se puede derivar $p \to (p \land q$).

$$
\frac{p \to q}{p \to (p \land q)} \quad \text{Absorción}
$$

Esta regla es útil cuando se necesita construir una conjunción dentro de la conclusión de un condicional.

***

# Tabla Resumen de Reglas

| Nombre                    | Hipótesis            | Conclusión                  |
|---------------------------|----------------------|-----------------------------|
| Modus Ponens (MP)         | $p \to q$, $p$       | $q$                         |
| Modus Tollens (MT)        | $p \to q$, $\neg q$  | $\neg p$                    |
| Silogismo Hipotético (SH) | $p \to q$, $q \to r$ | $p \to r$                   |
| Silogismo Disyuntivo (SD) | $p \lor q$, $\neg p$ | $q$                         |
| Adición (Ad)              | $p$                  | $p \lor q$                  |
| Simplificación (Simp)     | $p \land q$          | $p$ (o $q$)                 |
| Conjunción (Conj)         | $p$, $q$             | $p \land q$                 |
| Doble Negación (DN)       | $p$                  | $\neg \neg p$ (y viceversa) |
| Transposición (Trans)     | $p \to q$            | $\neg q \to \neg p$         |
| Exportación (Exp)         | $(p \land q) \to r$  | $p \to (q \to r)$           |
| Importación (Imp)         | $p \to (q \to r)$    | $(p \land q) \to r$         |
| Absorción (Abs)           | $p \to q$            | $p \to (p \land q)$         |

***

# Cómo Construir una Prueba Formal: Estrategia General

Antes de escribir la primera línea de una prueba, conviene seguir un proceso de análisis:

1. **Identificar la conclusión.** ¿Qué forma tiene la fórmula que se quiere demostrar? ¿Es un condicional, una conjunción, una negación?
2. **Revisar las premisas.** ¿Qué información está disponible? ¿Hay condicionales que podrían aprovecharse con MP o MT? ¿Hay disyunciones que podrían aprovecharse con SD?
3. **Trabajar hacia atrás (backward chaining).** Pensar: "para obtener $C$, ¿qué necesito tener disponible?". Si $C$ es $q$ y hay una premisa $p \to q$, solo se necesita derivar $p$.
4. **Escribir la prueba hacia adelante.** Una vez identificado el camino, escribir las líneas en orden, con justificación en cada una.

> **Analogía con programación:** Esto es similar al diseño descendente (top-down). Primero se define qué resultado se necesita, luego qué subproblemas hay que resolver para llegar a él, y finalmente se implementa de menor a mayor.

***

# Ejemplos Completos de Pruebas Formales

## Ejemplo 1 — Prueba con MP y SH

**Contexto:** En una red corporativa: si un usuario intenta conectarse a la VPN, se verifica su identidad; si se verifica su identidad, se registra el acceso en el log de auditoría.

---
**Variables:**
- $p$: el usuario intenta conectarse a la VPN
- $q$: se verifica la identidad del usuario
- $r$: se registra el acceso en el log de auditoría

---
**Premisas:**
1. $p \to q$
2. $q \to r$
3. $p$

**Conclusión a demostrar:** $r$

| Línea | Fórmula   | Justificación    |
|-------|-----------|------------------|
| 1     | $p \to q$ | Premisa          |
| 2     | $q \to r$ | Premisa          |
| 3     | $p$       | Premisa          |
| 4     | $p \to r$ | SH, líneas 1 y 2 |
| 5     | $r$       | MP, líneas 4 y 3 |

**Interpretación:** El usuario intentó conectarse a la VPN; por la cadena de condicionales, se concluye que el acceso quedó registrado en el log de auditoría.

***

## Ejemplo 2 — Prueba con MT y SD

**Contexto:** Un sistema de disponibilidad tiene la siguiente especificación:
- Si el servidor principal está activo, el servicio responde en menos de 200 ms.
- El servicio responde en menos de 200 ms, o se activa el servidor de respaldo.
- El servidor de respaldo no se activó.
- El servicio no responde en menos de 200 ms.

---
**Variables:**
- $a$: el servidor principal está activo
- $r$: el servicio responde en menos de 200 ms
- $b$: se activa el servidor de respaldo

---
**Premisas:**
1. $a \to r$
2. $r \lor b$
3. $\neg b$
4. $\neg r$

**Conclusión a demostrar:** $\neg a$

| Línea | Fórmula    | Justificación    |
|-------|------------|------------------|
| 1     | $a \to r$  | Premisa          |
| 2     | $r \lor b$ | Premisa          |
| 3     | $\neg b$   | Premisa          |
| 4     | $\neg r$   | Premisa          |
| 5     | $\neg a$   | MT, líneas 1 y 4 |

**Interpretación:** El servicio no responde dentro del tiempo esperado y el servidor de respaldo no se activó, lo que implica que el servidor principal tampoco está activo.

***

## Ejemplo 3 — Prueba con Conj y MP

**Contexto:** Una plataforma de pagos en línea establece: si el token de sesión es válido y el monto está dentro del límite autorizado, se aprueba la transacción; si la transacción es aprobada, se envía una notificación al usuario.

---
**Variables:**
- $p$: el token de sesión es válido
- $q$: el monto está dentro del límite autorizado
- $r$: la transacción es aprobada
- $s$: se envía una notificación al usuario

---
**Premisas:**
1. $p \land q$
2. $(p \land q) \to r$
3. $r \to s$

**Conclusión a demostrar:** $s$

| Línea | Fórmula             | Justificación    |
|-------|---------------------|------------------|
| 1     | $p \land q$         | Premisa          |
| 2     | $(p \land q) \to r$ | Premisa          |
| 3     | $r \to s$           | Premisa          |
| 4     | $r$                 | MP, líneas 2 y 1 |
| 5     | $s$                 | MP, líneas 3 y 4 |

**Interpretación:** La sesión es válida y el monto está autorizado; por lo tanto, la transacción se aprueba y el usuario recibe su notificación.

***

## Ejemplo 4

**Contexto de sistemas:** Una política de acceso a datos sensibles establece:

- Si el usuario tiene rol de administrador o tiene autorización especial, puede ver los registros.
- El usuario no tiene autorización especial.
- Si el usuario puede ver los registros y los registros están clasificados, debe firmar un acuerdo de confidencialidad.
- Los registros están clasificados.
- El usuario tiene rol de administrador.

---
**Variables:**
- $a$: el usuario tiene rol de administrador
- $e$: el usuario tiene autorización especial
- $v$: el usuario puede ver los registros
- $c$: los registros están clasificados
- $f$: el usuario debe firmar el acuerdo de confidencialidad

---
**Premisas:**
1. $(a \lor e) \to v$
2. $\neg e$
3. $(v \land c) \to f$
4. $c$
5. $a$

**Conclusión a demostrar:** $f$

| Línea | Fórmula             | Justificación      |
|-------|---------------------|--------------------|
| 1     | $(a \lor e) \to v$  | Premisa            |
| 2     | $\neg e$            | Premisa            |
| 3     | $(v \land c) \to f$ | Premisa            |
| 4     | $c$                 | Premisa            |
| 5     | $a$                 | Premisa            |
| 6     | $a \lor e$          | Ad, línea 5        |
| 7     | $v$                 | MP, líneas 1 y 6   |
| 8     | $v \land c$         | Conj, líneas 7 y 4 |
| 9     | $f$                 | MP, líneas 3 y 8   |

**Interpretación:** El usuario debe firmar el acuerdo de confidencialidad. Nótese la línea 6: para poder usar la premisa 1 (que tiene $a \lor e$ como antecedente), se construyó la disyunción a partir del hecho simple $a$ usando la regla de Adición. Este es un uso clásico de Adición que no resulta obvio a primera vista.

***

# Errores Comunes al Construir Pruebas

## Afirmación del Consecuente

De $p \to q$ y $q$, **no** se puede concluir $p$. Esta es una falacia clásica.

**Ejemplo erróneo:** "Si hay fuego, hay humo" y "hay humo"; por lo tanto, "hay fuego". Incorrecto: el humo puede tener otras causas.

En sistemas: "Si el sistema está bajo ataque DDoS, la red se satura" y "la red está saturada"; no se puede concluir automáticamente que hay un ataque DDoS — podría ser tráfico legítimo alto.

## Negación del Antecedente

De $p \to q$ y $\neg p$, **no** se puede concluir $\neg q$.

**Ejemplo erróneo:** "Si apruebas el examen, obtienes el certificado" y "no aprobaste el examen"; por lo tanto, "no obtienes el certificado". Incorrecto: podría haber otras vías para obtenerlo.

## Usar líneas fuera de orden incorrecto

Las reglas de inferencia solo pueden aplicarse a fórmulas que ya aparecieron en líneas **anteriores** de la prueba. No se puede usar una línea que todavía no ha sido derivada.

## Justificación incompleta

Escribir solo "MP" sin indicar los números de línea no es una justificación válida. Siempre deben citarse las líneas específicas de las que provienen las hipótesis de la regla.

***

# Modelado con Lógica de Proposiciones

El modelado lógico es el proceso de traducir un problema expresado en lenguaje natural a un conjunto de fórmulas proposicionales, y luego usar reglas de inferencia para derivar conclusiones.

## Proceso de Modelado

1. **Identificar las proposiciones atómicas** relevantes en el problema. Asignar una variable ($p, q, r, \ldots$) a cada una.
2. **Traducir las restricciones** del problema a fórmulas lógicas.
3. **Identificar qué se quiere demostrar** y escribirlo como conclusión.
4. **Construir la prueba formal.**

> **Observación:** No todas las oraciones en lenguaje natural se traducen directamente. Frases como "solo si", "a menos que", "ni..., ni...," requieren cuidado especial.

| Expresión en español          | Fórmula lógica                            |
|-------------------------------|-------------------------------------------|
| "Si $p$ entonces $q$"         | $p \to q$                                 |
| "$p$ solo si $q$"             | $p \to q$                                 |
| "$p$ a menos que $q$"         | $\neg q \to p$ (equivalente a $p \lor q$) |
| "Ni $p$ ni $q$"               | $\neg p \land \neg q$                     |
| "$p$ si y solo si $q$"        | $p \leftrightarrow q$                     |
| "No es el caso que $p$ y $q$" | $\neg(p \land q)$                         |

***

# Problema de Disponibilidad de Servicios

## El problema

En un sistema de cómputo distribuido:

1. Si el servicio de autenticación está disponible y el servicio de base de datos está disponible, entonces los usuarios pueden iniciar sesión.
2. Si los usuarios pueden iniciar sesión, entonces hay actividad en el sistema.
3. No hay actividad en el sistema.

¿Qué se puede concluir sobre la disponibilidad conjunta de los servicios?

## Modelado

- $a$: el servicio de autenticación está disponible
- $d$: el servicio de base de datos está disponible
- $s$: los usuarios pueden iniciar sesión
- $x$: hay actividad en el sistema

---
**Premisas:**
1. $(a \land d) \to s$
2. $s \to x$
3. $\neg x$

**Conclusión a demostrar:** $\neg(a \land d)$

| Línea | Fórmula             | Justificación    |
|-------|---------------------|------------------|
| 1     | $(a \land d) \to s$ | Premisa          |
| 2     | $s \to x$           | Premisa          |
| 3     | $\neg x$            | Premisa          |
| 4     | $(a \land d) \to x$ | SH, líneas 1 y 2 |
| 5     | $\neg(a \land d)$   | MT, líneas 4 y 3 |

**Interpretación:** No es el caso que ambos servicios estén disponibles simultáneamente. Aplicando De Morgan (equivalencia lógica ya conocida): al menos uno de los dos servicios está fuera de operación. El sistema no puede dar más información sin evidencia adicional sobre cuál de los dos es el que presenta problemas.

***

# Ejercicios para Resolver

Los siguientes ejercicios se resuelven aplicando únicamente las reglas presentadas en este material. En cada caso, se dan las premisas y la conclusión; la tarea es construir la prueba formal completa, justificando cada línea.

***

## Ejercicio 1

**Premisas:**
1. $p \to q$
2. $\neg q$
3. $p \lor r$

**Conclusión:** $r$

*Pista: Empieza por obtener $\neg p$ a partir de las premisas 1 y 2.*

***

## Ejercicio 2

**Premisas:**
1. $m \to n$
2. $n \to o$
3. $o \to p$
4. $m$

**Conclusión:** $p$

*Pista: Encadena las primeras tres premisas con SH antes de aplicar MP.*

***

## Ejercicio 3

**Premisas:**
1. $(a \land b) \to c$
2. $a$
3. $b$

**Conclusión:** $c$

***

## Ejercicio 4

**Contexto:** Sistema de alertas de seguridad.

- Si hay acceso no autorizado, se genera una alerta.
- Si se genera una alerta, el administrador es notificado.
- El administrador no fue notificado.
- Hay acceso no autorizado o el servidor está en mantenimiento.

---
**Variables:**
- $u$: hay acceso no autorizado
- $g$: se genera una alerta
- $n$: el administrador es notificado
- $m$: el servidor está en mantenimiento

---
**Premisas:**
1. $u \to g$
2. $g \to n$
3. $\neg n$
4. $u \lor m$

**Conclusión:** $m$

***

## Ejercicio 5

**Enunciado:** Tres estudiantes, Luis, María y Nora, presentaron el proyecto final. Se sabe:

- Si Luis no entregó el proyecto, María tampoco lo entregó.
- Nora entregó el proyecto si y solo si María lo entregó.
- Nora no entregó el proyecto.

¿Entregó Luis el proyecto?

*Tarea: Definir variables, traducir a fórmulas, construir la prueba y responder la pregunta con justificación formal.*

***

# Resumen: Prueba Formal Correcta

Una prueba formal válida tiene estas características:

- **Cada línea es una fórmula bien formada** (concepto ya conocido de sesiones anteriores).
- **Cada línea tiene exactamente una justificación**: o es premisa, o es el resultado de aplicar una regla a líneas anteriores numeradas.
- **Las reglas se aplican correctamente**: las hipótesis de la regla coinciden exactamente con las fórmulas citadas, incluyendo la estructura de los conectivos.
- **La última línea es la conclusión** que se quería demostrar.
- **No hay saltos**: si una fórmula parece "obvia", igual debe aparecer en su propia línea con justificación.

Una prueba formal en lógica proposicional tiene la misma función que un algoritmo bien documentado en programación: cada operación está justificada, el estado del sistema está explícito en cada paso, y el resultado final es verificable de forma mecánica.

***

# Conexión con Sistemas: ¿Para qué sirve esto realmente?

La capacidad de construir pruebas formales es directamente aplicable en varias áreas de los sistemas de información:

**Verificación de políticas de acceso.** Los sistemas de control de acceso basado en roles (RBAC) y en atributos (ABAC) definen reglas que pueden modelarse como condicionales proposicionales. Verificar que una política es consistente (no permite accesos contradictorios) equivale a buscar pruebas o refutaciones en un sistema lógico.

**Especificación de requisitos.** Al documentar requisitos de un sistema, expresiones como "si el usuario es administrador, puede modificar configuraciones" son condicionales proposicionales. Las pruebas formales permiten verificar que los requisitos no se contradicen entre sí.

**Motores de reglas.** Sistemas como Drools, Prolog (que se verá más adelante en el curso), o los motores de reglas en plataformas de inteligencia artificial operan exactamente aplicando variantes de modus ponens de manera automática. Entender la base formal permite leer, depurar y extender esos sistemas con solidez.

**Protocolos de red.** La verificación formal de protocolos de comunicación (como TLS, o los protocolos de consenso en sistemas distribuidos) utiliza sistemas de prueba formales más avanzados que tienen como fundamento exactamente las reglas de inferencia estudiadas aquí.
