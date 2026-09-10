# Modelos Semánticos de Datos
## Bases de Datos Avanzadas — UAM Cuajimalpa
### Sesión 3 · Modelo EER y Modelo Conceptual Orientado a Objetos

---

## 1. ¿Por qué un modelo semántico?

En sesiones anteriores quedó claro que el modelo relacional es poderoso para almacenar y consultar información estructurada, pero muestra sus costuras cuando el dominio es rico: jerarquías de tipos, atributos que pueden tener varios valores, entidades que no tienen identidad propia fuera de un contexto. El modelo relacional puede representar *cualquier* cosa, pero a veces lo hace con dificultad, forzando al diseñador a tomar atajos que oscurecen el significado real del dominio.

---

Un **modelo semántico de datos** es un modelo conceptual cuyo objetivo principal es capturar el *significado* del dominio que se va a representar: qué tipos de cosas existen, cómo se clasifican, qué restricciones impone el mundo real y cómo se relacionan los conceptos entre sí. Todo esto se decide *antes* de pensar en tablas, columnas o índices.

---

### Analogía: el plano arquitectónico y la lista de materiales

Imagínense dos formas de describir una casa. La primera es una **lista de materiales**: 800 ladrillos, 40 vigas de acero, 12 puertas, 25 ventanas. La segunda es un **plano arquitectónico**: un diagrama que muestra dónde va cada ladrillo, cuáles vigas son estructurales, qué puertas son exteriores y cuáles interiores, qué ventanas dan a la fachada. Ambas descripciones hablan de la misma casa, pero el plano captura el *significado* de cada pieza dentro del todo.

El modelo relacional plano es la lista de materiales: fiel, completa, pero sin estructura semántica explícita. Un modelo semántico como el EER es el plano arquitectónico: describe el dominio tal como se entiende, no solo como se almacena.

---

### Ejemplo: el archivo de un hospital

Considérense los registros de personas en un hospital. En una tabla relacional plana, todos caben en `PERSONA(id, nombre, fecha_nacimiento, telefono, especialidad, cedula_prof, num_expediente, alergias, turno, area)`. Pero en la realidad del hospital hay **médicos**, **pacientes** y **personal administrativo**: tres tipos de personas con atributos y responsabilidades distintas. Un médico tiene especialidad y cédula profesional; un paciente tiene número de expediente y alergias registradas; un administrativo tiene turno y área asignada.

Forzar todo en una sola tabla plana produce columnas con valores nulos en la mayoría de los registros y hace imposible imponer, por ejemplo, que *todo médico debe tener cédula profesional registrada* o que *los pacientes no pueden tener área asignada*. Un modelo semántico resuelve esto con jerarquías, herencia y tipos especializados.

---

## 2. El Modelo Entidad-Relación Extendido (EER)

El **Modelo Entidad-Relación Extendido** — conocido por sus siglas en inglés como **EER** (*Enhanced Entity-Relationship*) — es una extensión del modelo E-R clásico desarrollada en la década de 1980, principalmente por Ramez Elmasri y Shamkant Navathe. Su propósito fue dotar al modelado conceptual de herramientas más ricas para representar dominios complejos como sistemas de manufactura, telecomunicaciones e ingeniería.

---

El EER conserva todos los elementos del modelo E-R básico: entidades, atributos, relaciones, cardinalidad y restricciones de participación. A esos elementos les suma cuatro constructores adicionales que son el núcleo de esta sesión:

- **Especialización y generalización** — jerarquías entre tipos de entidades con herencia de atributos y relaciones
- **Atributos multivaluados** — atributos que pueden tomar más de un valor para la misma ocurrencia
- **Entidades débiles** — entidades cuya identidad depende de otra entidad
- **Agregación** — tratar una relación como entidad de nivel superior

---

### Recordatorio de notación base

Antes de avanzar, se repasan los símbolos del E-R estándar que también aparecen en todo diagrama EER:

- **Rectángulo simple** → entidad fuerte
- **Rectángulo doble** → entidad débil
- **Elipse simple** → atributo simple
- **Elipse doble** → atributo multivaluado
- **Elipse discontinua** → atributo derivado
- **Atributo subrayado** → atributo identificador (equivalente funcional a la llave primaria en el diseño lógico)
- **Atributo subrayado con línea discontinua** → discriminante de entidad débil
- **Rombo simple** → relación entre entidades fuertes
- **Rombo doble** → relación identificadora (conecta entidad débil con su entidad fuerte)
- **Línea doble** en la conexión entidad–relación → participación total
- **Línea simple** en la conexión entidad–relación → participación parcial

---

## 3. Entidades Débiles

Una **entidad débil** es un tipo de entidad que no posee atributos propios suficientes para identificar de forma única sus ocurrencias. Depende de la existencia de otra entidad —llamada **entidad identificadora** o **entidad propietaria**— tanto para su identidad como para su existencia: si la entidad propietaria desaparece, las ocurrencias de la entidad débil pierden sentido o deben eliminarse también.

---

El conjunto de atributos que, *combinado* con el identificador de la entidad propietaria, permite distinguir cada ocurrencia de la entidad débil recibe el nombre de **discriminante** o **llave parcial**. En el diagrama se representa con subrayado discontinuo. La relación que conecta a la entidad débil con su entidad propietaria es la **relación identificadora**, representada con rombo doble.

---

### Ejemplo tecnológico: lecturas de sensores

En una red de monitoreo ambiental, cada sensor genera cientos de lecturas a lo largo del tiempo. Una lectura individual no tiene sentido fuera del contexto del sensor que la produjo: si se perdiera la referencia al sensor, sería imposible saber qué dispositivo, en qué ubicación y bajo qué condiciones se generó esa lectura.

```
[SENSOR] ─────<GENERA>════[LECTURA]
 id_sensor              discriminante: timestamp
 tipo                   valor_medido
 ubicacion              unidad
                        calidad_señal
```

La entidad `LECTURA` es débil: su identificación completa requiere combinar `id_sensor` (proveniente de `SENSOR`) con `timestamp` (su discriminante). Dos sensores distintos pueden generar una lectura en el mismo instante; el `timestamp` solo no basta.

---

### Ejemplo cotidiano: los renglones de una factura

En un negocio, una factura agrupa varios productos comprados. El renglón número 3 de la factura A es un objeto distinto al renglón número 3 de la factura B, aunque ambos sean "el tercer renglón". Fuera de su factura, ese renglón no tiene identidad propia: ¿quién lo compró?, ¿cuándo?, ¿a qué precio total? Son preguntas que solo se responden en el contexto de la factura que lo contiene.

- `FACTURA` es la entidad identificadora (fuerte).
- `DETALLE_FACTURA` es la entidad débil.
- El discriminante de `DETALLE_FACTURA` es `num_renglon`.
- La relación identificadora es `CONTIENE` (rombo doble).
- Si se borra una factura, todos sus renglones de detalle deben borrarse también.

---

### ¿Cuándo reconocer una entidad débil?

Una entidad es débil cuando se cumplen las tres condiciones siguientes:

1. No tiene un identificador propio que sea suficiente por sí solo para distinguir sus ocurrencias.
2. Su ciclo de vida está ligado al de otra entidad: nace con ella y muere con ella.
3. Sus ocurrencias solo se distinguen *dentro* del contexto de la entidad propietaria.

Si una de esas tres condiciones no se cumple, conviene reconsiderar si la entidad es realmente débil o simplemente tiene una relación de cardinalidad 1:N con otra entidad fuerte.

---

## 4. Atributos Multivaluados

Un **atributo multivaluado** es aquel que puede contener más de un valor para la misma ocurrencia de una entidad. Desde el punto de vista del mundo real, no es raro: una persona puede hablar varios idiomas, un dispositivo puede tener varios números de serie registrados en distintas fechas, un curso puede impartirse en varios horarios. En el diagrama EER se representa con una **elipse doble** (doble borde).

---

El modelo relacional clásico no admite atributos multivaluados directamente en una columna sin violar la primera forma normal. El EER los representa de manera explícita en el nivel conceptual, dejando al diseñador lógico la decisión de cómo materializarlos —generalmente mediante una tabla auxiliar que almacena los valores individuales con referencia a la entidad principal.

---

### Ejemplo tecnológico: sistema de autenticación multi-factor

En un sistema de autenticación, un usuario puede tener registrados varios métodos de verificación: correo electrónico, número de teléfono móvil, aplicación autenticadora y llave de hardware (token físico). El atributo `metodo_2FA` es multivaluado porque un mismo usuario puede tener entre cero y varios métodos activos simultáneamente, y el conjunto puede cambiar con el tiempo.

```
           [USUARIO]
          /    |    \
      {id}  {nombre}  {metodo_2FA}  ← elipse doble
                       valores posibles:
                       email | SMS | app_auth | llave_HW
```

---

### Ejemplo cotidiano: los idiomas de una persona

Una persona puede hablar uno o más idiomas. El atributo `idioma` en la entidad `PERSONA` es multivaluado: María habla español e inglés; Ahmed habla árabe, francés y alemán. No hay un número fijo de idiomas por persona, y cada valor es simplemente "un idioma" más, sin estructura interna diferente.

---

### Distinción clave: multivaluado vs. compuesto

Un atributo **compuesto** tiene partes con significado propio y estructura interna. Por ejemplo, `dirección` se divide en `calle`, `número`, `colonia`, `ciudad` y `código postal`: cada parte es un dato distinto. Un atributo **multivaluado** tiene múltiples ocurrencias del mismo tipo simple: `teléfono` puede ser `55-1234-5678` y `55-8765-4321`, y ambos son simplemente "un teléfono".

Un atributo puede ser compuesto *y* multivaluado al mismo tiempo: `teléfono` podría tener estructura interna `{número, tipo}` (donde `tipo` es fijo o móvil) y a la vez permitir varios valores por persona. En el diagrama, un atributo compuesto y multivaluado se representa con una elipse doble que tiene subelipses internas.

---

## 5. Especialización y Generalización

### Definiciones

La **especialización** es un proceso de diseño de arriba hacia abajo (*top-down*): se parte de una entidad general —la **superclase**— y se identifican subgrupos dentro de ella que poseen atributos o participan en relaciones adicionales que el resto de las ocurrencias no tiene. Cada subgrupo se convierte en una **subclase**.

La **generalización** es el proceso inverso, de abajo hacia arriba (*bottom-up*): se parte de varias entidades que comparten atributos y relaciones comunes, y se factorizan esos elementos compartidos en una nueva entidad general que los agrupa.

---

Ambos procesos producen el mismo resultado en el diagrama: una **jerarquía de generalización/especialización**. La diferencia está únicamente en la dirección del razonamiento de diseño. En la práctica, los diseñadores combinan ambos procesos: generalizan entidades previamente existentes y, al mismo tiempo, especializan entidades generales para capturar subtipos relevantes.

---

### Herencia en el EER

La **herencia** es la propiedad por la cual una subclase adquiere automáticamente todos los atributos y relaciones definidos en su superclase, sin necesidad de redefinirlos. La subclase puede además agregar atributos y relaciones propios adicionales.

Esta propiedad elimina redundancia: si diez subclases de `DISPOSITIVO` necesitan almacenar `ubicacion_gps` y `fecha_instalacion`, esos atributos se definen una sola vez en la superclase y todas las subclases los heredan.

---

### Restricciones de la jerarquía

Toda jerarquía EER puede acompañarse de dos restricciones independientes que precisan su semántica:

**Restricción de disjunción** — ¿puede una ocurrencia pertenecer a más de una subclase?

- `d` — **Disjunta**: una ocurrencia pertenece a *lo sumo a una* subclase. Un vehículo es automóvil o motocicleta, no ambas cosas.
- `o` — **Superpuesta**: una ocurrencia puede pertenecer a *varias* subclases simultáneamente. Un empleado puede ser a la vez supervisor y técnico de campo.

---

**Restricción de completitud** — ¿debe toda ocurrencia de la superclase pertenecer a alguna subclase?

- **Total** (línea doble entre superclase y el círculo de jerarquía): *toda* ocurrencia de la superclase debe pertenecer a al menos una subclase. Todo dispositivo de la red es exactamente uno de los tipos definidos.
- **Parcial** (línea simple): algunas ocurrencias de la superclase pueden no pertenecer a ninguna subclase. Algunos empleados de la empresa no son ni supervisores ni técnicos; solo son personal de apoyo general.

---

### Notación en el diagrama EER

La jerarquía se dibuja de la siguiente manera:

1. La **superclase** en la parte superior (rectángulo simple).
2. Una línea desde la superclase hacia un **círculo** que contiene la letra `d` (disjunta) o `u` / `o` (superpuesta).
3. Líneas individuales del círculo hacia cada **subclase** (rectángulos).
4. Si la línea entre la superclase y el círculo es doble → especialización total; si es simple → especialización parcial.
5. Los atributos propios de cada subclase se representan dentro o junto a la subclase correspondiente; los atributos heredados *no* se repiten.

---

### Ejemplo completo: red de sensores ambientales

Una ciudad inteligente despliega tres tipos de dispositivos en campo. Todos comparten características comunes, pero cada tipo tiene requisitos específicos que los diferencian.

**Superclase:** `DISPOSITIVO`
Atributos: `id_dispositivo`, `ubicacion_gps`, `fabricante`, `fecha_instalacion`, `estado`

**Subclases** (especialización **disjunta** y **total** — todo dispositivo es exactamente uno de los tres tipos):

- `SENSOR` — agrega: `tipo_medida` (temperatura, humedad, CO₂, presión), `frecuencia_muestreo_hz`, `rango_min`, `rango_max`
- `ACTUADOR` — agrega: `tipo_accion` (abrir_valvula, activar_ventilador), `voltaje_operacion`
- `GATEWAY` — agrega: `protocolo_comunicacion` (LoRa, Zigbee, WiFi), `capacidad_nodos_max`

```
               [DISPOSITIVO]
               id_dispositivo
               ubicacion_gps
               fabricante
               fecha_instalacion
               estado
                     ║         ← línea doble: total
                  ───d───      ← d: disjunta
                /    |    \
         [SENSOR] [ACTUADOR] [GATEWAY]
         tipo_medida tipo_accion protocolo
         frecuencia  voltaje     capacidad
         rango_min
         rango_max
```

Con esta jerarquía queda expresado que: (a) todo dispositivo es exactamente uno de los tres tipos, (b) los atributos como `id_dispositivo` y `ubicacion_gps` se definen una sola vez y (c) las restricciones de dominio —como que un sensor *debe* tener frecuencia de muestreo— se pueden imponer por subclase.

---

### Ejemplo cotidiano: personal de una universidad

Se parte de dos entidades modeladas por separado:

- `PROFESOR(RFC, nombre, departamento, grado_academico, tipo_contrato)`
- `ESTUDIANTE(matricula, nombre, programa, trimestre_ingreso)`

Al notar que ambas entidades comparten `nombre`, `fecha_nacimiento` y `correo_institucional`, se generaliza hacia una superclase `PERSONA`:

- `PERSONA` → `id_persona`, `nombre`, `fecha_nacimiento`, `correo_institucional`
- `PROFESOR` (subclase) → agrega `RFC`, `departamento`, `grado_academico`, `tipo_contrato`
- `ESTUDIANTE` (subclase) → agrega `matricula`, `programa`, `trimestre_ingreso`

La restricción adecuada aquí es **superpuesta y parcial**: superpuesta porque algunos profesores de la universidad también cursan estudios de posgrado en ella (son a la vez profesor y estudiante); parcial porque hay personal administrativo que es persona pero no cae en ninguna de las dos subclases modeladas.

---

### Ejercicio de reflexión

> Se está diseñando la base de datos de una biblioteca universitaria. Las personas que interactúan con la biblioteca son: estudiantes de licenciatura, estudiantes de posgrado, profesores e investigadores externos con convenio.
>
> **Pregunta:** ¿Cuál sería la superclase adecuada? ¿La especialización debería ser disjunta o superpuesta? ¿Total o parcial? Toma en cuenta que un investigador externo puede ser también profesor de otra institución, y que algunos profesores de la universidad son simultáneamente estudiantes de posgrado en la misma institución.

Escribe la respuesta justificando cada restricción antes de ver la discusión general del grupo.

---

### Herencia múltiple

En algunos dominios, una subclase puede heredar de más de una superclase. Este caso se llama **herencia múltiple**.

Ejemplo: en el sistema universitario, un `ASISTENTE_DE_INVESTIGACION` es simultáneamente un `ESTUDIANTE` (tiene matrícula, programa) y un `EMPLEADO` (tiene salario, número de trabajador, horas contratadas). La subclase `ASISTENTE_DE_INVESTIGACION` hereda los atributos de ambas superclases y puede agregar los suyos propios.

La herencia múltiple es potente pero introduce complejidad: si dos superclases definen un atributo con el mismo nombre (por ejemplo, ambas tienen un atributo `id`), el diseñador debe especificar cómo se resuelve el conflicto.

---

## 6. Agregación

La **agregación** es una abstracción que permite tratar una **relación** —junto con todas las entidades que conecta— como si fuera ella misma una entidad de nivel superior. Esto hace posible que esa relación participe en *otras* relaciones.

Esta construcción es necesaria porque el modelo E-R estándar no permite que una relación participe directamente en otra relación. Cuando en el dominio real existe un hecho de que "una relación entre A y B tiene a su vez una relación con C", el E-R básico no puede expresarlo directamente sin introducir una entidad artificial. La agregación resuelve esto de manera semánticamente limpia.

---

### Analogía: el contrato de obra

Cuando una empresa contrata a un proveedor para ejecutar un proyecto específico, ese **hecho contractual** — la relación entre empresa, proveedor y proyecto — puede a su vez relacionarse con otras cosas: las facturas que genera ese contrato, los supervisores asignados específicamente a ese contrato, o las penalizaciones aplicadas por incumplimiento.

El "contrato" en sí mismo es una relación que se convierte en sujeto de otras relaciones. En el mundo real esto es natural; en el E-R básico, modelarlo exige crear una entidad artificial `CONTRATO`. La agregación lo expresa directamente, sin añadir entidades que no pertenecen al vocabulario del dominio.

---

### Ejemplo tecnológico: asignación de técnicos a proyectos de infraestructura

En un sistema de gestión de infraestructura de redes, los técnicos trabajan en proyectos de instalación. Esa relación `TRABAJA_EN` entre `TÉCNICO` y `PROYECTO` tiene fecha de inicio, horas semanales asignadas y un rol específico. Ahora bien, esa asignación puede requerir ciertos equipos especializados: un analizador de espectro, un medidor de potencia óptica, un equipo de prueba OTDR. Esos equipos no se asignan al técnico ni al proyecto por separado; se asignan a la **combinación específica** técnico+proyecto.

Sin agregación, habría que crear una entidad artificial intermedia solo para poder relacionar el equipo con la asignación. Con agregación, la relación `TRABAJA_EN` se trata como entidad de nivel superior y se le agrega la relación `REQUIERE` con `EQUIPO`:

```
╔══════════════════════════════════════╗
║  [TÉCNICO]──<TRABAJA_EN>──[PROYECTO] ║
║               fecha_inicio           ║
║               horas_semanales        ║
║               rol                    ║
╚══════════════════════════════════════╝
                    |
               <REQUIERE>
                    |
               [EQUIPO]
               num_serie
               tipo_equipo
               fecha_prestamo
```

El rectángulo exterior (representado con línea discontinua en la notación formal) es la **agregación** de la relación `TRABAJA_EN` funcionando como entidad de nivel superior.

---

### Ejemplo cotidiano: observación de clases universitarias

En una institución, un `PROFESOR` imparte una `MATERIA` a un `GRUPO` en un periodo determinado. Esa relación ternaria representa una `IMPARTICIÓN`. Los evaluadores externos de un proceso de acreditación observan `IMPARTICIONES` específicas: no observan al profesor en abstracto ni a la materia en abstracto, sino la combinación concreta profesor+materia+grupo en un periodo.

La relación `OBSERVA` conecta a `EVALUADOR` con la agregación de `IMPARTICIÓN`. Esto también permite registrar la fecha de la observación, el instrumento de evaluación utilizado y el dictamen, todos como atributos de la relación `OBSERVA`.

---

### Diferencia entre agregación y composición

En notaciones como UML, se distinguen dos variantes de relación todo-parte:

- **Agregación abierta** (*aggregation*): la parte puede existir independientemente del todo. Un motor puede existir sin estar en un automóvil; puede repararse y reinstalarse en otro vehículo.
- **Composición fuerte** (*composition*): las partes no tienen existencia independiente del todo. Los capítulos de un libro no existen fuera de ese libro; si el libro se elimina, los capítulos desaparecen con él.

En el contexto del EER, el término "agregación" se usa principalmente para referirse a la abstracción de una relación como entidad de nivel superior (tal como se describió arriba). La distinción todo-parte con sus variantes se aborda con mayor formalidad en el modelo orientado a objetos.

---

## 7. Comparación: E-R Simple vs. EER para el mismo problema

Para ver concretamente la ganancia expresiva del EER, se modela el mismo dominio de las dos formas: primero en E-R básico y luego en EER.

**Dominio:** sistema de monitoreo de una red de sensores desplegados en zonas de una ciudad inteligente.

---

### El modelo E-R simple

En el modelo E-R básico, todos los tipos de dispositivos deben caber en una sola entidad `DISPOSITIVO`. No hay forma de expresar que algunos dispositivos generan lecturas numéricas continuas, otros ejecutan acciones físicas y otros solo retransmiten señales. Los atributos específicos de cada tipo quedan como columnas opcionales, con valores nulos para todos los registros que no son de ese tipo.

```
[DISPOSITIVO]──────────<GENERA>────────[LECTURA]
  id_disp
  tipo_disp    ← texto libre: 'sensor' | 'actuador' | 'gateway'
  ubicacion
  frecuencia_Hz    ← NULL para actuadores y gateways
  tipo_medida      ← NULL para actuadores y gateways
  tipo_accion      ← NULL para sensores y gateways
  voltaje_op       ← NULL para sensores pasivos y gateways
  protocolo        ← NULL para sensores y actuadores
  nodos_max        ← NULL para sensores y actuadores
```

**Problemas que esto genera:**

- Columnas con NULL masivo: la mayoría de los registros tendrán la mayoría de las columnas vacías.
- No es posible imponer que *todo sensor debe tener frecuencia de muestreo registrada*, porque la columna también existe en actuadores y gateways donde sería NULL por diseño.
- Agregar un nuevo tipo de dispositivo (por ejemplo, una cámara de monitoreo) exige evaluar si el esquema de la tabla única necesita nuevas columnas.
- Las consultas que necesitan datos específicos de un tipo deben incluir siempre un filtro `WHERE tipo_disp = 'sensor'`, lo que no está garantizado por el esquema.

---

### El modelo EER equivalente

```
                [DISPOSITIVO]
                id_dispositivo
                ubicacion_gps
                estado
                fabricante
                fecha_instalacion
                      ║           ← línea doble: total
                   ───d───        ← disjunta
                 /    |    \
           [SENSOR]  [ACTUADOR]  [GATEWAY]
           tipo_medida tipo_accion protocolo
           frecuencia  voltaje     nodos_max
           rango_min
           rango_max
                 |
           (participación total)
                 |
           <GENERA>  ← rombo doble (relación identificadora)
                 ║
           [LECTURA]     ← entidad débil
           ~timestamp~   ← discriminante (subrayado discontinuo)
           valor
           unidad
           calidad_señal
```

**Ganancias del modelo EER sobre el E-R plano:**

- Las restricciones de dominio son explícitas: un sensor *debe* tener `frecuencia` y `rango_min`; un actuador *debe* tener `voltaje_op`. El esquema impone estas reglas, no el código de la aplicación.
- La herencia elimina redundancia: `id_dispositivo`, `ubicacion_gps` y `estado` se definen una sola vez y todas las subclases los poseen.
- La entidad débil `LECTURA` captura la dependencia de existencia: si se elimina un sensor, sus lecturas se eliminan en cascada por diseño conceptual.
- El modelo se extiende fácilmente: agregar una nueva subclase `CAMARA` solo implica añadir un nuevo rectángulo con sus atributos propios; el resto del diagrama no se modifica.

---

### Síntesis: limitaciones que el EER suaviza

El EER alivia —aunque no elimina del todo— las siguientes limitaciones del modelo relacional plano:

- **Jerarquías de tipos** → resueltas con especialización/generalización y herencia de atributos
- **Columnas con NULL masivo** → resueltas porque cada subclase define solo sus atributos propios
- **Dependencias de existencia** → resueltas con entidades débiles y relaciones identificadoras
- **Atributos con múltiples valores** → resueltos con atributos multivaluados explícitos
- **Relaciones que participan en relaciones** → resueltas con agregación

Lo que el EER **no resuelve**: comportamiento (métodos), encapsulamiento, identidad de objeto independiente del valor de los atributos, herencia de comportamiento y polimorfismo. Esas capacidades pertenecen al modelo orientado a objetos, que se aborda a continuación.

---

## 8. Modelo Conceptual Orientado a Objetos

### Clase y objeto

Una **clase** es una plantilla abstracta que describe la estructura y el comportamiento de un conjunto de entidades del dominio que comparten las mismas características. En el nivel conceptual, una clase es simplemente una "categoría de cosas del mundo real" que se quiere modelar.

Un **objeto** es una instancia concreta de una clase: representa una entidad específica del dominio con valores asignados a los atributos de su clase. Cada objeto posee un **identificador de objeto** (OID) único, asignado automáticamente por el sistema, que lo distingue de cualquier otro objeto *independientemente de los valores de sus atributos*.

---

Esta última propiedad es importante: en el modelo relacional, dos filas con los mismos valores en todas las columnas son indistinguibles (o están prohibidas por la llave primaria). En el modelo orientado a objetos, dos objetos pueden tener exactamente los mismos valores en todos sus atributos y aun así ser objetos diferentes, porque cada uno tiene su propio OID.

---

### Representación en diagrama de clases (UML)

En el **diagrama de clases UML** — que es la notación estándar para el modelo conceptual orientado a objetos — cada clase se representa como un rectángulo dividido en tres secciones:

```
┌──────────────────────────┐
│         SENSOR           │  ← nombre de la clase
├──────────────────────────┤
│ id: String               │  ← atributos con tipo de dato
│ ubicacion: Coordenada    │
│ tipo_medida: String      │
│ frecuencia: Float        │
│ estado: EstadoDisp       │
├──────────────────────────┤
│ tomar_lectura(): Lectura │  ← métodos (operaciones)
│ calibrar(): void         │
│ cambiar_estado(): void   │
└──────────────────────────┘
```

La primera sección contiene el nombre de la clase. La segunda contiene los atributos con sus tipos de dato. La tercera contiene los métodos, que representan las operaciones que los objetos de esa clase pueden realizar. Esta tercera sección es la diferencia más visible respecto al EER: el EER modela únicamente estructura; el diagrama de clases modela estructura *y* comportamiento.

---

### Asociaciones entre clases

Una **asociación** en el diagrama de clases es el equivalente conceptual de una relación en el E-R. Se representa como una línea que conecta dos clases, con **notación de multiplicidad** en los extremos:

- `1..1` → exactamente uno (o simplemente `1`)
- `0..1` → cero o uno (opcional)
- `1..*` → uno o más
- `0..*` → cero o más (o simplemente `*`)

La asociación también puede tener un nombre y una dirección de lectura (indicada con una flecha abierta sobre la línea), así como atributos propios que describen la relación en sí.

---

### Herencia en el diagrama de clases

La herencia entre clases se representa con una **flecha de punta triangular vacía** que apunta *de la subclase hacia la superclase*, leyéndose como "es un tipo de": `SENSOR` es un tipo de `DISPOSITIVO`.

```
        [DISPOSITIVO]
              △
        ┌─────┴─────┐
   [SENSOR]     [ACTUADOR]    [GATEWAY]
```

A diferencia del EER, el diagrama de clases UML no tiene símbolos integrados para indicar si la especialización es disjunta o total. Esas restricciones se expresan con etiquetas adicionales sobre la jerarquía: `{disjoint}` (disjunta), `{overlapping}` (superpuesta), `{complete}` (total), `{incomplete}` (parcial).

---

### Ejemplo: sistema de alertas sobre una red de sensores

```
┌─────────────────────────────┐
│           SENSOR            │
├─────────────────────────────┤
│ id: String                  │
│ ubicacion: Coordenada       │
│ estado: {activo,falla,mant} │
│ tipo_medida: String         │
│ frecuencia: Float           │
├─────────────────────────────┤
│ tomar_lectura(): Lectura    │
│ reportar_estado(): String   │
└─────────────────────────────┘
        0..*  genera  1
        ──────────────────────
┌─────────────────────────────┐
│           LECTURA           │
├─────────────────────────────┤
│ timestamp: DateTime         │
│ valor: Float                │
│ unidad: String              │
├─────────────────────────────┤
│ validar(): Boolean          │
│ convertir_unidad(): Float   │
└─────────────────────────────┘
        0..*  activa  0..*
        ──────────────────────
┌─────────────────────────────┐
│           ALERTA            │
├─────────────────────────────┤
│ id_alerta: String           │
│ nivel: {bajo,medio,critico} │
│ descripcion: String         │
│ timestamp_emision: DateTime │
├─────────────────────────────┤
│ escalar(): void             │
│ resolver(): void            │
└─────────────────────────────┘
```

Nótese que la relación entre `LECTURA` y `ALERTA` es de muchos a muchos (`0..*` en ambos extremos): una lectura puede activar varias alertas (distintos umbrales configurados) y una alerta puede estar respaldada en múltiples lecturas consecutivas.

---

### Diferencias entre EER y modelo conceptual orientado a objetos

Los dos modelos representan conceptos similares pero con diferencias relevantes cuando se piensa en implementación:

**Sobre el comportamiento:**
El EER es un modelo de estructura de datos: describe entidades, atributos y relaciones, pero no el comportamiento de las entidades. El diagrama de clases incluye métodos, que representan las operaciones que los objetos pueden ejecutar.

**Sobre la identidad:**
El EER identifica las ocurrencias mediante atributos identificadores (equivalentes a llaves primarias). El modelo OO usa OID (identificador de objeto) asignado automáticamente, independiente del valor de los atributos.

**Sobre las restricciones de jerarquía:**
El EER tiene notación explícita e integrada para las restricciones de jerarquía (d/o, total/parcial). UML expresa esas restricciones mediante etiquetas de texto adicionales.

**Sobre el propósito de diseño:**
El EER fue creado para derivar esquemas de bases de datos (relacionales o relacionales extendidos). El diagrama de clases está orientado al diseño de software y puede derivar tanto hacia código fuente como hacia bases de datos orientadas a objetos u objeto-relacionales.

---

## 9. Relación entre Modelos Semánticos, Modelo OO y Modelos Objeto-Relacionales

### El espectro de abstracción

Los modelos de datos se ubican en un espectro que va desde la abstracción conceptual pura hasta la implementación física:

```
NIVEL CONCEPTUAL                               NIVEL FÍSICO
────────────────────────────────────────────────────────────
Modelo semántico  →  Modelo lógico  →  Modelo físico
(EER, diagrama de    (relacional,      (tablas, índices,
  clases UML)        objeto-relacional) almacenamiento en disco)
```

El EER y el diagrama de clases pertenecen al nivel conceptual: describen *qué* existe en el dominio sin especificar *cómo* se almacena. El modelo relacional y el modelo objeto-relacional pertenecen al nivel lógico: describen la estructura de almacenamiento con independencia del motor físico concreto.

---

### Del modelo EER al modelo relacional: las tres estrategias de mapeo de jerarquías

Cuando un diseño EER con jerarquías se traduce al modelo relacional, las subclases deben "aplanarse" mediante alguna de las siguientes estrategias:

**Estrategia 1 — Una tabla para toda la jerarquía:**
Todos los atributos de la superclase y de todas las subclases van a una única tabla, con una columna discriminante que indica el tipo. Los atributos de subclases que no aplican a una ocurrencia quedan como NULL.

- Ventaja: consultas simples sobre la superclase no requieren JOINs.
- Desventaja: NULLs masivos y pérdida de restricciones de dominio por subclase.

---

**Estrategia 2 — Una tabla para la superclase más una tabla por cada subclase:**
La superclase tiene su propia tabla. Cada subclase tiene una tabla con solo sus atributos propios, ligada a la tabla de la superclase mediante su identificador.

- Ventaja: más normalizado; se pueden imponer restricciones por subclase.
- Desventaja: recuperar todos los datos de un objeto requiere un JOIN entre la tabla de la superclase y la tabla de la subclase correspondiente.

---

**Estrategia 3 — Solo tablas de subclases (sin tabla de superclase):**
Los atributos de la superclase se duplican en cada tabla de subclase. No existe tabla de superclase.

- Ventaja: consultas sobre una sola subclase no requieren JOINs.
- Desventaja: redundancia de atributos de la superclase; las consultas sobre la superclase requieren UNION de todas las subclases.

La elección entre estas estrategias depende no solo del modelo conceptual sino del patrón de acceso a los datos: si la mayoría de las consultas trabajan con una sola subclase, la estrategia 3 puede ser la más eficiente; si las consultas mezclan tipos, la estrategia 2 o la 1 pueden ser más convenientes.

---

### El modelo objeto-relacional: convergencia entre dos mundos

El **modelo objeto-relacional** (ORDBMS, *Object-Relational Database Management System*) es un intento de integrar la expresividad del modelo orientado a objetos con la infraestructura probada del modelo relacional. En lugar de construir un sistema completamente nuevo, extiende el motor relacional con características OO.

Las extensiones más relevantes que un sistema objeto-relacional añade sobre el relacional puro son:

- **Tipos definidos por el usuario (UDT):** permiten definir tipos de datos complejos más allá de enteros, cadenas y fechas. Por ejemplo, un tipo `Coordenada` con atributos `latitud` y `longitud`, o un tipo `Rango` con `valor_min` y `valor_max`.
- **Herencia de tablas:** una tabla puede heredar columnas y restricciones de otra tabla, de manera análoga a la herencia de clases.
- **Tipos de colección:** arreglos y conjuntos como tipos de dato de una columna, lo que permite representar atributos multivaluados directamente sin una tabla auxiliar.
- **Métodos de tipo:** funciones asociadas a un UDT que encapsulan comportamiento junto a los datos.
- **Referencias entre objetos (REF):** referencias directas entre filas de distintas tablas, permitiendo navegar relaciones sin JOINs explícitos.

PostgreSQL es el ejemplo más conocido y ampliamente usado de base de datos objeto-relacional de código abierto, con soporte para UDT, herencia de tablas, arreglos como tipo de columna y funciones definidas por el usuario.

---

### El mismo dominio en los tres niveles

**Dominio:** gestión de sensores y sus lecturas en una red de monitoreo.

**Nivel conceptual (EER):**
```
DISPOSITIVO (id, ubicacion, estado)
  ├── SENSOR (tipo_medida, frecuencia)    ← subclase
  └── ACTUADOR (tipo_accion, voltaje)     ← subclase
SENSOR ─<GENERA>─ LECTURA (débil: timestamp, valor, unidad)
```

---

**Nivel lógico relacional (mapeo estrategia 2: tabla por subclase):**
```sql
CREATE TABLE dispositivo (
    id_dispositivo   VARCHAR(20) PRIMARY KEY,
    ubicacion_lat    DECIMAL(9,6),
    ubicacion_lon    DECIMAL(9,6),
    estado           VARCHAR(15)
);

CREATE TABLE sensor (
    id_dispositivo   VARCHAR(20) PRIMARY KEY
                     REFERENCES dispositivo(id_dispositivo),
    tipo_medida      VARCHAR(30),
    frecuencia_hz    FLOAT,
    rango_min        FLOAT,
    rango_max        FLOAT
);

-- Llave compuesta: sensor + timestamp (entidad débil → tabla con PK compuesta)
CREATE TABLE lectura (
    id_dispositivo   VARCHAR(20)
                     REFERENCES sensor(id_dispositivo),
    ts               TIMESTAMP,
    valor            FLOAT,
    unidad           VARCHAR(10),
    PRIMARY KEY (id_dispositivo, ts)
);
```

---

**Nivel lógico objeto-relacional (PostgreSQL, usando UDT y herencia):**
```sql
-- Tipo definido por el usuario
CREATE TYPE tipo_coordenada AS (
    latitud   DECIMAL(9,6),
    longitud  DECIMAL(9,6)
);

-- Tabla base (superclase)
CREATE TABLE dispositivo (
    id_dispositivo   VARCHAR(20) PRIMARY KEY,
    ubicacion        tipo_coordenada,
    estado           VARCHAR(15)
);

-- Herencia de tabla: sensor hereda todos los atributos de dispositivo
CREATE TABLE sensor (
    tipo_medida   VARCHAR(30),
    frecuencia_hz FLOAT,
    rango_min     FLOAT,
    rango_max     FLOAT,
    -- atributo multivaluado como arreglo
    etiquetas     TEXT[]
) INHERITS (dispositivo);
```

En este modelo objeto-relacional, una consulta sobre `dispositivo` puede devolver filas que en realidad son sensores con todos sus atributos heredados. El atributo `etiquetas` es un arreglo de texto que representa un atributo multivaluado sin necesidad de una tabla auxiliar.

---

### ¿Por qué no siempre se usa el modelo más expresivo?

Una pregunta natural al comparar estos modelos es: si el EER y el modelo orientado a objetos son más expresivos, ¿por qué no siempre se usa el más expresivo? La respuesta involucra varios factores en tensión:

- **Complejidad de diseño:** un modelo más expresivo exige más decisiones de diseño y más conocimiento del dominio desde el inicio del proyecto.
- **Herramientas y ecosistema:** el modelo relacional acumula décadas de herramientas, optimizadores de consultas y profesionales familiarizados con él.
- **Rendimiento:** los motores relacionales están altamente optimizados para sus operaciones nativas; las extensiones objeto-relacionales pueden introducir sobrecarga en ciertos patrones de acceso.
- **Impedancia objeto-relacional:** incluso con bases de datos más expresivas, cuando la aplicación está escrita en un lenguaje orientado a objetos (Java, Python, C#), sigue existiendo un problema de traducción entre los objetos en memoria y la representación persistente en la base de datos.

Los modelos semánticos, el EER y el modelo orientado a objetos no son una "solución definitiva": son herramientas más ricas para capturar el significado del dominio, con sus propias compensaciones. La elección adecuada depende del dominio, los patrones de acceso, el equipo de desarrollo y la infraestructura disponible.

---

## 10. Actividad Central: Caso de Estudio — Red de Sensores

### Descripción del caso

Se cuenta con los siguientes requisitos para un sistema de monitoreo ambiental urbano que administra una red de dispositivos desplegados en distintas zonas de la ciudad:

1. La ciudad despliega dispositivos de cuatro tipos: **sensores de calidad del aire** (miden CO₂, partículas PM2.5 y ozono), **sensores meteorológicos** (miden temperatura, humedad, presión barométrica y velocidad del viento), **actuadores de respuesta** (abren/cierran válvulas de ventilación y activan aspersores) y **nodos de comunicación** (solo retransmiten datos, sin generar medidas propias).

2. Cada dispositivo tiene un identificador único, coordenadas GPS, fecha de instalación y estado operativo.

3. Los sensores generan lecturas periódicas. Cada lectura tiene una marca de tiempo, un valor numérico y la unidad de medida. Una lectura solo tiene sentido en el contexto del sensor que la generó.

4. Los sensores de calidad del aire pueden generar en el mismo instante lecturas de múltiples contaminantes: una sola "toma de datos" puede incluir simultáneamente el valor de CO₂, el de PM2.5 y el de ozono.

5. Cada dispositivo puede tener asignados varios responsables de mantenimiento: uno para mantenimiento preventivo, otro para mantenimiento correctivo, y posiblemente un tercero especializado en calibración. Los responsables pertenecen a empresas contratistas.

6. Una asignación de mantenimiento — la relación entre un dispositivo y un responsable — puede estar asociada con órdenes de trabajo específicas, que tienen número de orden, fecha y descripción de la tarea.

7. La ciudad divide su territorio en zonas geográficas. Cada zona puede subdividirse en subzonas, y las subzonas en puntos de monitoreo individuales, donde se instalan los dispositivos.

---

### Preguntas guía para el análisis del equipo

Al revisar los requisitos anteriores, el equipo debe identificar qué aspectos **no se expresan bien en un modelo relacional plano** y proponer la alternativa en un modelo EER.

---

**Sobre el requisito 1:**
Los cuatro tipos de dispositivos tienen atributos completamente distintos. ¿Cómo se modelaría esto en una tabla plana? ¿Qué problemas genera? ¿Qué constructor EER resuelve mejor esta situación, y con qué restricciones de jerarquía?

---

**Sobre el requisito 3:**
Las lecturas dependen de la existencia del sensor. ¿Qué ocurre con las lecturas si se elimina el sensor de la base de datos? ¿Qué tipo de entidad es `LECTURA` en el EER? ¿Cuál es su discriminante?

---

**Sobre el requisito 4:**
Un sensor de calidad del aire genera varios valores numéricos en un mismo instante, cada uno de un contaminante distinto. ¿Esto es un atributo multivaluado de `LECTURA`, una entidad débil adicional anidada, o una relación ternaria? Construye un argumento a favor de la representación que elijas y señala sus limitaciones.

---

**Sobre el requisito 5:**
Un dispositivo puede tener varios responsables de mantenimiento. ¿Este hecho se modela como un atributo multivaluado de `DISPOSITIVO` o como una relación independiente con la entidad `RESPONSABLE`? ¿Qué información adicional se pierde si se modela solo como atributo multivaluado?

---

**Sobre el requisito 6:**
La relación entre `DISPOSITIVO` y `RESPONSABLE` genera órdenes de trabajo. ¿Qué constructor EER permite modelar que esa relación participa a su vez en otra relación con `ORDEN_DE_TRABAJO`?

---

**Sobre el requisito 7:**
La jerarquía zona → subzona → punto de monitoreo sugiere una estructura recursiva. ¿Cómo se puede expresar una relación recursiva en el EER? ¿Qué cardinalidad aplica entre zona y subzona?

---

### Entregable del equipo

Cada equipo entrega:

**1. Diagrama EER** del dominio anterior, que incluya como mínimo:
- Una jerarquía de especialización/generalización con sus restricciones explícitas (d/o y total/parcial)
- Al menos un atributo multivaluado representado con elipse doble
- Al menos una entidad débil con su relación identificadora (rombo doble) y discriminante (subrayado discontinuo)
- Al menos un caso de agregación (si el análisis del equipo lo justifica)

**2. Nota de justificación** — máximo media cuartilla por cada decisión de modelado relevante:
- Por qué se eligió jerarquía de especialización en lugar de un atributo de tipo texto en columna única
- Por qué cierta entidad se modeló como débil y no como fuerte con relación 1:N
- Qué restricciones de jerarquía (d/o y total/parcial) se eligieron y por qué
- Qué limitaciones del modelo relacional plano quedan resueltas por cada decisión EER adoptada

---

### Criterios de evaluación del diagrama

Un diagrama EER correcto para este dominio debe cumplir:

- Usar correctamente la notación: rectángulos dobles para entidades débiles, elipses dobles para atributos multivaluados, rombos dobles para relaciones identificadoras, rectángulo discontinuo para agregación.
- Indicar explícitamente las restricciones de la jerarquía: la letra `d` u `o` en el círculo, y línea doble o simple entre la superclase y el círculo.
- Incluir cardinalidad y restricciones de participación (línea simple o doble) en todas las relaciones.
- No duplicar atributos de la superclase dentro de las subclases.
- Subrayar con línea discontinua el discriminante de las entidades débiles.
- Cada relación debe tener un nombre que exprese semánticamente lo que representa.

---

## 11. Glosario

**Agregación (EER):** abstracción que trata una relación, junto con las entidades que conecta, como una entidad de nivel superior para que pueda participar en otras relaciones.

**Atributo derivado:** atributo cuyo valor se puede calcular a partir de otros atributos existentes en el modelo. Se representa con elipse discontinua. Ejemplo: `edad` calculada a partir de `fecha_nacimiento`.

**Atributo discriminante:** atributo (o conjunto de atributos) de una entidad débil que, combinado con el identificador de la entidad propietaria, permite identificar de forma única cada ocurrencia de la entidad débil. Se representa con subrayado discontinuo.

**Atributo multivaluado:** atributo que puede tomar más de un valor para la misma ocurrencia de una entidad. Se representa con elipse doble.

**Clase:** plantilla abstracta que describe la estructura (atributos) y el comportamiento (métodos) de un conjunto de objetos del dominio.

**Completitud (restricción):** restricción de una jerarquía EER que indica si toda ocurrencia de la superclase debe pertenecer (total) o puede no pertenecer (parcial) a alguna subclase.

**Diagrama de clases UML:** representación gráfica del modelo conceptual orientado a objetos que muestra clases, atributos, métodos, herencia y asociaciones entre clases.

**Disjunción (restricción):** restricción de una jerarquía EER que indica si una ocurrencia puede pertenecer a más de una subclase simultáneamente (superpuesta, `o`) o solo a una (disjunta, `d`).

**EER (Enhanced Entity-Relationship):** extensión del modelo E-R clásico con soporte para jerarquías de tipos, herencia, entidades débiles, atributos multivaluados, agregación y tipos unión.

**Entidad débil:** entidad cuya identidad depende de otra entidad (identificadora); no posee un atributo identificador propio suficiente.

**Entidad identificadora:** entidad fuerte de la que depende existencialmente una entidad débil.

**Generalización:** proceso de diseño de abajo hacia arriba en el que se identifican atributos comunes de varias entidades y se agrupan en una superclase.

**Herencia:** propiedad por la cual una subclase adquiere automáticamente todos los atributos y relaciones de su superclase.

**Modelo objeto-relacional (ORDBMS):** sistema de gestión de bases de datos que extiende el modelo relacional con características del modelo orientado a objetos: tipos definidos por el usuario, herencia de tablas, métodos de tipo y colecciones.

**Modelo semántico de datos:** modelo conceptual que describe el significado del dominio — qué tipos de entidades existen, qué restricciones impone el mundo real, cómo se relacionan los conceptos — con independencia de la implementación física.

**Objeto:** instancia concreta de una clase, con valores asignados a sus atributos y un identificador de objeto (OID) único asignado automáticamente.

**OID (Object Identifier):** identificador único asignado por el sistema a cada objeto, independiente de los valores de sus atributos.

**Relación identificadora:** relación entre una entidad débil y su entidad identificadora. Se representa con rombo doble.

**Especialización:** proceso de diseño de arriba hacia abajo en el que una superclase se subdivide en subclases con atributos o relaciones adicionales propios.

**Subclase:** entidad tipo que hereda atributos y relaciones de una superclase y puede agregar los suyos propios.

**Superclase:** entidad tipo general de la que heredan una o más subclases.

**UDT (User-Defined Type):** tipo de dato complejo definido por el diseñador en un sistema objeto-relacional, más allá de los tipos primitivos del sistema.

---

*Bases de Datos Avanzadas — UAM Cuajimalpa*
*Material de clase: Modelos Semánticos de Datos · EER y Modelo Conceptual Orientado a Objetos*
