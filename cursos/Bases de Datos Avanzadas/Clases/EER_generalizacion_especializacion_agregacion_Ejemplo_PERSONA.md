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

---

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
