# SQL

**Definición.** SQL (Structured Query Language) es el lenguaje estándar declarativo para interactuar con bases de datos relacionales. Es **declarativo** porque describes **qué** quieres obtener, no **cómo** obtenerlo paso a paso.

SQL fue desarrollado por IBM en los años 70 y adoptado como estándar por ANSI e ISO, por lo que funciona, con variaciones menores, en sistemas como MySQL, PostgreSQL, Oracle, SQL Server y SQLite.

---

# Los tres sublenguajes de SQL

SQL se divide en tres categorías según su función.

## DDL - Data Definition Language

Controla la **estructura** de la base de datos: tablas, columnas, restricciones e índices.

**Comandos principales:**
- `CREATE` - Crear nuevas estructuras.
- `ALTER` - Modificar estructuras existentes.
- `DROP` - Eliminar estructuras.
- `TRUNCATE` - Vaciar una tabla sin eliminarla.

### CREATE TABLE

```sql
CREATE TABLE Estudiante (
  id INT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) UNIQUE,
  promedio DECIMAL(3,2),
  fecha_ingreso DATE
);
```

### Resultado estructural de `CREATE TABLE Estudiante`

La tabla queda creada **sin registros**, pero con su estructura definida.

| id | nombre | correo | promedio | fecha_ingreso |
|---:|---|---|---:|---|
| *(sin filas)* |  |  |  |  |

### ALTER TABLE

```sql
ALTER TABLE Estudiante
ADD COLUMN telefono VARCHAR(15);
```

### Resultado estructural después de `ALTER TABLE`

La tabla sigue sin registros, pero ahora tiene una nueva columna.

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| *(sin filas)* |  |  |  |  |  |

### DROP TABLE

```sql
DROP TABLE Estudiante;
```

### Efecto de `DROP TABLE`

La tabla `Estudiante` deja de existir en la base de datos.

---

## DML - Data Manipulation Language

Controla el **contenido** de las tablas: insertar, consultar, actualizar y eliminar datos.

**Comandos principales:**
- `SELECT` - Consultar datos (el más usado).
- `INSERT` - Agregar registros.
- `UPDATE` - Modificar registros existentes.
- `DELETE` - Eliminar registros.

### INSERT de un registro

```sql
INSERT INTO Estudiante (id, nombre, correo, promedio, fecha_ingreso)
VALUES (1, 'Ana López', 'ana@uam.mx', 9.5, '2024-01-15');
```

### Resultado después del primer `INSERT`

| id | nombre | correo | promedio | fecha_ingreso |
|---:|---|---|---:|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 |

### INSERT de múltiples registros

```sql
INSERT INTO Estudiante (id, nombre, correo, promedio, fecha_ingreso)
VALUES
  (2, 'Carlos Ruiz', 'carlos@uam.mx', 8.7, '2024-01-15'),
  (3, 'María Torres', 'maria@uam.mx', 9.2, '2024-01-16');
```

### Resultado después del `INSERT` múltiple

| id | nombre       | correo        | promedio | fecha_ingreso |
|---:|--------------|---------------|---------:|---------------|
|  1 | Ana López    | ana@uam.mx    |      9.5 | 2024-01-15    |
|  2 | Carlos Ruiz  | carlos@uam.mx |      8.7 | 2024-01-15    |
|  3 | María Torres | maria@uam.mx  |      9.2 | 2024-01-16    |

### UPDATE

```sql
UPDATE Estudiante
SET promedio = 9.8, correo = 'ana.lopez@uam.mx'
WHERE id = 1;
```

### Resultado después de `UPDATE`

| id | nombre | correo | promedio | fecha_ingreso |
|---:|---|---|---:|---|
| 1 | Ana López | ana.lopez@uam.mx | 9.8 | 2024-01-15 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 |

### DELETE

```sql
DELETE FROM Estudiante
WHERE promedio < 6.0;
```

### Observación

En este ejemplo no se elimina ninguna fila porque ningún registro tiene `promedio < 6.0`.

---

## DCL - Data Control Language

Controla **permisos** y acceso a la base de datos.

**Comandos principales:**
- `GRANT` - Otorgar permisos.
- `REVOKE` - Quitar permisos.

```sql
GRANT SELECT, INSERT ON Estudiante TO 'usuario_admin';
REVOKE DELETE ON Estudiante FROM 'usuario_lectura';
```

### Efecto conceptual

- `usuario_admin` puede consultar e insertar en `Estudiante`.
- `usuario_lectura` ya no puede ejecutar `DELETE` sobre `Estudiante`.

---

# Base de ejemplo para consultas

Para los ejemplos de `SELECT`, `GROUP BY` y `JOIN`, se usará una base pequeña con varias tablas y pocos registros, para que quepa en pantalla y permita mostrar resultados intermedios.

## Tabla `Estudiante`

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Tabla `Materia`

| id | nombre | id_profesor |
|---:|---|---:|
| 10 | BD | 100 |
| 11 | Redes | 101 |
| 12 | IA | 102 |

## Tabla `Profesor`

|  id | nombre    |
|----:|-----------|
| 100 | Dr. Soto  |
| 101 | Dra. Vega |
| 102 | Dr. Ríos  |

## Tabla `Inscripcion`

| id_estudiante | id_materia |
|---:|---:|
| 1 | 10 |
| 1 | 12 |
| 2 | 10 |
| 3 | 11 |
| 4 | 10 |

---

# SELECT

El comando `SELECT` es el principal de SQL. Sirve para **obtener información** de las tablas.

## Estructura básica

```sql
SELECT columnas
FROM tabla
WHERE condición;
```

```sql
SELECT nombre, promedio
FROM Estudiante;
```

## Paso 1: FROM Estudiante

Aquí **no se discrimina ninguna columna todavía**. La tabla de trabajo conserva todo lo que viene de `Estudiante`.

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Paso 2: SELECT nombre, promedio

Hasta este momento se proyectan solo las columnas pedidas.

| nombre | promedio |
|---|---:|
| Ana López | 9.5 |
| Carlos Ruiz | 8.7 |
| María Torres | 9.2 |
| Luis Pérez | 6.8 |

---

# WHERE

```sql
SELECT nombre, promedio
FROM Estudiante
WHERE promedio >= 9.0;
```

## Paso 1: FROM Estudiante

Se conserva la tabla completa con todas sus columnas.

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Paso 2: WHERE promedio >= 9.0

Primero se filtran filas, pero todavía sin reducir columnas.

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |

## Paso 3: SELECT nombre, promedio

| nombre | promedio |
|---|---:|
| Ana López | 9.5 |
| María Torres | 9.2 |

---

# ORDER BY - Ordenar resultados

```sql
SELECT nombre, promedio
FROM Estudiante
ORDER BY promedio DESC;
```

## Resultado ordenado

| nombre | promedio |
|---|---:|
| Ana López | 9.5 |
| María Torres | 9.2 |
| Carlos Ruiz | 8.7 |
| Luis Pérez | 6.8 |

---

# Funciones agregadas

Las funciones agregadas calculan un **valor único** a partir de múltiples filas.

**Funciones principales:**
- `COUNT()` - Contar registros.
- `SUM()` - Sumar valores.
- `AVG()` - Calcular promedio.
- `MAX()` - Obtener máximo.
- `MIN()` - Obtener mínimo.

```sql
SELECT COUNT(*) AS total_estudiantes
FROM Estudiante;

SELECT AVG(promedio) AS promedio_general
FROM Estudiante;

SELECT MAX(promedio) AS mejor, MIN(promedio) AS peor
FROM Estudiante;
```

## Resultados

| total_estudiantes |
|---:|
| 4 |

| promedio_general |
|---:|
| 8.55 |

| mejor | peor |
|---:|---:|
| 9.5 | 6.8 |

---

# GROUP BY - Agrupar datos

`GROUP BY` agrupa filas con valores similares y permite aplicar funciones agregadas **por grupo**.

```sql
SELECT fecha_ingreso, AVG(promedio) AS promedio_grupo
FROM Estudiante
GROUP BY fecha_ingreso;
```

## Paso 1: FROM Estudiante

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Paso 2: GROUP BY fecha_ingreso

### Grupo `2024-01-15`

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |

### Grupo `2024-01-16`

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Paso 3: SELECT fecha_ingreso, AVG(promedio)

| fecha_ingreso | promedio_grupo |
|---|---:|
| 2024-01-15 | 9.10 |
| 2024-01-16 | 8.00 |

---

# HAVING - Filtrar grupos

`HAVING` es como `WHERE`, pero para **grupos** después de `GROUP BY`.

Para que se vea realmente el filtrado de grupos, en este ejemplo se agregan más estudiantes.

## Tabla `Estudiante` usada aquí

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 |
| 6 | Jorge Nava | jorge@uam.mx | 7.9 | 2024-01-17 | 555-1006 |
| 7 | Sofía León | sofia@uam.mx | 9.0 | 2024-01-17 | 555-1007 |

```sql
SELECT fecha_ingreso, COUNT(*) AS total
FROM Estudiante
GROUP BY fecha_ingreso
HAVING COUNT(*) > 2;
```

## Paso 1: FROM Estudiante

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 |
| 6 | Jorge Nava | jorge@uam.mx | 7.9 | 2024-01-17 | 555-1006 |
| 7 | Sofía León | sofia@uam.mx | 9.0 | 2024-01-17 | 555-1007 |

## Paso 2: GROUP BY fecha_ingreso

### Grupo `2024-01-15`

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |

### Grupo `2024-01-16`

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

### Grupo `2024-01-17`

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 |
| 6 | Jorge Nava | jorge@uam.mx | 7.9 | 2024-01-17 | 555-1006 |
| 7 | Sofía León | sofia@uam.mx | 9.0 | 2024-01-17 | 555-1007 |

## Paso 3: HAVING COUNT(*) > 2

Aquí se eliminan los grupos con 2 registros y solo permanece el grupo que cumple la condición.

### Grupo que sobrevive

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 |
| 6 | Jorge Nava | jorge@uam.mx | 7.9 | 2024-01-17 | 555-1006 |
| 7 | Sofía León | sofia@uam.mx | 9.0 | 2024-01-17 | 555-1007 |

## Paso 4: SELECT fecha_ingreso, COUNT(*) AS total

| fecha_ingreso | total |
|---|---:|
| 2024-01-17 | 3 |

---

# JOIN - Combinar tablas

`JOIN` permite unir información de múltiples tablas relacionadas.

## INNER JOIN - Solo coincidencias

```sql
SELECT e.nombre, i.id_materia
FROM Estudiante e
INNER JOIN Inscripcion i ON e.id = i.id_estudiante;
```

## Paso 1: FROM Estudiante e

Todavía se conservan **todas** las columnas de `Estudiante`.

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Paso 2: INNER JOIN con Inscripcion i

Después del `JOIN`, la tabla intermedia contiene las columnas de ambas tablas involucradas.

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia |
|---:|---|---|---:|---|---|---:|---:|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 10 |
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 12 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 | 2 | 10 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 | 3 | 11 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 | 4 | 10 |

## Paso 3: SELECT e.nombre, i.id_materia

| nombre | id_materia |
|---|---:|
| Ana López | 10 |
| Ana López | 12 |
| Carlos Ruiz | 10 |
| María Torres | 11 |
| Luis Pérez | 10 |

---

## LEFT JOIN - Todos de la izquierda

Para que el `LEFT JOIN` se aprecie mejor, en este ejemplo se agrega un estudiante sin inscripción.

### Tabla `Estudiante` usada aquí

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 |

### Tabla `Inscripcion` usada aquí

| id_estudiante | id_materia |
|---:|---:|
| 1 | 10 |
| 1 | 12 |
| 2 | 10 |
| 3 | 11 |
| 4 | 10 |

```sql
SELECT e.nombre, i.id_materia
FROM Estudiante e
LEFT JOIN Inscripcion i ON e.id = i.id_estudiante;
```

## Paso 1: FROM Estudiante e

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 |

## Paso 2: LEFT JOIN con Inscripcion i

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia |
|---:|---|---|---:|---|---|---:|---:|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 10 |
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 12 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 | 2 | 10 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 | 3 | 11 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 | 4 | 10 |
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 | NULL | NULL |

## Paso 3: SELECT e.nombre, i.id_materia

| nombre | id_materia |
|---|---:|
| Ana López | 10 |
| Ana López | 12 |
| Carlos Ruiz | 10 |
| María Torres | 11 |
| Luis Pérez | 10 |
| Elena Gil | NULL |

---

## LEFT JOIN + WHERE paso a paso

Este caso ayuda a explicar por qué un filtro en `WHERE` puede eliminar filas que venían del `LEFT JOIN`.

```sql
SELECT e.nombre, i.id_materia
FROM Estudiante e
LEFT JOIN Inscripcion i ON e.id = i.id_estudiante
WHERE i.id_materia = 10;
```

## Paso 1: FROM + LEFT JOIN

Antes del `SELECT`, la tabla de trabajo todavía tiene todas las columnas que resultaron del `JOIN`.

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia |
|---:|---|---|---:|---|---|---:|---:|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 10 |
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 12 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 | 2 | 10 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 | 3 | 11 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 | 4 | 10 |
| 5 | Elena Gil | elena@uam.mx | 8.1 | 2024-01-17 | 555-1005 | NULL | NULL |

## Paso 2: WHERE i.id_materia = 10

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia |
|---:|---|---|---:|---|---|---:|---:|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 10 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 | 2 | 10 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 | 4 | 10 |

## Paso 3: SELECT e.nombre, i.id_materia

| nombre | id_materia |
|---|---:|
| Ana López | 10 |
| Carlos Ruiz | 10 |
| Luis Pérez | 10 |

## Resultado

Aunque se escribió `LEFT JOIN`, el `WHERE` quitó las filas con `NULL`, por lo que Elena ya no aparece.

---

## RIGHT JOIN - Todos de la derecha

Para que el `RIGHT JOIN` se aprecie al mismo nivel de detalle que el `LEFT JOIN`, en este ejemplo se agrega una inscripción sin estudiante asociado.

### Tabla `Estudiante` usada aquí

| id | nombre | correo | promedio | fecha_ingreso | telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

### Tabla `Inscripcion` usada aquí

| id_estudiante | id_materia |
|---:|---:|
| 1 | 10 |
| 1 | 12 |
| 2 | 10 |
| 3 | 11 |
| 4 | 10 |
| 99 | 12 |

```sql
SELECT e.nombre, i.id_materia
FROM Estudiante e
RIGHT JOIN Inscripcion i ON e.id = i.id_estudiante;
```

## Paso 1: FROM Estudiante e

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono |
|---:|---|---|---:|---|---|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 |

## Paso 2: RIGHT JOIN con Inscripcion i

Se conservan todas las filas de la tabla de la derecha, incluso si no tienen coincidencia en `Estudiante`.

| e.id | e.nombre | e.correo | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia |
|---:|---|---|---:|---|---|---:|---:|
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 10 |
| 1 | Ana López | ana@uam.mx | 9.5 | 2024-01-15 | 555-1001 | 1 | 12 |
| 2 | Carlos Ruiz | carlos@uam.mx | 8.7 | 2024-01-15 | 555-1002 | 2 | 10 |
| 3 | María Torres | maria@uam.mx | 9.2 | 2024-01-16 | 555-1003 | 3 | 11 |
| 4 | Luis Pérez | luis@uam.mx | 6.8 | 2024-01-16 | 555-1004 | 4 | 10 |
| NULL | NULL | NULL | NULL | NULL | NULL | 99 | 12 |

## Paso 3: SELECT e.nombre, i.id_materia

| nombre       | id_materia |
|--------------|-----------:|
| Ana López    |         10 |
| Ana López    |         12 |
| Carlos Ruiz  |         10 |
| María Torres |         11 |
| Luis Pérez   |         10 |
| NULL         |         12 |

## Resultado

La fila con `i.id_estudiante = 99` permanece porque `RIGHT JOIN` conserva todas las filas de `Inscripcion`, aunque no exista un estudiante correspondiente.

---

## Múltiples JOINs

```sql
SELECT e.nombre as estudiante, m.nombre AS materia, p.nombre AS profesor
FROM Estudiante e
  JOIN Inscripcion i ON e.id = i.id_estudiante
  JOIN Materia m ON i.id_materia = m.id
  JOIN Profesor p ON m.id_profesor = p.id;
```

## Paso 1: FROM Estudiante e

| e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono |
|-----:|--------------|---------------|-----------:|-----------------|------------|
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |
|    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   |
|    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   |
|    4 | Luis Pérez   | luis@uam.mx   |        6.8 | 2024-01-16      | 555-1004   |

## Paso 2: JOIN con Inscripción i

| e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia |
|-----:|--------------|---------------|-----------:|-----------------|------------|----------------:|-------------:|
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |               1 |           10 |
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |               1 |           12 |
|    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   |               2 |           10 |
|    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   |               3 |           11 |
|    4 | Luis Pérez   | luis@uam.mx   |        6.8 | 2024-01-16      | 555-1004   |               4 |           10 |

## Paso 3: JOIN con Materia m

| e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia | m.id | m.nombre | m.id_profesor |
|-----:|--------------|---------------|-----------:|-----------------|------------|-----------------|-------------:|-----:|----------|--------------:|
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   | 1               |           10 |   10 | BD       |           100 |
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   | 1               |           12 |   12 | IA       |           102 |
|    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   | 2               |           10 |   10 | BD       |           100 |
|    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   | 3               |           11 |   11 | Redes    |           101 |
|    4 | Luis Pérez   | luis@uam.mx   |        6.8 | 2024-01-16      | 555-1004   | 4               |           10 |   10 | BD       |           100 |

## Paso 4: JOIN con Profesor p

| e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono | i.id_estudiante | i.id_materia | m.id | m.nombre | m.id_profesor | p.id | p.nombre  |
|-----:|--------------|---------------|-----------:|-----------------|------------|-----------------|-------------:|-----:|----------|--------------:|------|-----------|
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   | 1               |           10 |   10 | BD       |           100 | 100  | Dr.Soto   |
|    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   | 1               |           12 |   12 | IA       |           102 | 102  | Dr. Ríos  |
|    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   | 2               |           10 |   10 | BD       |           100 | 100  | Dr.Soto   |
|    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   | 3               |           11 |   11 | Redes    |           101 | 101  | Dra. Vega |
|    4 | Luis Pérez   | luis@uam.mx   |        6.8 | 2024-01-16      | 555-1004   | 4               |           10 |   10 | BD       |           100 | 100  | Dr.Soto   |


## Paso 5: SELECT final

```sql
SELECT e.nombre as estudiante, m.nombre AS materia, p.nombre AS profesor ...
```

| estudiante   | materia | profesor  |
|--------------|---------|-----------|
| Ana López    | BD      | Dr. Soto  |
| Ana López    | IA      | Dr. Ríos  |
| Carlos Ruiz  | BD      | Dr. Soto  |
| María Torres | Redes   | Dra. Vega |
| Luis Pérez   | BD      | Dr. Soto  |

---

# UNION - Combinar consultas

`UNION` combina los resultados de dos o más consultas `SELECT`.

**Reglas:**
- Mismo número de columnas.
- Tipos de datos compatibles.
- `UNION` elimina duplicados y `UNION ALL` los conserva.

```sql
SELECT nombre FROM Estudiante
UNION
SELECT nombre FROM Profesor;
```

## Resultado

| nombre |
|---|
| Ana López |
| Carlos Ruiz |
| María Torres |
| Luis Pérez |
| Dr. Soto |
| Dra. Vega |
| Dr. Ríos |

---

# ORDEN DE EJECUCIÓN: Lo más importante

**NOTA:** El orden en que se escriben las cláusulas no es el orden en que SQL las ejecuta.

## Orden de escritura

```sql
SELECT columnas                    -- 1
FROM tabla                         -- 2
WHERE condición                    -- 3
GROUP BY columnas                  -- 4
HAVING condición_grupo             -- 5
ORDER BY columnas                  -- 6
```

## Orden de ejecución real

1. `FROM` y `JOIN` - Identifica y combina las tablas fuente.
2. `WHERE` - Filtra filas individuales.
3. `GROUP BY` - Agrupa las filas filtradas.
4. `HAVING` - Filtra grupos.
5. `SELECT` - Selecciona y calcula columnas.
6. `ORDER BY` - Ordena el resultado final.

---

# WHERE no puede usar alias de SELECT

```sql
SELECT nombre, promedio * 10 AS puntos
FROM Estudiante
WHERE puntos > 90;
```

## Explicación

Esto produce error porque el alias `puntos` todavía no existe cuando se evalúa `WHERE`.

## Forma correcta

```sql
SELECT nombre, promedio * 10 AS puntos
FROM Estudiante
WHERE promedio * 10 > 90;
```

---

# HAVING sí puede usar funciones agregadas

```sql
SELECT fecha_ingreso, COUNT(*) AS total
FROM Estudiante
GROUP BY fecha_ingreso
HAVING COUNT(*) > 1;
```

## Resultado

| fecha_ingreso | total |
|---|---:|
| 2024-01-15 | 2 |
| 2024-01-16 | 2 |

---

# ORDER BY sí puede usar alias

```sql
SELECT nombre, promedio * 10 AS puntos
FROM Estudiante
ORDER BY puntos DESC;
```

## Resultado

| nombre | puntos |
|---|---:|
| Ana López | 95 |
| María Torres | 92 |
| Carlos Ruiz | 87 |
| Luis Pérez | 68 |

---

# Ejemplo completo

```sql
SELECT
  m.nombre AS materia,
  COUNT(i.id_estudiante) AS total_inscritos,
  AVG(e.promedio) AS promedio_grupo,
  MAX(e.promedio) AS mejor_alumno
FROM Materia m
  JOIN Inscripcion i ON m.id = i.id_materia
  JOIN Estudiante e ON i.id_estudiante = e.id
WHERE e.promedio >= 7.0
GROUP BY m.nombre
HAVING COUNT(i.id_estudiante) >= 0
ORDER BY total_inscritos DESC, promedio_grupo DESC;
```

## Paso 1: FROM Materia m

| m.id | m.nombre | m.id_profesor |
|-----:|----------|--------------:|
|   10 | BD       |           100 |
|   11 | Redes    |           101 |
|   12 | IA       |           102 |

## Paso 2: JOIN con Inscripcion i

| m.id | m.nombre | m.id_profesor | i.id_estudiante | i.id_materia |
|-----:|----------|--------------:|----------------:|-------------:|
|   10 | BD       |           100 |               1 |           10 |
|   10 | BD       |           100 |               2 |           10 |
|   10 | BD       |           100 |               4 |           10 |
|   11 | Redes    |           101 |               3 |           11 |
|   12 | IA       |           102 |               1 |           12 |

## Paso 3: JOIN con Estudiante e

Aquí todavía se conservan todas las columnas provenientes de las tablas que participan.

| m.id | m.nombre | m.id_profesor | i.id_estudiante | i.id_materia | e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono |
|-----:|----------|--------------:|----------------:|-------------:|-----:|--------------|---------------|-----------:|-----------------|------------|
|   10 | BD       |           100 |               1 |           10 |    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |
|   10 | BD       |           100 |               2 |           10 |    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   |
|   10 | BD       |           100 |               4 |           10 |    4 | Luis Pérez   | luis@uam.mx   |        6.8 | 2024-01-16      | 555-1004   |
|   11 | Redes    |           101 |               3 |           11 |    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   |
|   12 | IA       |           102 |               1 |           12 |    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |

## Paso 4: WHERE e.promedio >= 7.0

| m.id | m.nombre | m.id_profesor | i.id_estudiante | i.id_materia | e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono |
|-----:|----------|--------------:|----------------:|-------------:|-----:|--------------|---------------|-----------:|-----------------|------------|
|   10 | BD       |           100 |               1 |           10 |    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |
|   10 | BD       |           100 |               2 |           10 |    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   |
|   11 | Redes    |           101 |               3 |           11 |    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   |
|   12 | IA       |           102 |               1 |           12 |    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |

## Paso 5: GROUP BY m.nombre

### Grupo `BD`

| m.id | m.nombre | m.id_profesor | i.id_estudiante | i.id_materia | e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono |
|-----:|----------|--------------:|----------------:|-------------:|-----:|--------------|---------------|-----------:|-----------------|------------|
|   10 | BD       |           100 |               1 |           10 |    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |
|   10 | BD       |           100 |               2 |           10 |    2 | Carlos Ruiz  | carlos@uam.mx |        8.7 | 2024-01-15      | 555-1002   |

### Grupo `Redes`

| m.id | m.nombre | m.id_profesor | i.id_estudiante | i.id_materia | e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono |
|-----:|----------|--------------:|----------------:|-------------:|-----:|--------------|---------------|-----------:|-----------------|------------|
|   11 | Redes    |           101 |               3 |           11 |    3 | María Torres | maria@uam.mx  |        9.2 | 2024-01-16      | 555-1003   |

### Grupo `IA`

| m.id | m.nombre | m.id_profesor | i.id_estudiante | i.id_materia | e.id | e.nombre     | e.correo      | e.promedio | e.fecha_ingreso | e.telefono |
|-----:|----------|--------------:|----------------:|-------------:|-----:|--------------|---------------|-----------:|-----------------|------------|
|   12 | IA       |           102 |               1 |           12 |    1 | Ana López    | ana@uam.mx    |        9.5 | 2024-01-15      | 555-1001   |

## Paso 6: HAVING COUNT(i.id_estudiante) >= 0

Todos los grupos permanecen porque todos los grupos (materias) tienen al menos un estudiante.

## Paso 7: SELECT

| materia | total_inscritos | promedio_grupo | mejor_alumno |
|---------|----------------:|---------------:|-------------:|
| BD      |               2 |           9.10 |          9.5 |
| Redes   |               1 |           9.20 |          9.2 |
| IA      |               1 |           9.50 |          9.5 |

## Paso 8: ORDER BY total_inscritos DESC, promedio_grupo DESC

| materia | total_inscritos | promedio_grupo | mejor_alumno |
|---------|----------------:|---------------:|-------------:|
| BD      |               2 |           9.10 |          9.5 |
| IA      |               1 |           9.50 |          9.5 |
| Redes   |               1 |           9.20 |          9.2 |

