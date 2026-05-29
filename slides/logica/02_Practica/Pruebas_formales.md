# Práctica de pruebas formales y modelado en lógica de proposiciones

Esta práctica se centra en construir pruebas formales cortas y en modelar pequeños problemas con lógica de proposiciones, usando únicamente las reglas de inferencia vistas en clase.  
El material está pensado para trabajo autónomo en dos horas, como hoja entregable para calificación.

***

## Objetivo general de la práctica

Una prueba formal es una secuencia de fórmulas numeradas, donde cada línea es una premisa o se obtiene aplicando una regla de inferencia correcta a fórmulas de líneas anteriores.  
El objetivo es practicar el uso ordenado de estas reglas para derivar conclusiones a partir de premisas en ejercicios de 4 a 6 pasos, además de modelar un problema sencillo desde lenguaje natural.

***

## Instrucciones de trabajo

Una proposición es un enunciado que puede ser verdadero o falso; las fórmulas se construyen combinando proposiciones con conectivos como negación, conjunción, disyunción, condicional y bicondicional.  
En esta práctica se usan reglas de inferencia básicas junto con equivalencias lógicas estudiadas en sesiones previas.

- Escribir claramente y limpiamente las respuestas.  
- Resolver todos ejercicios de prueba formal de los que aparecen más adelante.
- Numerar todas las líneas de cada prueba e indicar la justificación (Premisa, MP, MT, SH, SD, Ad, Simp, Conj, DN, Trans, DeMorgan, etc.).

***

## Recordatorio: reglas de inferencia permitidas

Una regla de inferencia es un patrón que preserva la verdad: si las fórmulas de la parte superior del patrón son verdaderas, la fórmula de la parte inferior también lo es.  
En esta práctica solo se usan las reglas listadas a continuación, que coinciden con las vistas en la sesión de reglas de inferencia y en la práctica de referencia.

| Nombre                    | Hipótesis                                    | Conclusión                    |
|---------------------------|----------------------------------------------|-------------------------------|
| Modus Ponens (MP)         |$p \rightarrow q$,$p$                  |$q$                        |
| Modus Tollens (MT)        |$p \rightarrow q$,$\neg q$             |$\neg p$                   |
| Silogismo hipotético (SH) |$p \rightarrow q$,$q \rightarrow r$    |$p \rightarrow r$          |
| Silogismo disyuntivo (SD) |$p \lor q$,$\neg p$                    |$q$                        |
| Adición (Ad)              |$p$                                       |$p \lor q$                 |
| Simplificación (Simp)     |$p \land q$                               |$p$, $q$                |
| Conjunción (Conj)         |$p$,$q$                                |$p \land q$                |
| Doble negación (DN)       |$p \equiv \neg\neg p$                      |$p \equiv \neg\neg p$       |
| Transposición (Trans)     |$p \rightarrow q$                         |$\neg q \rightarrow \neg p$|
| De Morgan (DM)            |$\neg(p \land q) \equiv \neg p \lor \neg q$| forma equivalente.            |
| De Morgan (DM)            |$\neg(p \lor q) \equiv \neg p \land \neg q$| forma equivalente.            |

***

## Recordatorio: leyes de simplificación por equivalencias

Una equivalencia lógica relaciona dos fórmulas con la misma tabla de verdad, de manera que cualquiera puede sustituir a la otra sin cambiar el significado de la condición.  
Las siguientes leyes se usan para simplificar fórmulas y para transformar condicionales y bicondicionales en expresiones con$\land$,$\lor$y$\neg$, sobre todo al preparar pruebas o formas normales.

| Ley                                     | Esquema equivalente                                                      |
|-----------------------------------------|--------------------------------------------------------------------------|
| Idempotencia ($\land$)                |$p \land p \equiv p$                                                  |
| Idempotencia ($\lor$)                 |$p \lor p \equiv p$                                                   |
| Complemento (contradicción)             |$p \land \neg p \equiv F$                                             |
| Complemento (tautología)                |$p \lor \neg p \equiv V$                                              |
| Identidad ($\land$)                   |$p \land V \equiv p$                                                  |
| Identidad ($\lor$)                    |$p \lor F \equiv p$                                                   |
| Dominación ($\land$)                  |$p \land F \equiv F$                                                  |
| Dominación ($\lor$)                   |$p \lor V \equiv V$                                                   |
| Absorción ($\land$)                   |$p \land (p \lor q) \equiv p$                                         |
| Absorción ($\lor$)                    |$p \lor (p \land q) \equiv p$                                         |
| Conmutatividad ($\land$)              |$p \land q \equiv q \land p$                                          |
| Conmutatividad ($\lor$)               |$p \lor q \equiv q \lor p$                                            |
| Asociatividad ($\land$)               |$(p \land q) \land r \equiv p \land (q \land r)$                      |
| Asociatividad ($\lor$)                |$(p \lor q) \lor r \equiv p \lor (q \lor r)$                          |
| Distributiva ($\land$sobre$\lor$) |$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$              |
| Distributiva ($\lor$sobre$\land$) |$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$               |
| De Morgan ($\land$)                   |$\neg(p \land q) \equiv \neg p \lor \neg q$                           |
| De Morgan ($\lor$)                    |$\neg(p \lor q) \equiv \neg p \land \neg q$                           |
| Doble negación                          |$\neg\neg p \equiv p$                                                 |
| Condicional–disyunción                  |$p \rightarrow q \equiv \neg p \lor q$                                |
| Bicondicional (condicionales)           |$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$|

***

## Ejemplo resuelto de referencia (en tabla)

Un ejemplo resuelto sirve como guía del tipo de prueba que se espera en la hoja: premisas numeradas, cada línea justificada y longitud moderada.  
El contexto mezcla un escenario de sistemas con razonamiento por encadenamiento y descarte, muy similar a los ejercicios intermedios de la práctica adjunta.

### Enunciado

En un sistema de respaldo:

- Si el respaldo automático está habilitado, los datos se replican cada hora.  
- Si los datos se replican cada hora, entonces el historial de cambios se mantiene consistente.  
- El historial de cambios no se mantiene consistente.

¿Qué se puede concluir sobre el respaldo automático?

### Variables

- $h$: el respaldo automático está habilitado.  
- $r$: los datos se replican cada hora.  
- $c$: el historial de cambios se mantiene consistente.

### Premisas formales

1. $h \rightarrow r$ 
2. $r \rightarrow c$ 
3. $\neg c$

### Conclusión a demostrar

$\neg h$

### Prueba formal en tabla

| Paso | Fórmula             | Justificación |
|------|---------------------|---------------|
| 1    |$h \rightarrow r$| Premisa       |
| 2    |$r \rightarrow c$| Premisa       |
| 3    |$\neg c$         | Premisa       |
| 4    |$h \rightarrow c$| SH, 1 y 2     |
| 5    |$\neg h$         | MT, 4 y 3     |

La lectura en lenguaje natural: si el respaldo automático estuviera habilitado, garantizaría que los datos se replican cada hora y, por lo tanto, que el historial es consistente; como el historial no es consistente, se concluye que el respaldo automático no estaba habilitado.

***

## Hoja de ejercicios de prueba formal

Los siguientes ejercicios son de nivel básico a intermedio; cada uno requiere entre 4 y 6 pasos usando solo las reglas permitidas.  
Se sugiere escoger al menos dos ejercicios de esta sección para desarrollarlos como parte de la entrega.

***

### Ejercicio 1 — Cadena condicional con conclusión compuesta

Contexto  
Si el servidor de aplicación está disponible, entonces las peticiones se atienden; si las peticiones se atienden, entonces el registro de actividad se actualiza; el servidor de aplicación está disponible.

Variables  

- $s$: el servidor de aplicación está disponible.  
- $p$: las peticiones se atienden.  
- $r$: el registro de actividad se actualiza.

Premisas  

1. $s \rightarrow p$ 
2. $p \rightarrow r$ 
3. $s$

Conclusión  

$p \land r$

***

### Ejercicio 2 — Disyunción y descarte en monitoreo

Contexto  
Si la CPU está sobrecargada o la memoria está sobrecargada, entonces se genera una alerta; si se genera una alerta, entonces se envía un correo al administrador; no se envió correo al administrador; hay sobrecarga en CPU o hay sobrecarga en memoria.

Variables  

- $c$: la CPU está sobrecargada.  
- $m$: la memoria está sobrecargada.  
- $a$: se genera una alerta.  
- $e$: se envía un correo al administrador.

Premisas  

1. $(c \lor m) \rightarrow a$ 
2. $a \rightarrow e$ 
3. $\neg e$ 
4. $c \lor m$

Conclusión  

$\neg (c \lor m)$

***

### Ejercicio 3 — Conjunción, simplificación y nueva conjunción

Contexto  
El sistema está en modo seguro y el registro de auditoría está activo; si el registro de auditoría está activo, se guardan eventos críticos; si el sistema está en modo seguro, se bloquean accesos no autorizados.

Variables  

- $s$: el sistema está en modo seguro.  
- $a$: el registro de auditoría está activo.  
- $g$: se guardan eventos críticos.  
- $b$: se bloquean accesos no autorizados.

Premisas  

1. $s \land a$ 
2. $a \rightarrow g$ 
3. $s \rightarrow b$

Conclusión  

$g \land b$

***

### Ejercicio 4 — De Morgan y modus tollens en reservas

Contexto  
Si el sistema no está en mantenimiento y hay conexión a la red, entonces se puede crear una reserva; si se puede crear una reserva, se envía un comprobante; no se envió comprobante.

Variables  

- $m$: el sistema está en mantenimiento.  
- $n$: hay conexión a la red.  
- $r$: se puede crear una reserva.  
- $c$: se envía un comprobante.

Premisas  

1. $(\neg m \land n) \rightarrow r$ 
2. $r \rightarrow c$ 
3. $\neg c$

Conclusión  

$m \lor \neg n$

***

## Problema de modelado con prueba formal

Modelar es traducir un problema narrado a fórmulas de lógica de proposiciones y luego derivar una conclusión usando reglas de inferencia.  
Este problema debe incluirse como parte de la entrega, con la estructura completa: variables, traducción, prueba y conclusión en lenguaje natural.

### Enunciado

Si Ana lleva credencial y el sistema de acceso está activo, entonces entra al laboratorio; si Ana entra al laboratorio, entonces enciende el equipo; Ana no encendió el equipo.

Variables  

- Aquí pones tus variables

Premisas formales  

1. Aquí pones tus premisas

Conclusión a demostrar  

No es cierto que Ana lleva credencial y el sistema de acceso está activo.


La conclusión debe acompañarse con una frase en lenguaje natural, por ejemplo: “no se puede afirmar que Ana tuviera credencial y que el sistema de acceso estuviera activo al mismo tiempo”.

***

## Verificación antes de entregar

La verificación final de la hoja es análoga a revisar un programa: cada línea de código debe tener sentido y cada transición debe estar justificada.

- La última línea de cada prueba coincide exactamente con la conclusión indicada.  
- Cada línea tiene una justificación clara (Premisa o nombre de regla con números de línea).  
- No se utilizan reglas fuera de la tabla de reglas permitidas.   
- El problema de modelado separa bien variables, premisas formales, prueba y conclusión en lenguaje natural.