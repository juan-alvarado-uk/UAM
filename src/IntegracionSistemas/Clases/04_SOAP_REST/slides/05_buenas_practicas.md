# Buenas prácticas de diseño de APIs REST

# Modelado de recursos y URIs

Una API REST clara modela recursos con nombres claros y consistentes, normalmente en plural (`/clientes`, `/pedidos`, `/facturas`), evitando incluir verbos en las rutas. Las relaciones se representan mediante URIs anidadas cuando tiene sentido (`/clientes/{id}/pedidos`) sin caer en niveles excesivos de profundidad que compliquen la navegación. Las URIs deben ser estables en el tiempo y reflejar el modelo de dominio, no detalles internos de implementación, lo que facilita evolucionar la lógica sin romper integraciones. 

# Uso de verbos HTTP y manejo de errores

Los verbos HTTP se utilizan de manera semántica: `GET` para recuperar recursos sin efectos secundarios, `POST` para crear o ejecutar operaciones no idempotentes, `PUT` para actualizar y `DELETE` para eliminar. El manejo de errores se apoya en códigos de estado: las respuestas exitosas usan códigos 2xx (como `200 OK` o `201 Created`), errores del cliente usan 4xx (`400 Bad Request`, `404 Not Found`, `409 Conflict`) y fallas internas usan 5xx (`500 Internal Server Error`). Además del código de estado, es recomendable devolver un cuerpo JSON estructurado que incluya campos como `status`, `code`, `title` o `message`, y opcionalmente identificadores de incidente.

**Actividad sugerida:**  
Diseñar respuestas de error JSON para un `POST /pedidos` con datos inválidos. 


# Seguridad y principio de mínimo privilegio

Además de autenticar correctamente (tokens, API keys u OAuth2), una API REST debe aplicar **autorización** fina para que cada consumidor solo pueda acceder a los recursos y operaciones que realmente necesita, siguiendo el principio de mínimo privilegio. Esto implica diseñar roles y permisos alineados con tareas concretas en vez de dar accesos genéricos como “admin” a la mayoría de los clientes. En el contexto de APIs, el mínimo privilegio también se aplica a los tokens: conviene que tengan alcances (scopes) específicos, expiraciones cortas y que se roten periódicamente, para reducir el impacto si se filtran o son comprometidos.

Desde el punto de vista de diseño, es buena práctica validar siempre que el sujeto autenticado tenga permiso sobre el recurso concreto (por ejemplo, que un cliente solo pueda ver sus propios `/pedidos`, no los de otros usuarios), evitando confiar únicamente en datos enviados por el cliente como `customerId` en el cuerpo. También ayuda limitar la superficie de ataque: exponer solo los endpoints necesarios, evitar datos sensibles en respuestas de error y registrar los accesos relevantes para poder auditar comportamientos sospechosos o intentos de abuso. Como precaución final, cualquier permiso no otorgado explícitamente debe asumirse como denegado por default.

**Actividad sugerida:**  
Definir tres roles para la API de `/clientes` y `/pedidos` (por ejemplo: `cliente-final`, `operador-ventas`, `admin-sistema`) indicando qué métodos (`GET`, `POST`, `PATCH`, `DELETE`) pueden usar sobre qué recursos. Discutir si algún rol tiene permisos “de más” y cómo recortarlos para cumplir mínimo privilegio.

***

# Filtrado, paginación y sort para colecciones

Cuando las colecciones crecen, devolver todos los elementos en un solo `GET /pedidos` degrada el desempeño y hace más difícil para el consumidor encontrar lo que necesita. Un patrón común es soportar paginación mediante parámetros de consulta como `?page=` y `?pageSize=`, devolviendo únicamente un subconjunto de resultados junto con metadatos sobre la paginación (por ejemplo, `total`, `page`, `pageSize`). Además, 
- el filtrado (`GET /pedidos?estado=pagado&clienteId=123`) y el
- ordenamiento (`?sort=fecha&direction=desc`) 

permiten que el cliente pida exactamente el subconjunto de datos que necesita, reduciendo tráfico y carga en el servidor.

Es importante documentar claramente qué parámetros de filtrado y ordenamiento soporta cada recurso, cuáles son obligatorios y qué valores son válidos, para evitar ambigüedades. También conviene validar y sanear estos parámetros, tanto para evitar consultas excesivamente costosas (por ejemplo, límites de página demasiado grandes) como para mitigar ataques de inyección contra la capa de datos. Desde el punto de vista de contrato, agregar paginación desde el inicio es recomendable, ya que introducirla después puede considerarse un cambio incompatible si antes se devolvían todas las filas sin restricciones.


### 5.5 Cache y encabezados HTTP para desempeño

Las APIs REST pueden aprovechar HTTP caching para reducir latencia y carga en el servidor, especialmente para recursos de lectura frecuente que cambian poco.[11][12] Encabezados como `Cache-Control`, `ETag` y `Last-Modified` permiten a clientes e intermediarios (por ejemplo, CDNs) reutilizar respuestas anteriores cuando el recurso no ha cambiado, evitando recalcular o reconsultar la base de datos en cada petición.[11] Por ejemplo, al devolver un `GET /clientes/{id}` se puede incluir un `ETag` y permitir al cliente hacer peticiones condicionales con `If-None-Match`, recibiendo un `304 Not Modified` cuando los datos siguen vigentes.[11]

Desde el diseño de recursos, conviene identificar qué endpoints son “cacheables” (típicamente `GET` sin efectos secundarios) y decidir tiempos de vida (`max-age`) apropiados según la naturaleza del dato: información estática puede tener caché larga, mientras que datos críticos (saldos, estados en tiempo real) tendrán caché muy corta o nula.[11][12] Además, cuando se usan versiones en la URL o en parámetros (por ejemplo, `/api/v1/config/{version}`), se puede establecer un cacheo agresivo para versiones específicas, ya que una nueva versión se representará con una nueva URI, evitando que los clientes vean información desfasada.[11][12]

**Actividad sugerida:**  
Los alumnos eligen dos recursos de la API de ejemplo: uno “casi estático” (por ejemplo, catálogo de productos) y uno muy dinámico (por ejemplo, estado actual del pedido). Para cada uno deben proponer valores de `Cache-Control` y si usarían `ETag` o `Last-Modified`, justificando su decisión.

***

### 5.6 Estrategias de versionado de APIs

El versionado de APIs ayuda a introducir cambios incompatibles sin romper integraciones existentes, pero debe usarse con moderación: no todo cambio requiere una nueva versión, especialmente si se trata de agregar campos opcionales o nuevos endpoints.[12][13] Una estrategia común es incluir la versión en la ruta, por ejemplo `/api/v1/clientes`, lo que facilita cachear por URL y tener en paralelo `/v1` y `/v2` mientras algunos clientes migran.[13] Otras opciones incluyen versionar por encabezado personalizado (`API-Version: 1.0`) o por parámetro de consulta (`?version=1`), que mantienen las rutas más “limpias” pero requieren mayor disciplina de cliente y servidor.[13][14]

Sea cual sea la estrategia, es importante documentar las versiones soportadas, el periodo de soporte de versiones antiguas y las reglas de compatibilidad (por ejemplo, “dentro de la misma versión mayor no se rompen contratos existentes”).[12][13] También es buena práctica anunciar de forma clara la deprecación de endpoints o versiones, ya sea mediante encabezados de respuesta, documentación o canales de comunicación con integradores, dando tiempo razonable para que actualicen sus clientes.[12] Esto conecta con el diseño de URIs estables: idealmente el cambio de versión refleja un cambio real en el contrato y no detalles internos, evitando versiones innecesarias que fragmenten el ecosistema de integraciones.[12][13]

**Actividad sugerida:**  
Pide que los alumnos propongan un plan de versionado para la API de `clientes` y `pedidos`:  
- Qué cambios considerarían “compatibles” (no requieren nueva versión).  
- Qué cambios romperían contrato y cómo expondrían `/v2`.  
Luego se discute cuál estrategia (ruta, header, query) ven más adecuada para un banco vs. una startup pequeña, y por qué.

