# Bases de Datos Orientadas a Objetos (Parte 2)

# Objetivos de aprendizaje

Al finalizar esta sesión, podrán

- Describir la diferencia entre **navegación** y **consultas declarativas** en BDOO.
- Explicar las ideas básicas de **OQL (Object Query Language)**.
- Comparar **modelos relacional, orientado a objetos y objeto‑relacional**.
- Mapear un pequeño dominio de aplicación a un esquema orientado a objetos.
- Relacionar BDOO con el uso de **ORM (Object‑Relational Mapping)** en aplicaciones.

---

# Acceso a datos en BDOO: navegación vs consultas

## Navegación (estilo procedimental)

- Se parte de un objeto raíz ya conocido.
- Se recorren las referencias hacia otros objetos relacionados.
- Es similar a recorrer estructuras enlazadas (listas, grafos) en memoria.

## Consultas declarativas

- Se especifica **qué** objetos se desean, no **cómo** llegar a ellos.
- Se utiliza un lenguaje de consulta (por ejemplo, OQL).
- Se parece a SQL pero aplicado a objetos.

Ambos enfoques pueden coexistir en una misma BDOO.

---

# Navegación: ejemplo en pseudocódigo

```python
# Supongamos que ya tenemos un objeto curso persistente
curso = db.query(Curso).filter(clave="BD101").first()

print("Curso:", curso.nombre)

for alumno in curso.alumnos:  # alumnos es una lista de objetos Alumno
    print("-", alumno.nombre)
```

- `curso.alumnos` devuelve una colección de objetos relacionados.
- La BD se encarga de seguir los OIDs y cargar los objetos cuando sea necesario.

---

# Consultas declarativas: OQL (Object Query Language)

OQL es un lenguaje de consultas para bases de datos orientadas a objetos.

- Sintaxis inspirada en SQL.
- Opera sobre **objetos** en lugar de filas.
- Permite expresiones de navegación (path expressions) como `alumno.cursos.nombre`.

Ejemplo básico de OQL:

```sql
SELECT a
FROM Alumno a
WHERE a.matricula = "2023001"
```

Esta consulta regresa un objeto Alumno (o un conjunto de ellos) cuyo atributo `matricula` coincide.

---

# Ejemplo comparativo: SQL vs OQL vs navegación directa

## SQL (modelo relacional)

```sql
SELECT c.nombre
FROM Cursos c
JOIN Alumnos_Cursos ac ON c.clave = ac.clave
WHERE ac.matricula = '2023001';
```

## OQL (modelo orientado a objetos)

```sql
SELECT c.nombre
FROM Alumno a, a.cursos c
WHERE a.matricula = "2023001"
```

## Navegación directa en el código

```python
# Recuperar al alumno por matrícula
alumno = db.query(Alumno).filter(matricula="2023001").first()

# Recorrer cursos
for curso in alumno.cursos:
    print(curso.nombre)
```

En los tres casos se obtiene la lista de nombres de cursos del alumno con matrícula "2023001".

---

# Comparación de modelos de bases de datos

## Modelos considerados

- **Modelo relacional**: datos en tablas, filas, columnas y claves.
- **Modelo orientado a objetos (BDOO)**: datos como objetos con identidad y relaciones por referencias.
- **Modelo objeto‑relacional**: híbrido; extiende el modelo relacional con tipos de datos complejos y algunas características OO.

---

# Comparación de características

| Característica      | Relacional                       | BDOO                                 | Objeto‑relacional                          |
|---------------------|----------------------------------|--------------------------------------|--------------------------------------------|
| Unidad básica       | Tupla / fila                    | Objeto                               | Fila con tipos objeto / compuestos         |
| Identidad           | Clave primaria (valor)          | OID (identificador de objeto)        | Combinación de clave y tipos objeto        |
| Relaciones          | Claves foráneas + JOIN          | Referencias / enlaces (OIDs)         | Ambas (claves foráneas y referencias)      |
| Herencia            | No nativo                       | Soportada de forma nativa            | Soportada parcialmente                     |
| Encapsulamiento     | No (solo datos)                 | Sí (datos + métodos)                 | Parcial (datos con funciones asociadas)    |
| Lenguaje de consulta| SQL                             | OQL u otros lenguajes sobre objetos  | SQL extendido con tipos y funciones        |
| Navegación          | No (se simula con JOINs)        | Sí, navegación por referencias       | Limitada, depende del SGBD                 |

---

# ¿Cuándo usar cada modelo?

## Modelo relacional

- Datos estructurados relativamente simples.
- Muchas consultas ad‑hoc, reportes y analítica.
- Integración con herramientas de Business Intelligence.
- Requisitos fuertes de transacciones ACID clásicas.

## Modelo orientado a objetos (BDOO)

- Modelos de datos con estructuras complejas y jerarquías profundas.
- Necesidad de preservar identidad, herencia y polimorfismo.
- Aplicaciones con fuerte orientación a objetos en el código.

---

# Ejemplos de aplicaciones para BDOO

- Sistemas **CAD (Computer‑Aided Design)**: diseño asistido por computadora, por ejemplo modelos 3D de piezas mecánicas o edificios.
- Sistemas **CAM (Computer‑Aided Manufacturing)**: fabricación asistida por computadora, que reutilizan los modelos CAD en procesos de producción.
- Sistemas **GIS (Geographic Information Systems)**: sistemas de información geográfica con objetos complejos (capas, mapas, entidades geoespaciales).
- Aplicaciones científicas con estructuras de datos complejas (simulaciones, grafos, modelos numéricos detallados).

En estos contextos, las estructuras de datos se parecen mucho a grafos de objetos, y una BDOO puede ser más natural que una BD relacional.

---

# Modelo objeto‑relacional (visión general)

Un SGBD objeto‑relacional extiende el modelo relacional con:

- Tipos definidos por el usuario (UDT, User‑Defined Types).
- Columnas que pueden almacenar estructuras complejas (por ejemplo, tuplas anidadas).
- Posibilidad de asociar funciones o métodos a tipos.

Ejemplos: PostgreSQL, Oracle con tipos objeto.

Limitaciones:

- La navegación directa entre objetos es limitada.
- La integración con lenguajes orientados a objetos no es tan transparente como en una BDOO pura.

---

# Caso práctico: dominio Cursos–Alumnos

## Requisitos simplificados

- Un alumno puede inscribirse en varios cursos.
- Un curso puede tener varios alumnos.
- Hay alumnos de licenciatura y alumnos de posgrado.
- Los alumnos de posgrado tienen un `tema_tesis` adicional.

Diseñaremos el modelo orientado a objetos y veremos cómo se almacena en una BDOO.

---

# Diseño de clases en POO

```python
class Persona:
    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

class Alumno(Persona):
    def __init__(self, id_persona, nombre, email, matricula):
        super().__init__(id_persona, nombre, email)
        self.matricula = matricula
        self.cursos = []  # Lista de objetos Curso

    def inscribir(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_alumno(self)

class AlumnoPosgrado(Alumno):
    def __init__(self, id_persona, nombre, email, matricula, tema_tesis):
        super().__init__(id_persona, nombre, email, matricula)
        self.tema_tesis = tema_tesis

class Curso:
    def __init__(self, clave, nombre, creditos):
        self.clave = clave
        self.nombre = nombre
        self.creditos = creditos
        self.alumnos = []  # Lista de objetos Alumno o AlumnoPosgrado

    def agregar_alumno(self, alumno):
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
```

Este diseño usa herencia, composición (listas) y relaciones bidireccionales.

---

# Diagrama UML del caso práctico

```
         ┌──────────────┐
         │   Persona    │
         ├──────────────┤
         │ - id_persona │
         │ - nombre     │
         │ - email      │
         └──────┬───────┘
                │
                │ (herencia)
                │
         ┌──────▼───────┐           ┌──────────────┐
         │    Alumno    │◆─────────◇│    Curso     │
         ├──────────────┤  n      m ├──────────────┤
         │ - matricula  │           │ - clave      │
         │ - cursos[]   │           │ - nombre     │
         └──────┬───────┘           │ - creditos   │
                │                   │ - alumnos[]  │
                │                   └──────────────┘
                │
         ┌──────▼──────────┐
         │ AlumnoPosgrado  │
         ├─────────────────┤
         │ - tema_tesis    │
         └─────────────────┘
```

La relación Alumno–Curso es muchos a muchos, y AlumnoPosgrado hereda de Alumno.

---

# Representación conceptual en una BDOO

- Cada clase corresponde a una **extensión** (conjunto de objetos) en la BD.
- Las listas `cursos` y `alumnos` almacenan **referencias (OIDs)** a otros objetos.

Esquema conceptual:

```
Clase Persona
├── Extensión: { objetos Persona (o subclases) }

Clase Alumno (hereda de Persona)
├── Extensión: { objetos Alumno }
│   └── Atributo cursos: lista de OIDs → objetos Curso

Clase AlumnoPosgrado (hereda de Alumno)
├── Extensión: { objetos AlumnoPosgrado }
│   └── Atributo tema_tesis: string (Tema de tesis)

Clase Curso
├── Extensión: { objetos Curso }
    └── Atributo alumnos: lista de OIDs → objetos Alumno / AlumnoPosgrado
```

La herencia se conserva directamente en la base de datos.

---

# Persistencia del caso práctico en BDOO

```python
# Crear objetos en memoria
curso_bd = Curso("BD101", "Bases de Datos", 8)

alumno1 = Alumno(1, "Ana López", "ana@mail.com", "2023001")
alumno2 = AlumnoPosgrado(2, "Carlos Ruiz", "carlos@mail.com",
                         "2023002", "ML en Medicina")

# Establecer relaciones
alumno1.inscribir(curso_bd)
alumno2.inscribir(curso_bd)

# Persistir en la BDOO (pseudocódigo)
db.store(curso_bd)
db.store(alumno1)
db.store(alumno2)
db.commit()
```

La BDOO almacena los objetos con sus OIDs y las referencias entre ellos.

---

# Recuperación y navegación en el caso práctico

```python
# Recuperar un curso por su clave
curso = db.query(Curso).filter(clave="BD101").first()

print("Curso:", curso.nombre)
print("Alumnos inscritos:")

for alumno in curso.alumnos:
    tipo = type(alumno).__name__
    print(f"- {alumno.nombre} ({tipo})")
    if isinstance(alumno, AlumnoPosgrado):
        print(f"  Tema de tesis: {alumno.tema_tesis}")
```

La consulta sobre la extensión de Curso devuelve objetos completos, y la navegación permite acceder a sus relaciones y subtipos.

---

# Consulta relacional equivalente (recordatorio)

En un modelo relacional similar, necesitaríamos varias tablas (Persona, Alumno, AlumnoPosgrado, Curso, Alumno_Curso) y una consulta con JOINs:

```sql
SELECT p.nombre, a.matricula, ap.tema_tesis
FROM Persona p
JOIN Alumno a ON p.id_persona = a.id_persona
LEFT JOIN AlumnoPosgrado ap ON a.id_persona = ap.id_persona
JOIN Alumno_Curso ac ON a.id_persona = ac.id_alumno
JOIN Curso c ON ac.curso_clave = c.clave
WHERE c.clave = 'BD101';
```

Comparar esta consulta con el código de navegación en BDOO ayuda a visualizar el cambio de paradigma.

---

# ORMs y su relación con BDOO

## ¿Qué es un ORM?

ORM significa **Object‑Relational Mapping** (mapeo objeto‑relacional).

- Es una tecnología o biblioteca que permite trabajar con **objetos** en el código, mientras los datos se almacenan en una **BD relacional**.
- El ORM se encarga de traducir operaciones sobre objetos a operaciones SQL (INSERT, UPDATE, DELETE, SELECT) sobre tablas.

Ejemplos de ORMs:

- Hibernate (Java).
- Django ORM (Python).
- SQLAlchemy (Python).
- Entity Framework (.NET).

---

# ¿Dónde se usan los ORMs?

- En el desarrollo de aplicaciones web y de escritorio que usan BD relacionales.
- En arquitecturas típicas de tres capas: presentación, lógica de negocio, datos.
- Para reducir código repetitivo de acceso a datos (boilerplate SQL).

Relación con BDOO:

- Los ORMs **no son** BDOO, pero intentan acercar el mundo de los objetos al mundo relacional.
- Muchos conceptos de BDOO (identidad, navegación, herencia) inspiran el diseño de los ORMs.

---

# Ventajas y desventajas de BDOO

## Ventajas

- Representación directa de objetos complejos y jerarquías.
- Navegación natural siguiendo referencias, sin JOINs.
- Soporte nativo para herencia y polimorfismo.
- Identidad de objeto preservada mediante OIDs.
- Coherencia entre el modelo en código y el modelo en la base de datos.

## Desventajas

- Menor adopción industrial comparada con BD relacionales.
- Ecosistema de herramientas (BI, reporting) menos desarrollado.
- Menos soporte estándar para consultas ad‑hoc complejas.
- Curva de aprendizaje para administradores y desarrolladores acostumbrados a SQL.

---

# Contexto actual y nichos de uso

## Nichos especializados

- **CAD (Computer‑Aided Design)**: diseño asistido por computadora.
- **CAM (Computer‑Aided Manufacturing)**: fabricación asistida por computadora.
- **GIS (Geographic Information Systems)**: sistemas de información geográfica.
- Aplicaciones científicas y de simulación con estructuras de datos complejas.

## Tendencias dominantes

- Uso de ORMs sobre BD relacionales.
- Uso de bases de datos NoSQL (por ejemplo, MongoDB) que almacenan documentos con estructura similar a objetos.
- Uso de características objeto‑relacionales en SGBD como PostgreSQL.

Comprender BDOO ayuda a entender mejor estas tecnologías.

---

# Síntesis final

Conceptos clave a recordar:

1. **Impedancia objeto‑relacional**: desajuste entre objetos y tablas.
2. **OID**: identificador de objeto, distinto de una clave primaria basada en valores.
3. **Persistencia de objetos**: objetos que sobreviven a la ejecución del programa.
4. **Navegación vs JOINs**: seguir referencias frente a combinar tablas.
5. **BDOO vs relacional vs objeto‑relacional**: distintos modelos para distintos problemas.

Las BDOO son menos comunes que las BD relacionales, pero el paradigma orientado a objetos sigue influyendo fuertemente en el diseño de ORMs y bases modernas.

---

# Para seguir estudiando

- Estándar ODMG (Object Data Management Group) para bases de datos orientadas a objetos.
- Documentación de BDOO como db4o, ObjectDB o similares.
- Características objeto‑relacionales de PostgreSQL.
- Documentación de ORMs populares (Hibernate, SQLAlchemy, Django ORM).
