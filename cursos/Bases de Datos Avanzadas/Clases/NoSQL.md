# Datos semiestructurados y NoSQL

En esta presentación veremos datos semiestructurados y las bases de datos NoSQL como complemento al modelo relacional. Retomaremos limitaciones con el uso del modelo relacional ya identificadas en sesiones previas ... 
- estructuras internas complejas, 
- listas de tamaño variable, 
- integración con formatos XML y JSON y 
- necesidades de escalabilidad y distribución que exceden el escenario relacional clásico. 

***

## El objetivo es explorar:
- Qué se entiende por dato semiestructurado.
- Cómo se organizan XML y JSON.
- Qué aportan las bases documentales frente a bases relacionales.
- Cuáles son las motivaciones técnicas para NoSQL.

***

# Datos semiestructurados: concepto general

**Definición.** Los datos semiestructurados son datos que conservan organización interna mediante atributos, anidamientos y listas, pero que no comparten obligatoriamente un esquema fijo idéntico para todos los registros. **Existe cierta estructura, pero con campos opcionales y variaciones entre instancias**. 

***

En un esquema relacional clásico, cada fila de una tabla comparte el mismo conjunto de columnas. Cuando el dominio incluye objetos con partes internas, colecciones de tamaño variable o jerarquías de tipos, el diseño tiende a multiplicar tablas y relaciones para poder representarlos, lo que incrementa complejidad de consultas, mantenimiento y migraciones. 

***

Los datos semiestructurados permiten:
- Campos opcionales según el caso.
- Anidamiento de objetos.
- Arreglos de elementos.
- Cambios frecuentes en estructura sin redefinir un esquema rígido central cada vez. 

***

# XML y JSON como formatos semiestructurados

## XML: elementos y atributos

**Definición.** XML (Extensible Markup Language) es un lenguaje de marcado que representa información mediante elementos y atributos organizados jerárquicamente. Un documento XML bien formado respeta reglas estructurales: cada etiqueta que se abre debe cerrarse, la anidación debe ser correcta y debe existir un único elemento raíz que contenga a los demás. 

***

Características básicas de XML:
- Elementos: delimitados por etiquetas de apertura y cierre.
- Atributos: pares nombre‑valor asociados a un elemento.
- Jerarquía: elementos contenidos unos dentro de otros.
- Documentos bien formados: cumplen reglas sintácticas y de estructura. 

***

## Ejemplo:

```xml
<alumno matricula="220145">
  <nombre>Ana López</nombre>
  <programa>LTSI</programa>
  <materias>
    <materia>Bases de Datos Avanzadas</materia>
    <materia>Sistemas Distribuidos</materia>
  </materias>
</alumno>
```

Este documento muestra un atributo (`matricula`), elementos simples (`nombre`, `programa`) y una estructura anidada (`materias` con varios elementos `materia`). 

***

## JSON: objetos, arreglos y pares atributo‑valor

**Definición.** JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos que representa información mediante objetos, arreglos y pares atributo‑valor. Es muy utilizado en servicios web, APIs, aplicaciones móviles y bases documentales (bases donde cada registro es un documento JSON/XML completo en vez de una fila en una tabla). 

***

Elementos básicos de JSON:
- Objetos: colecciones delimitadas por llaves `{}`, formados por pares atributo‑valor.
- Arreglos: listas delimitadas por corchetes `[]`.
- Atributos: cadenas de texto que identifican cada valor.
- Valores: pueden ser números, cadenas, booleanos, objetos o arreglos. 

***

## Ejemplo:

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

# Bases semiestructuradas y bases documentales

**Definición.** Una base de datos semiestructurada almacena datos cuya forma puede **variar entre registros**, normalmente como documentos o estructuras jerárquicas. Una base **documental** es un tipo de base NoSQL centrada en almacenar **documentos**, generalmente representados en JSON o XML o en formatos equivalentes. 

***

En una base documental:
- Los datos se agrupan en colecciones de documentos.
- Cada documento puede tener campos comunes y campos propios.
- Es posible anidar objetos y arreglos dentro de cada documento.
- El esquema puede evolucionar sin reestructurar constantemente tablas físicas. 

***

Comparación con el modelo relacional:
- El modelo relacional se apoya en tablas, filas y columnas con tipos definidos, llaves e integridad referencial. 
- Las bases documentales se apoyan en documentos completos que representan entidades o agregados importantes para la aplicación. 

***

## Ejemplo de documento en una base documental

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

# Motivaciones para bases de datos NoSQL

**Definición.** NoSQL se entiende como *Not Only SQL* y son tecnologías que amplían el panorama más allá del modelo relacional clásico para atender necesidades de flexibilidad, escalabilidad, distribución y disponibilidad. No implica que SQL deje de ser útil, sino que no es suficiente para todos los escenarios o no es la mejor opción. 

***

Motivaciones principales:

- **Escalabilidad.** Capacidad de mantener o mejorar rendimiento cuando crecen:
   - Volumen de datos.
   - Usuarios concurrentes.
   - Nodos o regiones involucradas. 

- **Alta disponibilidad.** Capacidad de mantener el servicio activo aún ante fallas de componentes individuales, mediante replicación y distribución de datos. 

- **Flexibilidad de esquemas.** Posibilidad de trabajar con datos complejos, multimedia, semiestructurados y formatos externos (JSON, XML) sin depender de esquemas rígidos con migraciones constantes. 

***

# Tipos principales de bases de datos NoSQL

**Definición.** Las bases NoSQL pueden agruparse según el modelo que usan para organizar los datos. Cada tipo prioriza ciertos patrones de acceso y casos de uso. 

***

## Bases de documentos (o documentales)

(De repaso...) 

Bases que almacenan información en documentos con estructura flexible, generalmente usando JSON o derivados. Son adecuadas cuando el objeto natural del dominio es un documento rico con listas, objetos anidados y campos opcionales. 

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
- Pedidos de comercio electrónico con variantes.
- Bitácoras de eventos con metadatos heterogéneos. 

***

## Bases llave‑valor

**Definición.** Bases que almacenan pares (identificador, valor) donde el identificador permite recuperar el valor asociado de forma directa. Adecuadas cuando el patrón de acceso principal es “dado un identificador, recuperar el valor completo”. (Redis, Amazon DynamoDB, Memorystore GCP)

***

Características:
- Acceso muy rápido por identificador.
- Modelo simple y directo.
- Usadas como cachés, almacenamiento de sesiones o configuraciones. 

***

## Ejemplo:

:::fullwidth
- Llave: session:U12345
- Valor: {"usuario": "Ana", "rol": "admin", "ultimoLogin": "2026-07-06T21:10:00"}



## Bases orientadas a columnas

**Definición.** Bases que organizan datos por familias de columnas y están diseñadas para grandes volúmenes de datos distribuidos, con muchas operaciones simultáneas de lectura y escritura. 

---
| Row Key | Personal_Info:Name | Personal_Info:Age | Academic_Info:Course |
| ------- | ------------------ | ----------------- | -------------------- |
| 101     | Ethan              | 21                | Data Science         |
| 102     | Harper             | 20                | Computer Science     |

En el modelo de columnas cada fila tiene un número de fila (row key), y los datos se agrupan en familias de columnas (por ejemplo, Personal_Info, Academic_Info).

Dentro de cada familia hay columnas como Name, Age, Course, y los valores se almacenan físicamente agrupados por columna, no por fila.

Este enfoque lo usan bases como Apache Cassandra, HBase y Google Bigtable (Amazon DynamoDB también es orientada a columnas, además de llave-valor).

***

Aplicaciones frecuentes:
- Series de tiempo.
- Métricas.
- Registros de eventos.
- Telemetría. 

***

## Bases de grafos

**Definición.** Bases que representan datos mediante nodos y aristas, centrando la atención en las relaciones entre entidades. Adecuadas cuando se requiere explorar estructuras de relaciones, como redes sociales, rutas, dependencias o vínculos entre eventos. (Ejemplos: Neo4j, Amazon Neptune (AWS))

En una base de grafos se podría hacer una consulta tipo “amigos de mis amigos” y obtener rápidamente los nodos conectados a través de varias aristas, algo que en SQL tradicional requeriría múltiples JOIN anidados.

***

# ACID y consistencia eventual

**Definición.** Un modelo de consistencia establece cómo se perciben los datos en sistemas con posibles réplicas, concurrencia y distribución. En particular, es importante notar el enfoque ACID tradicional con modelos como consistencia eventual. 

***

## ACID en bases relacionales clásicas
- **Atomicidad:** las transacciones se ejecutan completas o no se aplican.  
- **Consistencia:** las reglas declaradas se respetan antes y después de cada transacción.  
- **Aislamiento:** las transacciones concurrentes no comparten estados intermedios entre sí.  
- **Durabilidad:** una vez confirmadas, las transacciones persisten. 

Este enfoque es muy importante en dominios transaccionales estrictos. 

***

## Consistencia eventual

En varios sistemas distribuidos y bases NoSQL:
- Se admite que **no todas las réplicas reflejen el mismo estado en el mismo instante**.
- Si no hay cambios conflictivos, los estados convergen con el tiempo. 

***

Contraste:
- La consistencia fuerte busca que cada lectura vea el mismo estado en todos los nodos.
- La consistencia eventual acepta divergencias temporales para favorecer disponibilidad y baja latencia. 

La elección depende del dominio y del riesgo que se está dispuesto a aceptar. 
