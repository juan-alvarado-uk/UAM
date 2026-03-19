## Sección 4 – Síncrono vs asíncrono, colas, eventos y webhooks
### 4.1 Integración síncrona: REST y gRPC
En integración síncrona un cliente envía una petición y espera la respuesta para continuar, típico en HTTP/REST o gRPC. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Es adecuado cuando se necesita feedback inmediato (consultar saldo, validar credenciales) y la latencia es aceptable y predecible. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
Sin embargo, acopla la disponibilidad del cliente y el servidor: si el servicio está caído, la operación falla en ese momento. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

***
### 4.2 Integración asíncrona: colas y eventos
En integración asíncrona, un productor envía un mensaje o evento a una cola o bus, y los consumidores lo procesan más tarde sin bloquear al emisor. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Esto desacopla temporalmente a los sistemas, mejora tolerancia a fallos y permite procesar picos de carga de forma más suave. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
Tecnologías habituales incluyen colas de mensajes, logs de eventos y servicios de mensajería en la nube, pero el concepto se mantiene incluso con herramientas sencillas. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

***
### 4.3 Webhooks como “callback” HTTP
Un webhook es una llamada HTTP que un sistema hace hacia una URL registrada por el cliente cuando ocurre un evento (pago aprobado, envío enviado, etc.). [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Funcionan como una combinación: el evento se genera de forma asíncrona, pero la notificación concreta se envía mediante una llamada HTTP saliente. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
Requieren validar autenticidad (firmas, tokens) y manejar reintentos en caso de fallos de red. [learn.microsoft](https://learn.microsoft.com/es-es/legal/microsoft-apis/terms-of-use)

***
### Actividad breve 4 – “Clasifica el escenario”
El profesor dicta o proyecta 8–10 escenarios breves (ej. “validar una contraseña en tiempo real”, “generar reporte mensual pesado”, “enviar correo de bienvenida”). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
En equipos, etiqueten cada escenario como “síncrono”, “asíncrono” o “mixto (REST + eventos/webhooks)” y preparen una frase justificando su decisión. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Compartan una o dos respuestas por equipo y discutan dónde cambiarían de enfoque si la carga o los requisitos de experiencia de usuario crecen. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

***
### 4.4 Tendencias: API-first y event-driven
API-first implica diseñar primero los contratos de API (incluyendo semántica) antes de implementar, de modo que sirvan de base común para equipos de frontend, backend y socios. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
La arquitectura dirigida por eventos (event-driven) enfatiza que los cambios significativos del sistema se publican como eventos, que otros servicios observan y manejan de forma reactiva. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Juntas, estas ideas permiten sistemas más modulares, escalables y alineados con el negocio, pero exigen mayor disciplina en diseño de contratos y en gobernanza. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
