# Buenas prácticas de diseño de APIs REST

# Modelado de recursos y URIs

Una API REST modela recursos con nombres claros y significativos, normalmente en plural (`/clientes`, `/pedidos`, `/facturas`), evitando incluir verbos en las rutas. 

---
Las relaciones se representan mediante URIs anidadas cuando tiene sentido 

(`/clientes/{id}/pedidos`) 

sin caer en niveles excesivos de profundidad. Las URIs deben ser estables en el tiempo y reflejar el modelo, no detalles de implementación. 

# Uso de verbos HTTP y manejo de errores

Los verbos HTTP se utilizan de manera semántica: 
- `GET` para recuperar recursos sin efectos secundarios, 
- `POST` para crear o ejecutar operaciones no idempotentes, 
- `PUT` para actualizar y 
- `DELETE` para eliminar. 

El manejo de errores se apoya en códigos de estado, 
- las respuestas exitosas usan códigos 2xx (como `200 OK` o `201 Created`), 
- errores del cliente usan 4xx (`400 Bad Request`, `404 Not Found`, `409 Conflict`) y 
- fallas internas usan 5xx (`500 Internal Server Error`). 

Además del código de estado, es recomendable devolver un cuerpo JSON que incluya campos como `status`, `code` o `message`, y opcionalmente identificadores de incidente.

# Actividad  
Diseñar la respuesta de error JSON para un `GET /products/{id}:` para un producto inexistente y un `POST /products` con datos no válidos. Usar el editor Swagger y documento de la práctica "Pratica Contrato API en Swager"


# Seguridad y principio de mínimo privilegio

Además de autenticar correctamente (tokens, API keys u OAuth2), una API REST debe aplicar **autorización** para que cada usuario solo pueda acceder a los recursos y operaciones que necesita, siguiendo el principio de mínimo privilegio. Esto implica diseñar roles y permisos para tareas concretas. En el contexto de APIs, el mínimo privilegio también se aplica a los tokens: conviene que tengan alcances específicos, expiraciones cortas y que se roten periódicamente, para reducir el impacto si se filtran o son comprometidos.

Es buena práctica validar siempre que el sujeto autenticado tenga permiso sobre el recurso concreto (por ejemplo, que un cliente solo pueda ver sus propios `/pedidos`, no los de otros usuarios), evitando confiar únicamente en datos enviados por el cliente como `customerId` en el cuerpo. 

---
También ayuda limitar la superficie de ataque 

- exponer solo los endpoints necesarios, 
- evitar datos sensibles en respuestas de error y 
- registrar los accesos relevantes para poder auditar comportamientos sospechosos o intentos de abuso

Como precaución final, cualquier permiso no otorgado explícitamente debe asumirse como denegado por default.

# Actividad  
Definir tres roles para una API con recursos `/clientes` y `/pedidos` (por ejemplo: `cliente-final`, `operador-ventas`, `admin-sistema`) indicando qué métodos (`GET`, `POST`, `PATCH`, `DELETE`) pueden usar sobre qué recursos. Discutir si algún rol tiene permisos “de más” y cómo recortarlos para cumplir mínimo privilegio.


# Filtrado, paginación y sort para colecciones

Cuando las colecciones crecen, devolver todos los elementos en un solo `GET /pedidos` degrada el desempeño y hace más difícil encontrar lo que se necesita. Un patrón común es soportar paginación mediante parámetros de consulta como 
- `?page=` y 
- `?pageSize=`, 

devolviendo únicamente un subconjunto de resultados junto con metadatos sobre la paginación (por ejemplo, `total`, `page`, `pageSize`). 

---
Además, el filtrado 
- (`GET /pedidos?estado=pagado&clienteId=123`) 

y el ordenamiento 
- (`?sort=fecha&direction=desc`) 

permiten pedir exactamente el subconjunto de datos que se necesita, reduciendo tráfico y carga en el servidor.


# Cache y encabezados HTTP para desempeño

Las APIs REST pueden aprovechar HTTP caching para reducir latencia y carga en el servidor, especialmente para recursos de lectura frecuente que cambian poco. Encabezados como [Cache-Control](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Headers/Cache-Control), [ETag](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Headers/ETag) (entity tag) y [Last-Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Last-Modified) permiten a clientes e intermediarios (por ejemplo, CDNs) reutilizar respuestas anteriores cuando el recurso no ha cambiado, evitando recalcular o re-consultar la base de datos en cada petición. Por ejemplo, al devolver un `GET /clientes/{id}` se puede incluir un `ETag` y permitir al cliente hacer peticiones condicionales con `If-None-Match`, recibiendo un `304 Not Modified` cuando los datos siguen vigentes.

Desde el diseño de recursos, conviene identificar qué endpoints son “cacheables” (típicamente `GET` sin efectos secundarios) y decidir tiempos de vida (`max-age`) apropiados según la naturaleza del dato: información estática puede tener caché larga, mientras que datos críticos (saldos, estados en tiempo real) tendrán caché muy corta o nula. 

# Actividad  
Listar dos recursos de una API, uno “casi estático” y uno muy dinámico. Para cada uno deben proponer valores de `Cache-Control` y si usarían `ETag` o `Last-Modified`. Justificar decisión.
