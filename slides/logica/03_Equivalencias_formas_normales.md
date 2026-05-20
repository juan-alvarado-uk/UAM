# Equivalencias lógicas, formas normales

Las equivalencias lógicas permiten transformar fórmulas proposicionales sin cambiar su significado, y las formas normales (conjuntiva y disyuntiva) son “formatos estándar” que facilitan el análisis y la automatización en lógica y programación lógica.   

***

# Recordatorio mínimo: fórmulas y tablas de verdad

Una fórmula bien formada es una expresión construida con proposiciones que no se pueden separar, las llamaremos atómicas (p, q, r, …) y conectivos lógicos (¬, ∧, ∨, →, ↔) siguiendo las reglas sintácticas vistas previamente.   
La tabla de verdad de una fórmula muestra, para todas las combinaciones posibles de verdad de sus atómicas, si la fórmula resulta verdadera o falsa en cada caso.   

***

# Equivalencia lógica

Dos fórmulas proposicionales $ \varphi $ y $ \psi $ son lógicamente equivalentes si tienen exactamente la misma tabla de verdad.

---
Cuando esto ocurre se escribe $$ \varphi \equiv \psi $$ indicando que expresan la misma condición, aunque estén “escritas distinto”.  

---
Esto permite reemplazar una fórmula por otra equivalente dentro de razonamientos o programas, con la certeza de que no se cambia el comportamiento lógico.

***

# Leyes lógicas fundamentales

En lugar de comparar tablas de verdad desde cero en cada transformación, se usan leyes lógicas ya probadas como “reglas de reescritura”.   
Cada ley es una equivalencia lógica general que vale para cualquier proposición que se ponga en lugar de las letras p, q, r, etc.   




## Idempotencia

- Idempotencia de ∨:  
  \[
  A \lor A \equiv A
  \]  
- Idempotencia de ∧:  
  \[
  A \land A \equiv A
  \]  

Estas leyes dicen que repetir la misma proposición con ∧ o ∨ no cambia su valor lógico. 

***

## Complemento

**Algunas veces se encuentra con ⊥ para F y ⊤ para V):**  

- Para ∧:  
  \[
  A \land \neg A \equiv F
  \]  
- Para ∨:  
  \[
  A \lor \neg A \equiv V
  \]  

---
Es decir, “A y no A” es siempre falso (contradicción), y “A o no A” es siempre verdadero (tautología). 


## Identidad

**Forma básica:**

- Identidad de ∨:  
  \[
  A \lor F \equiv A
  \]  
- Identidad de ∧:  
  \[
  A \land V \equiv A
  \]  


## Dominación (también llamada “anulación”)

Esta es la “otra cara” de identidad.

- Dominación de ∨ (con tautología):  
  \[
  A \lor V \equiv V
  \]  
- Dominación de ∧ (con contradicción):  
  \[
  A \land F \equiv F
  \]  


## Absorción

-  
  \[
  A \lor (A \land B) \equiv A
  \]  
-  
  \[
  A \land (A \lor B) \equiv A
  \]  

Estas leyes capturan que, si A ya está presente, la parte extra \(A \land B\) o \(A \lor B\) no aporta nada nuevo en términos de condiciones lógicas. 


## Leyes conmutativas

Las leyes conmutativas dicen que, para conjunción y disyunción, el orden de las proposiciones no altera el resultado:  

- $$ p \land q \equiv q \land p $$  
- $$ p \lor q \equiv q \lor p $$

***

**Ejemplo de uso simbólico**  
$$
(p \land r) \land q \equiv p \land r \land q \equiv r \land p \land q
$$  
Aquí se combinan además leyes asociativas (siguiente subsección), pero la idea conmutativa es que se pueden “reordenar” los factores de una conjunción o disyunción sin cambiar el valor lógico.   

***

## Leyes asociativas

Las leyes asociativas indican que, para conjunción y disyunción, la forma de agrupar con paréntesis no modifica el resultado:  

- $$ (p \land q) \land r \equiv p \land (q \land r) $$
- $$ (p \lor q) \lor r \equiv p \lor (q \lor r) $$

***

**Ejemplo simbólico**  
$$
(p \land q) \land (r \land s) \equiv p \land q \land r \land s
$$  
La ley asociativa (junto con conmutativa) permite eliminar paréntesis internos y ver la conjunción como una colección sin orden.   

***

## Leyes distributivas

Las leyes distributivas conectan conjunción y disyunción de forma análoga a la distribución del producto sobre la suma en aritmética:  

- $$ p \land (q \lor r) \equiv (p \land q) \lor (p \land r) $$  
- $$ p \lor (q \land r) \equiv (p \lor q) \land (p \lor r) $$

***

Esta equivalencia será central para llevar fórmulas a forma normal disyuntiva o conjuntiva que se verán más adelante.   

***

## Leyes de De Morgan

Las leyes de De Morgan describen cómo se distribuye la negación sobre conjunciones y disyunciones:  

- $$ \neg (p \land q) \equiv \neg p \lor \neg q $$  
- $$ \neg (p \lor q) \equiv \neg p \land \neg q $$   


## Doble negación

La ley de doble negación dice que negar dos veces devuelve la fórmula original:  

- $$ \neg\neg p \equiv p $$.   


## Condicional y disyunción

**Relación fundamental**  

El condicional $$ p \to q $$ es lógicamente equivalente a la disyunción $$ \neg p \lor q $$  

- $$ p \to q \equiv \neg p \lor q $$.

**Ejemplo simbólico**  

Se transforma la fórmula:  
$$
(p \land q) \to r
$$  
Usando la equivalencia del condicional:  
$$
(p \land q) \to r \equiv \neg(p \land q) \lor r
$$ 

---

Aplicando De Morgan:  
$$
\neg(p \land q) \lor r \equiv (\neg p \lor \neg q) \lor r
$$  
Con asociatividad y conmutatividad de ∨ se puede escribir:  
$$
\neg p \lor \neg q \lor r
$$  

# Estrategia general de simplificación mediante equivalencias

El objetivo de simplificar una fórmula es obtener otra expresión equivalente más “ligera”, con menos conectivos o con una estructura más transparente para el análisis y la implementación.   
Las leyes vistas (conmutatividad, asociatividad, distributividad, De Morgan, doble negación, condicional-disyunción) se combinan como herramientas para ir transformando paso a paso.   

***

# Pasos típicos de simplificación 

1. Eliminar condicionales y bicondicionales usando equivalencias conocidas.  
2. Mover negaciones hacia adentro con De Morgan y doble negación, hasta dejar ¬ sólo sobre atómicas.  
3. Reordenar y reagrupar con conmutatividad y asociatividad para ver mejor la estructura.  
4. Aplicar distributividad si se requiere una forma específica (por ejemplo, conjuntiva o disyuntiva).  

***

**Ejemplo tecnológico de simplificación**  

Se modela la siguiente condición para un sistema de autenticación:  
“ Si el usuario está en la lista de permitidos y su contraseña es correcta entonces el acceso es concedido”.  

---
Sea:  
- p: “usuario está en la lista de permitidos”.  
- q: “contraseña es correcta”.  
- r: “acceso es concedido”.  

La fórmula es: $$ (p \land q) \to r $$

---
Esta se simplifica así...  
$$
(p \land q) \to r \equiv \neg(p \land q) \lor r 
$$  
$$
\equiv \neg p \lor \neg q \lor r
$$

Así, el sistema puede revisar esta condición como una disyunción de casos: o no está permitido, o la contraseña es incorrecta, o el acceso se concede.   

***

# Formas normales

Una forma normal es una manera estándar de escribir fórmulas proposicionales usando sólo ciertos conectivos en una estructura muy regular.   

---
Las dos más importantes son:  

- Forma normal conjuntiva (FNC): conjunción de disyunciones.  
- Forma normal disyuntiva (FND): disyunción de conjunciones.   

***

**Motivación**  

Trabajar con fórmulas en formas normales facilita algoritmos de verificación, razonadores automáticos y, en general, el análisis sistemático de especificaciones lógicas.   
Además, muchas técnicas posteriores (como métodos de satisfacibilidad y programación lógica) exigen que las fórmulas se expresen primero en alguna de estas formas.   

***

# Forma Normal Conjuntiva (FNC)

Una fórmula está en **forma normal conjuntiva** si es una conjunción de cláusulas, donde cada cláusula es una disyunción de literales, y un literal es una atómica o su negación.   

Ejemplo de FNC:  
$$
(\neg p \lor q \lor r) \land (\neg q \lor \neg r) \land (p \lor r)
$$  
Aquí se ve una conjunción (∧) de varios paréntesis, y en cada paréntesis sólo hay disyunciones (∨) de atómicas o negadas.   

***

**Intuición** 

Una FNC describe un conjunto de condiciones que todas deben cumplirse, y cada cláusula interna da alternativas dentro de esa condición.   
Por ejemplo, en seguridad de red se podría expresar que “en cada segmento de red se tiene (firewall activo o monitoreo activo) y (registro de actividad o alerta en tiempo real)”.   

***

## Método general para transformar a FNC

Cualquier fórmula proposicional puede transformarse a una fórmula equivalente en FNC siguiendo un esquema estándar.   

---
## Pasos típicos para trasformar a FNC

1. Eliminar condicionales y bicondicionales.  
   - Reemplazar $ p \to q $ por $ \neg p \lor q $.  
2. Mover negaciones hacia dentro.  
   - Usar De Morgan y doble negación, hasta tener negaciones sólo sobre atómicas.  
3. Usar conmutatividad y asociatividad para aclarar estructura.  
4. Distribuir disyunciones sobre conjunciones.  
   - $ p \lor (q \land r) \equiv (p \lor q) \land (p \lor r) $  

***

## Ejemplo completo de transformación a FNC

Se toma la fórmula:  
$$
(p \to q) \land (\neg q \lor r)
$$  

**Paso 1: eliminar condicional**  
$$
p \to q \equiv \neg p \lor q
$$  

---
Entonces:  
$$
(p \to q) \land (\neg q \lor r) 
$$  

$$
\equiv (\neg p \lor q) \land (\neg q \lor r)
$$ 
Ya no hay condicionales.   

***

**Paso 2: revisar negaciones**  

En esta fórmula la negación ya está directamente sobre atómicas ($\neg p$, $\neg q$), así que no es necesario aplicar De Morgan.   

***

**Paso 3: verificar estructura de FNC**  
La fórmula  
$$
(\neg p \lor q) \land (\neg q \lor r)
$$  
es una conjunción de dos disyunciones de literales, por lo que ya está en FNC.

***

## Ejemplo

Supóngase una política de disponibilidad para un servicio en línea:  
“ El servicio está disponible si el servidor principal funciona o el servidor de respaldo funciona, y además el enlace de red está operativo”.  

Sea:  
- p: “servidor principal funciona”.  
- q: “servidor de respaldo funciona”.  
- r: “enlace de red operativo”.  

La condición general puede escribirse como:  
$$
(p \lor q) \land r
$$  
Es una conjunción de dos cláusulas, por lo tanto, es FNC.  

- Primera cláusula: $$ (p \lor q) $$  
- Segunda cláusula: $$ r $$ (que se interpreta como disyunción de un solo literal).  

   

***

# Forma Normal Disyuntiva (FND)

Una fórmula está en forma normal disyuntiva si es una disyunción de términos, donde cada término es una conjunción de literales.   

Ejemplo de FND:  
$$
(p \land \neg q) \lor (q \land r) \lor (\neg p \land \neg r)
$$  
Aquí la estructura principal es una disyunción (∨) y cada bloque unido por ∧ es un “caso posible completo”.   

***

**Intuición**  
Una FND describe varios escenarios alternativos que hacen verdadera la fórmula; basta que se cumpla uno de los términos para que toda la expresión sea verdadera.   
Se puede ver como una lista de “configuraciones aceptables”, muy útil para pensar casos de prueba o estados permitidos.   

***

## Método general para transformar a FND

De forma análoga al caso conjuntivo, cualquier fórmula proposicional puede escribirse en FND siguiendo un proceso estándar.   

## Pasos típicos para transformar a FND

1. Eliminar condicionales y bicondicionales.  
2. Mover negaciones hacia las atómicas.  
3. Reordenar con conmutatividad y asociatividad.  
4. Distribuir conjunciones sobre disyunciones.  
   - Usar: $$ p \land (q \lor r) \equiv (p \land q) \lor (p \land r) $$  

   

***

## Ejemplo completo de transformación a FND

$$
p \lor (q \land r)
$$  

1. No hay condicionales ni bicondicionales.  
2. No hay negaciones externas.  
3. Se usa distributividad:  
   $$
   p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)
   $$  
   Pero esto produce una FNC, no una FND.  

Para obtener FND se parte de una forma donde la conjunción esté fuera  
$$
(p \land q) \lor r
$$  

Es una disyunción de dos cláusulas y cada cláusula es una conjunción, por lo tanto, es FND.
$ r $ se considera **conjunción de un solo literal**.

***

## Ejemplo con FND

Se describe la situación de un servicio de mensajería que considera correcto el envío si ocurre cualquiera de las siguientes combinaciones:  

- El servidor central está disponible y la base de datos responde.  
- O el servidor de respaldo está disponible y hay caché local válida.  

---
Sea:  
- p: “servidor central disponible”.  
- q: “base de datos responde”.  
- r: “servidor de respaldo disponible”.  
- s: “caché local válida”.  

Una FND podría ser:  
$$
(p \land q) \lor (r \land s)
$$  
La fórmula se ve como una lista de escenarios aceptables de operación.   

***

# Relación entre FNC y FND

**Equivalencia respecto a la fórmula original** 

**Si una fórmula es una contingencia** (no tautología ni contradicción), **entonces existe una FNC y una FND equivalentes a ella**.   

Cada una resalta distintos aspectos: la FNC enfatiza restricciones que todas deben cumplirse; la FND enfatiza conjuntos de condiciones alternativas que bastan para cumplir la fórmula.   

***

**Construcción a partir de tablas de verdad**  
- La FND se construye a partir de las filas donde la fórmula es verdadera (mintérminos).  
- La FNC se construye a partir de las filas donde la fórmula es falsa (maxtérminos).   

Esta relación entre filas verdaderas/falsas y términos conjuntivos/disyuntivos se conecta con métodos de satisfacibilidad y con el estudio formal de sistemas lógicos.   

## Tabla de verdad

Ejemplo: $ \varphi(p,q,r) = (p \land q) \lor r $

Primero se muestran las columnas de p, q, r, luego \(p \land q\) y finalmente \(\varphi\). 

| p | q | r | \(p \land q\) | \(\varphi = (p \land q) \lor r\) |
|---|---|---|---------------|----------------------------------|
| F | F | F | F             | F                                |
| F | F | V | F             | V                                |
| F | V | F | F             | F                                |
| F | V | V | F             | V                                |
| V | F | F | F             | F                                |
| V | F | V | F             | V                                |
| V | V | F | V             | V                                |
| V | V | V | V             | V                                |

En esta tabla se ve que \(\varphi\) es falsa en las filas 1, 3 y 5, y verdadera en las filas 2, 4, 6, 7 y 8. 

***

# FND desde la tabla (filas donde \(\varphi = V\))

Para la forma normal disyuntiva se usan las filas con \(\varphi = V\). 

**Filas verdaderas:** 2, 4, 6, 7 y 8.  

Regla:  
- Si en una fila p, q, r valen V, se escriben sin negación.  
- Si valen F, se escriben negadas. 

***

**Fila 2: \(p=F, q=F, r=V\)**  

- Literales: \(\neg p\), \(\neg q\), \(r\).  
- Término: \(\neg p \land \neg q \land r\).  

***

**Fila 4: \(p=F, q=V, r=V\)**  

- Literales: \(\neg p\), \(q\), \(r\).  
- Término: \(\neg p \land q \land r\).  

***

**Fila 6: \(p=V, q=F, r=V\)**  

- Literales: \(p\), \(\neg q\), \(r\).  
- Término: \(p \land \neg q \land r\).  

***

**Fila 7: \(p=V, q=V, r=F\)**  

- Literales: \(p\), \(q\), \(\neg r\).  
- Término: \(p \land q \land \neg r\).  

***

**Fila 8: \(p=V, q=V, r=V\)**  

- Literales: \(p\), \(q\), \(r\).  
- Término: \(p \land q \land r\).  

***

**FND resultante**  

\[
\text{FND}(\varphi) = (\neg p \land \neg q \land r) \lor (\neg p \land q \land r) \lor (p \land \neg q \land r) \lor (p \land q \land \neg r) \lor (p \land q \land r)
\]  

Esta es una disyunción de conjunciones de literales, por lo que está en forma normal disyuntiva y es equivalente a \((p \land q) \lor r\). 

***

# FNC desde la tabla (filas donde \(\varphi = F\))

Para la forma normal conjuntiva se usan las filas con \(\varphi = F\). 

**Filas falsas:** 1, 3 y 5.  

Regla:  
- Si una variable vale F en la fila → se escribe sin negación.  
- Si vale V → se escribe negada. 

***

**Fila 1: \(p=F, q=F, r=F\)**  

- Literales: \(p\), \(q\), \(r\).  
- Cláusula: \(p \lor q \lor r\).  

***

**Fila 3: \(p=F, q=V, r=F\)**  

- Literales: \(p\), \(\neg q\), \(r\).  
- Cláusula: \(p \lor \neg q \lor r\).  

***

**Fila 5: \(p=V, q=F, r=F\)**  

- Literales: \(\neg p\), \(q\), \(r\).  
- Cláusula: \(\neg p \lor q \lor r\).  

***

**FNC resultante**  

\[
\text{FNC}(\varphi) = (p \lor q \lor r) \land (p \lor \neg q \lor r) \land (\neg p \lor q \lor r)
\]  

Esta fórmula es conjunción de disyunciones de literales y es equivalente a \((p \land q) \lor r\).



# Ejemplos de transformación paso a paso (práctica conceptual)

## Ejemplo 1: simplificación y FNC

Se considera la fórmula:  
$$
(p \to q) \lor \neg q
$$  

**Paso 1: eliminar condicional**  
$$
p \to q \equiv \neg p \lor q
$$  
Entonces:  
$$
(p \to q) \lor \neg q \equiv (\neg p \lor q) \lor \neg q
$$  

***

**Paso 2: asociatividad y conmutatividad**  
Se reagrupa:  
$$
(\neg p \lor q) \lor \neg q \equiv \neg p \lor q \lor \neg q
$$  

---
La disyunción $$ q \lor \neg q $$ es una tautología; por tanto, toda la fórmula se simplifica a:  
$$
\neg p \lor \text{(tautología)} \equiv \text{tautología}
$$  

---
En consecuencia, la fórmula original es siempre verdadera, lo que muestra cómo las equivalencias pueden revelar propiedades globales de una especificación.   

***

## Ejemplo 2: de especificación a FNC

Se expresa:  
“ Si el sistema está en mantenimiento, ninguna petición externa se atiende, y si no está en mantenimiento las peticiones externas se atienden sólo si la cola está por debajo de cierto umbral”.  

---
Sea:  
- m: “sistema en mantenimiento”.  
- e: “se atiende una petición externa”.  
- c: “cola por debajo de umbral”.  

La especificación se puede resumir como:  
$$
(m \to \neg e) \land (\neg m \to (c \to e))
$$  

***

**Transformación inicial**  

1. Eliminar condicionales:  
   - $$ m \to \neg e \equiv \neg m \lor \neg e $$  
   - $$ c \to e \equiv \neg c \lor e $$  
   - $$ \neg m \to (c \to e) \equiv m \lor (\neg c \lor e) $$  

---
La fórmula se vuelve:  
$$
(\neg m \lor \neg e) \land (m \lor \neg c \lor e)
$$  

Las negaciones están ya sobre atómicas, y la estructura es conjunción de disyunciones; así, esta expresión ya está en FNC.   

***

# Ejercicios tipo para reforzar conceptos

Los siguientes tipos de ejercicios son para practicar equivalencias y formas normales, generando secuencias de transformación claramente justificadas paso a paso.   


## Transformación a FNC

- Reescribir en FNC:  
  1. $$ (p \lor q) \to r $$  
  2. $$ \neg(p \land (q \lor r)) $$  
  3. $$ (p \to q) \land (q \to r) $$  

En cada caso se espera usar: eliminación de condicional, De Morgan, doble negación, conmutatividad, asociatividad y distributividad según sea necesario para obtener una conjunción de disyunciones de literales.   

***

## Transformación a FND

- Reescribir en FND (usando equivalencias o tabla de verdad cuando sea conveniente):  
  1. $$ (p \land \neg q) \lor (\neg p \land r) $$  
  2. $$ \neg p \lor (q \land r) $$  
  3. $$ (p \lor q) \land r $$  

***

## Uso de equivalencias para simplificar

- Simplificar, usando leyes lógicas, hasta obtener una forma más corta y clara:  
  1. $$ \neg\neg(p \land q) \lor (p \land q) $$  
  2. $$ (p \lor q) \land (p \lor \neg q) $$  
  3. $$ (p \to q) \land (p \to \neg q) $$  

El objetivo es acostumbrarse a justificar cada paso con una ley concreta: conmutatividad, asociatividad, distributividad, De Morgan, doble negación, condicional-disyunción, etc.   

