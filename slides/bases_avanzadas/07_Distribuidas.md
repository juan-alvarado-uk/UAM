# Bases de datos distribuidas: fundamentos, organización y diseño

***

## Por qué distribuir una base de datos

Una base de datos distribuida aparece cuando dejar todos los datos en un solo servidor deja de ser suficiente, ya sea por rendimiento, escalabilidad o por la necesidad de acercar los datos a personas que se encuentran lejos geográficamente. En lugar de tener un único “gran almacén”, se tienen varios almacenes coordinados que, en conjunto, ofrecen la ilusión de una sola base lógica. 

***

### Definición básica

Definición:  
Una **base de datos distribuida** es una colección de datos lógicamente relacionados, almacenados en varios nodos de una red, que se presentan al usuario como si fueran una única base integrada. 

---
- “Lógicamente relacionados” significa que los datos siguen perteneciendo al mismo sistema de información (por ejemplo, el sistema académico completo de una universidad). 
- “Distribuidos en varios nodos” implica que las tablas o partes de ellas están físicamente en diferentes máquinas, centros de datos o regiones. 

***

### Ejemplo 

Una cadena de supermercados.

- Toda la información de inventario podría estar en un solo almacén de datos central, al que todas las sucursales se conectan.  
- En un enfoque distribuido, cada sucursal mantiene parte de la información (lo que vende localmente) y existe coordinación para compartir datos necesarios a nivel nacional (por ejemplo, estadísticas de ventas globales). 

---
Para la persona que revisa un reporte nacional, el sistema parece uno solo, aunque en realidad consulta a varios nodos coordinados.

***

### Ventajas y retos

Ventajas: 

- Mejor rendimiento local: se consulta y actualiza en nodos cercanos a usuarios concretos.  
- Escalabilidad horizontal: es posible agregar nodos y repartir carga.  
- Mayor disponibilidad: si un nodo falla, otros pueden seguir atendiendo ciertas operaciones.

---
Retos principales: 

- Consistencia: mantener la información coherente entre nodos no es trivial.  
- Complejidad de diseño: se debe decidir cómo fragmentar, replicar y coordinar los datos.  
- Coordinación en caso de fallas: se necesitan protocolos para detectar fallas y recuperar el estado.

***

### Para pensar...

Se pide diseñar un sistema de bibliotecas en varias ciudades.  
Preguntas a discutir:

---
- ¿Qué información tendría sentido que esté en todas las sedes (por ejemplo, catálogo global)?  

---
- ¿Qué información conviene que viva localmente (por ejemplo, préstamos de cada sucursal)?  

---
- ¿Qué problemas aparecerían si se pierde momentáneamente la conexión con la sede central?

***

# Arquitecturas: centralizado, cliente–servidor, distribuido y federado

***

### Sistemas centralizados

Definición:  
Un sistema de base de datos **centralizado** es aquel en el que todos los datos residen en un solo servidor, aunque existan muchos clientes conectados a él. 

---
Ejemplo:  
Un pequeño negocio que guarda todas sus ventas y clientes en un solo servidor dentro del local. Si ese servidor se apaga, nadie puede consultar ni registrar ventas.

***

### Arquitectura cliente–servidor

Definición:  
En la arquitectura **cliente–servidor**, un conjunto de clientes (aplicaciones) envían solicitudes a uno o varios servidores de base de datos, que responden con resultados. 

---
Ejemplo tecnológico:  

- Aplicaciones web de la UAM que consultan una base de datos académica central.  
- El navegador actúa como cliente (a través del backend), el servidor de base de datos atiende consultas SQL. 

---
Características:

- El cliente no necesita conocer detalles de almacenamiento físico.  
- El servidor concentra funciones de seguridad, control de concurrencia y consultas complejas. 

***

### Sistemas de bases de datos distribuidos

Definición:  
Un **sistema de bases de datos distribuido** es un conjunto de nodos, cada uno con su propio manejador de base de datos, que cooperan para ofrecer una vista única y coherente de los datos. 

---
Características importantes:

- Transparencia de localización: idealmente, el usuario no sabe en qué nodo está cada dato.  
- Transparencia de fragmentación: una tabla puede estar dividida en partes, pero se ve como una sola. 
- Uso de fragmentación y replicación para lograr rendimiento y tolerancia a fallas. 

---
Analogía:  
Parece un solo “súper almacén de información”, pero por dentro es una red de muchas bodegas coordinadas.

***

### Sistemas federados

Definición:  
Un **sistema de bases de datos federado** integra varias bases de datos que pueden pertenecer incluso a manejadores o dueños distintos, pero que cooperan mediante un esquema común o vistas integradas. 

- Cada base participante conserva su autonomía (puede tener su propio esquema y reglas).  
- La federación expone una vista lógica que permite combinar datos de varias fuentes. 

---
Ejemplo:

- Una federación que integra:  
  - La base de recursos humanos de una institución.  
  - La base académica de alumnos y planes de estudio.  
  - La base contable de pagos y becas.  

Desde la vista federada, se pueden hacer consultas cruzadas sin unificar físicamente todos los datos en un solo servidor.

***

### Comparación breve

| Tipo de sistema  | Datos                             | Autonomía de nodos  | Vista lógica                           |
|------------------|-----------------------------------|---------------------|----------------------------------------|
| Centralizado     | En un solo nodo                   | Nula                | Única, simple                          |
| Cliente–servidor | Servidor central, muchos clientes | Nula en el servidor | Única                                  |
| Distribuido      | Repartidos en varios nodos        | Media               | Única, con transparencia deseable      |
| Federado         | Varias bases existentes           | Alta                | Vista integrada sobre fuentes diversas |

 

***

### Ejemplo

Un servicio de transporte por app

- Un diseño centralizado pone toda la información de viajes, usuarios y pagos en un solo servidor.  


- Un diseño distribuido puede tener clusters por región: Ciudad de México, Guadalajara, Monterrey, cada uno con sus datos locales, pero con mecanismos para obtener estadísticas nacionales. 


- Un sistema federado integraría, además, una base externa para pagos, otra para mapas y otra para verificación de identidad, manteniendo cada una su propia administración.

***

# Fragmentación de datos

***

### Definición general

Definición:  
La **fragmentación** consiste en dividir una relación (tabla lógica) en partes más pequeñas llamadas fragmentos, que pueden almacenarse en distintos nodos, manteniendo la posibilidad de reconstruir la tabla original mediante operaciones como UNION o JOIN. 

---
Objetivos principales:

- Acercar los datos a los usuarios que los usan con más frecuencia.  
- Mejorar rendimiento y escalabilidad al repartir carga entre nodos.  
- Reducir tráfico de red al evitar mover datos que no se necesitan en ciertos sitios. 

---
Requisitos importantes:

- **Completitud**: la unión de todos los fragmentos representa todos los datos originales. 
- **Reconstruibilidad**: se puede recuperar la tabla original con operaciones relacionales adecuadas. 
- **No superposición innecesaria**: en fragmentación pura, un registro no debería aparecer en dos fragmentos al mismo tiempo (salvo que se combine con replicación). 

***

### Fragmentación horizontal

Definición:  
La **fragmentación horizontal** divide una tabla por filas, generando fragmentos que contienen subconjuntos de registros, típicamente definidos por condiciones sobre atributos. 

---
Ejemplo

- Una cadena de gimnasios tiene una tabla de “Socios” con sucursal, nombre, tipo de membresía y fecha de registro.  
- Fragmentación horizontal por sucursal:  
  - Fragmento CDMX: socios cuya sucursal = CDMX.  
  - Fragmento Guadalajara: socios cuya sucursal = Guadalajara.  
  - Fragmento Monterrey: socios cuya sucursal = Monterrey.

Cada gimnasio puede almacenar solo sus socios, pero el sistema central puede reconstruir la tabla global mediante la unión de todos los fragmentos.

---
Ejemplo en contexto académico:

- Tabla Estudiante con atributo campus.  
- Fragmentos:  
  - Estudiante_Cuajimalpa: filas donde campus = “Cuajimalpa”.  
  - Estudiante_Azcapotzalco: filas donde campus = “Azcapotzalco”.  
  - Estudiante_Xochimilco: filas donde campus = “Xochimilco”. 

---
La reconstrucción se realiza con:

\[
Estudiante = Estudiante\_Cuajimalpa \cup Estudiante\_Azcapotzalco \cup Estudiante\_Xochimilco
\]

 
---
Ventajas:

- Cada nodo trabaja solo con “sus” filas, lo que mejora rendimiento local.  
- Es natural cuando las consultas se concentran en regiones o segmentos definidos. 

***

### Ejercicio

Se propone la tabla `Venta(id, tienda, fecha, total)` con muchas filas.

- Diseñar fragmentos horizontales por tienda (por ejemplo, Toluca, CDMX, Puebla).  
- Preguntarse: ¿qué consultas se benefician si cada tienda atiende sus propias ventas?  
- ¿Qué sucede con un reporte nacional de ventas mensuales?

***

### Fragmentación vertical

Definición:  
La **fragmentación vertical** divide una tabla por columnas, generando fragmentos que contienen subconjuntos de atributos, generalmente repitiendo el identificador para poder reconstruir la tabla original mediante JOIN. 

---
Ejemplo

- En un banco, la información básica de clientes (nombre, fecha de nacimiento, CURP) puede almacenarse en un fragmento.  
- Los datos sensibles de seguridad (contraseñas hash, preguntas secretas, factores de autenticación) pueden estar en otro fragmento, quizá en un nodo más protegido. 

---
Ejemplo en tablas (simple)

Tabla original `Cliente(idcliente, nombre, correo, telefono, saldo, limitecredito)`.  

---
Fragmentos:

- `Cliente_DatosBasicos(idcliente, nombre, correo, telefono)`  
- `Cliente_Finanzas(idcliente, saldo, limitecredito)`

---
La reconstrucción se hace con:

\[
Cliente = Cliente\_DatosBasicos \bowtie Cliente\_Finanzas
\]

usando `idcliente` como identificador común. 

---
Ventajas:

- Mejora seguridad y privacidad: ciertos atributos pueden vivir en nodos más controlados.  
- Optimiza I/O si algunas consultas solo necesitan un subconjunto de columnas. 

---
Desventajas:

- Se incrementa el costo de consultas que requieren unir frecuentemente ambos fragmentos.  
- Se debe garantizar que el identificador esté presente en todos los fragmentos. 

***

### Ejercicio

Dada una tabla `Usuario(id, nombre, correo, telefono, fecharegistro, ultimologin, rol)`:

- Proponer una fragmentación vertical que separe datos estáticos (nombre, correo) y datos de actividad (fecharegistro, ultimologin, rol).  
- Plantear un JOIN que reconstruya la vista completa de usuario.

***

### Fragmentación híbrida o mixta

Definición:  
La **fragmentación híbrida** (o mixta) combina fragmentación horizontal y vertical sobre la misma tabla, de modo que el resultado sean fragmentos que son subconjuntos de filas y columnas al mismo tiempo. 

---
Ejemplo:

Se retoma la tabla `Socio(id, sucursal, nombre, correo, tipomembresia, fechainicio, saldo)`.

- Paso 1 – Fragmentación horizontal por sucursal:  
  - `Socio_CDMX`, `Socio_Guadalajara`, `Socio_Monterrey`.  

---
- Paso 2 – Sobre `Socio_CDMX`, fragmentación vertical:  
  - `Socio_CDMX_Publico(id, sucursal, nombre, tipomembresia)`.  
  - `Socio_CDMX_Sensible(id, correo, saldo)`.

---
El conjunto de todos los fragmentos mantiene la información completa del esquema original. 

---
Uso típico:

- Diseño fino donde ciertos nodos necesitan solo parte de los datos de ciertas regiones.  
- Escenarios con requisitos estrictos de seguridad y cumplimiento (por ejemplo, separar datos identificables de datos estadísticos).

***

### Consideraciones de diseño en la fragmentación

Al decidir cómo fragmentar, se discute:

- **Patrones de acceso**: qué consultas son más frecuentes y dónde.  
- **Localidad**: qué datos conviene mantener cerca de qué grupo de usuarios.  
- **Equilibrio de carga**: cómo evitar que un nodo se sature mientras otros están subutilizados. 

También se recuerda que la fragmentación por sí sola no crea copias redundantes; para eso se combina con replicación.

***

# Replicación de datos

***

### Definición y motivación

Definición:  
La **replicación de datos** consiste en mantener múltiples copias de un mismo objeto o fragmento de datos en diferentes nodos de la red, sincronizadas mediante algún protocolo, con el objetivo de mejorar rendimiento de lectura, disponibilidad y tolerancia a fallas. 

---
Motivaciones principales:

- **Rendimiento en lectura**: varios nodos pueden responder consultas sobre los mismos datos.  
- **Alta disponibilidad**: si un nodo falla, otro con la misma información puede seguir atendiendo solicitudes. 
- **Tolerancia a fallas**: el sistema puede seguir funcionando, aun cuando uno o varios nodos estén inactivos. 

---
Analogía:

Un grupo de estudiantes que comparten apuntes de clase.  
Si solo una persona tiene el cuaderno y falta, todos se quedan sin información.  
Si varios tienen copias (actualizadas) de los apuntes, es más difícil que todo el grupo se quede sin acceso.

***

### Tipos de replicación (visión general)

Aunque la terminología exacta puede variar entre productos, a nivel conceptual se distingue: 

- **Replicación completa**: todos los nodos mantienen una copia del conjunto total de datos.  
- **Replicación parcial**: solo ciertos fragmentos se replican en los nodos que los necesitan.  
- **Replicación síncrona**: una actualización se considera confirmada solo cuando ha sido aplicada en todas las réplicas relevantes.  
- **Replicación asíncrona**: una actualización se aplica primero en un nodo y se propaga después a los demás, admitiendo breves periodos de inconsistencia. 

---
Efectos típicos:

- La replicación síncrona mejora la consistencia fuerte, pero puede incrementar la latencia.  
- La replicación asíncrona reduce latencia percibida y mejora disponibilidad, pero puede aceptar estados intermedios donde no todas las réplicas tienen el mismo valor. 

***

### Replicación, rendimiento y tolerancia a fallas 

La replicación se relaciona de forma directa con: 

---
- **Rendimiento**:  
  - Las lecturas pueden balancearse entre múltiples réplicas.  
  - Las escrituras pueden convertirse en un cuello de botella si se exige replicación inmediata en muchos nodos.

---
- **Alta disponibilidad**:  
  - Si un nodo deja de responder, otro con los mismos datos puede tomar su lugar.  
  - Se reducen ventanas de inactividad percibida por usuarios.

---
- **Tolerancia a fallas**:  
  - Se evitan puntos únicos de falla: un nodo caído no implica pérdida de datos, siempre que exista al menos una réplica actualizada. 

---
Ejemplo:

- En un sistema de mensajería, los mensajes recientes pueden replicarse en varios centros de datos.  
- Si una región tiene problemas, los usuarios pueden ser redirigidos a otra donde las réplicas están casi al día, de modo que la aplicación sigue funcionando con mínima degradación.

***

### Replicación y consistencia

La replicación introduce una tensión natural entre:

- **Consistencia fuerte**: todos los nodos deben ver los mismos datos en todo momento.  
- **Disponibilidad y baja latencia**: se prefiere responder rápido, incluso si alguna réplica tarda en actualizarse. 

Aunque el análisis detallado de modelos de consistencia se aborda en otros temas, para bases distribuidas relacionales es importante notar:

- En replicación síncrona, las transacciones suelen bloquearse hasta que todas las réplicas confirman la operación.  
- En replicación asíncrona, pueden aparecer lecturas de datos “antiguos” en algunas réplicas, pero el sistema logra soportar mejor fallas. 

***

### Ejercicio de reflexión

Se considera un sistema de reservas de vuelos:

- ¿En qué casos se aceptaría leer datos ligeramente desactualizados, si eso reduce latencia?  
- ¿En qué operaciones es indispensable consistencia fuerte (por ejemplo, venta de un asiento)?  
- ¿Qué combinación de replicación síncrona y asíncrona podría utilizarse?

***

# Organización y diseño de una base de datos distribuida

***

### Decisiones clave de diseño

Al diseñar una base de datos distribuida, se toman decisiones encadenadas: 

1. ¿Qué datos estarán **fragmentados** y de qué manera (horizontal, vertical o híbrida)?  
2. ¿Qué fragmentos estarán **replicados**, en qué nodos y con qué tipo de replicación?  
3. ¿Cómo se mantendrá la **consistencia** entre nodos (protocolos de actualización y, si aplica, consenso)?  
4. ¿Qué **transparencias** se desea ofrecer al usuario: localización, fragmentación, replicación, etc.?

En todas estas decisiones influye lo que se vio previamente sobre rendimiento, escalabilidad y limitaciones del modelo relacional en entornos distribuidos. 

***

### Ejemplo guiado: sistema de campus múltiples

Se imagina una institución con tres campus: Norte, Sur y Centro.  
La base lógica contempla tablas como:

- `Alumno(id, nombre, correo, campus, programa)`  
- `Curso(idcurso, nombre, campus)`  
- `Inscripcion(idalumno, idcurso, calificacion)`

### Diseño

1. **Fragmentación horizontal de Alumno por campus**  
   - `Alumno_Norte`, `Alumno_Sur`, `Alumno_Centro`, cada uno en un nodo cercano a su campus. 
2. **Fragmentación horizontal de Curso por campus**  
   - `Curso_Norte`, `Curso_Sur`, `Curso_Centro`.  
3. **Fragmentación horizontal de Inscripcion por campus del curso**  
   - `Inscripcion_Norte`, etc.  
4. **Replicación parcial** de una vista de `Curso` (idcurso, nombre) en los tres nodos, para permitir que cualquier campus consulte el catálogo global de cursos. 

### Comentarios

- Consultas locales (por ejemplo, lista de alumnos de Norte con sus cursos) se resuelven en un solo nodo.  
- Reportes globales (por ejemplo, total de inscritos en todos los campus) requieren combinar resultados de varios nodos, pero esto es poco frecuente y se tolera cierto costo. 

***

### Analogía: red de sucursales bancarias

En una red de bancos:

- Cada sucursal podría tener fragmentos de cuentas locales (fragmentación horizontal).  
- Ciertas tablas de tipos de cuenta o tasas de interés se replican en todas las sucursales (replicación completa).  
- Los datos de tarjetas de crédito pueden estar fragmentados verticalmente, separando datos de identidad de datos de transacciones, con distintos niveles de protección. 

Este tipo de organización reduce tráfico y mantiene la seguridad, al tiempo que permite consultas centralizadas cuando se requieren.

***

### Aspectos prácticos

- La **gran mayoría** de las consultas de una aplicación se atiendan en un solo nodo o en pocos nodos.  
- Las operaciones que involucran varios nodos no se conviertan en cuellos de botella diarios, sino en operaciones de reporte o mantenimiento con frecuencia controlada. 
- La **fragmentación** y la **replicación** se ajusten con el tiempo conforme cambia el patrón de uso real del sistema.

