## 1. Introducción: datos semiestructurados y NoSQL

Esta sesión se centra en dos ideas principales: los datos semiestructurados y las bases de datos NoSQL como complemento al modelo relacional. Se retoman las tensiones ya identificadas en sesiones previas: estructuras internas ricas, listas de tamaño variable, integración con formatos XML y JSON y necesidades de escalabilidad y distribución que exceden el escenario relacional clásico. 

***

El objetivo es comprender:
- Qué se entiende por dato semiestructurado.
- Cómo se organizan XML y JSON.
- Qué aportan las bases documentales frente a bases relacionales.
- Cuáles son las motivaciones técnicas para NoSQL.
- Qué tipos de bases NoSQL existen y cómo se relacionan con modelos de consistencia, particionamiento y replicación. 

***

## 2. Datos semiestructurados: concepto general

**Definición.** Los datos semiestructurados son datos que conservan organización interna mediante atributos, anidamientos y listas, pero que no comparten obligatoriamente un esquema fijo idéntico para todos los registros. Es decir, existe cierta estructura, pero con campos opcionales y variaciones entre instancias. 

***

En un esquema relacional clásico, cada fila de una tabla comparte el mismo conjunto de columnas. Cuando el dominio incluye objetos con partes internas, colecciones de tamaño variable o jerarquías de tipos, el diseño tiende a multiplicar tablas y relaciones para poder representarlos, lo que incrementa complejidad de consultas, mantenimiento y migraciones. 

***

Los datos semiestructurados permiten:
- Campos opcionales según el caso.
- Anidamiento de objetos.
- Arreglos de elementos.
- Cambios frecuentes en estructura sin redefinir un esquema rígido central cada vez. 

***

## 3. XML y JSON como formatos semiestructurados

### 3.1 XML: elementos y atributos

**Definición.** XML (Extensible Markup Language) es un lenguaje de marcado que representa información mediante elementos y atributos organizados jerárquicamente. Un documento XML bien formado respeta reglas estructurales: cada etiqueta que se abre debe cerrarse, la anidación debe ser correcta y debe existir un único elemento raíz que contenga a los demás. 

***

Características básicas de XML:
- Elementos: delimitados por etiquetas de apertura y cierre.
- Atributos: pares nombre‑valor asociados a un elemento.
- Jerarquía: elementos contenidos unos dentro de otros.
- Documentos bien formados: cumplen reglas sintácticas y de estructura. 

***

Ejemplo ilustrativo:

```xml
<alumno matricula="220145">
  <nombre>Ana López</nombre>
  <programa>TSI</programa>
  <materias>
    <materia>Bases de Datos Avanzadas</materia>
    <materia>Sistemas Distribuidos</materia>
  </materias>
</alumno>
```

Este documento muestra un atributo (`matricula`), elementos simples (`nombre`, `programa`) y una estructura anidada (`materias` con varios elementos `materia`). 

***

### 3.2 JSON: objetos, arreglos y pares atributo‑valor

**Definición.** JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos que representa información mediante objetos, arreglos y pares atributo‑valor. Es ampliamente utilizado en servicios web, APIs, aplicaciones móviles y bases documentales. 

***

Elementos básicos de JSON:
- Objetos: colecciones delimitadas por llaves `{}`, formados por pares atributo‑valor.
- Arreglos: listas delimitadas por corchetes `[]`.
- Atributos: cadenas de texto que identifican cada valor.
- Valores: pueden ser números, cadenas, booleanos, objetos o arreglos. 

***

Ejemplo:

```json
{
  "matricula": 220145,
  "nombre": "Ana López",
  "programa": "TSI",
  "materias": [
    "Bases de Datos Avanzadas",
    "Sistemas Distribuidos"
  ]
}
```

Este objeto JSON representa la misma información que el ejemplo XML anterior y se adapta de forma directa a estructuras usadas en aplicaciones web y servicios REST. 

***

JSON es especialmente útil cuando:
- Se intercambian datos entre servicios y aplicaciones.
- Se requiere una representación compacta y legible.
- La aplicación ya maneja datos en forma de objetos y arreglos. 

***

## 4. Bases semiestructuradas y bases documentales

**Definición.** Una base de datos semiestructurada almacena datos cuya forma puede variar entre registros, normalmente como documentos o estructuras jerárquicas. Una base documental es un tipo de base NoSQL centrada en almacenar documentos, generalmente representados en JSON o en formatos binarios equivalentes. 

***

En una base documental:
- Los datos se agrupan en colecciones de documentos.
- Cada documento puede tener campos comunes y campos propios.
- Es posible anidar objetos y arreglos dentro de cada documento.
- El esquema puede evolucionar sin reestructurar constantemente tablas físicas. 

***

Frente al modelo relacional:
- El modelo relacional se apoya en tablas, filas y columnas con tipos definidos, claves e integridad referencial. 
- Las bases documentales se apoyan en documentos completos que representan entidades o agregados destacados para la aplicación. 

***

Ejemplo típico de documento en una base documental:

```json
{
  "pedidoId": 8451,
  "cliente": {
    "nombre": "María Hernández",
    "correo": "maria@example.com"
  },
  "productos": [
    {"nombre": "Cuaderno", "cantidad": 3, "precio": 45},
    {"nombre": "Pluma", "cantidad": 5, "precio": 12}
  ],
  "direccionEnvio": {
    "ciudad": "Toluca",
    "cp": "50000"
  },
  "estado": "en preparación"
}
```

Este tipo de estructura podría representarse en relacional con varias tablas y relaciones, pero en una base documental se almacena como unidad lógica. 

***

## 5. Motivaciones para bases de datos NoSQL

**Definición.** NoSQL se entiende como *Not Only SQL*: tecnologías que amplían el panorama más allá del modelo relacional clásico para atender necesidades de flexibilidad, escalabilidad, distribución y disponibilidad. No implica que SQL deje de ser útil, sino que no es suficiente para todos los escenarios. 

***

Motivaciones principales:

1. **Escalabilidad.** Capacidad de mantener o mejorar rendimiento cuando crecen:
   - Volumen de datos.
   - Usuarios concurrentes.
   - Nodos o regiones involucradas. 

2. **Alta disponibilidad.** Capacidad de mantener el servicio activo aun ante fallos de componentes individuales, mediante replicación y distribución de datos. 

3. **Flexibilidad de esquemas.** Posibilidad de trabajar con datos complejos, multimedia, semiestructurados y formatos externos (JSON, XML) sin depender de esquemas rígidos con migraciones frecuentes. 

***

En el entorno actual:
- Las aplicaciones interactúan desde múltiples dispositivos y regiones. 
- Las interacciones generan lecturas y escrituras continuas sobre las bases. 
- No basta con escalar verticalmente una instancia relacional única, sino que se requiere pensar en distribución, replicación y diferentes modelos de consistencia. 

***

## 6. Tipos principales de bases de datos NoSQL

**Definición.** Las bases NoSQL pueden agruparse según el modelo que usan para organizar los datos. Cada tipo prioriza ciertos patrones de acceso y casos de uso. 

***

### 6.1 Bases de documentos

**Definición.** Bases que almacenan información en documentos con estructura flexible, generalmente usando JSON o derivados. Son adecuadas cuando el objeto natural del dominio es un documento rico con listas, objetos anidados y campos opcionales. 

***

Características:
- Colecciones de documentos.
- Esquema flexible a nivel de documento.
- Integración directa con datos JSON.
- Consultas sobre campos simples y campos anidados. 

***

Ejemplos de uso:
- Catálogos de productos con atributos variables.
- Perfiles de usuario con configuración y preferencias.
- Pedidos de comercio electrónico complejos.
- Bitácoras de eventos con metadatos heterogéneos. 

***

### 6.2 Bases clave‑valor

**Definición.** Bases que almacenan pares (identificador, valor) donde el identificador permite recuperar el valor asociado de forma directa. Adecuadas cuando el patrón de acceso principal es “dado un identificador, recuperar el valor completo”. 

***

Características:
- Acceso muy rápido por identificador.
- Modelo simple y directo.
- Usadas como cachés, almacenamiento de sesiones o configuraciones. 

***

### 6.3 Bases orientadas a columnas

**Definición.** Bases que organizan datos por familias de columnas y están diseñadas para grandes volúmenes de datos distribuidos, con muchas operaciones simultáneas de lectura y escritura. 

***

Aplicaciones frecuentes:
- Series de tiempo.
- Métricas.
- Registros de eventos.
- Telemetría. 

***

### 6.4 Bases de grafos

**Definición.** Bases que representan datos mediante nodos y aristas, centrando la atención en las relaciones entre entidades. Adecuadas cuando se requiere explorar estructuras de relaciones, como redes sociales, rutas, dependencias o vínculos entre eventos. 

***

En esta sesión se mencionan como parte del panorama general, aunque el estudio detallado se reserva para sesiones posteriores. 

***

## 7. Modelos de consistencia: ACID y consistencia eventual

**Definición.** Un modelo de consistencia establece cómo se perciben los datos en sistemas con posibles réplicas, concurrencia y distribución. En particular, se contrasta el enfoque ACID tradicional con modelos como consistencia eventual. 

***

### 7.1 Transacciones ACID

En bases relacionales clásicas:
- **Atomicidad:** las transacciones se ejecutan completas o no se aplican.  
- **Consistencia:** las reglas declaradas se respetan antes y después de cada transacción.  
- **Aislamiento:** las transacciones concurrentes no se ven en estados intermedios entre sí.  
- **Durabilidad:** una vez confirmadas, las transacciones persisten. 

Este enfoque es esencial en dominios transaccionales estrictos. 

***

### 7.2 Consistencia eventual

En varios sistemas distribuidos y bases NoSQL:
- Se admite que no todas las réplicas reflejen el mismo estado en el mismo instante.
- Si dejan de producirse cambios conflictivos, los estados convergen con el tiempo. 

***

Contraste:
- La consistencia fuerte busca que cada lectura vea el mismo estado en todos los nodos.
- La consistencia eventual acepta divergencias temporales para favorecer disponibilidad y baja latencia. 

La elección depende del dominio y del riesgo que se está dispuesto a aceptar. 

***

## 8. Distribución de datos: particionamiento y replicación

**Definición.** La distribución de datos implica almacenar y gestionar la información en varios nodos de una red para mejorar rendimiento, escalabilidad y disponibilidad. Dos mecanismos centrales son la fragmentación (particionamiento) y la replicación. 

***

### 8.1 Particionamiento (sharding)

**Definición.** El particionamiento consiste en dividir un conjunto lógico de datos en fragmentos que se almacenan en nodos distintos, manteniendo la capacidad de reconstruir el conjunto completo. En entornos NoSQL, el término sharding describe este reparto horizontal. 

***

Criterios típicos:
- Por rango de identificadores.
- Por región geográfica.
- Por función hash.
- Por tipos de datos o clientes. 

***

Efectos:
- Mejora reparto de carga.
- Permite agregar nodos para escalar horizontalmente.
- Complica localización de datos y consultas que requieren múltiples fragmentos. 

***

### 8.2 Replicación

**Definición.** La replicación de datos consiste en mantener múltiples copias del mismo objeto o fragmento en nodos distintos, sincronizadas mediante algún protocolo, para mejorar rendimiento de lectura, disponibilidad y tolerancia a fallos. 

***

Tipos conceptuales:
- Replicación completa: todos los nodos guardan todos los datos.
- Replicación parcial: cada nodo guarda copias solo de algunos fragmentos. 

Sincronización:
- Síncrona: una actualización se considera confirmada cuando ha llegado a todas las réplicas relevantes. 
- Asíncrona: se confirma en un nodo y después se propaga, aceptando posibles desfases temporales. 

***

Relación con consistencia:
- Síncrona tiende a consistencia fuerte, a costa de mayor latencia.
- Asíncrona favorece baja latencia y alta disponibilidad, a costa de permitir lecturas ligeramente desactualizadas. 

***

En sistemas reales se combinan particionamiento y replicación:
- Los datos se dividen en fragmentos para repartir carga.
- Algunos fragmentos se replican para tolerar fallos y acelerar lectura. 

***

## 9. Mini práctica integrada: MongoDB y datos semiestructurados

En esta sección se integra una práctica breve con MongoDB para reforzar los conceptos de datos semiestructurados y bases documentales en el contexto de la sesión.

***

### 9.1 Contexto de práctica

Se utiliza una base de datos `tienda` en MongoDB y una colección `pedidos`. Cada documento `pedido` representa un pedido completo con información de cliente, lista de productos y estado.

MongoDB almacena documentos en BSON, un formato binario cercano a JSON, de modo que:
- Cada documento puede tener campos comunes y campos específicos.
- Es posible anidar objetos y arreglos dentro del documento.
- La aplicación puede evolucionar añadiendo campos sin migraciones de tablas. 

***

### 9.2 Inserción de documentos de ejemplo

Se supone que se está trabajando en el entorno de `mongo` o con el driver que ejecute comandos equivalentes.

Inserción de tres pedidos con estructuras similares, pero no idénticas:

```js
use tienda;

db.pedidos.insertMany([
  {
    pedidoId: 1001,
    cliente: { nombre: "Ana López", correo: "ana@example.com" },
    productos: [
      { nombre: "Laptop", cantidad: 1, precio: 18999 }
    ],
    direccionEnvio: { ciudad: "CDMX", cp: "01000" },
    estado: "pagado",
    metodoPago: "tarjeta",
    etiquetas: ["premium", "electronica"]
  },
  {
    pedidoId: 1002,
    cliente: { nombre: "Luis Pérez", correo: "luis@example.com" },
    productos: [
      { nombre: "Tenis deportivos", cantidad: 2, precio: 1299 },
      { nombre: "Playera", cantidad: 3, precio: 299 }
    ],
    direccionEnvio: { ciudad: "Toluca", cp: "50010" },
    estado: "en preparación",
    metodoPago: "efectivo",
    etiquetas: ["ropa"]
  },
  {
    pedidoId: 1003,
    cliente: { nombre: "Carla Ruiz", correo: "carla@example.com" },
    productos: [
      { nombre: "Libro", cantidad: 1, precio: 350 }
    ],
    direccionEnvio: { ciudad: "Guadalajara", cp: "44100" },
    estado: "enviado",
    etiquetas: ["libros", "regalo"]
  }
]);
```

En el tercer pedido no se incluye `metodoPago`, lo que muestra la flexibilidad de esquema: no todos los documentos necesitan tener exactamente las mismas claves, manteniendo la coherencia conceptual del dominio. 

***

### 9.3 Consultas básicas sobre documentos JSON

Consulta de pedidos con estado `"en preparación"`:

```js
db.pedidos.find(
  { estado: "en preparación" },
  { _id: 0, pedidoId: 1, "cliente.nombre": 1, estado: 1 }
);
```

Esta consulta:
- Filtra por un campo simple (`estado`).
- Proyecta solo algunos campos del documento, incluyendo un subcampo anidado (`cliente.nombre`). 

***

Consulta de pedidos enviados a la ciudad `"Toluca"`:

```js
db.pedidos.find(
  { "direccionEnvio.ciudad": "Toluca" },
  { _id: 0, pedidoId: 1, "cliente.nombre": 1, "direccionEnvio": 1 }
);
```

La notación con puntos indica acceso a subdocumentos anidados (`direccionEnvio.ciudad`). 

***

### 9.4 Operaciones sobre arreglos anidados

Consulta de pedidos en los que algún producto tiene precio mayor a 1500:

```js
db.pedidos.find(
  { "productos.precio": { $gt: 1500 } },
  { _id: 0, pedidoId: 1, productos: 1 }
);
```

En MongoDB:
- `productos` es un arreglo de subdocumentos.
- El motor permite usar condiciones sobre campos dentro de cualquier elemento del arreglo sin requerir una tabla distinta para detalles de pedido. 

***

Cálculo del total de cada pedido (cantidad por precio) utilizando agregación:

```js
db.pedidos.aggregate([
  {
    $addFields: {
      total: {
        $sum: {
          $map: {
            input: "$productos",
            as: "p",
            in: { $multiply: ["$$p.cantidad", "$$p.precio"] }
          }
        }
      }
    }
  },
  {
    $project: {
      _id: 0,
      pedidoId: 1,
      "cliente.nombre": 1,
      total: 1,
      estado: 1
    }
  }
]);
```

Esta tubería de agregación:
- Opera sobre el arreglo `productos` dentro de cada documento.
- Calcula un total derivado sin desnormalizar la estructura a múltiples tablas. 

***

### 9.5 Actualización de documentos semiestructurados

Actualización de todos los documentos para añadir un campo de prioridad basada en el total calculado:

```js
db.pedidos.updateMany(
  {},
  [
    {
      $set: {
        total: {
          $sum: {
            $map: {
              input: "$productos",
              as: "p",
              in: { $multiply: ["$$p.cantidad", "$$p.precio"] }
            }
          }
        }
      }
    },
    {
      $set: {
        prioridad: {
          $cond: [{ $gt: ["$total", 5000] }, "prioritario", "normal"]
        }
      }
    }
  ]
);
```

En esta actualización:
- Se calcula `total` basándose en los productos.
- Se establece un campo `prioridad` según el valor del total.
- No se requiere ajustar un esquema previo de columnas, porque el documento puede recibir nuevos campos de manera directa. 

***

### 9.6 Conexión con los conceptos de la sesión

Esta mini práctica con MongoDB ilustra:
- Uso de JSON como representación interna de documentos. 
- Manejo de campos opcionales y estructuras anidadas en una base documental. 
- Operaciones de consulta y agregación sobre arreglos de subdocumentos.
- Flexibilidad de esquema en un entorno donde el dominio puede cambiar con frecuencia, lo que se conecta con las limitaciones del modelo relacional ante estructuras complejas y semiestructuradas. 

***

## 10. Resumen conceptual de la sesión

En esta sesión se han definido los datos semiestructurados, se han revisado XML y JSON como formatos representativos, se ha presentado el papel de las bases documentales y se ha descrito el contexto en el que surgen las bases NoSQL: necesidad de escalabilidad, alta disponibilidad, flexibilidad de esquemas y operación distribuida. 

***

También se han revisado los tipos principales de bases NoSQL, los modelos de consistencia (ACID frente a consistencia eventual) y los mecanismos de particionamiento y replicación dentro de arquitecturas distribuidas. La mini práctica con MongoDB muestra cómo un sistema documental concreta el uso de datos semiestructurados y operaciones sobre documentos JSON en un contexto que responde directamente a las limitaciones del modelo relacional frente a dominios complejos y cambiantes. 

***

¿Quieres que extienda la mini práctica para incluir un ejemplo de particionamiento (sharding) y replicación en MongoDB Atlas, manteniendo el mismo tono expositivo?