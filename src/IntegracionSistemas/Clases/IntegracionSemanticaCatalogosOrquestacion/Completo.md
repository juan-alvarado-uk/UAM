# Integración semántica y tendencias modernas (5 horas)
## Sección 1 – Integración semántica y Web Semántica
### 1.1 ¿Qué es la integración semántica?
En integración semántica no sólo conectamos sistemas, conectamos **significados**: acordamos qué quiere decir “cliente”, “pedido” o “total”. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)
Si dos APIs usan nombres distintos para representar el mismo concepto, los vocabularios y ontologías ligeras ayudan a declarar que son equivalentes, reduciendo transformaciones ad‑hoc. [gredos.usal](https://gredos.usal.es/bitstream/10366/124158/1/DIA_GarroteFernandezAntonio_Tesis.pdf)
Una ontología ligera es un conjunto de términos (clases y propiedades) y relaciones básicas entre ellos, suficiente para describir un dominio sin toda la complejidad de la Web Semántica completa. [gredos.usal](https://gredos.usal.es/bitstream/10366/124158/1/DIA_GarroteFernandezAntonio_Tesis.pdf)

***
### 1.2 Vocabularios y ontologías ligeras
En la Web Semántica, un vocabulario define un conjunto de términos estándar (por ejemplo, “Person”, “Organization”, “address”) que muchos sistemas pueden reutilizar. [developer.chrome](https://developer.chrome.com/blog/creating-semantic-sites-with-web-components-and-jsonld?hl=es-419)
Ontologías ligeras como las de schema.org o modelos de “Core Vocabularies” en Europa permiten describir personas, organizaciones y localizaciones sin construir un modelo desde cero. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)
En integración de sistemas, adoptar vocabularios conocidos reduce la fricción al compartir datos entre microservicios internos, socios y plataformas públicas. [dantofema](https://dantofema.ar/blog/json-ld-el-lenguaje-oculto-que-potencia-nuestras-apis)

***
### 1.3 JSON-LD en APIs
JSON-LD (“JSON for Linked Data”) es una forma de agregar significado semántico a documentos JSON sin cambiar su estructura básica. [ionos](https://www.ionos.com/es-us/digitalguide/paginas-web/creacion-de-paginas-web/los-datos-estructurados-en-la-web-semantica/)
Se añade un bloque `@context` que mapea claves del JSON (“name”, “email”, “address”) a URIs de vocabularios estándar (por ejemplo, schema.org), convirtiendo el JSON en datos enlazados. [dantofema](https://dantofema.ar/blog/json-ld-el-lenguaje-oculto-que-potencia-nuestras-apis)
Muchos buscadores y plataformas recomiendan JSON-LD para datos estructurados porque se integra como un script adicional sin modificar el HTML ni la forma tradicional de consumir la API. [woorank](https://www.woorank.com/es/blog/impacto-web-semantica-ecommerce)

***
### Actividad breve 1 – “Diccionario común de la clase”
En equipos de 3–4, elijan un dominio cercano (p. ej., e‑commerce, clínica, cafetería) y hagan una lista de 10 términos clave (Cliente, Pedido, Producto, etc.).  
En la pantalla del salón o en sus laptops, busquen en schema.org o vocabularios públicos equivalentes para esos términos y anoten qué clase o propiedad usarían. [developer.chrome](https://developer.chrome.com/blog/creating-semantic-sites-with-web-components-and-jsonld?hl=es-419)
Luego discutan rápidamente qué ventajas ven en que todos sus futuros microservicios usen ese “diccionario común” en vez de inventar nombres distintos en cada equipo. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)

***
### 1.4 Etiquetas semánticas en APIs
Las APIs pueden exponer su semántica no sólo en el cuerpo JSON, sino también en los contratos (OpenAPI), encabezados y documentación. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)
Un patrón común es publicar un contexto JSON-LD en una URL y referenciarlo desde las respuestas o desde la especificación OpenAPI, mapeando campos de la API a clases y propiedades del modelo. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)
Esto permite que otras herramientas automaticen transformaciones a RDF, integren datos con grafos de conocimiento o generen documentación más precisa sobre el significado de cada campo. [gredos.usal](https://gredos.usal.es/bitstream/10366/124158/1/DIA_GarroteFernandezAntonio_Tesis.pdf)

***
## Sección 2 – Catálogos de APIs y términos de uso
### 2.1 Portales de APIs modernos
Los catálogos modernos evolucionan la idea de UDDI hacia portales de APIs que concentran: documentación, ejemplos, consola de pruebas y gestión de llaves. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
En empresas grandes, estos portales actúan como “tienda interna” de servicios, donde los equipos descubren qué APIs existen antes de crear una nueva. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
También suelen incluir buscadores por dominio de negocio, tags y versiones, y paneles de uso para monitorear consumo por aplicación cliente. [euipo.europa](https://euipo.europa.eu/tunnel-web/secure/webdav/guest/document_library/contentPdfs/law_and_practice/decisions_president/EX-25-1_annex-1_v2_en.pdf)

***
### 2.2 Documentación y contratos publicados
Los portales exponen contratos REST (OpenAPI) o de otros estilos y pueden incluir variantes enriquecidas con semántica (ej. JSON-LD o enlaces a vocabularios). [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)
Es habitual que muestren snippets listos para copiar en varios lenguajes, SDK generados automáticamente y guías de “getting started”. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Para integradores, el portal es la primera fuente para entender límites de uso, formatos, errores y ciclos de vida (versionado, deprecaciones). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

***
### 2.3 Términos de uso y políticas
Los términos de uso de APIs definen qué se puede hacer con los datos y con la infraestructura del proveedor, incluyendo límites de cuota y restricciones legales. [godaddy](https://www.godaddy.com/es/legal/agreements/godaddy-api-terms-of-use)
Ejemplos típicos: no exceder ciertas tasas de llamadas, no almacenar datos más allá de lo permitido, no revender datos ni el acceso a la API, y cumplir normativas de privacidad aplicables. [learn.microsoft](https://learn.microsoft.com/es-es/legal/microsoft-apis/terms-of-use)
Ignorar estos términos puede tener consecuencias legales o la revocación de llaves, por lo que deben considerarse parte del diseño de integración. [i.dell](https://i.dell.com/sites/csdocuments/Legal_Docs/es/es/api-terms-of-use_es.pdf)

***
### Actividad breve 2 – “API detective”
Cada equipo selecciona un portal público (Microsoft, Google, GitHub, etc.) y localiza:  
Nombre de la API, enlace a documentación, límites de uso básicos y al menos una cláusula relevante de términos de uso. [godaddy](https://www.godaddy.com/es/legal/agreements/godaddy-api-terms-of-use)
Compartan en voz alta qué restricciones impactarían más el diseño de un sistema distribuido (por ejemplo, cachés, reintentos, volumen de llamadas). [i.dell](https://i.dell.com/sites/csdocuments/Legal_Docs/es/es/api-terms-of-use_es.pdf)

***
### 2.4 APIs internas, externas y de socios
En una organización hay APIs sólo internas, APIs públicas abiertas y APIs de socios con acuerdos específicos. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Las internas suelen priorizar velocidad de entrega y pueden asumir más conocimiento compartido; las públicas necesitan contratos muy claros, versionado cuidadoso y límites de consumo. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
Las APIs “partner” incorporan acuerdos de negocio (SLA, seguridad, privacidad) que afectan patrones de integración y monitoreo. [euipo.europa](https://euipo.europa.eu/tunnel-web/secure/webdav/guest/document_library/contentPdfs/law_and_practice/decisions_president/EX-25-1_annex-1_v2_en.pdf)

***
## Sección 3 – Patrones SOAP–REST–microservicios y flujo de trabajo
### 3.1 Patrones de coexistencia SOAP–REST
En entornos empresariales es común tener un núcleo legado SOAP y nuevos servicios REST más ligeros alrededor. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
Un patrón frecuente es el “façade” REST sobre servicios SOAP: un microservicio expone REST/JSON hacia clientes modernos y traduce internamente a llamadas SOAP al core. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
Este enfoque reduce el impacto en sistemas heredados y permite evolucionar gradualmente hacia arquitecturas más flexibles. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)

***
### 3.2 Microservicios y descomposición
Los microservicios dividen un dominio de negocio en servicios pequeños, desplegables de forma independiente, usualmente con sus propias bases de datos. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
Cada microservicio expone APIs claras (REST, gRPC, mensajes) y se integra con otros servicios mediante contratos bien definidos. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
Esto mejora escalabilidad y resiliencia, pero aumenta la complejidad de integración y de observabilidad de los flujos de negocio. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

***
### 3.3 Flujos de trabajo y orquestación
En un flujo de trabajo distribuido, varias llamadas a servicios componen un proceso de negocio (alta de cliente, compra en línea, etc.). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
La orquestación se refiere a un componente central (orquestador) que coordina la secuencia, decisiones, compensaciones y manejo de errores entre servicios. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)
La coreografía, en contraste, reparte la lógica entre los servicios, que reaccionan a eventos sin un controlador central único. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

***
### Actividad breve 3 – “Role play de orquestación”
El salón representa un sistema de e‑commerce: cada equipo es un servicio (Catálogo, Carrito, Pago, Envíos, Notificaciones).  
Se elige a una persona como “orquestador” que, en voz alta, va indicando a qué “servicio” le toca actuar y qué información recibe y devuelve en cada paso. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)
Luego repitan el ejercicio sin orquestador, usando tarjetas o notas orales como “eventos” que van pasando entre equipos para simular una coreografía basada en eventos. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

***
### 3.4 Ejemplo conceptual de flujo SOAP–REST–eventos
Imaginemos un proceso de compra en línea donde el sistema de facturación es SOAP legado, el carrito y catálogo son REST, y las notificaciones por correo se disparan por eventos. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
El flujo puede iniciar con una llamada REST del cliente al servicio de Pedidos, que luego llama internamente a un servicio SOAP de facturación y, tras el éxito, publica un evento “PedidoConfirmado”. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
Otros servicios (Logística, Notificaciones) escuchan ese evento y ejecutan su propia lógica sin bloquear la respuesta al usuario. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

***
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

***
## Sección 5 – GraphQL, serverless y prácticas de laboratorio
### 5.1 GraphQL y consulta flexible
GraphQL es un lenguaje de consulta para APIs que permite al cliente pedir exactamente los campos que necesita en una sola llamada. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
A diferencia de REST centrado en recursos y endpoints, GraphQL organiza el acceso a datos en torno a un esquema tipado y operaciones de consulta y mutación. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
También se combina con enfoques semánticos (GraphQL-LD) y con backend serverless y event-driven para construir APIs flexibles y eficientes. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)

***
### 5.2 Serverless en integración
En plataformas serverless, la infraestructura se gestiona automáticamente y los desarrolladores despliegan funciones que se ejecutan bajo demanda. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
Esto reduce costos cuando la carga es variable y facilita construir pipelines de eventos que reaccionan a cambios en datos o mensajes entrantes. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)
Combinado con colas y APIs, habilita integrar sistemas sin mantener servidores dedicados, útil para picos o tareas periódicas. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)

***
### 5.3 Actividad breve 5 – “Mapa de tendencias”
En grupos, dibujen un mapa rápido en la pizarra o en su laptop donde ubiquen: REST, SOAP, GraphQL, colas/eventos, webhooks, serverless y API-first. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
Marquen con flechas cómo se combinan (por ejemplo, “REST + eventos”, “GraphQL + serverless + colas”) en un escenario real como e‑commerce o sistema clínico. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
Discutan qué combinación usarían si tuvieran que rediseñar el proyecto final de la materia para soportar mucho más tráfico y más socios externos. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

***
### 5.4 Práctica 1 – Diagrama de flujo de compra en línea (no entregable)
Objetivo: visualizar un flujo de compra identificando llamadas SOAP, REST y uso de eventos, basándose en un escenario con core legado.

Pasos:

1. Elijan un contexto de tienda en línea (puede ser alguno de los proyectos de equipo del curso, adaptado).  
2. En una hoja, pizarra o herramienta digital simple (draw.io, diagrams.net en el navegador) dibujen el flujo desde que el usuario agrega un producto al carrito hasta que recibe la confirmación del pedido.  
3. Identifiquen al menos estos pasos:  
   - Consulta de catálogo y disponibilidad (REST).  
   - Creación de pedido (REST).  
   - Llamada a sistema de facturación/ERP legado (SOAP, simulado).  
   - Generación de evento “PedidoConfirmado” y publicación en un bus o cola lógica. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
4. Marquen cada interacción con un color o etiqueta:  
   - Azul: llamadas REST síncronas.  
   - Rojo: llamadas SOAP al core legado.  
   - Verde: pasos basados en eventos/colas (notificaciones, preparación de envío, actualización de analíticos). [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
5. Revisen el diagrama en equipo y ajusten para que el usuario reciba la confirmación sólo cuando las partes críticas (pago y facturación) se completan, pero dejando tareas largas (envío de correo, generación de reporte) como asíncronas. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

***
### 5.5 Práctica 2 – Diagrama de integración (entregable)
Objetivo: elaborar un diagrama de integración que muestre cliente, API del equipo, servicio externo y componentes de datos/colas.

Herramientas sugeridas (todas gratuitas y multiplataforma):

- Navegador + diagrams.net (https://app.diagrams.net) o yEd Live. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)
- Alternativamente, draw.io Desktop (Windows/macOS) si desean instalar cliente local. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)

Pasos:

1. Definir el escenario  
   - Elijan un caso concreto: compra en línea, clínica, cafetería, biblioteca digital o el proyecto final del equipo.  
   - Identifiquen al menos: Cliente (web o móvil), API principal del sistema, un servicio externo (puede ser SOAP o REST: pagos, facturación, envíos, etc.) y una base de datos o cola de mensajes. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

2. Crear el lienzo  
   - Abran diagrams.net en el navegador.  
   - Seleccionen un diagrama en blanco y elijan guardar en dispositivo para poder exportar después.  

3. Dibujar componentes  
   - Añadan un ícono para el Cliente (navegador/app).  
   - Añadan un rectángulo para la API del equipo (indiquen si es REST, gRPC u otro estilo).  
   - Añadan al menos un rectángulo adicional para el servicio externo (etiquetado como SOAP o REST). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
   - Añadan símbolos para Base de Datos y/o Cola/Event Bus, según aplique al escenario. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

4. Dibujar conexiones  
   - Trace flechas desde el Cliente hacia la API del equipo, anotando el tipo de llamada (REST síncrono, GraphQL, etc.). [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
   - Desde la API del equipo hacia el servicio externo, especifiquen si la llamada es SOAP o REST y si es síncrona. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
   - Añadan flechas entre la API y la Base de Datos/Cola indicando operaciones de lectura/escritura o publicación de eventos. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

5. Anotar patrones de integración  
   - Junto a cada flecha, indiquen si el canal es síncrono o asíncrono y, en su caso, si se apoya en colas o webhooks. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
   - Señalen brevemente qué operación de negocio representa (crear pedido, registrar pago, enviar notificación).  

6. Resaltar tendencias  
   - Marquen en el diagrama dónde se ve API-first (contrato centralizado), dónde hay integración event-driven (publicación/consumo de eventos) y si consideran que alguna parte podría moverse a serverless. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

7. Exportar entregable  
   - Desde diagrams.net, usen “Archivo → Exportar como → PNG” o “SVG” y guarden el archivo con nombre: `EquipoX_DiagramaIntegracion.png`.  
   - Entreguen el archivo según el mecanismo indicado por el profesor (plataforma, correo, repositorio, etc.).  

***
## Manuales de laboratorio (sección aparte)
### Manual Lab 1 – Flujo SOAP–REST–eventos (no entregable)
1. Preparación conceptual  
   - Revisen en equipo los conceptos de integración síncrona/asíncrona, SOAP y REST ya vistos en clases previas, sólo para recordar diferencias de alto nivel. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5c230302-fc47-4a58-8b04-4b086818c350/01_Diff_SOAP_REST.md)
   - Lean la Sección 3 y 4 de este material para alinear terminología de orquestación y eventos. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

2. Definir escenario detallado  
   - Elijan un proceso de compra en línea específico (por ejemplo, compra de libros, comida, boletos).  
   - Escriban en un documento de texto simple (Bloc de notas, TextEdit) una lista numerada de pasos principales (al menos 8 pasos).  

3. Clasificar llamadas por tipo  
   - Para cada paso, decidan si el usuario requiere respuesta inmediata (síncrono) o si puede diferirse sin afectar su experiencia (asíncrono). [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
   - Marquen qué pasos se comunicarían con un sistema legado crítico (candidato a SOAP) y cuáles con APIs modernas REST/gRPC. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)

4. Construir el diagrama de flujo  
   - Utilicen diagrams.net: seleccionen formas de “inicio/fin”, “proceso” y “decisión”.  
   - Dibu-jen el flujo desde el inicio (usuario entra a la tienda) hasta el fin (pedido confirmado y notificaciones enviadas).  
   - En cada flecha, agreguen texto corto indicando “REST síncrono”, “SOAP síncrono”, “Evento a cola”, etc. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

5. Validar y ajustar  
   - Revísen que ningún paso dependa innecesariamente de una operación asíncrona que pueda retrasar al usuario.  
   - Marquen alternativas de reintentos y manejo de fallos para llamadas críticas (por ejemplo, si falla el pago, mostrar error y no publicar evento). [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

6. Discusión grupal  
   - Cada equipo explica en 3–4 minutos cómo decidió qué era síncrono y qué era asíncrono.  
   - El profesor comparará patrones recurrentes con arquitecturas event-driven modernas. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

***
### Manual Lab 2 – Diagrama de integración con herramientas gratuitas (entregable)
1. Instalación/uso de herramienta  
   - Opción recomendada: abrir https://app.diagrams.net en el navegador (no requiere instalación ni registro). [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)
   - Alternativa offline: descargar draw.io Desktop desde su sitio oficial y ejecutarlo en Windows o macOS (licencia gratuita). [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)

2. Configuración inicial  
   - Crear un nuevo diagrama en blanco.  
   - Elegir guardar el archivo localmente (por ejemplo, `ProyectoIntegracion.drawio`).  

3. Modelar componentes principales  
   - Arrastrar una forma para el Cliente (rectángulo o ícono de usuario) y etiquetarlo (p. ej., “Cliente Web/Móvil”).  
   - Arrastrar una forma para la API del equipo; escribir el nombre del sistema y el estilo de API (REST, GraphQL, etc.). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
   - Añadir al menos un bloque para “Servicio externo” (pago, envíos, facturación) indicando si es SOAP o REST. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
   - Agregar figuras para Base de Datos y/o Cola/Event Bus. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)

4. Conectar y etiquetar canales  
   - Dibujar flechas del Cliente → API del equipo especificando “REST síncrono / JSON”.  
   - Dibujar flechas API → Servicio externo con etiquetas “SOAP (WSDL heredado)” o “REST de terceros”. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
   - Dibujar flechas entre API → BD y API → Cola/Event Bus con etiquetas “persistencia” o “publicación de evento”. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

5. Enriquecer con notas semánticas  
   - Añadir pequeñas notas (shapes tipo comentario) donde indiquen qué entidades del dominio fluyen (Pedido, Cliente, Pago).  
   - Cuando apliquen, anoten si piensan usar vocabularios estándar (por ejemplo, schema.org/Person) o JSON-LD para describir los datos. [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)

6. Resaltar patrones y tendencias  
   - Usar colores o bordes distintos para servicios síncronos y componentes puramente event-driven/serverless. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
   - Opcional: marcar qué parte sería buena candidata a serverless (p. ej., un procesador de eventos “EnviarCorreoConfirmación”). [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)

7. Exportar y entregar  
   - Utilizar “Archivo → Exportar como → PNG” y generar una imagen con resolución suficiente.  
   - Nombrar el archivo `EquipoX_Lab2_DiagramaIntegracion.png` y subirlo por el canal que indique el profesor.  

***
## Referencias (para el profesor)
-  TodosTemas.txt – Esquema general de contenidos de la materia de Integración de Sistemas. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)
-  01_Diff_SOAP_REST.md – Diferencias SOAP vs REST. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5c230302-fc47-4a58-8b04-4b086818c350/01_Diff_SOAP_REST.md)
-  XML_servicios_web_XSD.md – XML y XSD para servicios web. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/c07d3024-c14d-405f-b57c-cd5885a2d974/XML_servicios_web_XSD.md)
-  SOAP_Actualmente_Util.md – Contexto de vigencia de SOAP y coexistencia con APIs modernas. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/25580c4d-b37a-4a88-a12f-8a701d8159e9/SOAP_Actualmente_Util.md)
-  Enriquecimiento semántico de APIs y JSON-LD en OpenAPI (SEMIC, Comisión Europea). [interoperable-europe.ec.europa](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/semantic-enrichment-apis-openapi-case-study)
-  Garrote, A. “APIs Semánticas para la Web Orientada a Datos Enlazados”. [gredos.usal](https://gredos.usal.es/bitstream/10366/124158/1/DIA_GarroteFernandezAntonio_Tesis.pdf)
-  Blog Chrome Developers – JSON-LD y Web Components. [developer.chrome](https://developer.chrome.com/blog/creating-semantic-sites-with-web-components-and-jsonld?hl=es-419)
-  “Json-LD: el lenguaje oculto que potencia nuestras APIs”. [dantofema](https://dantofema.ar/blog/json-ld-el-lenguaje-oculto-que-potencia-nuestras-apis)
-  Woorank – Impacto de la Web Semántica en eCommerce. [woorank](https://www.woorank.com/es/blog/impacto-web-semantica-ecommerce)
-  IONOS – Datos estructurados en la Web Semántica. [ionos](https://www.ionos.com/es-us/digitalguide/paginas-web/creacion-de-paginas-web/los-datos-estructurados-en-la-web-semantica/)
-  Microsoft APIs – Terms of Use. [learn.microsoft](https://learn.microsoft.com/es-es/legal/microsoft-apis/terms-of-use)
-  GoDaddy API Terms of Use. [godaddy](https://www.godaddy.com/es/legal/agreements/godaddy-api-terms-of-use)
-  Dell – Condiciones de uso de APIs. [i.dell](https://i.dell.com/sites/csdocuments/Legal_Docs/es/es/api-terms-of-use_es.pdf)
-  Alex DeBrie – Event-driven architectures vs event-based compute. [alexdebrie](https://alexdebrie.com/posts/event-driven-vs-event-based/)
-  “Build Cost Effective Asynchronous GraphQL APIs Using Serverless and Event-driven Architectures”. [apiscene](https://www.apiscene.io/graphql/build-cost-effective-asynchronous-graphql-apis-serverless/)
-  Material sobre arquitecturas serverless event-driven y uso combinado de comunicación síncrona/asíncrona. [youtube](https://www.youtube.com/watch?v=xRDU-LbLftU)

¿Qué tipo de sistema (e‑commerce, salud, educación, etc.) prefieres que usemos como caso principal en clase para aterrizar estos conceptos?