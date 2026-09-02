# Bases de Datos Orientadas a Objetos (Parte 1)

# Objetivos de aprendizaje

- Explicar qué es la **impedancia objeto‑relacional** y por qué es un problema.
- Describir los conceptos básicos del **modelo orientado a objetos** aplicado a bases de datos.
- Diferenciar entre **objetos transitorios** y **objetos persistentes**.
- Explicar el papel de los **identificadores de objeto (OID)** en una BDOO.
- Describir cómo se navega en una BDOO usando referencias/enlaces en lugar de JOINs.

---

# Recordatorio: Programación Orientada a Objetos

## Conceptos fundamentales

- **Clase**: plantilla o molde para crear objetos con atributos y métodos.
- **Objeto**: instancia concreta de una clase que vive en memoria.
- **Atributo**: dato o propiedad que caracteriza al objeto.
- **Método**: comportamiento o función asociada al objeto.

## Pilares de POO

- **Encapsulamiento**: ocultar detalles internos y exponer solo una interfaz pública.
- **Herencia**: definir jerarquías de clases por especialización y reutilizar código.
- **Polimorfismo**: un mismo mensaje puede tener diferentes implementaciones según la clase concreta.

---

# Identidad vs igualdad en objetos

- Dos objetos pueden tener los mismos valores en sus atributos y aun así ser objetos distintos.
- **Igualdad**: comparación de valores de atributos (`alumno1.nombre == alumno2.nombre`).
- **Identidad**: referencia única en memoria; dos objetos con misma información pueden tener identidades distintas.
- En memoria, la identidad suele estar dada por la dirección de memoria o referencia.

Esta diferencia será fundamental cuando hablemos de bases de datos y **OID**.

---

# Ejemplo de clases en código (Python)

```python
class Alumno:
    def __init__(self, matricula, nombre):
        self.matricula = matricula
        self.nombre = nombre
        self.cursos = []  # Lista de objetos Curso

    def inscribir(self, curso):
        self.cursos.append(curso)
        curso.agregar_alumno(self)

class Curso:
    def __init__(self, clave, nombre):
        self.clave = clave
        self.nombre = nombre
        self.alumnos = []  # Lista de objetos Alumno

    def agregar_alumno(self, alumno):
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
```

Este ejemplo modela una relación muchos a muchos Alumno–Curso de forma natural en POO.

---

# ¿Cómo se mapean estos objetos a tablas relacionales?
De objetos a tablas relacionales

## Tablas relacionales correspondientes 
Tablas relacionales del ejemplo anterior 

## Tabla Alumnos

| matricula | nombre |
|-----------|--------|
| 2023001   | Ana    |
| 2023002   | Carlos |

---
## Tabla Cursos

| clave | nombre         |
|-------|----------------|
| BD101 | Bases de Datos |
| POO01 | POO Avanzada   |

---
## Tabla Alumnos_Cursos (relación muchos a muchos)

| matricula | clave |
|-----------|-------|
| 2023001   | BD101 |
| 2023001   | POO01 |
| 2023002   | BD101 |

Para representar una lista de cursos dentro de un Alumno se necesita una tabla intermedia y claves foráneas.

---

# Problemas del enfoque relacional (impedancia objeto‑relacional)
Un problema que se menciona cuando se habla de bases de datos relacionales y bases de datos orientadas a objetos es la impedancia objeto-relacional

## Pérdida (o transformación) de identidad de objeto

- En memoria, un objeto tiene identidad propia (referencia).
- En la BD relacional, solo se almacenan **valores** y **claves primarias**.
- La identidad de un registro se basa en un valor (por ejemplo, la matrícula), no en el objeto.

## Necesidad de JOINs para reconstruir objetos

```sql
SELECT a.nombre, c.nombre
FROM Alumnos a
JOIN Alumnos_Cursos ac ON a.matricula = ac.matricula
JOIN Cursos c ON ac.clave = c.clave
WHERE a.matricula = '2023001';
```

Para obtener los cursos de un alumno, se requieren varios JOINs entre tablas.

---

# Ejemplo: Herencia en código

```python
class Alumno:
    def __init__(self, matricula, nombre):
        self.matricula = matricula
        self.nombre = nombre

class AlumnoPosgrado(Alumno):
    def __init__(self, matricula, nombre, tema_tesis):
        super().__init__(matricula, nombre)
        self.tema_tesis = tema_tesis
```

La herencia es natural en POO: AlumnoPosgrado reutiliza atributos y comportamiento de Alumno, y agrega `tema_tesis`.

---

# Ejemplo: Herencia en tablas (Opción 1)

**Opción 1: Tabla única con columna tipo**

| matricula | nombre | tipo         | tema_tesis      |
|-----------|--------|--------------|-----------------|
| 2023001   | Ana    | Licenciatura | NULL            |
| 2023002   | Carlos | Posgrado     | ML en Medicina  |

- Ventaja: una sola tabla.
- Desventaja: muchas columnas NULL y lógica extra para interpretar la columna `tipo`.

---

# Ejemplo: Herencia en tablas (Opción 2)

**Opción 2: Varias tablas relacionadas por claves foráneas**

**Tabla Alumno (superclase)**

| id_alumno | matricula | nombre |
|----------:|-----------|--------|
|         1 | 2023001   | Ana    |
|         2 | 2023002   | Carlos |

**Tabla AlumnoPosgrado (subclase)**

(Hereda de Alumno)

| id_alumno | tema_tesis      |
|----------:|-----------------|
|         2 | ML en Medicina  |

Para reconstruir un objeto AlumnoPosgrado se necesita hacer JOIN:

```sql
SELECT a.matricula, a.nombre, ap.tema_tesis
FROM Alumno a
JOIN AlumnoPosgrado ap ON a.id_alumno = ap.id_alumno;
```

- Ventaja: evita columnas NULL.
- Desventaja: requiere **más JOINs** y mayor complejidad en las consultas.

---

# Impedancia objeto‑relacional (resumen)

**Definición:**

Desajuste conceptual y estructural entre:

- El paradigma orientado a objetos (objetos con identidad, referencias, herencia, métodos).
- El paradigma relacional (tablas, filas, valores, claves, JOINs).

---
**Consecuencias prácticas:**

- Código adicional para mapear objetos ↔ tablas.
- Complejidad en las consultas que involucran herencia y relaciones complejas.
- Posibles problemas de rendimiento y mantenimiento.

Este problema motiva el surgimiento de las **bases de datos orientadas a objetos (BDOO)**.

---

# Modelo orientado a objetos (conceptual)
Ahora veamos el **Modelo Orientado a Objetos** a nivel conceptual

## Componentes principales

- **Clases**: definen tipos de objetos con atributos y métodos.
- **Objetos**: instancias concretas de clases.
- **Asociaciones**: relaciones entre clases (uno a uno, uno a muchos, muchos a muchos).
- **Agregación**: relación parte–todo donde la parte puede existir sin el todo.
- **Composición**: relación parte–todo fuerte; la parte no existe sin el todo.

Este modelo conceptual se puede representar con diagramas UML.

---

# Diagrama de clases (UML simplificado)

```
┌─────────────────┐         ┌─────────────────┐
│     Alumno      │         │      Curso      │
├─────────────────┤         ├─────────────────┤
│ - matricula     │◆───────◇│ - clave         │
│ - nombre        │  n    m │ - nombre        │
│ - cursos[]      │         │ - alumnos[]     │
├─────────────────┤         ├─────────────────┤
│ + inscribir()   │         │ + agregar()     │
└─────────────────┘         └─────────────────┘
```

Comparación con modelo Entidad–Relación (E‑R):

- Clases ≈ Entidades.
- Asociaciones ≈ Relaciones.
- Diferencia importante: las clases incluyen **comportamiento** (métodos).

---

# ¿Qué es una Base de Datos Orientada a Objetos (BDOO)?
**Bases de datos orientadas a objetos**

## Definición general

Una BDOO es un sistema de administración de bases de datos que almacena **objetos** (no solo filas o documentos), preservando:

- Identidad propia de cada objeto.
- Encapsulamiento de datos y métodos.
- Herencia entre clases.
- Polimorfismo en las operaciones sobre objetos.

El objetivo principal es reducir o eliminar la impedancia objeto‑relacional.

---

# Objetos transitorios vs objetos persistentes
Veamos ahora el concepto de objetos transitorios y objetos persistentes. Estos conceptos son valiosos para la elaboración del concepto de bases de datos orientadas a objetos.

## Objeto transitorio (solo en memoria)

```python
alumno1 = Alumno("2023001", "Ana")
# El objeto existe mientras el programa está en ejecución
```

## Objeto persistente (almacenado en la BD)

```python
# Pseudocódigo
alumno1 = Alumno("2023001", "Ana")

db.store(alumno1)   # Guardar el objeto en la base de datos orientada a objetos
# El objeto sobrevive a la finalización del programa
```

**Persistencia transparente:**

- El objeto se usa de la misma manera en el código, esté solo en memoria o almacenado en la BD.
- El programador no necesita reescribir lógica para cargar/guardar atributos individuales.

---

# Identificadores de objeto (OID)
Veamos los identificadores de objeto (OID) y su relación con las formas de identificar la información en bases de datos relacionales.

## Claves primarias en BD relacionales

- Identifican filas usando **valores** (por ejemplo, `matricula` en Alumnos).
- Si el valor cambia, hay que actualizar claves foráneas en otras tablas.

## OID en BDOO

- Identificador único e inmutable asignado por el sistema.
- Independiente de los valores de los atributos.
- Similar a una **referencia** o **puntero** persistente.

Ejemplo conceptual de objeto con OID:

```
Alumno OID: 0x7F3A2B1C
  matricula: "2023001"
  nombre: "Ana"
  cursos: [OID: 0x8E4B3C2D, OID: 0x9F5C4D3E]
```

Cambiar la matrícula no afecta la identidad del objeto (su OID).

---

# Clases como esquema de la BD

En muchas BDOO:

- El esquema de la BD está definido por las **clases** registradas en el sistema.
- No se usa un DDL clásico (CREATE TABLE), sino definiciones de clases con sus atributos y métodos.

---
- La base de datos almacena metadatos de:
  - Atributos y sus tipos.
  - Relaciones entre clases.
  - Jerarquías de herencia.

Esto hace que el modelo de la BD se parezca mucho al modelo de objetos del lenguaje de programación.

---

# Navegación por enlaces en BDOO
La navegación implica poder encontrar lo que busco en mi conjunto de datos y las bases de datos relacionales y las orientadas a objetos no lo hacen igual.


## En BD relacionales (con JOINs)

```sql
SELECT c.*
FROM Cursos c
JOIN Alumnos_Cursos ac ON c.clave = ac.clave
WHERE ac.matricula = '2023001';
```

## En BDOO (navegación directa)

```python
# Pseudocódigo en una BDOO

# Recuperar al alumno por matrícula usando una consulta
alumno = db.query(Alumno).filter(matricula="2023001").first()

# Navegar por la lista de cursos relacionados
for curso in alumno.cursos:  # cursos es una lista de referencias/OIDs
    print(curso.nombre)
```

No se escriben JOINs explícitos; se siguen las referencias almacenadas en los objetos.

---

# Encapsulamiento en la base de datos
Encapsulamiento en la base de datos.

## Ejemplo de clase con atributo privado

```python
class Producto:
    def __init__(self, precio_base):
        self.__precio_base = precio_base  # Atributo privado

    def get_precio_con_iva(self):
        return self.__precio_base * 1.16

# Recuperación desde una BDOO (pseudocódigo)
producto = db.get(OID_producto)

# Acceso directo al atributo privado (incorrecto)
# producto.__precio_base  # No debería ser accesible

# Uso correcto a través del método público
precio = producto.get_precio_con_iva()
```

La BDOO respeta el encapsulamiento definido en las clases: los datos están protegidos y solo se exponen los métodos públicos.
