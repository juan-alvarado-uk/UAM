## Práctica de Lógica de Proposiciones

## Objetivo de la práctica

Esta práctica consolida los conocimientos sobre proposiciones y conectivos lógicos. El objetivo es desarrollar habilidades para: 

1. Distinguir qué enunciados son proposiciones
2. Traducir enunciados en lenguaje natural a fórmulas de lógica de proposiciones
3. Identificar el conectivo principal de una fórmula

***

## Sección I: Reconocimiento de Proposiciones

### Definición

Una **proposición** es un enunciado declarativo que puede ser calificado como verdadero o falso, pero no ambos simultáneamente. Las proposiciones transmiten información que puede evaluarse en términos de su valor de verdad. 

### Características de las proposiciones

- Expresan hechos, afirmaciones o negaciones concretas
- Tienen exactamente un valor de verdad: verdadero (V) o falso (F)
- No pueden ser preguntas, órdenes, exclamaciones ni expresiones ambiguas

***

### Ejemplos demostrativos

**Enunciados que SÍ son proposiciones:**

1. "El sistema operativo Linux es de código abierto" → Es proposición (puede verificarse como verdadera)
2. "7 es un número primo" → Es proposición (tiene valor de verdad definido) 
3. "La autenticación de dos factores mejora la seguridad" → Es proposición (afirmación verificable)
4. "El protocolo HTTP opera en el puerto 80" → Es proposición (hecho técnico verificable)

***

**Enunciados que NO son proposiciones:**

1. "¿Qué es una base de datos?" → No es proposición (es una pregunta)
2. "Instala el antivirus ahora" → No es proposición (es una orden)
3. "¡Qué rápida es esta conexión!" → No es proposición (es una exclamación)
4. "x + 5 > 10" → No es proposición simple (depende del valor de x; es predicado)
5. "Este programa es bueno" → No es proposición clara (ambigüedad en "bueno")

***

### Ejercicios Parte I.A: Identificación de proposiciones

**Instrucciones:** Indica si cada enunciado es proposición (P) o no es proposición (NP). Justifica brevemente tu respuesta.

1. "Python es un lenguaje de programación interpretado"
2. "¿El algoritmo de ordenamiento burbuja tiene complejidad O(n²)?"
3. "Configura el enrutador con la dirección IP 192.168.1.1"
4. "La memoria RAM es volátil"
5. "Un servidor web debería tener alta disponibilidad"
6. "2 + 2 = 5"
7. "¡Cuidado con el desbordamiento de buffer!"
8. "Si n es par, entonces n es divisible por 2"
9. "Todos los virus informáticos son maliciosos"
10. "x es mayor que y"

***

### Ejercicios Parte I.B: Construcción de proposiciones

**Instrucciones:** Escribe 5 proposiciones relacionadas con Tecnologías y Sistemas de Información. Verifica que cada enunciado pueda ser verdadero o falso. 

**Ejemplo:** "Un sistema de archivos distribuido permite acceder a datos desde múltiples nodos de red"

**Espacios para tus proposiciones:**

- 1 _______________________________________________
- 2 _______________________________________________
- 3 _______________________________________________
- 4 _______________________________________________
- 5 _______________________________________________


## Sección II: Conectivos Lógicos y Formalización

### Definición de conectivos lógicos

Los **conectivos lógicos** son operadores que permiten construir proposiciones compuestas a partir de proposiciones simples. Cada conectivo tiene reglas específicas para determinar el valor de verdad de la proposición resultante. 

***

### Conectivos básicos

| Conectivo | Símbolo | Nombre | Ejemplo en lenguaje natural |
|-----------|---------|--------|----------------------------|
| Negación | ¬ | "no", "no es cierto que" | "No está lloviendo" |
| Conjunción | ∧ | "y", "pero", "además" | "Llueve y hace frío" |
| Disyunción | ∨ | "o" | "Estudiamos o descansamos" |
| Condicional | → | "si...entonces", "implica" | "Si estudias, apruebas" |
| Bicondicional | ↔ | "si y solo si", "equivale a" | "Apruebas si y solo si estudias" |

***

### Ejemplos de formalización

**Definamos las variables proposicionales:**
- p: "El usuario está autenticado"
- q: "El sistema permite el acceso"
- r: "Hay registro en el log"

***

**Ejemplos de traducción:**

1. "El usuario no está autenticado"  
   **Formalización:** ¬p

2. "El usuario está autenticado y el sistema permite el acceso"  
   **Formalización:** p ∧ q 

3. "Si el usuario está autenticado, entonces el sistema permite el acceso"  
   **Formalización:** p → q

4. "El sistema permite el acceso si y solo si el usuario está autenticado"  
   **Formalización:** q ↔ p

5. "El usuario está autenticado o hay registro en el log"  
   **Formalización:** p ∨ r

6. "No es cierto que el usuario esté autenticado y el sistema permita el acceso"  
   **Formalización:** ¬(p ∧ q) 

7. "Si el usuario no está autenticado, entonces el sistema no permite el acceso"  
   **Formalización:** ¬p → ¬q 


### Ejemplo de la vida cotidiana

**Situación:** En una cafetería

- p: "Tengo dinero suficiente"
- q: "Hay café disponible"  
- r: "Compro café"

**Enunciados:**

1. "Compro café si tengo dinero suficiente y hay café disponible"  
   - (p ∧ q) → r

2. "Si no hay café disponible, entonces no compro café"  
   - ¬q → ¬r

***

### Ejercicios Parte II.A: Traducción de lenguaje natural a fórmulas

**Variables proposicionales para sistemas de información:**
- p: "El servidor está activo"
- q: "La red está disponible"
- r: "Los usuarios pueden conectarse"
- s: "Se registra actividad en el sistema"

***

**Instrucciones:** Traduce cada enunciado a una fórmula lógica usando las variables proporcionadas. 

1. "El servidor está activo y la red está disponible"

2. "Si el servidor está activo, entonces los usuarios pueden conectarse"

3. "Los usuarios pueden conectarse si y solo si el servidor está activo y la red está disponible"

4. "No es cierto que el servidor esté activo y la red esté disponible"

5. "Si la red no está disponible, entonces los usuarios no pueden conectarse"

6. "El servidor está activo o se registra actividad en el sistema"

7. "Si el servidor está activo y la red está disponible, entonces los usuarios pueden conectarse y se registra actividad"

8. "No es cierto que si el servidor está activo, entonces los usuarios pueden conectarse"

9. "El servidor está activo pero los usuarios no pueden conectarse"

10. "Ni el servidor está activo ni la red está disponible"


### Ejercicios Parte II.B: Formalización con contexto de redes

**Define tus propias variables proposicionales basadas en el siguiente contexto:**

"En una arquitectura de red, el enrutador principal gestiona el tráfico. Si el enrutador está operativo y no hay congestión en la red, entonces los paquetes se transmiten correctamente. Los paquetes se pierden si hay congestión o el enrutador presenta errores."

***

**Instrucciones:**
1. Identifica al menos 4 proposiciones simples
2. Asigna variables (p, q, r, s...)
3. Formaliza las dos afirmaciones principales del párrafo

**Tu solución:**

Variables:
- p: _______________________________________________
- q: _______________________________________________
- r: _______________________________________________
- s: _______________________________________________

Formalizaciones:
- 1 _______________________________________________
- 2 _______________________________________________


## Sección III: Identificación del Conectivo Principal

### Definición

El **conectivo principal** de una fórmula es el último operador que se aplica al evaluar la expresión completa. Determina la estructura fundamental de la proposición compuesta. 

### Reglas de jerarquía y precedencia

La jerarquía de operadores (de menor a mayor precedencia):
1. Bicondicional (↔)
2. Condicional (→)
3. Disyunción (∨)
4. Conjunción (∧)
5. Negación (¬)

**Nota importante:** Los paréntesis alteran la precedencia natural y deben respetarse siempre.

### Estrategia para identificar el conectivo principal

1. Localiza el conectivo que NO está dentro de paréntesis
2. Si hay varios, el de menor precedencia es el principal
3. Si hay varios del mismo tipo al mismo nivel, considera el último (de derecha a izquierda para →, de izquierda a derecha para los demás)

***

### Ejemplos demostrativos

**Ejemplo 1:** p ∧ q → r

**Análisis:**
- Tenemos conjunción (∧) y condicional (→)
- El condicional tiene menor precedencia
- **Conectivo principal:** → (condicional)
- **Lectura:** "Si (p y q), entonces r"

***

**Ejemplo 2:** ¬p ∨ (q ∧ r)

**Análisis:**
- Tenemos negación (¬), disyunción (∨) y conjunción (∧)
- La conjunción está dentro de paréntesis, se evalúa primero
- Entre ¬p y ∨, la disyunción es el conectivo principal
- **Conectivo principal:** ∨ (disyunción)
- **Lectura:** "(no p) o (q y r)"

***

**Ejemplo 3:** (p → q) ∧ (r → s)

**Análisis:**
- Ambos condicionales están dentro de paréntesis
- La conjunción conecta las dos subexpresiones
- **Conectivo principal:** ∧ (conjunción)
- **Lectura:** "(Si p entonces q) y (si r entonces s)"

***

**Ejemplo 4:** ¬(p ∨ q) → r

**Análisis:**
- La disyunción está dentro de paréntesis con negación
- El condicional conecta ¬(p ∨ q) con r
- **Conectivo principal:** → (condicional)
- **Lectura:** "Si no es cierto que (p o q), entonces r"

***

**Ejemplo 5:** p ↔ (q → r)

**Análisis:**
- El condicional está dentro de paréntesis
- El bicondicional conecta p con toda la expresión (q → r)
- **Conectivo principal:** ↔ (bicondicional)
- **Lectura:** "p si y solo si (si q entonces r)"

***

### Ejercicios Parte III.A: Identificar conectivo principal

**Instrucciones:** Para cada fórmula, identifica el conectivo principal y justifica brevemente tu respuesta.

1. p ∨ q ∧ r

2. (p ∨ q) ∧ r

3. ¬p → q

4. p → (q ∨ r)

5. (p → q) ∨ (r → s)

6. ¬(p ∧ q) ∨ r

7. p ∧ q → r ∨ s

8. (p ↔ q) → r

9. p → q → r

10. ¬p ∨ ¬q ∧ r

***

### Ejercicios Parte III.B: Análisis completo de fórmulas

**Instrucciones:** Para cada fórmula, realiza lo siguiente:
1. Identifica el conectivo principal
2. Identifica las subexpresiones que conecta
3. Escribe una lectura en lenguaje natural aproximada

***

**Ejemplo resuelto:**

**Fórmula:** (p ∧ q) → (r ∨ s)

1. **Conectivo principal:** → (condicional)
2. **Subexpresiones:** 
   - Antecedente: (p ∧ q)
   - Consecuente: (r ∨ s)
3. **Lectura:** "Si p y q, entonces r o s"

***

**Ejercicio 1:**

**Fórmula:** ¬p ∨ (q → r)

1. Conectivo principal: _______________
2. Subexpresiones: _______________
3. Lectura: _______________

**Ejercicio 2:**

**Fórmula:** (p ∨ q) ↔ (¬r ∧ s)

1. Conectivo principal: _______________
2. Subexpresiones: _______________
3. Lectura: _______________


**Ejercicio 3:**

**Fórmula:** p → q ∧ ¬r

1. Conectivo principal: _______________
2. Subexpresiones: _______________
3. Lectura: _______________

**Ejercicio 4:**

**Fórmula:** ¬(p → q) ∨ (r ∧ s)

1. Conectivo principal: _______________
2. Subexpresiones: _______________
3. Lectura: _______________

***

## Sección IV: Ejercicios Integrados

### Parte IV.A: Análisis completo de proposiciones

**Contexto:** Sistema de control de acceso universitario

Las siguientes variables representan condiciones del sistema:
- a: "El estudiante tiene credencial vigente"
- b: "El estudiante está registrado en el sistema"
- c: "La puerta se abre"
- d: "Se registra el acceso en el log"

***

**Instrucciones:** Para cada enunciado:
1. Determina si es una proposición válida (P/NP)
2. Si es proposición, formalízala
3. Identifica el conectivo principal de tu formalización

***

**Ejercicio 1:**
"Si el estudiante tiene credencial vigente y está registrado, entonces la puerta se abre"

1. ¿Es proposición? _______________
2. Formalización: _______________
3. Conectivo principal: _______________

**Ejercicio 2:**
"¿La puerta se abre cuando el estudiante tiene credencial vigente?"

1. ¿Es proposición? _______________
2. Formalización: _______________
3. Conectivo principal: _______________


**Ejercicio 3:**
"Se registra el acceso en el log si y solo si la puerta se abre"

1. ¿Es proposición? _______________
2. Formalización: _______________
3. Conectivo principal: _______________

**Ejercicio 4:**
"No es cierto que el estudiante tenga credencial vigente pero no esté registrado"

1. ¿Es proposición? _______________
2. Formalización: _______________
3. Conectivo principal: _______________

***

### Parte IV.B: Ejercicio Integrado de Formalización

**Contexto:** Proceso de respaldo de base de datos

Lee el siguiente escenario y responde:

"El sistema realiza respaldos automáticos cada noche. Un respaldo es exitoso si el servidor de almacenamiento está disponible y hay espacio suficiente en disco. Si el respaldo no es exitoso, se envía una alerta al administrador. El administrador puede iniciar un respaldo manual cuando lo considere necesario."

***

**Instrucciones:**

1. Identifica al menos 5 enunciados que sean proposiciones

2. Define variables proposicionales para cada una

3. Formaliza la siguiente afirmación del texto:
   "Un respaldo es exitoso si el servidor de almacenamiento está disponible y hay espacio suficiente en disco"

4. Formaliza esta otra afirmación:
   "Si el respaldo no es exitoso, se envía una alerta al administrador"

5. Identifica el conectivo principal de cada formalización anterior


## Sección V: Ejercicios Adicionales de Consolidación

### Parte V.A: Verdadero o Falso

**Instrucciones:** Indica si cada afirmación es verdadera (V) o falsa (F). Justifica las falsas brevemente.

1. "El algoritmo de búsqueda es eficiente" es una proposición válida porque puede evaluarse como verdadera o falsa.

2. En la fórmula p ∧ (q ∨ r), el conectivo principal es la conjunción (∧).

3. Toda pregunta puede convertirse en proposición reformulándola como afirmación.

4. La negación (¬) siempre tiene la mayor precedencia entre todos los conectivos.

5. En (p → q) ↔ (¬q → ¬p), el conectivo principal es el condicional (→).

6. "x + y = 10" es una proposición porque tiene un valor de verdad definido.

7. La fórmula ¬p ∨ q → r tiene como conectivo principal el condicional (→).

8. Dos fórmulas con el mismo conectivo principal siempre son equivalentes.

***

### Parte V.B: Corrección de errores

**Instrucciones:** Las siguientes formalizaciones contienen errores. Identifica el error y proporciona la formalización correcta.

**Variables:**
- p: "El firewall está activo"
- q: "Hay intentos de intrusión"
- r: "Se bloquean los paquetes sospechosos"

***

1. **Enunciado:** "Si el firewall está activo, entonces se bloquean los paquetes sospechosos"  
   **Formalización incorrecta:** p ∧ r  
   **Error:** _______________  
   **Corrección:** _______________

2. **Enunciado:** "No hay intentos de intrusión y el firewall está activo"  
   **Formalización incorrecta:** ¬(q ∧ p)  
   **Error:** _______________  
   **Corrección:** _______________

3. **Enunciado:** "Hay intentos de intrusión o el firewall no está activo"  
   **Formalización incorrecta:** q → ¬p  
   **Error:** _______________  
   **Corrección:** _______________

4. **Enunciado:** "Si hay intentos de intrusión entonces, si el firewall está activo, se bloquean los paquetes"  
   **Formalización incorrecta:** (q ∧ p) → r  
   **Error:** _______________  
   **Corrección:** _______________

***

## Recomendaciones

1. **Lee cuidadosamente cada enunciado** antes de determinar si es proposición
2. **Identifica primero las proposiciones simples** antes de formalizar expresiones complejas
3. **Respeta los paréntesis** al escribir fórmulas; determinan la estructura lógica
4. **Verifica la precedencia** de operadores al identificar conectivos principales
5. **Usa ejemplos del contexto de sistemas** para practicar la formalización
6. **Revisa tus respuestas** asegurándote de que la formalización capture el significado del enunciado original

***

## Entrega

- **Formato:** PDF con las respuestas escritas a mano (en hojas de papel o sobre archivo digital) 
- **Contenido:** Respuestas simbólicas y justificaciones breves  
- **Identificación:** Nombre completo, matrícula, fecha  
- **Presentación:** Ordenada, legible, numeración clara de ejercicios

**Nota:** No es necesario copiar los enunciados completos; indica el número de ejercicio y tu respuesta.

