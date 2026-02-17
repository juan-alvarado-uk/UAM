# OpenAPI/Swagger “WSDL” para REST

# OpenAPI

OpenAPI es una especificación que permite describir una API REST de forma estructurada: versión, información general, servidores, rutas (`paths`), métodos HTTP, parámetros, cuerpos de petición, respuestas y esquemas de datos. Esta descripción se guarda normalmente en un archivo YAML o JSON que actúa como contrato vivo entre quienes implementan la API y quienes la consumen, similar al rol del WSDL en el mundo SOAP. Dentro de `paths` se documenta cada endpoint con sus métodos (`get`, `post`, etc.), descripciones, parámetros de ruta, cabeceras y ejemplos, mientras que en `components/schemas` se definen los modelos de datos reutilizables. El resultado es una visión unificada de qué hace cada endpoint, qué espera y qué devuelve, lo que facilita la integración entre equipos y sistemas.

# Herramientas Swagger y flujo API‑first

Swagger (hoy parte del ecosistema de OpenAPI) ofrece herramientas como editores visuales, generadores de código cliente/servidor y visualizadores de documentación interactiva. Con estas herramientas, un equipo de desarrollo puede seguir un enfoque API‑first: primero diseña el contrato en OpenAPI, discute y acuerda con los consumidores, y solo después genera *stubs* o implementaciones que respeten ese contrato. Este enfoque reduce el riesgo de malentendidos, porque todos leen la misma especificación y pueden incluso probar la API mediante entornos de prueba basados en el documento. OpenAPI actúa como la pieza que formaliza el diseño REST y lo hace consumible por personas y herramientas, en paralelo al papel que WSDL cumple para SOAP.

**Actividad**  
Fragmento breve de un documento OpenAPI en YAML. 



Localizar visualmente: 
a) el título de la API, 
b) una ruta específica, 
c) el método HTTP y 
d) el esquema de respuesta. 

