## Sección 4 – OpenAPI/Swagger como “WSDL moderno” para REST

### 4.1 Qué describe OpenAPI

OpenAPI es una especificación que permite describir una API REST de forma estructurada: versión, información general, servidores, rutas (`paths`), métodos HTTP, parámetros, cuerpos de petición, respuestas y esquemas de datos. Esta descripción se guarda normalmente en un archivo YAML o JSON que actúa como contrato vivo entre quienes implementan la API y quienes la consumen, similar al rol del WSDL en el mundo SOAP. Dentro de `paths` se documenta cada endpoint con sus métodos (`get`, `post`, etc.), descripciones, parámetros de ruta, cabeceras y ejemplos, mientras que en `components/schemas` se definen los modelos de datos reutilizables. El resultado es una visión unificada de qué hace cada endpoint, qué espera y qué devuelve, lo que facilita la integración entre equipos y sistemas. [smartbear](https://smartbear.com/learn/api-design/soap-vs-rest-apis/)

### 4.2 Herramientas Swagger y flujo API‑first

Swagger (hoy parte del ecosistema de OpenAPI) ofrece herramientas como editores visuales, generadores de código cliente/servidor y visualizadores de documentación interactiva. Con estas herramientas, un equipo puede seguir un enfoque API‑first: primero diseña el contrato en OpenAPI, discute y acuerda con los consumidores, y solo después genera *stubs* o implementaciones que respeten ese contrato. Este enfoque reduce el riesgo de malentendidos, porque todos leen la misma especificación y pueden incluso probar la API mediante entornos de prueba basados en el documento. En el contexto de la materia, basta con entender OpenAPI como la pieza que formaliza el diseño REST y lo hace consumible por personas y herramientas, en paralelo al papel que WSDL cumple para SOAP. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/f01cc666-b44a-418a-b026-ef8107a86747/TodosTemas.txt)

**Actividad sugerida:**  
Proyecta un fragmento breve de un documento OpenAPI en YAML. Pide a los estudiantes localizar visualmente: a) el título de la API, b) una ruta específica, c) el método HTTP y d) el esquema de respuesta. Esto ayuda a que asocien cada sección con su rol sin entrar todavía a todos los detalles de la sintaxis.
