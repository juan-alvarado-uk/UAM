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

***

# EER: generalización, especialización y agregación

El modelo Entidad‑Relación extendido (EER) es una evolución del modelo ER clásico que añade mecanismos para expresar jerarquías, especializaciones, generalizaciones y agregaciones. La generalización permite abstraer un supertipo a partir de varios subtipos (por ejemplo, “persona” como supertipo de “estudiante”, “docente” y “administrativo”), mientras que la especialización descompone un tipo general en variantes que heredan atributos y relaciones del supertipo.

---
Estas extensiones permiten representar de forma explícita que ciertos atributos se comparten y otros se añaden solo en subtipos específicos, evitando ambigüedades como columnas opcionales poco claras.

---
Este nivel de detalle semántico prepara mejor el camino para decidir, más adelante, cómo se traducirán estas jerarquías a tablas relacionales, eligiendo entre diferentes estrategias de mapeo según las necesidades del sistema.

---

**Capacidades del EER**

- Expresa:  
  - Jerarquías de tipos.  
  - Generalizaciones y especializaciones.  
  - Agregaciones (entidades compuestas).  

---
- Beneficios:  
  - Atributos comunes y específicos bien diferenciados.  
  - Menos ambigüedad al pasar a tablas.

***

# Agregación y objetos compuestos

La agregación, por su parte, permite elevar a entidad la combinación de varias entidades y su relación, tratándola como una unidad conceptual de nivel superior. Estas ideas ayudan a modelar de forma más natural objetos compuestos, jerarquías de tipos y unidades complejas que en un esquema relacional básico se reparten en muchas tablas.

---
Por ejemplo, en un sistema de gestión de proyectos, la relación entre empleado, proyecto y rol puede considerarse como una entidad agregada que representa una asignación específica. Modelar esto explícitamente en EER facilita entender qué se está midiendo (asignación) y cómo se relaciona con otras partes del sistema, como tiempos, costos o evaluaciones.

---
Esta claridad semántica no elimina la necesidad de bases relacionales, pero sí ofrece un marco conceptual más sólido para decidir qué tablas y relaciones se necesitan, y cómo se justifican en términos del dominio.

***

# Ejemplo: “persona” y subtipos

En un sistema educativo, por ejemplo, un enfoque puramente relacional podriamos concentrar todo en una sola tabla de usuarios con muchas columnas opcionales (matrícula, área académica, salario, promedio, rol administrativo, etc.). 

---
Desde una perspectiva semántica, resulta mejor pensar en una entidad general “persona” y en subtipos con propiedades particulares, de modo que el modelo refleje que no todas las personas comparten las mismas características.

---
Este enfoque no solo mejora la comprensión, sino que también facilita la comunicación entre quienes diseñan el sistema, quienes lo implementan y quienes lo usan. Las decisiones de diseño dejan de basarse únicamente en conveniencias técnicas y se alinean mejor con la lógica del dominio, reduciendo la brecha entre “cómo se guardan los datos” y “qué significan esos datos”.

---

- Tabla única de usuarios:  
  - Muchos campos opcionales.  
  - Menor claridad semántica.

- Modelo EER con “persona” y subtipos:  
  - Atributos mejor distribuidos.  
  - Mejor alineación con el dominio educativo.


# Tabla base: PERSONA

Esta tabla concentra lo que es común a todas las personas del sistema.

```sql
CREATE TABLE persona (
    id_persona      INT PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    apellido        VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    correo          VARCHAR(150),
    telefono        VARCHAR(50)
);
```


| id_persona | nombre  | apellido | fecha_nacimiento | correo                     | telefono     |
|-----------:|---------|----------|------------------|----------------------------|--------------|
|          1 | Ana     | López    | 2000-05-10       | ana.lopez@cua.uam.mx       | 555-111-1111 |
|          2 | Juan    | Alvarado | 1980-03-22       | jalvarado@cua.uam.mx       | 555-222-2222 |
|          3 | Beatriz | Sánchez  | 1975-11-15       | beatriz.sanchez@cua.uam.mx | 555-333-3333 |

***

# Subtipo: ESTUDIANTE

Solo aplica a quienes tienen rol de estudiante (ej., matrícula, promedio, programa).

```sql
CREATE TABLE estudiante (
    id_persona      INT PRIMARY KEY,
    matricula       VARCHAR(20) NOT NULL,
    programa        VARCHAR(100),
    promedio        DECIMAL(3,2),
    fecha_ingreso   DATE,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);
```

| id_persona | matricula | programa               | promedio | fecha_ingreso |
|-----------:|-----------|------------------------|----------|---------------|
|          1 | A0123456  | Ingeniería en Sistemas | 9.1      | 2019-08-15    |

***

# Subtipo: PROFESOR

Solo aplica a quienes tienen rol docente (ej., área académica, nivel, salario).

```sql
CREATE TABLE profesor (
    id_persona      INT PRIMARY KEY,
    area_academica  VARCHAR(100),
    categoria       VARCHAR(50),   
    salario         DECIMAL(10,2),
    fecha_contratacion DATE,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);
```


| id_persona | area_academica | categoria | salario  | fecha_contratacion |
|-----------:|----------------|-----------|----------|--------------------|
|          2 | Tecnologías    | Asistente | 45000.00 | 2025-01-10         |

***

# Subtipo: ADMINISTRATIVO

Solo aplica a roles administrativos (ej., área administrativa, puesto, tipo de contrato).

```sql
CREATE TABLE administrativo (
    id_persona      INT PRIMARY KEY,
    area_admin      VARCHAR(100),
    puesto          VARCHAR(100),
    tipo_contrato   VARCHAR(50),
    salario         DECIMAL(10,2),
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);
```


| id_persona | area_admin          | puesto               | tipo_contrato   | salario  |
|-----------:|---------------------|----------------------|-----------------|----------|
|          3 | Servicios Escolares | Coordinadora de área | Tiempo completo | 38000.00 |

***

# Reconstruir la vista de ESTUDIANTE con JOIN

Para ver la información “completa” de estudiantes, combinamos lo común (persona) con lo específico (estudiante).

```sql
SELECT 
    p.id_persona,
    p.nombre,
    p.apellido,
    p.correo,
    e.matricula,
    e.programa,
    e.promedio,
    e.fecha_ingreso
FROM persona p
JOIN estudiante e
    ON p.id_persona = e.id_persona;
```


| id_persona | nombre | apellido | correo               | matricula | programa               | promedio | fecha_ingreso |
|-----------:|--------|----------|----------------------|-----------|------------------------|----------|---------------|
|          1 | Ana    | López    | ana.lopez@cua.uam.mx | A0123456  | Ingeniería en Sistemas | 9.1      | 2019-08-15    |

El JOIN “reconstruye” el subtipo **estudiante** como una vista unificada, sin columnas opcionales innecesarias.

***

# Reconstruir la vista de PROFESOR con JOIN

```sql
SELECT 
    p.id_persona,
    p.nombre,
    p.apellido,
    p.correo,
    pr.area_academica,
    pr.categoria,
    pr.salario,
    pr.fecha_contratacion
FROM persona p
JOIN profesor pr
    ON p.id_persona = pr.id_persona;
```


| id_persona | nombre | apellido | correo               | area_academica | categoria | salario | fecha_contratacion |
|-----------:|--------|----------|----------------------|----------------|-----------|---------|--------------------|
|          2 | Juan   | Alvarado | jalvarado@cua.uam.mx | Tecnologías    | Asistente | 45000   | 2025-01-10         |

***

# Reconstruir la vista de ADMINISTRATIVO con JOIN

```sql
SELECT 
    p.id_persona,
    p.nombre,
    p.apellido,
    p.correo,
    a.area_admin,
    a.puesto,
    a.tipo_contrato,
    a.salario
FROM persona p
JOIN administrativo a
    ON p.id_persona = a.id_persona;
```


| id_persona | nombre  | apellido | correo                     | area_admin          | puesto               | tipo_contrato   | salario |
|-----------:|---------|----------|----------------------------|---------------------|----------------------|-----------------|---------|
|          3 | Beatriz | Sánchez  | beatriz.sanchez@cua.uam.mx | Servicios Escolares | Coordinadora de área | Tiempo completo | 38000   |

***

# Vista unificada con tipo de persona

Para generar una vista que muestre todas las personas con su tipo (estudiante/profesor/administrativo) y atributos específicos, se puede usar un LEFT JOIN y una columna derivada para clasificar:

```sql
SELECT
    p.id_persona,
    p.nombre,
    p.apellido,
    CASE 
        WHEN e.id_persona IS NOT NULL THEN 'ESTUDIANTE'
        WHEN pr.id_persona IS NOT NULL THEN 'PROFESOR'
        WHEN a.id_persona IS NOT NULL THEN 'ADMINISTRATIVO'
        ELSE 'DESCONOCIDO'
    END AS tipo_persona,
    e.matricula,
    e.programa,
    pr.area_academica,
    pr.categoria,
    a.area_admin,
    a.puesto
FROM persona p
LEFT JOIN estudiante e
    ON p.id_persona = e.id_persona
LEFT JOIN profesor pr
    ON p.id_persona = pr.id_persona
LEFT JOIN administrativo a
    ON p.id_persona = a.id_persona;
```

Este tipo de consulta muestra cómo, partiendo de un diseño semánticamente más claro (persona + subtipos), se pueden reconstruir “usuarios” con sus propiedades sin recurrir a una única tabla con campos opcionales y llenos de nulos.


# Cierre: EER y modelo relacional

El uso de modelos semánticos y EER no reemplaza al modelo relacional, sino que lo complementa: el diseño conceptual captura el dominio con más fidelidad, y luego se decide qué partes conviene llevar a tablas clásicas y qué partes sugieren alternativas o extensiones en la arquitectura global del sistema. De este modo, el modelo relacional se mantiene como una herramienta poderosa, pero se reconoce que en dominios complejos necesita apoyarse en modelos de mayor capacidad expresiva para evitar esquemas rígidos, difíciles de mantener y poco alineados con la realidad.

- Modelo relacional:  
  - Sigue siendo central.  

- Modelos semánticos (EER):  
  - Mejoran la representación del dominio.  
  - Ayudan a evitar rigidez y desalineación.  
