

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

En el tercer pedido no se incluye `metodoPago`, lo que muestra la flexibilidad de esquema: no todos los documentos necesitan tener exactamente las mismas llaves, manteniendo la coherencia conceptual del dominio. 

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