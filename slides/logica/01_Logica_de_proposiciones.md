# Lógica de proposiciones

**Definición**: La lógica de proposiciones es un sistema formal que permite representar enunciados que pueden ser **verdaderos** o **falsos**, y razonar rigurosamente a partir de ellos usando reglas bien definidas. 

En el contexto de los sistemas de información, la lógica de proposiciones aparece cuando se describe si un sistema se encuentra en determinado estado, si se cumple una política de seguridad o si un módulo debe ejecutarse bajo ciertas condiciones. 
Así como en programación se combinan expresiones booleanas con `&&`, `||` o `!`, en lógica se combinan proposiciones con conectivos como “y”, “o” y “no”. 


## Ejemplo tecnológico

Se considera un sistema de autenticación muy sencillo:

- “El usuario ingresó una contraseña válida”.
- “El usuario tiene una cuenta activa”.
- “Se permite el acceso al sistema”.

Cada una de estas frases puede pensarse como algo que, para un intento de inicio de sesión concreto, es **verdadero** o **falso**.  
La **lógica de proposiciones** permite representar estas ideas **simbólicamente** y **combinarlas para expresar reglas** como: “el sistema concede acceso solo si la contraseña es válida y la cuenta está activa”. 

***

# Proposiciones

**Definición**: Una proposición es un enunciado declarativo al que se le puede asignar, de manera clara, un **valor de verdad**: verdadero (V) o falso (F), pero no ambos a la vez. 

Esto significa que el enunciado describe un hecho o situación que, en principio, podría verificarse.

## Ejemplos de proposiciones

1. “Hoy llueve en Toluca.”  
   - Es proposición: o bien efectivamente llueve, o bien no llueve.  
   - Tiene un valor de verdad bien definido para este día y lugar. 
2. “3 es un número primo.”  
   - Es proposición y es verdadera. 
3. “La base de datos principal está disponible.”  
   - Es proposición: o el servicio está disponible o no lo está, aunque en la práctica sea necesario un monitoreo para saberlo. 
4. “El servidor respondió en menos de dos segundos.”  
   - Es proposición, porque la condición de tiempo se verifica o se incumple. 
5. “El usuario está autenticado y tiene rol de administrador.”  
   - Es proposición compuesta; combina dos proposiciones más simples mediante un conectivo lógico (se detallará después). 


## Enunciados que no son proposiciones

Hay enunciados que **_no se consideran proposiciones_** porque no admiten un valor de verdad claro.

1. Preguntas:
   - “¿Qué hora es?”  
   - No es proposición, no tiene valor de verdad. 
2. Órdenes o instrucciones:
   - “Cierra la ventana del navegador.”  
   - No describe un hecho que pueda ser verdadero o falso; solo indica una acción. 
3. Expresiones de deseo u opinión vaga:
   - “Sería bueno actualizar el sistema operativo.”  
   - No se modela como verdadera o falsa en este nivel; mezcla deseos, valoraciones y contexto. 
4. Enunciados ambiguos:
   - “Esta frase es falsa.”  
   - No se usa como proposición en lógica elemental porque no admite un valor de verdad consistente; genera una paradoja;


## Identificar proposiciones (ejemplos)

Decidir si los siguientes enunciados son proposiciones o no, y por qué:

1. “El proceso de respaldo se ejecutó correctamente.”  
2. “¿El servidor está encendido?”  
3. “Guarda tu trabajo antes de cerrar la sesión.”  
4. “2 + 2 = 5.”  
5. “La red tendrá mejor rendimiento el próximo mes.”  


# Proposiciones simples y compuestas

**Definición**: Una proposición simple (o atómica) es aquella que no se descompone, dentro del lenguaje de trabajo, en proposiciones más pequeñas unidas por conectivos lógicos. 

**Definición**: Una proposición compuesta es aquella formada a partir de dos o más proposiciones simples unidas por uno o varios conectivos lógicos, o bien la negación de una proposición. 


## Ejemplos de proposiciones simples

- “El servidor web está activo.”  
- “El usuario ingresó su contraseña.”  
- “El archivo existe.”  
- “Hoy es miércoles.”  

En todas estas frases no se observa, a nivel lógico, ninguna unión explícita con otros enunciados mediante “y”, “o”, “si… entonces…”, etc. 


## Ejemplos de proposiciones compuestas

- “El servidor web está activo y la base de datos está disponible.”  
- “El usuario está autenticado o el acceso será rechazado.”  
- “Si el usuario no acepta los términos, entonces no puede continuar.”  
- “El sistema es seguro si y solo si todas las políticas están habilitadas.”  

Estas proposiciones **combinan** partes más simples y utilizan **conectivos lógicos** como **“y”**, **“o”**, “**si… entonces…**”, “**si y solo si…**”. 


## Ejemplos para practicar (simple vs compuesta)

1. “La aplicación móvil está actualizada.”  
2. “La consulta terminó en error o el tiempo de espera fue excedido.”  
3. “Si se interrumpe la energía eléctrica, el sistema entra en modo de respaldo.”  
4. “El servicio de correo funciona.”   


# Representación simbólica de proposiciones

**Definición**: En lógica de proposiciones, cada proposición simple se representa mediante una letra proposicional (generalmente mayúscula), como P, Q, R, S, etc., para trabajar de forma más concisa y abstracta. 

Esta sustitución de frases largas por símbolos funciona como una especie de “alias” para razonamiento lógico; el contenido específico se puede anotar aparte. 


## Asociar enunciados con letras

Se considera el siguiente ejemplo de un sistema de autenticación:

- P: “La contraseña es correcta.”  
- Q: “La cuenta está activa.”  
- R: “El usuario tiene permisos de administrador.”  

Estos símbolos permiten escribir en forma breve expresiones como:

- “La contraseña es correcta y la cuenta está activa” → \(P \land Q\).  
- “Si la contraseña es correcta y la cuenta está activa, entonces se permite el acceso” → se verá más adelante como una expresión con condicional. 


## Ejemplo

- P: “Hoy hace frío.”  
- Q: “Está lloviendo.”  
- R: “La persona lleva paraguas.”  

Al representar enunciados de este modo, es más sencillo manipularlos y analizar sus combinaciones, dejando de lado detalles no lógicos del lenguaje natural. 

***

# Conectivos lógicos básicos

**Definición**: Un conectivo lógico es un **símbolo** que permite construir **nuevas proposiciones** a partir de una o más proposiciones ya dadas, de forma similar a como las operaciones aritméticas construyen nuevas expresiones a partir de números. 

---
Los conectivos básicos que veremos son:

- Negación  
- Conjunción  
- Disyunción  
- Condicional  
- Bicondicional 


## Negación (no)

**Definición**: La negación de una proposición P, escrita ¬P, es una nueva proposición que es verdadera cuando P es falsa, y falsa cuando P es verdadera. 

Símbolo habitual: ¬ (también se usa a veces ~).  
Lecturas comunes: “no P”, “no es el caso que P”. 


### Ejemplos de negación

1. P: “El servidor está en línea.”  
   - ¬P: “El servidor no está en línea.”   
2. Q: “Hoy es viernes.”  
   - ¬Q: “Hoy no es viernes.”  
3. R: “La conexión es segura (cifrada).”  
   - ¬R: “La conexión no es segura (no está cifrada).” 


### Tabla de verdad básica de la negación

Una tabla de verdad muestra el valor de verdad de una fórmula para todas las combinaciones posibles de verdad de sus componentes.

| P | ¬P |
|---|----|
| V | F  |
| F | V  |


## Conjunción (y)

**Definición**: La conjunción de P y Q, escrita \(P \land Q\), es verdadera únicamente cuando P y Q son ambas verdaderas; en cualquier otro caso es falsa. 

Símbolo habitual: ∧.  
Lecturas comunes: “P y Q”, “P además Q”. 

***

### Ejemplos de conjunción

Ejemplo:

- P: “La contraseña es correcta.”  
- Q: “La cuenta está activa.”  
- \(P \land Q\): “La contraseña es correcta y la cuenta está activa.”  

Esta proposición describe la situación donde ambas condiciones se cumplen; si alguna falla, la conjunción completa deja de ser verdadera.

***

### Tabla de verdad básica de la conjunción

| P | Q | \(P \land Q\) |
|---|---|---------------|
| V | V | V             |
| V | F | F             |
| F | V | F             |
| F | F | F             |

***

## Disyunción (o)

**Definición**.  
La disyunción de P y Q, escrita \(P \lor Q\), es verdadera cuando al menos una de las dos proposiciones es verdadera, y solo es falsa cuando ambas son falsas. 

Símbolo habitual: \( \lor \).  
Lecturas comunes: “P o Q” (en sentido inclusivo: puede ser P, o Q, o ambas). 

***

### Ejemplos de disyunción

Ejemplo:

- P: “Llueve.”  
- Q: “Hace mucho frío.”  
- \(P \lor Q\): “Llueve o hace mucho frío (o ambas cosas).” 

***

### Tabla de verdad básica de la disyunción

| P | Q | \(P \lor Q\) |
|---|---|--------------|
| V | V | V            |
| V | F | V            |
| F | V | V            |
| F | F | F            |

***

## Condicional (si… entonces…)

**Definición**.  
El condicional, escrito \(P \to Q\), se lee “si P, entonces Q” y se considera falso solo cuando P es verdadera y Q es falsa; en cualquier otro caso se considera verdadero. 

Símbolo habitual: \( \to \).  
Lecturas comunes: “si P entonces Q”, “P implica Q”. 

***

### Ejemplos de condicional

Ejemplo:

- P: “El usuario está autenticado.”  
- Q: “El usuario puede acceder al panel de administración.”  
- \(P \to Q\): “Si el usuario está autenticado, entonces puede acceder al panel de administración.”

***

### Tabla de verdad básica del condicional

| P | Q | \(P \to Q\) |
|---|---|-------------|
| V | V | V           |
| V | F | F           |
| F | V | V           |
| F | F | V           |


Pensemos el condicional como una promesa:

"Si pasa \(P\), entonces garantizo \(Q\)"

- Si \(P\) ocurre y \(Q\) falla \( \to \) promesa rota (falso)  
- En cualquier otro caso \( \to \) no se rompe la promesa (verdadero)

---
Ejemplo para desarrollar.
- \(P\): "Estudio para el examen"  
- \(Q\): "Apruebo el examen"

La proposición:
\(P \to Q\)
"Si estudio para el examen, entonces apruebo el examen"


## Bicondicional (si y solo si)

**Definición**.  
El bicondicional, escrito \(P \leftrightarrow Q\), es verdadero cuando P y Q tienen el mismo valor de verdad (ambas verdaderas o ambas falsas) y es falso cuando tienen valores distintos. 

Símbolo habitual: ↔.  
Lecturas comunes: “P si y solo si Q”, “P es equivalente a Q”. 

***

### Ejemplos de bicondicional

Ejemplo:

- P: “Tiene acceso al estacionamiento.”  
- Q: “Cuenta con la tarjeta de residente vigente.”  
- \(P \leftrightarrow Q\): “Tiene acceso al estacionamiento si y solo si cuenta con la tarjeta de residente vigente.” 

***

### Tabla de verdad básica del bicondicional

| P | Q | \(P \leftrightarrow Q\) |
|---|---|-------------------------|
| V | V | V                       |
| V | F | F                       |
| F | V | F                       |
| F | F | V                       |


***

# Fórmulas bien formadas (FBF)

**Definición**: Una fórmula bien formada (FBF) es una expresión construida correctamente a partir de letras proposicionales y conectivos lógicos, siguiendo reglas sintácticas que indican cómo se pueden combinar.

De manera informal, las reglas mínimas son las siguientes:

1. Toda letra proposicional (P, Q, R, …) es una FBF.  
2. Si ϕ es una FBF, entonces ¬ϕ también es una FBF.  
3. Si ϕ y ψ son FBF, entonces \((ϕ \land ψ)\), \((ϕ \lor ψ)\), \((ϕ \to ψ)\), \((ϕ \leftrightarrow ψ)\) son FBF. 
4. Nada más es FBF salvo lo que se puede construir aplicando finitamente estas reglas. 

***

## Importancia de los paréntesis

Los paréntesis se usan para dejar claro qué conectivo actúa primero, del mismo modo que en una expresión aritmética se decide si primero se suma o se multiplica. 

Ejemplo:

- \((P \land Q) \lor R\)  
- \(P \land (Q \lor R)\)  

Ambas son FBF y representan situaciones distintas:  
en la primera, se exige que P y Q se cumplan juntos, o bien R;  
en la segunda, basta P y, además, al menos una de Q o R. 

***

## Ejemplos de fórmulas bien formadas

Dadas las letras proposicionales P, Q, R:

1. \(P\)  
2. ¬P  
3. \((P \land Q)\)  
4. \((P \lor (¬Q))\)  
5. \(((P \land Q) \to R)\)  
6. \((P \leftrightarrow (Q \lor R))\) 

Todas estas expresiones se pueden generar aplicando las reglas indicadas; por tanto son fórmulas bien formadas.

***

## Ejemplos de expresiones que NO son FBF

1. \(P \land \land Q\)  
   - Tiene dos conectivos seguidos sin una proposición entre ellos.   
2. \(¬ \lor P\)  
   - La negación no está aplicada a una fórmula, y el “o” tampoco tiene dos argumentos visibles.  
3. \(P Q \land\)  
   - No respeta el patrón “proposición conectivo proposición”.

***

## Ejemplos para practicar (es FBF o no lo es)

Se analiza si las siguientes expresiones son fórmulas bien formadas:

1. \(P \land (Q \lor R)\)  
2. \((¬P \to Q)\)  
3. \(P \lor Q \land\)  
4. \((P \leftrightarrow (Q \to R))\)  
5. \(¬(P \lor)\)


# De lenguaje natural a fórmulas de lógica de proposiciones (traducción)

## Traducción

**Definición**: La traducción de lenguaje natural a fórmulas de lógica de proposiciones consiste en asociar a cada enunciado simple una letra proposicional y reemplazar conectores del lenguaje cotidiano (“no”, “y”, “o”, “si… entonces…”, “si y solo si…”) por los conectivos lógicos correspondientes. 

Este paso permite analizar de forma abstracta reglas de negocio, políticas de seguridad o condiciones de ejecución presentes en sistemas informáticos. 


## Pasos típicos para traducir

1. Identificar las proposiciones simples que la forman.  
2. Asignar una letra proposicional a cada una.  
3. Determinar qué conectores del lenguaje natural están presentes (“no”, “y”, “o”, “si… entonces…”).  
4. Escribir la fórmula usando las letras y los conectivos lógicos adecuados.  
5. Agregar paréntesis cuando sea necesario para evitar ambigüedades. 


## Ejemplos de traducción

Ejemplo 1.  
Enunciado: “Si el usuario está autenticado y tiene rol de administrador, entonces puede eliminar registros.”  

---

- P: “El usuario está autenticado.”  
- Q: “El usuario tiene rol de administrador.”  
- R: “El usuario puede eliminar registros.”  

--- 

Fórmula:

\[
((P \land Q) \to R)
\]

El par de paréntesis exteriores agrupa todo el condicional, y los internos dejan claro que primero se construye \(P \land Q\). 

***

Ejemplo 2.  
Enunciado: “El sistema genera una alerta si la temperatura es mayor a 80 grados o el ventilador está apagado.”  

---
- P: “La temperatura es mayor a 80 grados.”  
- Q: “El ventilador está apagado.”  
- R: “El sistema genera una alerta.”  

---

\[
((P \lor Q) \to R)
\]

***

Ejemplo 3.  
Enunciado: “El sistema está disponible si y solo si la base de datos está disponible y la red está activa.”  

---
- P: “El sistema está disponible.”  
- Q: “La base de datos está disponible.”  
- R: “La red está activa.”  

---

\[
P \leftrightarrow (Q \land R)
\]

---

Ejemplo 4.  
Enunciado: “No es cierto que llueva y haga calor al mismo tiempo.”  

- P: “Llueve.”  
- Q: “Hace calor.”  

---

Fórmula:

\[
¬(P \land Q)
\]

Se niega la conjunción: la frase indica que esa combinación (lluvia y calor simultáneos) no se da. 

***

Ejemplo 5.  
Enunciado: “Si estudia y duerme bien, entonces tendrá mejor rendimiento.”  

- P: “Estudia.”  
- Q: “Duerme bien.”  
- R: “Tiene mejor rendimiento.”  

---

Fórmula:

\[
((P \land Q) \to R)
\]

***

## Ejemplos para practicar (traducción)

1. “Si la batería está baja o el equipo está en modo de ahorro de energía, entonces se reduce el brillo de la pantalla.”  
2. “Si el usuario acepta los términos, entonces puede continuar y acceder al servicio.”  
3. “La red no está disponible o el servicio se encuentra en mantenimiento.”  
4. “El respaldo se completará si y solo si hay suficiente espacio y no ocurre ningún error durante el proceso.”  

En cada caso se espera:

- Identificación de proposiciones simples y su simbolización.  
- Uso adecuado de ¬, ∧, ∨, →, ↔ y paréntesis. 


# Identificación del conectivo principal de una fórmula

**Definición**.  
El conectivo principal de una fórmula es el conectivo de más “alto nivel” que estructura toda la expresión, es decir, el último que se aplicó al construirla según las reglas de formación. 

Identificarlo resulta importante para:

- Entender la forma global de la fórmula.  
- Desarrollar tablas de verdad de manera ordenada.  
- Aplicar transformaciones o reglas de inferencia sobre la estructura adecuada. 

***

## Cómo localizar el conectivo principal

1. Se observa la fórmula completa, con paréntesis.  
2. Se busca el conectivo que no está encerrado totalmente dentro de otros paréntesis, o que “divide” a la fórmula más externa en dos partes.  
3. En el caso de la negación, si la fórmula tiene forma ¬ϕ y nada más por fuera, el conectivo principal es la negación. 

***

## Ejemplos de conectivo principal

Ejemplo 1.  

\[
(P \land Q)
\]

- La fórmula completa está entre paréntesis.  
- El conectivo que une P y Q es \( \land \).  
Conectivo principal: conjunción (\( \land \)). 

***

Ejemplo 2.  

\[
(P \land Q) \to R
\]

- La fórmula puede verse como ϕ \( \to \) R, donde ϕ es \((P \land Q)\).  
- El conectivo que estructura todo es \( \to \).  
Conectivo principal: condicional (\( \to \)). 

***

Ejemplo 3.  

\[
¬(P \lor Q)
\]

- Toda la fórmula está bajo una negación y luego entre paréntesis.  
- El símbolo más externo es \( ¬ \).  
Conectivo principal: negación \( ¬ \). 

***

Ejemplo 4.  

\[
(P \land Q) \leftrightarrow (R \lor S)
\]

- A la izquierda hay una conjunción, a la derecha una disyunción, y ambas partes están unidas por \( \leftrightarrow \).  
- El conectivo principal es el bicondicional. 

***

## Ejemplos para practicar (conectivo principal)

1. \((P \lor Q) \land R\)  
2. \(¬(P \to Q)\)  
3. \((P \to (Q \land R))\)  
4. \((P \leftrightarrow Q) \lor R\)  
5. \(¬P \lor Q\) 

El análisis se apoya en la estructura de paréntesis y en la posición relativa de los conectivos.
