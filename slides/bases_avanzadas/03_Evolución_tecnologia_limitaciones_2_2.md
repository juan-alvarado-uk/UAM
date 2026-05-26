# Rendimiento y escalabilidad

Una base de datos no se evalúa solo por cómo modela, sino por cómo responde bajo carga real. El **rendimiento** y la **escalabilidad** son dimensiones relacionadas pero distintas que describen ese comportamiento.

---
**Rendimiento**

El rendimiento es la capacidad de una base de datos para responder con tiempos aceptables y uso razonable de recursos, bajo una carga dada.

- En otras palabras, responde a:  
  - ¿Qué tan rápido contesta una consulta?  
  - ¿Cuántos recursos consume para lograrlo?  
  - ¿Se mantiene estable bajo la carga actual?

---
**Escalabilidad**

La escalabilidad es la capacidad de sostener o mejorar ese comportamiento cuando crecen datos, usuarios o distribución geográfica.

- Esto implica:  
  - Mantener tiempos de respuesta aceptables al crecer el volumen de datos.  
  - Mantener o mejorar rendimiento al aumentar usuarios concurrentes.  
  - Adaptarse a usuarios en múltiples regiones sin degradación notable.

***

# Sistemas distribuidos y arquitectura de almacenamiento

En sistemas distribuidos actuales, una misma aplicación tiene usuarios en múltiples regiones, que interactúan con servicios desde múltiples tipos de dispositivos. Cada interacción genera lecturas y escrituras sobre la base de datos, por lo que la arquitectura de almacenamiento debe equilibrar tiempos de respuesta, consistencia y disponibilidad, algo que no siempre se consigue solo con escalar una única instancia relacional.

---
- Entorno actual:  
  - Usuarios distribuidos geográficamente.  
  - Diversos dispositivos (móvil, web, etc.).  
  - Interacciones constantes (lecturas y escrituras).

---
- Retos para la base de datos:  
  - Mantener tiempos de respuesta bajos.  
  - Mantener consistencia de la información.  
  - Mantener alta disponibilidad del servicio.  
  - Evitar depender únicamente de una instancia relacional única.

***

# Diseño de esquema y eficiencia

La combinación de alto volumen y alta concurrencia hace que las decisiones de diseño de esquema (índices, normalización, llaves) tengan impacto directo en la eficiencia de la base de datos.

---
- Índices:  
  - Aceleran consultas, pero aumentan costo de escritura.  
- Normalización:  
  - Reduce redundancia, pero puede aumentar el número de uniones.  
- Llaves (primarias y foráneas):  
  - Afectan integridad referencial y estrategias de acceso.

***

# Escalado vertical y horizontal

Escalar verticalmente significa agregar recursos a un mismo servidor (más CPU, memoria o disco), mientras que escalar horizontalmente significa agregar nodos y repartir la carga entre ellos. El escalado vertical puede ser más simple pero también puede llegar a un límite físico además de práctico; el horizontal permite crecer más, con el costo de mayor complejidad de coordinación y para mantener consistencia.

---
**Analogía coloquial**

En términos coloquiales, el escalado vertical se parece a comprar un camión más grande para transportar más mercancía, mientras que el escalado horizontal se parece a organizar una flota de camiones que comparten el trabajo. La flota puede transportar mucha mercancía, pero requiere rutas claras, coordinación entre conductores y mecanismos de control para evitar pérdidas o inconsistencias.


| Tipo de escalado | Definición técnica breve                                 | Analogía coloquial                | Ventaja principal                | Desventaja principal                               |
|------------------|----------------------------------------------------------|-----------------------------------|----------------------------------|----------------------------------------------------|
| Vertical         | Aumentar recursos de un solo servidor                    | Camión más grande                 | Simplicidad de gestión           | Límite físico y de costo                           |
| Horizontal       | Añadir más servidores y repartir la carga                | Flota de camiones                 | Mayor capacidad de crecimiento   | Mayor complejidad de coordinación y consistencia   |

***

# Replicación, partición y consenso

En bases de datos, cuando hay situaciones como las mencionadas, se debe decidir sobre **replicación** (cuántas copias de los datos existen y dónde), **partición o fragmentación** (cómo se distribuyen los datos entre nodos) y mecanismos de consenso o coordinación entre servidores. 

---
- Replicación:  
  - Múltiples copias de los datos.  
  - Mejora disponibilidad y lectura, complica sincronización.

---
- Partición / fragmentación:  
  - Datos divididos entre nodos (por rango, hash, etc.).  
  - Mejora reparto de carga, dificulta la localización de datos.

---
- Consenso / coordinación:  
  - Protocolos para acordar el estado entre servidores.  
  - Aseguran consistencia, aumentan latencia y complejidad.

***

# Cuellos de botella y combinaciones de técnicas

En entornos masivos, las consultas con muchas uniones sobre grandes volúmenes y las escrituras concurrentes en puntos centralizados pueden producir cuellos de botella. La réplica ayuda a atender más lecturas, pero las escrituras se concentran en nodos concretos. Con la fragmentación se reparten los datos entre servidores, pero es necesario pensar en cómo localizar la información y sincronizar actualizaciones.

---
Muchas arquitecturas combinan varias técnicas:  
- Réplicas de solo lectura para descargar consultas frecuentes.  
- Partición por rango, hash o id de cliente para distribuir carga de escritura.  
- Cachés intermedias para reducir la presión sobre la base principal.

---
Estas soluciones funcionan, pero muestran que el modelo relacional clásico, de una única imagen lógica de los datos, fue pensado para un escenario menos distribuido. La tensión aparece cuando se busca mantener fuertes la consistencia y coherencia en un entorno distribuido y de alta escala.

---
**Resumen de problemas y soluciones**

- Problemas:  
  - Cuellos de botella en joins masivos.  
  - Puntos únicos de escritura saturados.  
  - Dificultad para mantener consistencia.

---
- Soluciones:  
  - Réplicas para lectura.  
  - Fragmentación para escritura.  
  - Cachés para lecturas repetidas.  

La conclusión a la que se llega es que el modelo relacional clásico en el contexto de entornos altamente distribuidos provoca tensiones considerables.

***

# Rigidez del esquema y datos semiestructurados

Además de lo anterior, la rigidez del esquema frente a datos semiestructurados. XML y JSON permiten anidamientos, arreglos y campos opcionales, de modo que distintos registros comparten una base común, pero no necesariamente las mismas propiedades.

---
**Datos semiestructurados**

- Estructura flexible:  
  - Campos opcionales.  
  - Anidamiento de objetos.  
  - Arreglos de elementos.

---
**Esquema relacional**
- Dificultad para representar variación sin multiplicar columnas o tablas.  

***

# Ejemplo: catálogo de productos

En un catálogo de productos, ciertos tipos pueden requerir atributos específicos. Intentar unificar todo esto en una sola tabla de productos produce muchas columnas nulas y lógica adicional en la aplicación para interpretar qué columnas aplican a cada tipo de producto.

---

- Atributos específicos:  
  - Ropa: talla, color.  
  - Dispositivos: memoria, procesador.  
  - Alimentos: caducidad, ingredientes.

---

- Consecuencias de una sola tabla:  
  - Muchas columnas nulas.  
  - Lógica condicional compleja en la aplicación.  
  - Esquema difícil de mantener y extender.

***

# Cambios en el dominio y su impacto

Si el dominio se actualiza constantemente, tenemos:  
- Nuevos tipos de productos.  
- Nuevas propiedades.  
- Cambios en reglas de negocio.

---
Cada ajuste puede exigir:  
- Alterar el esquema.  
- Migrar datos.  
- Introducir soluciones temporales.

Todo lo cual incrementa la complejidad del sistema.

---
**En resumen...**

- Dominios dinámicos → cambios frecuentes.  
- Cada cambio repercute en:  
  - Estructura de la base.  
  - Procesos de migración.  
  - Complejidad operativa.

***

# Problemas por rigidez del esquema

Problemas típicos derivados de la rigidez del esquema son (algunos ya los hemos mencionado):

- Columnas opcionales que quedan vacías para muchos registros.  
- Reestructuración del esquema ante cambios frecuentes en el dominio.  
- Dificultad para conservar la estructura original de datos anidados sin deformarla.  
- Diseños difíciles de entender cuando el dominio admite muchas variaciones.

---
A lo anterior puede añadirse la dificultad para reutilizar datos con otros sistemas que esperan formatos semiestructurados, así como la necesidad de capas de transformación que incrementan el acoplamiento entre componentes. Cada una de estas señales indica que quizá el esquema relacional, tal como se ha definido, no es el mejor reflejo del dominio actual.


# Modelos semánticos y EER como respuesta conceptual

Para abordar estas limitaciones, se recurre a modelos semánticos de datos. Un modelo semántico pone el énfasis en el significado del dominio, las relaciones entre conceptos y las reglas de negocio, más que en detalles físicos de almacenamiento. La idea central es que un buen modelo no solo guarda datos, sino que representa con claridad qué es cada cosa, cómo se relaciona con las demás y qué restricciones rigen esas relaciones.

---
Este tipo de modelos, como el modelo Entidad‑Relación Extendido (EER), se sitúan en un nivel de abstracción más alto que las tablas físicas. Permiten dialogar con personas expertas del dominio usando un lenguaje cercano a su realidad (personas, cursos, productos, pedidos, dispositivos) y solo después se traducen a estructuras concretas de almacenamiento.

---
Los modelos semánticos ayudan a detectar inconsistencias, omisiones y ambigüedades desde etapas tempranas del diseño, lo que reduce el riesgo de que el esquema físico arrastre errores conceptuales difíciles de corregir más adelante.
