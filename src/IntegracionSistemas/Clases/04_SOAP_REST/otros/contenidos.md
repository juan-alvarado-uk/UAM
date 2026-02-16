# Manual de laboratorio – Diseño de 5–6 endpoints REST para e‑commerce + facturación

## Objetivo general de la práctica

Diseñar un conjunto pequeño pero coherente de endpoints REST para integrar un sistema de e‑commerce con un sistema de facturación, aplicando conceptos de recursos, URIs, verbos HTTP y manejo de errores. Se realizará sobre papel o editor de texto, sin necesidad de programar, pero con el rigor suficiente para que el diseño sea implementable posteriormente. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

***

## Parte A – Preparación (30–40 minutos)

### Paso 1: Entender el escenario

1. Considera que existe un sistema de e‑commerce que gestiona productos, clientes y pedidos, y un sistema de facturación que emite facturas a partir de pedidos pagados. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
2. El objetivo de la integración es que el e‑commerce pueda:  
   - Consultar datos de clientes.  
   - Registrar pedidos.  
   - Solicitar la generación de facturas.  
   - Consultar el estado de una factura. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

3. Forma equipos de 3–4 estudiantes y definan brevemente (en 4–5 líneas) qué flujo imaginan, por ejemplo: “el cliente crea un pedido, lo paga, y el sistema de facturación genera una factura”. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/6de2559c-14e7-4f9e-bd1c-a03903b984c9/Integracion_Sistemas.txt)

### Paso 2: Elegir recursos principales

1. En equipo, identifiquen al menos estos recursos: `clientes`, `productos`, `pedidos`, `facturas`. [stackoverflow](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
2. Opcionalmente, agreguen uno más si lo consideran útil (por ejemplo, `pagos` o `carritos`). [moesif](https://www.moesif.com/blog/technical/api-development/essential-REST-API-best-practices/)
3. En una tabla, anoten para cada recurso: nombre, descripción breve y sistema “dueño” (e‑commerce o facturación). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

***

## Parte B – Diseño de endpoints (aprox. 2 horas)

### Paso 3: Definir 5–6 endpoints REST

1. A partir de los recursos identificados, diseñen de 5 a 6 endpoints REST que cubran el flujo básico de integración. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
2. Usen esta guía mínima (pueden ajustarla):

   - `GET /productos` – listar productos disponibles.  
   - `POST /pedidos` – crear un nuevo pedido.  
   - `GET /pedidos/{id}` – consultar detalle de un pedido.  
   - `POST /facturas` – generar una factura para un pedido existente.  
   - `GET /facturas/{id}` – consultar detalle/estado de una factura.  
   - (Opcional) `GET /clientes/{id}` – consultar datos de un cliente.  

3. Para cada endpoint, definan:  
   - Recurso y URI.  
   - Verbo HTTP.  
   - Descripción de qué hace.  
   - Sistema que lo expone (e‑commerce o facturación). [florimond](https://florimond.dev/en/posts/2018/08/restful-api-design-13-best-practices-to-make-your-users-happy)

**Activación en medio:**  
Cada equipo pega sus URIs en el pizarrón o las comparte en un documento colaborativo. La clase hace una “galería” rápida, revisando que las URIs usen sustantivos y que los verbos estén solo en métodos HTTP, no en las rutas. [stackoverflow](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

### Paso 4: Definir estructuras básicas de petición/respuesta

1. Para al menos 3 de los endpoints, diseñen el JSON de entrada y salida de forma esquemática (no es necesario incluir todos los campos del mundo, solo los esenciales). [moesif](https://www.moesif.com/blog/technical/api-development/essential-REST-API-best-practices/)
2. Por ejemplo, para `POST /pedidos` definan algo como:  
   - Cuerpo de petición: `clienteId`, lista de `items` (cada uno con `productoId` y `cantidad`).  
   - Respuesta: `id` del pedido, estado inicial, total calculado. [moesif](https://www.moesif.com/blog/technical/api-development/essential-REST-API-best-practices/)
3. Validen que la información que espera `POST /facturas` se pueda derivar de lo que devuelve `POST /pedidos` y/o de recursos relacionados, para mantener consistencia entre sistemas. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

### Paso 5: Manejo de errores

1. Elijan al menos 2 endpoints y definan 2–3 posibles errores para cada uno. [stackoverflow](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
   - Ejemplo: en `POST /facturas`, error si el pedido no existe, si ya está facturado o si el sistema de facturación no está disponible.  
2. Asignen a cada error:  
   - Código HTTP apropiado (`400`, `404`, `409`, `500`, etc.).  
   - Cuerpo JSON de error con campos como `status`, `code`, `message`. [stackoverflow](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

***

## Parte C – Documentación estilo OpenAPI (1.5–2 horas)

### Paso 6: Elegir herramienta y archivo

1. Cada equipo trabajará en un archivo de texto plano (`.yaml` o `.yml`) usando:  
   - En Windows: Bloc de notas, Visual Studio Code o un editor que ya usen.  
   - En macOS: TextEdit en modo texto plano o Visual Studio Code.  

2. No es necesario instalar nada adicional, pero si tienen acceso a VS Code, pueden aprovechar el resaltado de sintaxis para YAML. [baeldung](https://www.baeldung.com/swagger-format-descriptions)

### Paso 7: Crear esqueleto básico OpenAPI

1. En el archivo YAML, escriban un esqueleto mínimo, por ejemplo:

   ```yaml
   openapi: 3.0.0
   info:
     title: API Integración E‑commerce–Facturación
     version: 1.0.0
   paths: {}
   ```

2. Verifiquen que la indentación sea consistente (dos espacios por nivel) para evitar errores de formato. [baeldung](https://www.baeldung.com/swagger-format-descriptions)

### Paso 8: Documentar al menos 2 endpoints

1. Elijan 2 de los endpoints diseñados (por ejemplo, `POST /pedidos` y `POST /facturas`) y añadan su definición al documento, de forma simplificada. [swagger](https://swagger.io/docs/specification/v3_0/about/)
2. Incluyan:  
   - Descripción general de la operación.  
   - Resumen de parámetros de entrada (en `requestBody`).  
   - Respuestas con códigos `201` y algún error (`400`, `404`), con descripciones breves. [swagger](https://swagger.io/docs/specification/v3_0/about/)

3. El objetivo no es cubrir toda la especificación, sino habituarse a ver el contrato REST como un documento estructurado similar en espíritu a un WSDL. [xoriant](https://www.xoriant.com/blog/swagger-introduction-specification-for-describing-restful-apis)

***

## Parte D – Entregable y cierre (30–40 minutos)

### Paso 9: Entregable de la práctica

Cada equipo debe entregar (en el formato que indique el profesor, digital o impreso):

- Lista de 5–6 endpoints con URI, verbo HTTP y descripción.  
- Definición de JSON de entrada/salida de al menos 3 endpoints.  
- Definición de manejo de errores para al menos 2 endpoints.  
- Archivo YAML con un esqueleto OpenAPI conteniendo al menos 2 endpoints documentados a nivel básico. [swagger](https://swagger.io/docs/specification/v3_0/about/)

### Paso 10: Discusión final

1. En plenaria, se elige un equipo para presentar su conjunto de endpoints y otro su fragmento OpenAPI.  
2. El grupo comenta:  
   - ¿Los recursos están bien nombrados?  
   - ¿Los verbos HTTP se usan de acuerdo con las convenciones?  
   - ¿Los errores son claros para un consumidor externo?  

3. El profesor relaciona las observaciones con los criterios que se usarán en las siguientes sesiones para implementar un servicio REST real con Node.js/Express o Python/FastAPI, sin entrar todavía a detalles de código. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

***

## Referencias (para el profesor)

- Unidad de aprendizaje “Integración de Sistemas”, plan de estudios LTSI, UAM Cuajimalpa. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/6de2559c-14e7-4f9e-bd1c-a03903b984c9/Integracion_Sistemas.txt)
- “Evolución de Integración: SOAP a REST y Microservicios”, notas de curso. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
- AWS – “SOAP vs REST - Difference Between API Technologies”. [aws.amazon](https://aws.amazon.com/compare/the-difference-between-soap-rest/)
- Zuplo – “SOAP vs REST APIs: The Ultimate Showdown”. [zuplo](https://zuplo.com/learning-center/soap-vs-rest-apis-ultimate-showdown)
- DigitalAPI – “REST vs SOAP: Key Differences, Pros and Cons, and Use Cases”. [digitalapi](https://www.digitalapi.ai/blogs/rest-vs-soap-key-differences)
- Superblocks – “SOAP vs REST: 9 Key Differences & When to Use Each in 2026”. [superblocks](https://www.superblocks.com/blog/soap-vs-rest)
- Swagger – “What is OpenAPI?”. [swagger](https://swagger.io/docs/specification/v3_0/about/)
- Xoriant – “Swagger Introduction - Specification for Describing RESTful APIs”. [xoriant](https://www.xoriant.com/blog/swagger-introduction-specification-for-describing-restful-apis)
- Baeldung – “Format Swagger Text Descriptions”. [baeldung](https://www.baeldung.com/swagger-format-descriptions)
- Stack Overflow Blog – “Best practices for REST API design”. [stackoverflow](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- Florimond.dev – “RESTful API Design: 13 Best Practices to Make Your Users Happy”. [florimond](https://florimond.dev/en/posts/2018/08/restful-api-design-13-best-practices-to-make-your-users-happy)
- Moesif – “Build Great APIs with These Essential REST API Best Practices”. [moesif](https://www.moesif.com/blog/technical/api-development/essential-REST-API-best-practices/)