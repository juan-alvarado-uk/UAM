# Modelo Conceptual Orientado a Objetos

Una **clase** es una plantilla que describe la estructura (atributos) y el comportamiento (métodos) de un conjunto de entidades del dominio.

Un **objeto** es una instancia concreta de una clase con un **OID** (*Object Identifier*) único asignado automáticamente, independiente del valor de sus atributos. Dos objetos con los mismos valores en todos sus atributos siguen siendo objetos distintos.

---

## Diagrama de clases UML — notación

```
┌──────────────────────────┐
│         SENSOR           │  ← nombre
├──────────────────────────┤
│ id: String               │  ← atributos
│ ubicacion: Coordenada    │
│ tipo_medida: String      │
│ frecuencia: Float        │
├──────────────────────────┤
│ tomar_lectura(): Lectura │  ← métodos
│ calibrar(): void         │
└──────────────────────────┘
```

**Asociaciones** (multiplicidad): `1..1`, `0..1`, `1..*`, `0..*`

**Herencia:** flecha de punta triangular vacía de la subclase hacia la superclase. Las restricciones se indican con etiquetas: `{disjoint}`, `{overlapping}`, `{complete}`, `{incomplete}`.

---

## Diferencias EER vs. diagrama de clases

| Aspecto                    | EER                                          | Diagrama de clases UML         |
|----------------------------|----------------------------------------------|--------------------------------|
| Comportamiento             | No (solo estructura)                         | Sí (métodos explícitos)        |
| Identidad de ocurrencia    | Atributo identificador                       | OID (Object Identifier)        |
| Restricciones de jerarquía | Notación integrada (d/o, línea simple/doble) | Etiquetas de texto adicionales |
| Propósito de diseño        | Derivar esquemas de BD                       | Diseño de software o BD OO     |

---

# Modelos Semánticos, OO y Objeto-Relacional

## El espectro de abstracción

```
CONCEPTUAL            LÓGICO                FÍSICO
─────────────────────────────────────────────────
EER / Clases UML  →  Relacional /       →  Tablas, índices,
                     Objeto-relacional      almacenamiento
```

---



## El modelo objeto-relacional (ORDBMS)

Extiende el motor relacional con capacidades OO sin abandonar su infraestructura. Extensiones principales:

- **UDT** (*User-Defined Types*): tipos de dato complejos definidos por el diseñador (`Coordenada`, `Rango`).
- **Herencia de tablas**: una tabla hereda columnas y restricciones de otra.
- **Tipos de colección**: arreglos y conjuntos como tipo de columna (atributos multivaluados directos).
- **REF**: referencias directas entre filas sin JOINs explícitos.

PostgreSQL es un ejemplo de sistema objeto-relacional de código abierto.

---

**Ejemplo — mismo dominio en tres niveles:**

```
-- EER (conceptual)
DISPOSITIVO (id, ubicacion, estado)
  ├── SENSOR (tipo_medida, frecuencia)
  └── ACTUADOR (tipo_accion, voltaje)
SENSOR ─<GENERA>─ LECTURA (débil: timestamp, valor, unidad)

-- Relacional lógico (estrategia 2)
CREATE TABLE dispositivo (id_dispositivo VARCHAR(20) PRIMARY KEY, ...);
CREATE TABLE sensor (id_dispositivo VARCHAR(20) REFERENCES dispositivo, ...);
CREATE TABLE lectura (id_dispositivo VARCHAR(20), ts TIMESTAMP,
                      PRIMARY KEY (id_dispositivo, ts));

-- Objeto-relacional (PostgreSQL)
CREATE TYPE tipo_coordenada AS (latitud DECIMAL(9,6), longitud DECIMAL(9,6));
CREATE TABLE dispositivo (id_dispositivo VARCHAR(20) PRIMARY KEY,
                          ubicacion tipo_coordenada, estado VARCHAR(15));
CREATE TABLE sensor (tipo_medida VARCHAR(30), frecuencia_hz FLOAT,
                     etiquetas TEXT[]) INHERITS (dispositivo);
```

---
