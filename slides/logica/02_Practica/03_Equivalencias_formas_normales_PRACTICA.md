# Equivalencias lógicas y formas normales

## Introducción
Una equivalencia lógica es una relación entre dos fórmulas que tienen exactamente la misma tabla de verdad; aunque se escriban distinto, se comportan igual en todos los casos posibles. Una forma normal es una presentación estandarizada de una fórmula.

En esta práctica se transformarán fórmulas, se justificará cada paso con leyes lógicas y se obtendrán fórmulas simplificadas o escritas en FNC y FND.

Se trabajará con los siguientes conceptos: equivalencia lógica, simplificación simbólica, eliminación de conectivos derivados, traslado de negaciones y uso de distributividad para llegar a FNC o FND.

## Repertorio de leyes
Una ley lógica es una transformación válida que conserva el valor de verdad de la fórmula. Cada paso escrito en los ejercicios deberá nombrar la ley utilizada.

### Leyes básicas a utilizar
- Idempotencia: $ p \lor p \equiv p $, $ p \land p \equiv p $. 
- Complemento: $ p \lor \neg p \equiv V $, $ p \land \neg p \equiv F $. 
- Identidad: $ p \lor F \equiv p $, $ p \land V \equiv p $. 
- Dominación: $ p \lor V \equiv V $, $ p \land F \equiv F $. 
- Absorción: $ p \lor (p \land q) \equiv p $, $ p \land (p \lor q) \equiv p $. 

- Conmutatividad:  
  - $ p \lor q \equiv q \lor p $  
  - $ p \land q \equiv q \land p $. 

- Asociatividad:  
  - $ (p \lor q) \lor r \equiv p \lor (q \lor r) $  
  - $ (p \land q) \land r \equiv p \land (q \land r) $. 

- Distributividad:  
  - $ p \lor (q \land r) \equiv (p \lor q) \land (p \lor r) $  
  - $ p \land (q \lor r) \equiv (p \land q) \lor (p \land r) $. 
- De Morgan:  
  - $ \neg (p \lor q) \equiv \neg p \land \neg q $  
  - $ \neg (p \land q) \equiv \neg p \lor \neg q $. 
- Doble negación: $ \neg\neg p \equiv p $. 
- Condicional: $ p \to q \equiv \neg p \lor q $. 
- Bicondicional:  
  - $ p \leftrightarrow q \equiv (p \to q) \land (q \to p) $  
  - $ p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q) $. 


## Formas normales
La FNC es una conjunción de disyunciones de literales, mientras que la FND es una disyunción de conjunciones de literales; un literal (o atómica) es una variable proposicional o su negación. 

Para transformar una fórmula a forma normal se seguirá esta secuencia general: eliminar $ \to $ y $ \leftrightarrow $, mover negaciones hasta los literales con De Morgan, quitar dobles negaciones y aplicar distributividad, etc., hasta obtener la estructura deseada.

***

## Convenciones de trabajo
Una secuencia de transformación es una cadena de fórmulas equivalentes donde cada renglón se obtiene del anterior mediante una ley identificable. La presentación debe ser limpia, lineal y verificable.

En cada ejercicio se espera este formato de respuesta:
- Fórmula original.
- Transformación paso a paso.
- Justificación de cada paso en forma de tabla.
- Fórmula final simplificada, FNC o FND según se solicite.
- Cuando se pida equivalencia, una verificación breve por tabla de verdad solo en los ejercicios indicados.

***

## Formato de justificación de soluciones

La entrega debe mostrar no solo el resultado, sino el razonamiento simbólico completo.

Cada solución deberá escribirse con esta plantilla:

1. **Ejercicio:** fórmula original.  
2. **Objetivo:** simplificar, obtener FNC, obtener FND o verificar equivalencia.  
3. **Tabla de justificación:**  
   - La primera fila siempre contendrá la fórmula original, con “NA” en la columna de la ley usada, porque todavía no se ha aplicado ninguna transformación.

      | Ley usada | Fórmula / equivalencia |
      |-----------|------------------------|
      | NA        | $ F_0 $                |
      | …         | $ \equiv F_1 $         |
      | …         | $ \equiv F_2 $         |
      | …         | $ \equiv F_n $         |

4. **Resultado final:** fórmula $ F_n $ destacada como respuesta.  



## Ejemplo guiado 1
Una simplificación lógica busca reducir una fórmula sin alterar su significado. 

**Ejemplo.** Simplificar:

$$
(p \land q) \lor (p \land \neg q)
$$

Justificación:

| Ley usada       | Fórmula / equivalencia                |
|-----------------|---------------------------------------|
| NA              | $ (p \land q) \lor (p \land \neg q) $ |
| distributividad | $ \equiv p \land (q \lor \neg q) $    |
| complemento     | $ \equiv p \land V $                  |
| identidad       | $ \equiv p $                          |

Resultado final: $ p $. 

***

## Ejemplo guiado 2
Transformar a FNC significa llegar a una conjunción de cláusulas disyuntivas.

**Ejemplo.** Llevar a FNC:

$$
(p \leftrightarrow q) \to r
$$

Justificación resumida:

| Ley usada        | Fórmula / equivalencia                                                                 |
|------------------|----------------------------------------------------------------------------------------|
| NA               | $ (p \leftrightarrow q) \to r $                                                        |
| condicional      | $ \equiv \neg(p \leftrightarrow q) \lor r $                                            |
| bicondicional    | $ \equiv \neg[(p \land q) \lor (\neg p \land \neg q)] \lor r $                         |
| De Morgan        | $ \equiv [\neg(p \land q) \land \neg(\neg p \land \neg q)] \lor r $                    |
| De Morgan + ¬¬   | $ \equiv [(\neg p \lor \neg q) \land (p \lor q)] \lor r $                              |
| distributividad  | $ \equiv (\neg p \lor \neg q \lor r) \land (p \lor q \lor r) $                         |

Resultado final en FNC:

$$
(\neg p \lor \neg q \lor r) \land (p \lor q \lor r)
$$

 

***

## Ejemplo guiado 3
Transformar a FND significa obtener una disyunción de términos conjuntivos. Puede verse como enumerar combinaciones de condiciones suficientes para que un servicio esté disponible.

**Ejemplo.** Llevar a FND:

$$
(p \leftrightarrow q) \to r
$$

Justificación resumida:

| Ley usada        | Fórmula / equivalencia                                                   |
|------------------|--------------------------------------------------------------------------|
| NA               | $ (p \leftrightarrow q) \to r $                                          |
| condicional      | $ \equiv \neg(p \leftrightarrow q) \lor r $                              |
| bicondicional    | $ \equiv \neg[(p \to q) \land (q \to p)] \lor r $                        |
| condicional      | $ \equiv [\neg(\neg p \lor q) \lor \neg(\neg q \lor p)] \lor r $         |
| De Morgan + ¬¬   | $ \equiv (p \land \neg q) \lor (q \land \neg p) \lor r $                 |

Resultado final en FND:

$$
(p \land \neg q) \lor (q \land \neg p) \lor r
$$

 

***

## Sección A. Clasificación
Aqui se distinguirá si una expresión ya está simplificada, si está en FNC, en FND o si aún contiene conectivos que deben eliminarse.

1. Indicar si cada fórmula está en FNC, en FND, en ambas o en ninguna:
   - $ (p \lor \neg q) \land (r \lor s) $  
   - $ (p \land q) \lor (\neg r \land s) $  
   - $ (p \lor q) \to r $  
   - $ \neg(p \land q) $  
   - $ (\neg p \lor q \lor r) \land s $  


## Sección B. Simplificar
Resolver mostrando todos los pasos en tablas de justificación y nombrando la ley usada en cada renglón.

1. $ (p \land V) \lor (q \land F) $  
2. $ (p \lor q) \land (p \lor \neg q) $  
3. $ (p \land q) \lor (p \land \neg q) $  
4. $ (p \lor \neg p) \land (q \lor \neg q) $  

***

## Sección C. Eliminación de conectivos derivados
Reescribir simplificando primero sin $ \to $ ni $ \leftrightarrow $, y luego otras leyes usando tablas de justificación.
 
1. $ \neg p \to q $  
2. $ (p \land q) \to r $  
3. $ p \to (q \lor r) $  
4. $ p \leftrightarrow (q \lor r) $  

***

## Sección E. Transformación a FNC
La FNC expresa una fórmula como una conjunción de cláusulas. 

Llevar a FNC mediante equivalencias y mostrar la secuencia completa en tabla de justificación.

1. $ (p \lor q) \to r $  
2. $ p \to (q \land r) $  
3. $ (p \land q) \to r $  
4. $ (p \leftrightarrow q) \to r $  

***

## Sección F. Transformación a FND
La FND enumera configuraciones suficientes para que la fórmula sea verdadera.

Llevar a FND mediante equivalencias y mostrar la secuencia completa en tabla de justificación.

1. $ p \to q $  
2. $ (p \lor q) \land r $  
3. $ \neg(p \land q) $  
4. $ \neg(p \leftrightarrow q) $  

***

## Sección H. Equivalencia lógica por tabla de verdad
Dos fórmulas son equivalentes cuando sus columnas finales coinciden en todas las valuaciones. En esta sección la tabla de verdad se usa como verificación puntual. 

Construir la tabla de verdad y decidir si las parejas son equivalentes.

1. $ \neg(p \land q) $ y $ \neg p \lor \neg q $  
2. $ \neg(p \lor q) $ y $ \neg p \land \neg q $  
3. $ (p \land q) \lor (p \land \neg q) $ y $ p $  

***

## Entrega
La entrega debe mostrar no solo el resultado, sino el razonamiento simbólico completo.

Cada solución deberá escribirse con esta plantilla:

1. **Ejercicio:** fórmula original.  
2. **Objetivo:** simplificar, obtener FNC, obtener FND o verificar equivalencia.  
3. **Tabla de justificación:**  

   | Ley usada | Fórmula / equivalencia |
   |-----------|------------------------|
   | NA        | $ F_0 $                |
   | …         | $ \equiv F_1 $         |
   | …         | $ \equiv F_2 $         |
   | …         | $ \equiv F_n $         |

4. **Resultado final:** fórmula $ F_n $ destacada como respuesta.  

***

## Criterios de calidad del trabajo
Una solución correcta conserva equivalencia en todos los pasos y termina en la forma pedida. Una solución clara además evita saltos injustificados, cuida paréntesis y usa con precisión los nombres de las leyes.

Se considerará trabajo bien elaborado cuando:
- Cada transformación sea equivalente a la anterior.  
- Las leyes estén bien nombradas.  
- La fórmula final sí esté en FNC o FND cuando se pida.  
- La simplificación elimine redundancias visibles.  
- La escritura sea ordenada y legible.  
