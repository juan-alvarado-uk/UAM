A continuación tienes dos exámenes pensados para resolverse en 2 horas cada uno, en formato compatible con Google Forms (Google Classroom). Cada reactivo es de opción múltiple e incluye tanto conceptos teóricos (tomados de los .md del espacio) como situaciones prácticas alineadas con las prácticas indicadas. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5fa752c0-54f2-4f21-a4e8-72b916623d66/Practica_Construccion_de_SOAP.md)

***

## Examen 1 – SOAP, XML/XSD, WSDL y monolito mínimo Node.js

### Sección A: Conceptos teóricos (SOAP, XML, XSD, WSDL)

1. ¿Cuál es el propósito principal de usar XML en servicios web SOAP?
- A) Reducir el tamaño de los mensajes de red
- B) Representar datos estructurados de forma jerárquica y validable mediante esquemas
- C) Asegurar que todos los mensajes sean binarios
- D) Evitar el uso de HTTP como transporte

2. ¿Qué característica define a un documento XML “bien formado”?
- A) Tener solo elementos de tipo string
- B) Usar siempre el mismo prefijo de espacio de nombres
- C) Tener un único elemento raíz y etiquetas correctamente anidadas y cerradas
- D) Incluir al menos un atributo en cada elemento

3. En un esquema XSD, ¿qué diferencia hay entre un tipo simple y un tipo complejo?
- A) El tipo simple solo se usa para atributos, el complejo solo para elementos
- B) El tipo simple describe valores atómicos; el complejo agrupa elementos y atributos anidados
- C) El tipo complejo solo se usa en WSDL, el simple solo en XML
- D) No hay diferencia; ambos se usan indistintamente

4. ¿Cuál es el rol de XSD en el contexto de WSDL y servicios SOAP?
- A) Optimizar el rendimiento del servidor HTTP
- B) Describir la estructura y tipos de los mensajes XML que intercambia el servicio
- C) Registrar servicios en directorios públicos
- D) Gestionar la seguridad y el cifrado de los mensajes

5. ¿Cuál de las siguientes opciones describe mejor a WSDL?
- A) Un formato ligero de datos alternativo a JSON
- B) Un protocolo de transporte para servicios web
- C) Un lenguaje basado en XML que describe operaciones, mensajes, tipos de datos y endpoints de un servicio
- D) Una base de datos de servicios web en la nube

6. En un mensaje SOAP típico, ¿qué elemento es obligatorio?
- A) soap:Header
- B) soap:Body
- C) soap:Fault
- D) soap:Security

7. ¿Qué ventaja clave ofrece el uso de WSDL con contratos estrictos?
- A) Permite cambiar la estructura de los mensajes sin coordinar con los consumidores
- B) Facilita la generación de código cliente/servidor y la validación automática de mensajes
- C) Elimina la necesidad de usar XML
- D) Permite que el servicio sea completamente stateless sin esfuerzo

8. ¿Qué componente de la “pila clásica” SOAP se diseñó para publicar y descubrir servicios?
- A) SOAP
- B) WSDL
- C) UDDI
- D) WS-Security

9. ¿Cuál de las siguientes afirmaciones sobre SOAP y REST es correcta?
- A) SOAP usa típicamente XML y contratos formales; REST suele usar JSON y contratos más ligeros
- B) SOAP y REST siempre usan JSON
- C) REST requiere UDDI para descubrir servicios
- D) SOAP no puede usar HTTP como transporte

10. ¿En qué contexto suele seguir siendo razonable usar SOAP en lugar de solo APIs REST?
- A) Aplicaciones móviles sin requisitos de seguridad
- B) Prototipos rápidos con cambios frecuentes de contrato
- C) Integraciones reguladas de largo plazo con contratos muy estructurados y WS-Security
- D) Sitios estáticos de contenido público

### Sección B: Práctica SOAP/XML y WSDL (opción múltiple sobre casos)

11. Te dan el siguiente JSON de respuesta de un producto:
```json
{ "id": 1, "name": "Laptop", "price": 25000.0 }
```
¿Cuál sería el elemento principal más adecuado en el Body de un mensaje SOAP de respuesta?
- A) `<GetProductRequest>`
- B) `<ProductResponse>` o equivalente que agrupe los datos del producto
- C) `<ErrorResponse>`
- D) `<EnvelopeProduct>`

12. En un mensaje SOAP bien formado que representa una respuesta de producto, ¿qué combinación es la más adecuada?
- A) Un único `<soap:Envelope>` con `<soap:Header>` y `<soap:Body>` internos
- B) Varios `<soap:Envelope>` anidados para cada elemento del producto
- C) Un `<soap:Body>` sin `<soap:Envelope>`
- D) Un XML sin namespaces para simplificar

13. Si validas un XML de mensaje SOAP contra un XSD y el validador indica que el elemento `<price>` no es numérico, ¿qué significa?
- A) El WSDL está mal escrito
- B) El XML no es bien formado
- C) El valor del elemento no cumple el tipo de dato definido en el XSD
- D) El servidor HTTP está caído

14. Tienes un WSDL con tipos XSD embebidos en la sección `<types>`. ¿Qué necesitas hacer para validar un mensaje de ejemplo contra esos tipos?
- A) Ignorar la sección `<types>` y validar solo con el navegador
- B) Extraer o referenciar el XSD de la sección `<types>` y usarlo como esquema en un validador XML/XSD
- C) Convertir el WSDL a JSON y validarlo con OpenAPI
- D) No es posible validar mensajes usando un WSDL

15. Un `<soap:Fault>` en un mensaje SOAP se utiliza principalmente para:
- A) Enviar datos de negocio adicionales
- B) Configurar la autenticación del servicio
- C) Establecer una conexión persistente
- D) Comunicar errores de procesamiento con código, motivo y detalles

### Sección C: Teórico/práctico Node.js – Monolito mínimo

16. En el laboratorio de “Monolito mínimo con Node.js y Express”, ¿qué característica distingue a las rutas iniciales implementadas?
- A) Solo exponen métodos GET y POST para recursos como productos y pedidos en memoria
- B) Incluyen persistencia en base de datos relacional
- C) Exponen exclusivamente métodos PUT y DELETE
- D) Usan colas de mensajes en lugar de HTTP

17. ¿Cuál es el propósito de usar `app.use(express.json())` en una API Express?
- A) Permitir que Express sirva archivos estáticos
- B) Habilitar el parseo automático de cuerpos JSON en las peticiones
- C) Configurar el motor de plantillas HTML
- D) Asegurar la conexión HTTPS

18. En una ruta `GET /productos/:id`, el segmento `:id` en Express se conoce como:
- A) Query string
- B) Middleware
- C) Parámetro de ruta
- D) Header obligatorio

19. Para extender la API del monolito mínimo y permitir eliminar un producto específico, ¿cuál de las siguientes rutas es más apropiada?
- A) `DELETE /productos`
- B) `DELETE /productos/:id`
- C) `GET /productos/delete`
- D) `POST /productos/remove/:id`

20. Si una petición intenta obtener un producto por `id` que no existe, ¿qué código HTTP es más apropiado regresar?
- A) 200 OK con un cuerpo vacío
- B) 201 Created
- C) 404 Not Found
- D) 500 Internal Server Error

21. En la práctica de “monolito mínimo extendido”, al implementar `PUT /productos/:id`, ¿cuál es el comportamiento esperado?
- A) Crear siempre un producto nuevo sin importar si existe
- B) Actualizar los campos del producto existente identificado por `id`
- C) Reiniciar el servidor
- D) Devolver siempre 204 sin contenido y sin cambios

22. ¿Qué ventaja tiene mantener los datos de productos y pedidos en estructuras en memoria durante el laboratorio?
- A) Permite simular la lógica de negocio sin configurar una base de datos real
- B) Asegura durabilidad de datos entre reinicios
- C) Mejora la seguridad ante ataques externos
- D) Obliga a usar transacciones distribuidas

23. En pruebas con `curl` o Postman sobre el monolito mínimo, ¿cuál de estas opciones representa correctamente una petición POST para crear un producto?
- A) `POST /products` sin cuerpo, esperando que el servidor genere los datos
- B) `POST /productos` con encabezado `Content-Type: application/json` y un cuerpo JSON con los campos del producto
- C) `GET /productos/new` con parámetros en la URL
- D) `PUT /productos` con un cuerpo vacío

24. Cuando se extiende el monolito mínimo para manejar recursos “pedidos” además de “productos”, ¿qué principio se refuerza?
- A) Que todas las rutas deben compartir el mismo prefijo
- B) La separación de responsabilidades por tipo de recurso en la API
- C) Que solo se puede definir un recurso por servidor
- D) Que los métodos HTTP son intercambiables

25. ¿Cuál es una diferencia clave entre la API monolítica mínima y una arquitectura de microservicios?
- A) En el monolito, todo el código corre en un mismo despliegue; en microservicios se distribuye en servicios independientes
- B) En un monolito no se pueden usar rutas HTTP
- C) Los microservicios no pueden comunicarse vía HTTP
- D) El monolito siempre es más escalable que cualquier microservicio

***

## Examen 2 – Tipos de integración, SOAP vs REST, WSDL vs REST, prácticas de integración

### Sección A: Tipos de integración y panorama histórico

1. En integración de sistemas, la integración “punto a punto” se caracteriza por:
- A) Un bus central que conecta todos los sistemas
- B) Conexiones directas específicas entre cada par de aplicaciones, generando “spaghetti” al crecer
- C) El uso exclusivo de colas de mensajes
- D) La obligación de usar solo SOAP/XML

2. ¿Qué objetivo principal tiene la arquitectura SOA frente al “spaghetti” punto a punto?
- A) Aumentar el número de conexiones
- B) Agrupar la lógica en servicios de negocio con contratos claros y reutilizables
- C) Eliminar la necesidad de contratos
- D) Obligar a usar microservicios

3. ¿Cuál de las siguientes afirmaciones describe mejor a REST en el contexto de integración?
- A) Es un protocolo binario para redes locales
- B) Es un estilo arquitectónico que aprovecha HTTP y trata recursos mediante métodos estándar como GET, POST, PUT, DELETE
- C) Es un lenguaje de programación orientado a objetos
- D) Es un reemplazo obligatorio de SOAP en todos los contextos

4. ¿Qué ventaja principal aportó REST+JSON en comparación con SOAP/XML para muchas APIs modernas?
- A) Mayores requisitos de herramientas especializadas
- B) Contratos más rígidos e inflexibles
- C) Mensajes más ligeros y fáciles de consumir desde navegadores y apps móviles
- D) Imposibilidad de usar HTTPS

5. En el contexto actual, ¿qué es común encontrar en organizaciones grandes?
- A) Solo monolitos puros sin integración
- B) Solo microservicios sin legado
- C) La convivencia de monolitos, servicios SOAP heredados, APIs REST y mecanismos basados en eventos
- D) Exclusivamente colas de mensajes sin APIs

6. ¿Qué tipo de integración se centra principalmente en compartir y sincronizar información (por ejemplo, tablas de clientes) entre sistemas?
- A) Integración de datos
- B) Integración funcional
- C) Integración semántica
- D) Integración física

7. ¿Qué tipo de integración implica consumir capacidades o funciones remotas, como “consultar saldo” o “crear pedido”?
- A) Integración de datos
- B) Integración funcional
- C) Integración semántica
- D) Integración de red

8. ¿A qué se refiere la integración semántica?
- A) A compartir archivos de texto sin estructura
- B) A alinear el significado de los datos y conceptos entre sistemas, evitando ambigüedades
- C) A comprimir mensajes para ahorrar ancho de banda
- D) A usar siempre el mismo tipo de base de datos

9. En un ejercicio donde mapeas sistemas de una organización y clasificas sus conexiones, ¿qué criterio usarías para etiquetar una integración como “crítica”?
- A) Que use JSON
- B) Que sea la que más ancho de banda consume
- C) Que, si falla, afecta procesos de negocio esenciales como facturación o pagos
- D) Que sea la más nueva

10. ¿Qué efecto tiene agregar muchas integraciones punto a punto a lo largo del tiempo?
- A) Facilita el mantenimiento porque todas son similares
- B) Disminuye la dependencia entre sistemas
- C) Aumenta la complejidad, la duplicación de lógica y el acoplamiento
- D) Elimina la necesidad de documentación

### Sección B: SOAP vs REST, pila SOAP y vigencia de SOAP

11. ¿Cuál de las siguientes es una característica típica de SOAP en la era SOA?
- A) Uso exclusivo de JSON
- B) Mensajes con sobre `<Envelope>`, `<Header>` y `<Body>` en XML
- C) Eliminación de contratos formales
- D) Comunicación solo dentro de un mismo proceso

12. ¿Qué elemento de la pila SOAP describe las operaciones disponibles y los tipos de mensajes?
- A) SOAP Envelope
- B) WSDL
- C) UDDI
- D) WS-Security

13. ¿Qué rol jugaron las especificaciones WS-* (como WS-Security, WS-Policy) en el ecosistema SOAP?
- A) Definir formatos de imagen
- B) Extender SOAP con capacidades avanzadas de seguridad, políticas, confianza y transacciones
- C) Reemplazar completamente a WSDL
- D) Hacer innecesario el uso de XML

14. ¿En qué sectores se menciona que SOAP sigue siendo comúnmente utilizado?
- A) Redes sociales y aplicaciones de mensajería instantánea
- B) Videojuegos móviles informales
- C) Banca, gobierno y salud con fuertes requisitos regulatorios
- D) Sitios web estáticos

15. ¿Cuál de las siguientes situaciones favorece seguir usando un servicio SOAP existente en lugar de migrarlo inmediatamente a REST?
- A) El proveedor solo ofrece WSDL y WS-* y la integración es estable y de largo plazo
- B) La API se usa solo para pruebas internas temporales
- C) Se requiere una interfaz gráfica rica
- D) No hay requisitos de seguridad

16. ¿Cuál es una diferencia conceptual clave entre mensajes SOAP y mensajes REST/JSON?
- A) REST/JSON obliga a usar WS-Security
- B) SOAP incluye un sobre estandarizado y namespaces; REST/JSON suele enviar directamente los datos sin esa envoltura
- C) SOAP no permite tipos de datos complejos
- D) REST requiere UDDI

17. ¿Qué describe mejor a una API REST bien diseñada?
- A) Operaciones definidas por verbos arbitrarios en la URL
- B) Recursos identificados por URIs y manipulados con métodos HTTP estándar y códigos de estado apropiados
- C) Mensajes exclusivamente XML
- D) Ausencia total de contrato o documentación

18. ¿En qué caso es especialmente importante decidir “cuándo convivir con SOAP y encapsularlo, y cuándo migrar a APIs más ligeras”?
- A) Cuando solo hay un sistema aislado sin integraciones
- B) Cuando no hay restricciones regulatorias ni de seguridad
- C) Cuando se integran sistemas legacy SOAP con nuevas aplicaciones y microservicios
- D) Cuando todos los servicios ya son REST

### Sección C: Prácticas – Tipos de integración, comparación WSDL vs REST

19. En la práctica de “tipos de integración”, un equipo dibuja varios sistemas y marca una integración entre el ERP y el sistema de facturación donde solo se replica la tabla de clientes cada noche. ¿Qué tipo de integración es la más adecuada?
- A) Funcional
- B) Semántica
- C) De datos
- D) De red

20. En esa misma práctica, otra integración permite que una app móvil invoque “consultar saldo” en un sistema bancario remoto. ¿Qué tipo de integración representa mejor esta situación?
- A) De datos, porque solo importa la tabla de saldos
- B) Funcional, porque se consume una capacidad remota de negocio
- C) Semántica, porque solo se alinea el significado
- D) Física, porque usa redes móviles

21. En el ejercicio de comparación WSDL vs REST, ¿cuál de estos elementos es más natural encontrar en un WSDL?
- A) Definiciones de `paths` y `responses` en JSON
- B) Elementos `<portType>`, `<operation>` y `<message>` que describen el contrato
- C) Documentación en formato Markdown
- D) Solo ejemplos de llamadas con `curl`

22. En la documentación de una API REST equivalente, ¿qué preguntas se suelen responder de forma explícita?
- A) Qué URIs existen, qué métodos HTTP soportan, qué estructura de JSON esperan y devuelven
- B) Cómo generar código a partir de WSDL
- C) Cómo registrar el servicio en UDDI
- D) Cómo usar WS-Security

23. Cuando en la práctica se pide comparar un WSDL con una API REST, ¿qué objetivo conceptual se busca?
- A) Convertir siempre el WSDL en REST
- B) Identificar elementos de contrato en ambos enfoques y discutir ventajas/desventajas
- C) Demostrar que uno de los dos está obsoleto
- D) Medir solo el tamaño de los mensajes

24. En un escenario donde un servicio SOAP y una API REST exponen la misma funcionalidad de “consultar saldo”, ¿qué diferencia práctica suele encontrarse?
- A) El SOAP se consume solo desde navegadores
- B) El WSDL describe tipos y operaciones en XML, mientras que la API REST suele usar JSON y documentación tipo OpenAPI o similar
- C) El SOAP es siempre más rápido
- D) La API REST no puede usar HTTPS

25. En un ejercicio grupal, se identifica una integración donde dos sistemas usan el mismo campo “balance” con significados distintos (uno es saldo disponible, otro saldo contable total). ¿Qué tipo de problema se ilustra?
- A) Problema de sintaxis XML
- B) Problema de transporte HTTP
- C) Problema de integración semántica
- D) Problema exclusivo de rendimiento

***

Si quieres, en el siguiente paso puedo proponerte claves sugeridas de respuesta para ambos exámenes, o ajustar el número de preguntas/dificultad para que se ajusten mejor al tiempo de 2 horas.