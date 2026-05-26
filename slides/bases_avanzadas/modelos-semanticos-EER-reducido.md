# ¿Modelo semántico?

Un **modelo semántico de datos** es un modelo conceptual cuyo objetivo es capturar el *significado* del dominio: qué tipos de cosas existen, qué restricciones impone el mundo real y cómo se relacionan los conceptos, todo antes de pensar en tablas o índices.

El modelo relacional plano puede representar cualquier cosa, pero a veces lo hace con dificultad. Imagínense el archivo de un hospital con una única tabla `PERSONA(id, nombre, especialidad, cedula_prof, num_expediente, alergias, turno, area)`. Forzar médicos, pacientes y administrativos en la misma tabla produce columnas con valores nulos para la mayoría de los registros e impide imponer restricciones por tipo, como que *todo médico debe tener cédula profesional*. Un modelo semántico resuelve esto con jerarquías, herencia y tipos especializados.

---

# El Modelo Entidad-Relación Extendido (EER)

El **EER** (*Enhanced Entity-Relationship*) es una extensión del E-R clásico desarrollada en los años 1980 por Elmasri y Navathe. Conserva todos los elementos del E-R básico y agrega cuatro constructores:

- **Especialización / Generalización** — jerarquías entre tipos de entidades con herencia
- **Atributos multivaluados** — atributos que toman más de un valor por ocurrencia
- **Entidades débiles** — entidades cuya identidad depende de otra entidad
- **Agregación** — tratar una relación como entidad de nivel superior

---

## Notación base 

- **Rectángulo simple / doble** → entidad fuerte / débil
- **Elipse simple / doble / discontinua** → atributo simple / multivaluado / derivado
- **Atributo subrayado** → atributo identificador; **subrayado discontinuo** → discriminante
- **Rombo simple / doble** → relación normal / relación identificadora
- **Línea doble / simple** en la conexión entidad–relación → participación total / parcial

---

# Entidades Débiles

Una **entidad débil** no posee atributos propios suficientes para identificar sus ocurrencias de forma única. Depende de una **entidad identificadora** (fuerte) tanto para su identidad como para su existencia.

El **discriminante** es el atributo (o conjunto) que, combinado con el identificador de la entidad propietaria, distingue cada ocurrencia. La relación que las une es la **relación identificadora** (rombo doble).

---

**Ejemplo — lecturas de sensores:**

```
[SENSOR] ─────<GENERA>════[LECTURA]
 id_sensor              ~timestamp~   ← discriminante
 tipo                   valor_medido
 ubicacion              unidad
```

`LECTURA` es débil: su identificación completa requiere `id_sensor` + `timestamp`. Dos sensores distintos pueden generar una lectura en el mismo instante; el `timestamp` solo no basta.

---

**Cuándo reconocer una entidad débil** — se cumplen las tres condiciones:
1. No tiene identificador propio suficiente.
2. Su ciclo de vida está ligado al de la entidad propietaria.
3. Sus ocurrencias solo se distinguen *dentro* del contexto de esa entidad propietaria.

---

# Atributos Multivaluados

Un **atributo multivaluado** puede contener más de un valor para la misma ocurrencia. Se representa con **elipse doble**. El modelo relacional no los admite directamente (violan la primera forma normal); el EER los declara en el nivel conceptual y la materialización se decide en el diseño lógico.

**Ejemplo — autenticación multi-factor:**

```
           [USUARIO]
          /    |    \
      {id}  {nombre}  {metodo_2FA}  ← elipse doble
                       email | SMS | app_auth | llave_HW
```

Un usuario puede tener entre cero y varios métodos activos simultáneamente.

---

**Distinción: multivaluado vs. compuesto**

Un atributo **compuesto** tiene partes con significado propio (`dirección` → calle, número, colonia). Un atributo **multivaluado** tiene múltiples ocurrencias del mismo tipo (`teléfono` → varios números). Un atributo puede ser ambas cosas a la vez.

---

# Especialización y Generalización

**Especialización** (*top-down*): se parte de una **superclase** y se identifican subgrupos con atributos o relaciones adicionales; cada subgrupo se convierte en **subclase**.

**Generalización** (*bottom-up*): se parte de varias entidades con atributos comunes y se factorizan en una nueva superclase.

Ambos producen el mismo resultado en el diagrama: una **jerarquía**. La **herencia** garantiza que cada subclase adquiere automáticamente todos los atributos y relaciones de su superclase.

---

## Restricciones de la jerarquía

**Disjunción** — ¿puede una ocurrencia pertenecer a más de una subclase?
- `d` — **Disjunta**: pertenece a lo sumo a una subclase (vehículo es automóvil *o* motocicleta).
- `o` — **Superpuesta**: puede pertenecer a varias (un empleado puede ser supervisor *y* técnico).

**Completitud** — ¿debe toda ocurrencia de la superclase pertenecer a alguna subclase?
- **Total** (línea doble): toda ocurrencia pertenece a al menos una subclase.
- **Parcial** (línea simple): algunas ocurrencias pueden no pertenecer a ninguna.

---

## Ejemplo — red de sensores (disjunta, total)

```
               [DISPOSITIVO]
               id_dispositivo
               ubicacion_gps
               fabricante · estado
                     ║         ← total
                  ───d───      ← disjunta
                /    |    \
         [SENSOR] [ACTUADOR] [GATEWAY]
         tipo_medida tipo_accion protocolo
         frecuencia  voltaje     nodos_max
         rango_min/max
```

Todo dispositivo es exactamente uno de los tres tipos. Los atributos comunes se definen una sola vez en la superclase.

---

## Ejercicio de reflexión

> Se diseña la base de datos de una biblioteca universitaria. Los usuarios son: estudiantes de licenciatura, estudiantes de posgrado, profesores e investigadores externos. Algunos profesores también cursan posgrado en la misma institución; algunos investigadores externos son profesores de otra institución.
>
> **¿Cuál es la superclase? ¿La especialización es disjunta o superpuesta? ¿Total o parcial? Justifica.**

---

# Agregación

La **agregación** permite tratar una relación —junto con las entidades que conecta— como una entidad de nivel superior, de modo que esa relación pueda participar en otras relaciones. Resuelve el caso en que "una relación entre A y B tiene a su vez una relación con C", que el E-R básico no puede expresar directamente.

**Ejemplo — técnicos en proyectos de infraestructura:**

```
╔══════════════════════════════════════╗
║  [TÉCNICO]──<TRABAJA_EN>──[PROYECTO] ║
║               fecha_inicio           ║
║               horas_semanales · rol  ║
╚══════════════════════════════════════╝
                    |
               <REQUIERE>
                    |
               [EQUIPO]
               num_serie · tipo_equipo
```

Los equipos no se asignan al técnico ni al proyecto por separado; se asignan a la *combinación específica* técnico+proyecto. La agregación lo expresa sin crear entidades artificiales.

---

# E-R Simple vs. EER — mismo problema

**Dominio:** red de sensores en una ciudad inteligente.

## Modelo E-R simple

```
[DISPOSITIVO]──<GENERA>──[LECTURA]
  tipo_disp    ← texto libre
  frecuencia_Hz    ← NULL para actuadores/gateways
  tipo_accion      ← NULL para sensores/gateways
  voltaje_op       ← NULL para sensores/gateways
  protocolo        ← NULL para sensores/actuadores
```

Problemas: NULLs masivos, restricciones de dominio no expresables, extensión obliga a alterar el esquema completo.

---

## Modelo EER equivalente

```
                [DISPOSITIVO]
                id_dispositivo · ubicacion_gps
                estado · fabricante
                      ║  (total)
                   ───d───  (disjunta)
                 /    |    \
           [SENSOR]  [ACTUADOR]  [GATEWAY]
           tipo_medida tipo_accion protocolo
           frecuencia  voltaje     nodos_max
                 ║  (participación total)
               <GENERA>  ← rombo doble
                 ║
           [LECTURA]  ← entidad débil
           ~timestamp~ · valor · unidad
```

**Ganancias:** restricciones por subclase explícitas en el esquema; herencia elimina redundancia; entidad débil captura la dependencia de existencia; extensión solo agrega una subclase nueva.

---

## Limitaciones que el EER suaviza

- Jerarquías de tipos → especialización/generalización
- NULLs masivos → subclases con solo sus atributos propios
- Dependencias de existencia → entidades débiles
- Atributos con múltiples valores → atributos multivaluados
- Relaciones que participan en relaciones → agregación

**Lo que el EER no resuelve:** comportamiento (métodos), encapsulamiento, identidad de objeto independiente del valor, polimorfismo — eso lo aporta el modelo orientado a objetos.

---

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

| Aspecto | EER | Diagrama de clases UML |
|---|---|---|
| Comportamiento | No (solo estructura) | Sí (métodos explícitos) |
| Identidad de ocurrencia | Atributo identificador | OID automático |
| Restricciones de jerarquía | Notación integrada (d/o, línea simple/doble) | Etiquetas de texto adicionales |
| Propósito de diseño | Derivar esquemas de BD | Diseño de software o BD OO |

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

## Las tres estrategias de mapeo de jerarquías al modelo relacional

**Estrategia 1 — Una tabla para toda la jerarquía:** todos los atributos de superclase y subclases en una sola tabla con columna discriminante. Ventaja: sin JOINs. Desventaja: NULLs masivos.

**Estrategia 2 — Tabla de superclase + tabla por subclase:** la superclase tiene su tabla; cada subclase tiene la suya con solo sus atributos propios, ligada por el identificador. Ventaja: normalizado. Desventaja: JOIN necesario para datos completos.

**Estrategia 3 — Solo tablas de subclases:** los atributos de la superclase se duplican en cada subclase. Ventaja: sin JOINs para consultas de subclase. Desventaja: redundancia y UNION para consultas sobre la superclase.

---

## El modelo objeto-relacional (ORDBMS)

Extiende el motor relacional con capacidades OO sin abandonar su infraestructura. Extensiones principales:

- **UDT** (*User-Defined Types*): tipos de dato complejos definidos por el diseñador (`Coordenada`, `Rango`).
- **Herencia de tablas**: una tabla hereda columnas y restricciones de otra.
- **Tipos de colección**: arreglos y conjuntos como tipo de columna (atributos multivaluados directos).
- **REF**: referencias directas entre filas sin JOINs explícitos.

PostgreSQL es el ejemplo más conocido de sistema objeto-relacional de código abierto.

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

# Actividad Central — Red de Sensores

## Requisitos del sistema

1. Cuatro tipos de dispositivos: **sensores de calidad del aire** (CO₂, PM2.5, ozono), **sensores meteorológicos** (temperatura, humedad, presión, viento), **actuadores** (válvulas, aspersores) y **nodos de comunicación** (solo retransmiten).
2. Todo dispositivo tiene: identificador único, coordenadas GPS, fecha de instalación, estado.
3. Los sensores generan lecturas periódicas con marca de tiempo, valor y unidad. Una lectura solo existe en el contexto de su sensor.
4. Los sensores de calidad del aire generan en el mismo instante lecturas de múltiples contaminantes.
5. Cada dispositivo puede tener varios responsables de mantenimiento (preventivo, correctivo, calibración).
6. La relación dispositivo–responsable puede asociarse con órdenes de trabajo específicas.
7. La ciudad se divide en zonas → subzonas → puntos de monitoreo donde se instalan los dispositivos.

---

## Preguntas guía

- **Req. 1:** ¿Qué constructor EER resuelve los cuatro tipos de dispositivo? ¿Disjunta o superpuesta? ¿Total o parcial?
- **Req. 3:** ¿Por qué `LECTURA` es entidad débil? ¿Cuál es su discriminante?
- **Req. 4:** ¿El hecho de generar múltiples valores en el mismo instante es un atributo multivaluado, una entidad débil anidada, o una relación ternaria? Argumenta.
- **Req. 5:** ¿Atributo multivaluado o relación independiente con `RESPONSABLE`? ¿Qué se pierde si solo se usa atributo multivaluado?
- **Req. 6:** ¿Qué constructor EER permite que la relación dispositivo–responsable participe en otra relación con `ORDEN_DE_TRABAJO`?
- **Req. 7:** ¿Cómo se expresa la jerarquía recursiva zona→subzona en el EER?

---

## Entregable

1. **Diagrama EER** con: jerarquía de especialización (restricciones explícitas), al menos un atributo multivaluado, al menos una entidad débil con discriminante, y agregación si aplica.
2. **Nota de justificación** (máx. media cuartilla por decisión): por qué jerarquía y no columna de tipo; por qué entidad débil y no fuerte con relación 1:N; qué restricciones de jerarquía se eligieron y por qué.

---

# Glosario esencial

**Agregación (EER):** abstracción que trata una relación como entidad de nivel superior para participar en otras relaciones.

**Atributo discriminante:** atributo de entidad débil que, combinado con el identificador de la propietaria, identifica cada ocurrencia. Subrayado discontinuo en el diagrama.

**Atributo multivaluado:** atributo con más de un valor por ocurrencia. Elipse doble en el diagrama.

**Completitud:** restricción de jerarquía — total (toda ocurrencia en alguna subclase) o parcial (algunas pueden no estarlo).

**Disjunción:** restricción de jerarquía — disjunta `d` (una subclase como máximo) o superpuesta `o` (varias posibles).

**EER:** extensión del E-R clásico con jerarquías, herencia, entidades débiles, atributos multivaluados y agregación.

**Entidad débil:** entidad sin identificador propio suficiente; su existencia depende de la entidad identificadora.

**Herencia:** propiedad por la cual una subclase adquiere automáticamente los atributos y relaciones de su superclase.

**OID:** identificador único asignado automáticamente a cada objeto en el modelo orientado a objetos, independiente del valor de los atributos.

**ORDBMS / Modelo objeto-relacional:** extensión del modelo relacional con UDT, herencia de tablas, colecciones y referencias entre objetos.

**Especialización:** proceso top-down de dividir una superclase en subclases con atributos propios adicionales.

**Generalización:** proceso bottom-up de agrupar entidades con atributos comunes en una superclase.

---

*Bases de Datos Avanzadas — UAM Cuajimalpa*
*Versión compacta: Modelos Semánticos · EER y Modelo Conceptual Orientado a Objetos*
