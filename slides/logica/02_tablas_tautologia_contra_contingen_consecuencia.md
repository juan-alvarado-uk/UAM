# Introducción

Las tablas de verdad son un procedimiento sistemático para determinar el valor de verdad de una fórmula en todas las combinaciones posibles de sus proposiciones simples. Usaremos fórmulas de 2 y 3 proposiciones, y clasificaremos como tautología, contradicción o contingente, y se revisa la consecuencia lógica mediante la búsqueda de contraejemplos. 


# Tabla de verdad

Una tabla de verdad es un mapa completo de casos posibles. Así como en pruebas de software se revisan **distintas** entradas para ver cómo responde un sistema, en lógica se revisan **todas** las asignaciones posibles de verdad para observar cómo responde una fórmula.

Si una fórmula usa dos proposiciones, existen 4 combinaciones posibles de valores. Si usa tres proposiciones, existen 8 combinaciones posibles, porque cada proposición puede tomar dos valores y el total crece como \(2^n\), donde \(n\) es el número de proposiciones distintas.

## Número de renglones

- 1 proposición \(\rightarrow 2\) renglones.
- 2 proposiciones \(\rightarrow 4\) renglones.
- 3 proposiciones \(\rightarrow 8\) renglones.
- 4 proposiciones \(\rightarrow 16\) renglones.

Esta idea es importante porque evita omisiones. Una tabla incompleta produce conclusiones incorrectas.

# Construcción sistemática

Construir sistemáticamente una tabla de verdad significa seguir un orden fijo para no perder renglones ni cometer saltos en los valores. El objetivo no es adivinar el resultado, sino llegar a él por un procedimiento repetible.

El proceso general consta de cuatro partes:

- Identificar las proposiciones simples distintas.
- Calcular cuántos renglones tendrá la tabla.
- Escribir las columnas de las proposiciones simples con el patrón correcto de V y F.
- Agregar columnas intermedias hasta obtener la columna final de la fórmula.

***

## Patrón de llenado para 2 proposiciones

Si la fórmula contiene \(p\) y \(q\), se usan 4 renglones:

| p | q |
|---|---|
| V | V |
| V | F |
| F | V |
| F | F |

Este orden puede verse como un contador binario lógico. La primera proposición cambia más lento y la última cambia más rápido.


## Patrón de llenado para 3 proposiciones

Si la fórmula contiene \(p\), \(q\) y \(r\), se usan 8 renglones:

| p | q | r |
|---|---|---|
| V | V | V |
| V | V | F |
| V | F | V |
| V | F | F |
| F | V | V |
| F | V | F |
| F | F | V |
| F | F | F |

Aquí también se sigue un ritmo fijo:

- \(p\) cambia cada 4 renglones.
- \(q\) cambia cada 2 renglones.
- \(r\) cambia en cada renglón.


## Orden correcto de evaluación

La tabla se construye desde las subfórmulas internas hasta la fórmula completa. Es parecido al seguimiento de una expresión en programación: primero se resuelven los componentes internos y luego se combina el resultado.

Por ejemplo, para \((p \land q)\rightarrow r\), conviene crear primero la columna de \(p \land q\), y después usar esa columna para evaluar el condicional completo.


## Ejemplo 1: construcción completa con 2 proposiciones

La fórmula \(p \rightarrow q\) expresa que si ocurre \(p\), entonces ocurre \(q\). En un ejemplo cotidiano: “si llueve, entonces la calle se moja”.

| p | q | \(p \rightarrow q\) |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

La columna final muestra que esta fórmula no siempre es verdadera ni siempre es falsa. Tiene al menos un caso verdadero y al menos un caso falso; por eso es contingente.


### Lectura del caso falso

En un condicional, el único caso falso ocurre cuando el antecedente es verdadero y el consecuente es falso. En lenguaje cotidiano, el problema aparece cuando se prometió algo y no se cumplió.

Ejemplo de sistemas: “si el usuario introduce credenciales válidas, entonces obtiene acceso”. Esa afirmación sería falsa justo en el caso en que las credenciales sean válidas y, aun así, no se permita el acceso.


## Ejemplo 2: construcción completa con subfórmulas

La fórmula \((p \lor q)\land \neg p\) combina una disyunción y una negación. Para evitar errores, se crean columnas intermedias.

| p | q | \(p \lor q\) | \(\neg p\) | \((p \lor q)\land \neg p\) |
|---|---|---|---|---|
| V | V | V | F | F |
| V | F | V | F | F |
| F | V | V | V | V |
| F | F | F | V | F |

La fórmula final resulta verdadera en un solo caso. Esto basta para afirmar que no es contradicción, y también basta para afirmar que no es tautología.

***

## Ejemplo 3: tabla con 3 proposiciones

La fórmula \((p \land q)\rightarrow r\) puede leerse en contexto tecnológico así: “si el servidor está activo y la base de datos responde, entonces el servicio queda disponible”.

| p | q | r | \(p \land q\) | \((p \land q)\rightarrow r\) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | V | F | V | F |
| V | F | V | F | V |
| V | F | F | F | V |
| F | V | V | F | V |
| F | V | F | F | V |
| F | F | V | F | V |
| F | F | F | F | V |

La fórmula solo es falsa cuando \(p\) y \(q\) son verdaderas pero \(r\) es falsa. En términos de operación de sistemas, ese es el caso donde las condiciones previas se cumplen, pero el resultado esperado no ocurre.

# Clasificación de fórmulas

La clasificación de una fórmula depende únicamente de la columna final de su tabla de verdad. Esa columna funciona como la “firma de comportamiento” de la fórmula.

Existen tres clases fundamentales:

- Tautología: la columna final contiene solo V.
- Contradicción: la columna final contiene solo F.
- Contingente: la columna final contiene tanto V como F.


## Tautología

Una tautología es una fórmula verdadera en todas las combinaciones posibles. Es como una política del sistema que se mantiene correcta sin importar el estado de entrada.

Ejemplo:
\[
p \lor \neg p
\]

Tabla breve:

| p | \(\neg p\) | \(p \lor \neg p\) |
|---|---|---|
| V | F | V |
| F | V | V |

Siempre resulta verdadera. No existe ninguna asignación que la vuelva falsa.


## Contradicción

Una contradicción es una fórmula falsa en todas las combinaciones posibles. Representa una condición imposible de satisfacer.

Ejemplo:
\[
p \land \neg p
\]

Tabla breve:

| p | \(\neg p\) | \(p \land \neg p\) |
|---|---|---|
| V | F | F |
| F | V | F |

Nunca resulta verdadera. No existe ningún caso que la haga cumplirse.


## Fórmula contingente

Una fórmula contingente es verdadera en algunas combinaciones y falsa en otras. Es la situación más común en lógica aplicada, porque muchas condiciones dependen del estado del entorno.

Ejemplo:
\[
p \land q
\]

| p | q | \(p \land q\) |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

Como aparece al menos una V y al menos una F, se trata de una fórmula contingente.


# Criterio visual rápido de clasificación

Clasificar una fórmula puede hacerse sin volver a leer toda la expresión si ya se construyó bien la tabla. Basta con observar la última columna.

- Todo V \(\rightarrow\) tautología.
- Todo F \(\rightarrow\) contradicción.
- Mezcla de V y F \(\rightarrow\) contingente.

Este criterio ahorra tiempo en prácticas y evita decisiones intuitivas sin respaldo. En lógica, la clasificación se demuestra; no se supone.


## Ejemplos de clasificación

La expresión “hoy llueve o no llueve” tiene forma \(p \lor \neg p\). Es tautológica porque cubre exhaustivamente ambos casos posibles.

La expresión “la puerta está abierta y no está abierta al mismo tiempo” tiene forma \(p \land \neg p\). Es contradictoria porque exige algo y su negación de manera simultánea.

La expresión “si estudio, apruebo” con forma \(p \rightarrow q\) es contingente. A veces será verdadera y existe al menos una situación donde será falsa.



## Errores frecuentes al construir tablas

Un error frecuente es usar menos renglones de los necesarios. Cuando esto ocurre, la tabla deja fuera casos posibles y la clasificación pierde validez.

Otro error común es calcular directamente la fórmula completa sin columnas intermedias. Esto suele provocar confusión, sobre todo en expresiones con negaciones o agrupaciones.

También es frecuente invertir el comportamiento del condicional. Debe recordarse que \(p \rightarrow q\) solo es falso en el caso \(V \rightarrow F\).

# Analogía con pruebas de sistemas

Una tabla de verdad se parece a una matriz exhaustiva de escenarios. Cada renglón representa una combinación distinta de estados de entrada.

Clasificar una fórmula equivale a identificar el comportamiento global de una especificación:

- Tautología: la condición se cumple en todos los escenarios.
- Contradicción: la condición no se cumple en ninguno.
- Contingente: depende del escenario.

Verificar consecuencia lógica equivale a revisar si existe un escenario válido para las premisas en el que la salida esperada no ocurra. Ese escenario sería el contraejemplo.


# Consecuencia lógica

La consecuencia lógica estudia si una conclusión se sigue necesariamente de una o varias premisas. En términos intuitivos, se pregunta si hay alguna situación donde todas las premisas sean verdaderas y la conclusión sea falsa.

Si esa situación existe, entonces la conclusión no se sigue lógicamente. Si no existe, entonces sí hay consecuencia lógica.


## Contraejemplo

Un contraejemplo es un renglón de la tabla donde:

- Todas las premisas valen V.
- La conclusión vale F.

Ese único renglón basta para destruir la consecuencia lógica. Es parecido a encontrar un caso de prueba que rompe una afirmación general sobre un sistema: un solo caso contrario es suficiente para mostrar que la relación no era necesaria.


# Método con tablas de verdad para verificar consecuencia

Para decidir si
\[
P_1, P_2, \dots, P_n \models C
\]
se construye una sola tabla con todas las proposiciones involucradas. Después se agregan columnas para cada premisa y una para la conclusión.

Al final se revisan únicamente los renglones donde todas las premisas son verdaderas:

- Si en alguno de esos renglones la conclusión es falsa, no hay consecuencia lógica.
- Si en todos esos renglones la conclusión es verdadera, sí hay consecuencia lógica.


## Ejemplo 4: sí hay consecuencia lógica

Se analizan las premisas:

- \(p \rightarrow q\)
- \(p\)

y la conclusión:

- \(q\)


| p | q | \(p \rightarrow q\) | Premisa \(p\) | Conclusión \(q\) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | F |
| F | V | V | F | V |
| F | F | V | F | F |

Ahora se buscan renglones donde ambas premisas sean verdaderas. Eso solo ocurre en el primer renglón, y allí la conclusión también es verdadera.

Por tanto, no hay contraejemplo. Sí existe consecuencia lógica:
\[
p \rightarrow q,\ p \models q
\]



## Lectura intuitiva del ejemplo

En lenguaje cotidiano: “si estudio, apruebo; estudio; por lo tanto, apruebo”. La tabla muestra que no aparece ningún caso donde las dos premisas se mantengan verdaderas y la conclusión falle.

En sistemas: “si el token es válido, el acceso queda autorizado; el token es válido; por lo tanto, el acceso queda autorizado”. Bajo esta estructura lógica, la conclusión se sigue de las premisas.


## Ejemplo 5: no hay consecuencia lógica

Premisas:

- \(p \rightarrow q\)
- \(q\)

Conclusión:

- \(p\)

Tabla:

| p | q | \(p \rightarrow q\) | Premisa \(q\) | Conclusión \(p\) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | F | V |
| F | V | V | V | F |
| F | F | V | F | F |

Se observan los renglones donde ambas premisas son verdaderas. Eso ocurre en el primero y en el tercero.

- En el primer renglón, la conclusión es V.
- En el tercer renglón, la conclusión es F.

El tercer renglón es un contraejemplo. Por tanto, no hay consecuencia lógica:
\[
p \rightarrow q,\ q \not\models p
\]



## Lectura intuitiva del contraejemplo

En lenguaje cotidiano: “si estudio, apruebo; aprobé; por lo tanto, estudié”. Eso no se sigue necesariamente, porque pudo haberse aprobado por otra razón.

En sistemas: “si el servicio principal está activo, entonces hay respuesta; hay respuesta; por lo tanto, el servicio principal está activo”. Tampoco es necesario, porque la respuesta pudo venir de un respaldo, de caché o de una réplica.


## Ejemplo 6: consecuencia con 3 proposiciones

Premisas:

- \(p \land q\)
- \((p \land q) \rightarrow r\)

Conclusión:

- \(r\)

Tabla resumida:

| p | q | r | \(p \land q\) | \((p \land q)\rightarrow r\) | Conclusión \(r\) |
|---|---|---|---|---|---|
| V | V | V | V | V | V |
| V | V | F | V | F | F |
| V | F | V | F | V | V |
| V | F | F | F | V | F |
| F | V | V | F | V | V |
| F | V | F | F | V | F |
| F | F | V | F | V | V |
| F | F | F | F | V | F |

Se buscan renglones donde las dos premisas sean verdaderas al mismo tiempo. Eso solo ocurre en el primer renglón.

En ese renglón, la conclusión \(r\) es verdadera. No existe contraejemplo; por tanto, sí hay consecuencia lógica.




# Práctica

Resolver ejercicios de tablas de verdad requiere disciplina en el orden de trabajo. El objetivo es que el resultado sea verificable por cualquier otra persona.

Secuencia de trabajo:

1. Identificar las letras proposicionales distintas.
2. Calcular el número de renglones.
3. Construir las columnas base de V y F.
4. Agregar columnas intermedias de cada subfórmula.
5. Obtener la columna final.
6. Clasificar la fórmula observando la última columna.
7. Si hay premisas y conclusión, localizar contraejemplos.


# Ejercicio 1

\[
\neg(p \land q)
\]

---

- Es verdadera cuando no se cumplen \(p\) y \(q\) simultáneamente.
- Solo es falsa cuando ambas son verdaderas.
- Por tanto, es contingente.



# Ejercicio 2

\[
(p \rightarrow q)\lor (q \rightarrow p)
\]

---

Al construir la tabla completa se observa que siempre da V. En cualquier combinación, al menos uno de los dos condicionales resulta verdadero.

Por tanto, es tautología.

# Ejercicio 3

\[
(p \lor q)\land \neg(p \lor q)
\]

---

La fórmula exige que una misma subfórmula sea verdadera y falsa al mismo tiempo. Eso hace que todos los renglones terminen en F.

Por tanto, es contradicción.


# Ejercicio 4

\[
(p \lor q)\rightarrow p
\]

---

Primero se construye \(p \lor q\), luego el condicional.

| p | q | \(p \lor q\) | \((p \lor q)\rightarrow p\) |
|---|---|---|---|
| V | V | V | V |
| V | F | V | V |
| F | V | V | F |
| F | F | F | V |

La fórmula es contingente porque mezcla V y F.



# Ejercicio 5

\[
(p \land q)\rightarrow (p \lor q)
\]

---

| p | q | \(p \land q\) | \(p \lor q\) | \((p \land q)\rightarrow (p \lor q)\) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | V | V |
| F | V | F | V | V |
| F | F | F | F | V |

La fórmula siempre resulta verdadera. Por tanto, es una tautología.


# Ejercicio 6

Se revisa si de las premisas
\[
p \lor q,\ \neg p
\]
se sigue la conclusión
\[
q
\]

---


| p | q | \(p \lor q\) | \(\neg p\) | Conclusión \(q\) |
|---|---|---|---|---|
| V | V | V | F | V |
| V | F | V | F | F |
| F | V | V | V | V |
| F | F | F | V | F |

Se buscan renglones donde las dos premisas sean verdaderas. Solo ocurre en el tercer renglón.

En ese renglón, la conclusión es verdadera. No aparece contraejemplo, así que sí hay consecuencia lógica.



## Algunos ejercicios más para resolver

- Construir la tabla de verdad de \((p \land q)\rightarrow q\) y clasificarla.
- Construir la tabla de verdad de \((p \rightarrow q)\land p\) y clasificarla.
- Construir la tabla de verdad de \(\neg(p \lor q)\) y clasificarla.
- Decidir si \(p \rightarrow q,\ \neg q \models \neg p\).
- Decidir si \(p \lor q,\ q \models p\).
- Decidir si \(p \land q \models p\).

