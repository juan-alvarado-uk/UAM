# Rendimiento, escalabilidad y rigidez del esquema

Una base de datos no se evalúa solo por cómo modela, sino por cómo **responde bajo carga real**. 

---
El **rendimiento** es la capacidad de responder con **tiempos aceptables** y **uso razonable de recursos**. 

---
La **escalabilidad** es la capacidad de **sostener o mejorar** ese comportamiento **cuando crecen datos, usuarios o distribución geográfica**. 

---

En sistemas distribuidos actuales, una misma aplicación tiene usuarios en múltiples regiones, que interactúan con servicios desde multiples tipos de dispositivos. Cada interacción genera lecturas y escrituras sobre la base de datos, por lo que la arquitectura de almacenamiento debe equilibrar tiempos de respuesta, consistencia y disponibilidad, algo que no siempre se consigue solo con escalar una única instancia relacional. 

---
La combinación de alto volumen y alta concurrencia hace que las decisiones de diseño de esquema (índices, normalización, claves) tengan impacto directo en la eficiancia de la base de datos. 

---

Escalar verticalmente significa agregar recursos a un mismo servidor (más CPU, memoria o disco), mientras que escalar horizontalmente significa agregar nodos y repartir la carga entre ellos. El escalado vertical suele ser más simple pero puede llegar a un límite físico (por ejemplo, cuando una máquina virtual en la nube ya no puede crecer más) además de pŕactico; el horizontal permite crecer más, a costa de mayor complejidad de coordinación y consistencia. 

---

En términos coloquiales, el escalado vertical se parece a comprar un camión más grande para transportar más mercancía, mientras que el escalado horizontal se parece a organizar una flota de camiones que comparten el trabajo. La flota puede transportar mucha mercancia, pero requiere rutas claras, coordinación entre conductores y mecanismos de control para evitar pérdidas o inconsistencias. 

---

En bases de datos, esto se traduce en decisiones sobre replicación (cuántas copias de los datos existen y dónde), partición o fragmentación (cómo se distribuyen los datos entre nodos) y mecanismos de consenso o coordinación entre servidores. Cada estrategia introduce ventajas pero también complejidad adicional en el diseño y la operación del sistema. 

***

*En entornos masivos, las consultas con muchas uniones sobre grandes volúmenes y las escrituras concurrentes en puntos centralizados pueden producir cuellos de botella*. La réplica ayuda a atender más lecturas, pero las escrituras se concentran en nodos concretos. Con la fragmentación se reparten los datos entre servidores, pero es necesario pensar en cómo localizar la información y sincronizar actualizaciones. 

---

Muchas arquitecturas combinan varias técnicas:  
- Réplicas de solo lectura para descargar consultas frecuentes.  
- Partición por rango, hash o clave de cliente para distribuir carga de escritura.  
- Cachés intermedias para reducir la presión sobre la base principal. 

---

Estas soluciones funcionan, pero muestran que el **modelo relacional clásico**, de una **única imagen lógica de los datos**, fue pensado para un escenario **menos distribuido**. La tensión aparece cuando se busca mantener fuertes la consistencia y coherencia en un entorno distribuido y de alta escala.

***

Además de lo anterior, la **rigidez del esquema** frente a datos **semiestructurados**. *XML* y *JSON* permiten anidamientos, arreglos y campos opcionales, de modo que 
- *distintos registros comparten una base común, pero no necesariamente las mismas propiedades*.  

---

Por ejemplo, en un catálogo de productos, ciertos tipos pueden requerir atributos específicos (talla y color para ropa, memoria y procesador para dispositivos, caducidad e ingredientes para alimentos). Intentar unificar todo esto en una sola tabla de productos suele producir gran cantidad de columnas nulas y lógica adicional en la aplicación para interpretar qué columnas aplican a cada tipo de producto. 

---

Cuando el dominio se actualiza con frecuencia (nuevos tipos de productos, nuevas propiedades, cambios en reglas de negocio), cada ajuste puede exigir alterar el esquema, migrar datos o introducir soluciones temporales que incrementan la complejidad del sistema. Esto es especialmente costoso en entornos donde el tiempo de inactividad debe ser mínimo. 

***

Problemas típicos derivados de la rigidez del esquema son (algunos ya los hemos mencionado):

- Columnas opcionales que quedan vacías para muchos registros.  
- Reestructuración del esquema ante cambios frecuentes en el dominio.  
- Dificultad para conservar la estructura original de datos anidados sin deformarla.  
- Diseños difíciles de entender cuando el dominio admite muchas variaciones. 

A estos puntos puede añadirse la *dificultad para reutilizar datos con otros sistemas que esperan formatos semiestructurados*, así como la necesidad de capas de transformación que incrementan el acoplamiento entre componentes. Cada una de estas señales indica que quizá el esquema relacional, tal como se ha definido, no es el mejor **reflejo del dominio actual**. 

***

## Modelos semánticos y EER como respuesta conceptual

Para abordar estas limitaciones, se recurre a **modelos semánticos de datos**. Un **modelo semántico** pone el énfasis en el **significado del dominio**, las relaciones entre conceptos y las reglas de negocio, más que en detalles físicos de almacenamiento. La idea central es que *un buen modelo no solo guarda datos, sino que representa con claridad qué es cada cosa, cómo se relaciona con las demás y qué restricciones rigen esas relaciones*. 

Este tipo de modelos, como el modelo **Entidad‑Relación Extendido (EER)**, se sitúan en un nivel de abstracción más alto que las tablas físicas. *Permiten dialogar con personas expertas del dominio usando un lenguaje cercano a su realidad (personas, cursos, productos, pedidos, dispositivos) y solo después se traducen a estructuras concretas de almacenamiento.* 

*Los modelos semánticos ayudan a detectar inconsistencias, omisiones y ambigüedades desde etapas tempranas del diseño, lo que reduce el riesgo de que el esquema físico arrastre errores conceptuales difíciles de corregir más adelante.* 

***

El **modelo Entidad‑Relación extendido (EER)** es una evolución del modelo ER clásico que añade mecanismos para expresar *jerarquías*, *especializaciones*, *generalizaciones* y *agregaciones*. La **generalización** permite abstraer un *supertipo* a partir de varios *subtipos* (por ejemplo, “persona” como supertipo de “estudiante”, “docente” y “administrativo”), mientras que la **especialización** descompone un tipo general en variantes que heredan atributos y relaciones del *supertipo*. 

Estas extensiones permiten representar de forma explícita que ciertos atributos se comparten y otros se añaden solo en subtipos específicos, *evitando ambigüedades como columnas opcionales poco claras*. 

*Este nivel de detalle semántico prepara mejor el camino para decidir, más adelante, cómo se traducirán estas jerarquías a tablas relacionales, eligiendo entre diferentes estrategias de mapeo según las necesidades del sistema.* 

***

La **agregación**, por su parte, permite elevar a entidad la *combinación de varias entidades y su relación*, tratándola como una unidad conceptual de nivel superior. Estas ideas ayudan a modelar de forma más natural objetos compuestos, jerarquías de tipos y unidades complejas que en un esquema relacional básico se reparten en muchas tablas. 

Por ejemplo, en un sistema de gestión de proyectos, la relación entre empleado, proyecto y rol puede considerarse como una entidad agregada que representa una asignación específica. Modelar esto explícitamente en EER facilita entender qué se está midiendo (asignación) y cómo se relaciona con otras partes del sistema, como tiempos, costos o evaluaciones. 

Esta claridad semántica no elimina la necesidad de bases relacionales, pero sí ofrece un marco conceptual más sólido para decidir qué tablas y relaciones se necesitan, y cómo se justifican en términos del dominio.

***

En un sistema educativo, por ejemplo, un enfoque puramente relacional podría concentrar todo en una sola tabla de usuarios con muchas columnas opcionales (matrícula, área académica, salario, promedio, rol administrativo, etc.). Desde una perspectiva semántica, resulta más claro pensar en una entidad general “persona” y en subtipos con propiedades particulares, de modo que el modelo refleje que no todas las personas comparten las mismas características. 

Este enfoque no solo mejora la comprensión, sino que también facilita la comunicación entre quienes diseñan el sistema, quienes lo implementan y quienes lo usan. Las decisiones de diseño dejan de basarse únicamente en conveniencias técnicas y se alinean mejor con la lógica del dominio, reduciendo la brecha entre “cómo se guardan los datos” y “qué significan esos datos”. 

***

# Actividad 2: Rediseño semántico usando EER

# Para cerrar

El uso de modelos semánticos y EER no reemplaza al modelo relacional, sino que lo complementa: el diseño conceptual captura el dominio con más fidelidad, y luego se decide qué partes conviene llevar a tablas clásicas y qué partes sugieren alternativas o extensiones en la arquitectura global del sistema. De este modo, el modelo relacional se mantiene como una herramienta poderosa, pero se reconoce que en dominios complejos necesita apoyarse en modelos de mayor capacidad expresiva para evitar esquemas rígidos, difíciles de mantener y poco alineados con la realidad. 