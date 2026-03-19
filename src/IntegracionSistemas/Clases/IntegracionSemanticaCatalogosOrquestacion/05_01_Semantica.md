# Integración semántica y Web Semántica

# Integración semántica
En la integración semántica no sólo se conectan sistemas, se conectan **significados**. Es decir, acordamos qué quiere decir “cliente”, “pedido” o “total”. 
Si dos APIs usan nombres distintos para representar el mismo concepto, los vocabularios y ontologías ligeras ayudan a declarar que son equivalentes, reduciendo transformaciones ad‑hoc. 
Una ontología ligera es un conjunto de términos (clases y propiedades) y relaciones básicas entre ellos, suficiente para describir un dominio sin toda la complejidad de la Web Semántica completa. 


# Vocabularios y ontologías ligeras
En la Web Semántica, un vocabulario define un conjunto de términos estándar (por ejemplo, “Person”, “Organization”, “address”) que muchos sistemas pueden reutilizar. 
Ontologías ligeras como las de [schema.org](schema.org) o modelos de [Core Vocabularies](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/core-vocabularies) permiten describir muchas cosas sin construir un modelo desde cero. 
En integración de sistemas, o para abarcar todavía más, en el desarrollo de sistemas, adoptar vocabularios conocidos reduce la fricción al compartir datos entre microservicios internos, socios y plataformas públicas. 


# JSON-LD en APIs
JSON-LD (“JSON for Linked Data”) es una forma de agregar significado semántico a documentos JSON sin cambiar su estructura básica. 
Se añade un bloque `@context` que mapea claves del JSON (“name”, “email”, “address”) a URIs de vocabularios estándar (por ejemplo, schema.org), convirtiendo el JSON en datos enlazados.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Ana López",
  "email": "ana.lopez@correo.com",
  "jobTitle": "Ingeniera de Software",
  "url": "https://ejemplo.com/ana",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Av. Universidad 123",
    "addressLocality": "Toluca",
    "postalCode": "50000",
    "addressCountry": "MX"
  }
}
```

# Actividad – “Diccionario común de la clase”
En equipos de 4–5, elijan un dominio cercano (p. ej., e‑commerce, clínica, cafetería) y hagan una lista de 10 términos importantes de ese dominio (Cliente, Pedido, Producto, etc.).  
Busquen en schema.org esos términos y anoten qué clase o propiedad usarían. 
Discutir qué ventajas tiene que todos sus futuros desarrollos usen este “diccionario común” en vez de inventar nombres distintos en cada equipo. 

# Etiquetas semánticas en APIs
Las APIs pueden exponer su semántica no sólo en el cuerpo JSON, sino también en los contratos (OpenAPI), encabezados y documentación. 
Un patrón común es publicar un contexto JSON-LD en una URL y referenciarlo desde las respuestas o desde la especificación OpenAPI, mapeando campos de la API a clases y propiedades del modelo. 

Por ejemplo, llamada y respuestas pueden hacer referencia al uso de JSON, pero no cualquier JSON, sino LD y el encabezado `Link` apunta al contexto JSON-LD donde se mapean propiedades de la respuesta.
```text
GET /customers/123
Accept: application/ld+json
```
Respuesta:
```text
HTTP/1.1 200 OK
Content-Type: application/ld+json
Link: <https://example.com/contexts/customer.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"
```
