# Práctica de tablas de verdad y clasificación de fórmulas

## Objetivo de la práctica

Esta práctica tiene ejercicios para construir tablas de verdad, clasificar fórmulas y revisar si una conclusión realmente se sigue de unas premisas.

Una tabla de verdad es un arreglo sistemático de casos posibles para las proposiciones que aparecen en una fórmula. Con esta práctica, los alumnos serán capaces de construir tablas completas de fórmulas de dos y tres proposiciones, clasificar fórmulas como tautología, contradicción o contingente, y detectar contraejemplos cuando una conclusión no se siga de las premisas.

Una tautología es una fórmula que resulta verdadera en todos los renglones; una contradicción resulta falsa en todos; una contingente mezcla renglones verdaderos y falsos. Esta clasificación funciona como una prueba de estrés: una tautología se comporta como una condición que nunca falla, una contradicción como una condición imposible, y una contingente como una regla cuyo resultado depende del contexto.

## Recordatorio conceptual mínimo

Una fórmula bien formada es una expresión construida correctamente con proposiciones y conectivos. En esta práctica se usarán los conectivos básicos ya estudiados: negación $\neg$, conjunción $\land$, disyunción $\lor$, condicional $\to$ y bicondicional $\leftrightarrow$.

Para construir una tabla de verdad de manera sistemática se procede por columnas. Primero se listan todas las combinaciones de valores de verdad de las proposiciones simples; después se calculan las subfórmulas; al final se obtiene la columna de la fórmula completa, que es la que permite clasificarla o decidir si hay consecuencia lógica.

## Convenciones de trabajo

Una tabla completa de dos proposiciones tiene 4 renglones, porque hay cuatro combinaciones posibles de verdad. Una tabla completa de tres proposiciones tiene 8 renglones, porque cada nueva proposición duplica el número de casos.

Se usarán las letras **V** y **F** para representar verdadero y falso. Cuando se revise una consecuencia lógica, la atención se pondrá en los renglones donde todas las premisas sean verdaderas; si en alguno de esos renglones la conclusión es falsa, aparece un contraejemplo y la consecuencia lógica no se cumple.

## Método de construcción paso a paso

Una construcción sistemática evita errores y funciona como un procedimiento de laboratorio. El orden recomendado es el siguiente:

1. Identificar las proposiciones simples de la fórmula.
2. Determinar cuántos renglones tendrá la tabla: 4 para dos proposiciones, 8 para tres.
3. Llenar las columnas base con el patrón de valores de verdad.
4. Construir columnas intermedias para cada subfórmula entre paréntesis.
5. Completar la columna final de la fórmula.
6. Clasificar o analizar la relación entre premisas y conclusión.

### Patrón base para dos proposiciones

| p | q |
|---|---|
| V | V |
| V | F |
| F | V |
| F | F |

### Patrón base para tres proposiciones

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

## Ejemplo guiado 1: tabla de verdad y clasificación

Una conjunción afirma que dos condiciones se cumplen al mismo tiempo. Si en un sistema de acceso se define que “el acceso se concede si la credencial es válida y la huella coincide”, la conjunción solo será verdadera cuando ambas partes sean verdaderas.

**Fórmula:** $p \land q$

**Interpretación tecnológica:**  
- $p$: la credencial es válida.  
- $q$: la huella coincide.

| p | q | $p \land q$ |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

La fórmula no es siempre verdadera ni siempre falsa. Por tanto, $p \land q$ es una fórmula contingente.

## Ejemplo guiado 2: fórmula tautológica

Una tautología se comporta como una verificación que siempre sale bien sin importar el escenario. La fórmula $p \lor \neg p$ expresa que una proposición o bien es verdadera o bien no lo es; por eso cubre todos los casos posibles.

**Fórmula:** $p \lor \neg p$

| p | $\neg p$ | $p \lor \neg p$ |
|---|---|---|
| V | F | V |
| F | V | V |

Como la columna final contiene solo valores verdaderos, esta fórmula es una tautología.

## Ejemplo guiado 3: fórmula contradictoria

Una contradicción es una condición imposible, como pedir que un servicio esté disponible y no disponible al mismo tiempo en el mismo instante. La fórmula $p \land \neg p$ nunca puede resultar verdadera.

**Fórmula:** $p \land \neg p$

| p | $\neg p$ | $p \land \neg p$ |
|---|---|---|
| V | F | F |
| F | V | F |

Como la columna final contiene solo valores falsos, esta fórmula es una contradicción.

## Ejemplo guiado 4: consecuencia lógica con tabla de verdad

Una conclusión es consecuencia lógica de unas premisas cuando no existe ningún caso en el que todas las premisas sean verdaderas y la conclusión sea falsa. En términos de revisión de redes, sería como afirmar que, si todas las condiciones operativas declaradas se cumplen, entonces el resultado esperado también debe cumplirse sin excepción.

**Premisas:**  
1. $p \to q$  
2. $p$

**Conclusión:**  
- $q$

**Interpretación cotidiana:**  
- $p$: está lloviendo.  
- $q$: la calle se moja.

| p | q | $p \to q$ | Premisas verdaderas al mismo tiempo | Conclusión $q$ |
|---|---|---|---|---|
| V | V | V | Sí | V |
| V | F | F | No | F |
| F | V | V | No | V |
| F | F | V | No | F |

Solo interesa el renglón donde ambas premisas son verdaderas al mismo tiempo. En ese renglón, la conclusión también es verdadera; por eso sí hay consecuencia lógica.

## Ejemplo guiado 5: detección de contraejemplo

Un contraejemplo es un renglón de la tabla donde todas las premisas son verdaderas y la conclusión es falsa. Encontrar un solo contraejemplo basta para negar la consecuencia lógica, igual que basta una sola prueba fallida para mostrar que un criterio no garantiza el resultado prometido.

**Premisas:**  
1. $p \lor q$

**Conclusión:**  
- $p$

**Interpretación tecnológica:**  
- $p$: el servidor principal está disponible.  
- $q$: el servidor de respaldo está disponible.

| p | q | $p \lor q$ | Conclusión $p$ |
|---|---|---|---|
| V | V | V | V |
| V | F | V | V |
| F | V | V | F |
| F | F | F | F |

En el renglón $p=F$, $q=V$, la premisa es verdadera y la conclusión es falsa. Ese renglón es un contraejemplo; por tanto, la conclusión no se sigue de la premisa.

## Sección I: ejercicios de construcción de tablas de verdad

Una tabla de verdad completa exige que no se omita ningún caso posible. En este bloque se practica la mecánica de construcción, como quien revisa todas las rutas de ejecución de un proceso antes de afirmar que entiende su comportamiento.


Construir la tabla completa de cada fórmula y completar todas las columnas intermedias.

1. $\neg p \lor q$
2. $(p \to q) \land p$
3. $(p \lor q) \to p$
4. $(p \land \neg q) \lor q$
5. $(p \to q) \lor r$
6. $(p \leftrightarrow q) \to r$
7. $p \to (q \to r)$
8. $(p \land r) \lor (q \land \neg r)$

## Sección II: ejercicios de clasificación de fórmulas

Clasificar una fórmula consiste en leer su columna final como si se leyera un diagnóstico. Si todo sale verdadero, la fórmula es tautología; si todo sale falso, es contradicción; si el resultado cambia según el caso, es contingente.

**Instrucción general:** para cada fórmula, construir la tabla de verdad completa y escribir al final una de estas tres etiquetas: tautología, contradicción o contingente.

1. $(p \to q) \lor (q \to p)$
2. $(p \land q) \land \neg p$
3. $(p \to q) \land (q \to p)$
4. $(p \lor q) \to (q \lor p)$

### Con contexto aplicado

1. $(a \land b) \to a$  
   - $a$: el usuario ingresó credenciales válidas.  
   - $b$: el segundo factor fue aprobado.
2. $d \land \neg d$  
   - $d$: el servicio está disponible.
3. $n \lor \neg n$  
   - $n$: la red responde al ping.
4. $(s \to t) \land s$  
   - $s$: el sensor envía señal.  
   - $t$: el panel recibe datos.

## Sección III: ejercicios de consecuencia lógica

La consecuencia lógica se revisa observando premisas y conclusión en la misma tabla. En esta sección no basta con llenar columnas: también debe identificarse si existe o no al menos un contraejemplo.

**Instrucción general:** construir la tabla de verdad completa y responder dos cosas:  
1. ¿La conclusión se sigue de las premisas?  
2. Si no se sigue, ¿cuál es un contraejemplo?

---

1. Premisas: $(p \to q)$, $(q \to r)$, $p$  
   Conclusión: $r$
2. Premisas: $(p \land q) \to r$, $p \land q$  
   Conclusión: $r$
3. Premisas: $p \to q$, $r$  
   Conclusión: $q$
4. Premisas: $(p \lor q) \to r$, $p$  
   Conclusión: $r$


### Con aplicaciones

1. Premisas:  
   - $a \to b$  
   - $a$  
   Conclusión: $b$  
   Interpretación: si el intento de autenticación es válido, entonces la sesión se habilita; el intento es válido; por tanto, la sesión se habilita.

2. Premisas:  
   - $m \to n$  
   - $n$  
   Conclusión: $m$  
   Interpretación: si hay mantenimiento, entonces el servicio se detiene; el servicio se detiene; por tanto, hay mantenimiento.

3. Premisas:  
   - $r \lor s$  
   - $\neg r$  
   Conclusión: $s$  
   Interpretación: o responde el enlace principal o responde el enlace alterno; no responde el enlace principal; por tanto, responde el alterno.

4. Premisas:  
   - $(d \land e) \to f$  
   - $d \land e$  
   Conclusión: $f$  
   Interpretación: si hay energía y conectividad, entonces la estación transmite; hay energía y conectividad; por tanto, la estación transmite.

