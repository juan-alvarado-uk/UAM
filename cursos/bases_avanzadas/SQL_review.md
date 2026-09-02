# SQL

**Definición.** SQL (Structured Query Language) es el lenguaje estándar declarativo para interactuar con bases de datos relacionales. Es **declarativo** porque describes **qué** quieres obtener, no **cómo** obtenerlo paso a paso. 

SQL fue desarrollado por IBM en los años 70 y adoptado como estándar por ANSI e ISO, lo que significa que funciona (con variaciones menores) en casi todos los sistemas de bases de datos relacionales: MySQL, PostgreSQL, Oracle, SQL Server, SQLite. 

***

# Los tres sub-lenguajes de SQL

SQL se divide en tres categorías según su función:

## DDL - Data Definition Language

Controla la **estructura** de la base de datos: tablas, columnas, restricciones, índices. 

**Comandos principales:**
- `CREATE` - Crear nuevas estructuras
- `ALTER` - Modificar estructuras existentes
- `DROP` - Eliminar estructuras
- `TRUNCATE` - Vaciar una tabla sin eliminarla

```sql
CREATE TABLE Estudiante (
  id INT PRIMARY KEY,                    -- Llave primaria
  nombre VARCHAR(100) NOT NULL,          -- Texto obligatorio
  correo VARCHAR(100) UNIQUE,            -- Sin duplicados
  promedio DECIMAL(3,2),                 -- Número con decimales
  fecha_ingreso DATE
);
```

```sql
ALTER TABLE Estudiante 
ADD COLUMN telefono VARCHAR(15);
```

```sql
DROP TABLE Estudiante;
```

***

## DML - Data Manipulation Language

Controla el **contenido** de las tablas: insertar, consultar, actualizar, eliminar datos. 

**Comandos principales:**
- `SELECT` - Consultar datos (el más usado)
- `INSERT` - Agregar registros
- `UPDATE` - Modificar registros existentes
- `DELETE` - Eliminar registros

```sql
INSERT INTO Estudiante (id, nombre, correo, promedio, fecha_ingreso)
VALUES (1, 'Ana López', 'ana@uam.mx', 9.5, '2024-01-15');

-- Insertar múltiples registros
INSERT INTO Estudiante (id, nombre, correo, promedio, fecha_ingreso)
VALUES 
  (2, 'Carlos Ruiz', 'carlos@uam.mx', 8.7, '2024-01-15'),
  (3, 'María Torres', 'maria@uam.mx', 9.2, '2024-01-16');
```

```sql
UPDATE Estudiante 
SET promedio = 9.8, correo = 'ana.lopez@uam.mx'
WHERE id = 1;
```

```sql
DELETE FROM Estudiante 
WHERE promedio < 6.0; 
-- Ejemplo peligroso
```

***

## DCL - Data Control Language

Controla **permisos** y acceso a la base de datos.

**Comandos principales:**
- `GRANT` - Otorgar permisos
- `REVOKE` - Quitar permisos

```sql
GRANT SELECT, INSERT ON Estudiante TO 'usuario_admin';
REVOKE DELETE ON Estudiante FROM 'usuario_lectura';
```

***

# SELECT

El comando `SELECT` es el principal de SQL. Sirve para **obtener información** de las tablas.

## Estructura básica

```sql
SELECT columnas
FROM tabla
WHERE condición;
```

```sql
-- Seleccionar todas las columnas
SELECT * FROM Estudiante;

-- Seleccionar columnas específicas
SELECT nombre, promedio FROM Estudiante;

-- Con filtro (WHERE)
SELECT nombre, promedio 
FROM Estudiante 
WHERE promedio >= 9.0;

-- Con múltiples condiciones
SELECT nombre, promedio 
FROM Estudiante 
WHERE promedio >= 9.0 AND fecha_ingreso >= '2024-01-01';

-- con LIKE
SELECT nombre 
FROM Estudiante 
WHERE promedio > 9.0 OR correo LIKE '%@uam.mx';
```

# ORDER BY - Ordenar resultados

```sql
-- Orden ascendente (por default)
SELECT nombre, promedio 
FROM Estudiante 
ORDER BY promedio ASC;

-- Orden descendente
SELECT nombre, promedio 
FROM Estudiante 
ORDER BY promedio DESC;

-- Ordenar por múltiples columnas
SELECT nombre, promedio 
FROM Estudiante 
ORDER BY promedio DESC, nombre ASC;
```

# Funciones agregadas

Las funciones agregadas calculan un **valor único** a partir de múltiples filas. 

**Funciones principales:**
- `COUNT()` - Contar registros
- `SUM()` - Sumar valores
- `AVG()` - Calcular promedio
- `MAX()` - Obtener máximo
- `MIN()` - Obtener mínimo

```sql
-- Contar total de estudiantes
SELECT COUNT(*) AS total_estudiantes 
FROM Estudiante;

-- Promedio general
SELECT AVG(promedio) AS promedio_general 
FROM Estudiante;

-- Mejor y peor promedio
SELECT MAX(promedio) AS mejor, MIN(promedio) AS peor 
FROM Estudiante;
```


# GROUP BY - Agrupar datos

`GROUP BY` agrupa filas con valores similares y permite aplicar funciones agregadas **por grupo**. 

```sql
-- Promedio por fecha de ingreso
SELECT fecha_ingreso, AVG(promedio) AS promedio_grupo
FROM Estudiante
GROUP BY fecha_ingreso;
```


# HAVING - Filtrar grupos

`HAVING` es como `WHERE`, pero para **grupos** (después de `GROUP BY`). 

```sql
-- Solo mostrar fechas con más de 3 estudiantes
SELECT fecha_ingreso, COUNT(*) AS total
FROM Estudiante
GROUP BY fecha_ingreso
HAVING COUNT(*) > 3;
```

**Diferencia:**
- `WHERE` filtra **filas** antes de agrupar
- `HAVING` filtra **grupos** después de agrupar

***

# JOIN - Combinar tablas

`JOIN` permite unir información de **múltiples tablas** relacionadas.

## INNER JOIN - Solo coincidencias
```sql
SELECT e.nombre, i.materia
FROM Estudiante e
INNER JOIN Inscripcion i ON e.id = i.id_estudiante;
```

## LEFT JOIN - Todos de la izquierda
```sql
SELECT e.nombre, i.materia
FROM Estudiante e
LEFT JOIN Inscripcion i ON e.id = i.id_estudiante;
```

## RIGHT JOIN - Todos de la derecha
```sql
SELECT e.nombre, i.materia
FROM Estudiante e
RIGHT JOIN Inscripcion i ON e.id = i.id_estudiante;
```

## Múltiples JOINs
```sql
-- Si no se especifíca INNER, LEFT o RIGHT, por default es INNER
SELECT e.nombre, m.nombre AS materia, p.nombre AS profesor
FROM Estudiante e
  JOIN Inscripcion i ON e.id = i.id_estudiante
  JOIN Materia m ON i.id_materia = m.id
  JOIN Profesor p ON m.id_profesor = p.id;
```


# UNION - Combinar consultas

`UNION` combina los **resultados** de dos o más consultas `SELECT`. 

**Reglas:**
- Mismo número de columnas
- Tipos de datos compatibles
- `UNION` elimina duplicados, `UNION ALL` los conserva

```sql
-- Todos los nombres (estudiantes y profesores)
SELECT nombre FROM Estudiante
UNION
SELECT nombre FROM Profesor;

-- Con UNION ALL (incluye duplicados)
SELECT nombre FROM Estudiante
UNION ALL
SELECT nombre FROM Profesor;
```

***

# ORDEN DE EJECUCIÓN: Lo más importante

**NOTA:** El orden en que se **escriben** las cláusulas NO es el orden en que SQL las **ejecuta**. 

# Orden de escritura (sintaxis obligatoria):
```sql
SELECT columnas                    -- 1
FROM tabla                         -- 2
WHERE condición                    -- 3
GROUP BY columnas                  -- 4
HAVING condición_grupo             -- 5
ORDER BY columnas                  -- 6
```

# Orden de ejecución real (semántica interna):
```
1. FROM (y JOIN)     -- Identifica y combina las tablas fuente
2. WHERE             -- Filtra filas individuales
3. GROUP BY          -- Agrupa las filas filtradas
4. HAVING            -- Filtra grupos
5. SELECT            -- Selecciona y calcula columnas
6. ORDER BY          -- Ordena el resultado final
```

# WHERE no puede usar alias de SELECT

```sql
-- ERROR - El alias aún no existe cuando se ejecuta WHERE
SELECT nombre, promedio * 10 AS puntos
FROM Estudiante
WHERE puntos > 90;

-- CORRECTO usa 'promedio'
SELECT nombre, promedio * 10 AS puntos
FROM Estudiante
WHERE promedio * 10 > 90;
```

# HAVING SÍ puede usar funciones agregadas

```sql
-- CORRECTO - HAVING se ejecuta después de GROUP BY
SELECT fecha_ingreso, COUNT(*) AS total
FROM Estudiante
GROUP BY fecha_ingreso
HAVING COUNT(*) > 5;
```

# ORDER BY SÍ puede (debe) usar alias de SELECT

```sql
-- CORRECTO - ORDER BY se ejecuta al final
SELECT nombre, promedio * 10 AS puntos
FROM Estudiante
ORDER BY puntos DESC;
```

# Ejemplo completo

```sql
-- Mostrar materias populares con buen rendimiento
SELECT 
  m.nombre AS materia,
  COUNT(i.id_estudiante) AS total_inscritos,
  AVG(e.promedio) AS promedio_grupo,
  MAX(e.promedio) AS mejor_alumno
FROM Materia m
  JOIN Inscripcion i ON m.id = i.id_materia
  JOIN Estudiante e ON i.id_estudiante = e.id
WHERE e.promedio >= 7.0                      -- Solo estudiantes aprobados
GROUP BY m.nombre                            -- Agrupar por materia
HAVING COUNT(i.id_estudiante) > 5            -- Solo materias con más de 5
ORDER BY total_inscritos DESC, promedio_grupo DESC;

```

**Ejecución paso a paso:**
1. **FROM + JOIN:** Combina Materia, Inscripcion y Estudiante
2. **WHERE:** Filtra solo estudiantes con promedio ≥ 7.0
3. **GROUP BY:** Agrupa por nombre de materia
4. **HAVING:** Filtra grupos con más de 5 estudiantes
5. **SELECT:** Calcula COUNT, AVG, MAX y crea los alias
6. **ORDER BY:** Ordena por inscritos y luego por promedio
