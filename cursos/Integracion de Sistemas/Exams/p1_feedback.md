A continuación tienes un feedback específico por pregunta para ambos exámenes, con una frase para respuesta correcta y otra para respuesta incorrecta. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_2308645d-8bcf-4483-94ed-f720d1b304cb/5c230302-fc47-4a58-8b04-4b086818c350/01_Diff_SOAP_REST.md)

***

## Examen 1 – Feedback por pregunta

1.  
- Correcta: Entendido: XML se usa para representar datos jerárquicos y validables, lo que es clave en mensajes SOAP.  
- Incorrecta: Revisa que XML en servicios web se valora por su estructura jerárquica y validación con XSD, no por tamaño reducido ni por ser binario.

2.  
- Correcta: Bien: identificas que un XML bien formado tiene un solo elemento raíz y etiquetas bien anidadas y cerradas.  
- Incorrecta: Vuelve a revisar las reglas de “bien formado”: un único root y etiquetas correctamente anidadas son esenciales.

3.  
- Correcta: Correcto: distingues que tipos simples son valores atómicos y los complejos agrupan elementos y atributos.  
- Incorrecta: Revisa la diferencia entre tipo simple (valor atómico) y tipo complejo (estructura con elementos/atributos).

4.  
- Correcta: Bien: reconoces que XSD describe la estructura y tipos de los mensajes XML usados por el servicio.  
- Incorrecta: Recuerda que XSD no optimiza HTTP ni seguridad; su foco es definir estructura y tipos de datos de los mensajes.

5.  
- Correcta: Correcto: WSDL es un lenguaje XML para describir operaciones, mensajes, tipos y endpoints de un servicio.  
- Incorrecta: Revisa que WSDL no es ni un formato de datos ni un protocolo: es un contrato descriptivo basado en XML.

6.  
- Correcta: Bien: identificas que el Body es obligatorio en un mensaje SOAP, el Header y Fault son opcionales.  
- Incorrecta: Recuerda que el elemento obligatorio en SOAP es el Body; el Header y Fault aparecen solo cuando se requieren.

7.  
- Correcta: Correcto: ves que WSDL permite generar código y validar mensajes de forma automática gracias al contrato estricto.  
- Incorrecta: Revisa la ventaja de contratos estrictos: facilitan generación de código y validación, pero exigen disciplina al evolucionar.

8.  
- Correcta: Bien: UDDI se diseñó como registro para publicar y descubrir servicios web.  
- Incorrecta: Recuerda que SOAP es protocolo de mensajería, WSDL describe el contrato, y UDDI es el registro/catalogo.

9.  
- Correcta: Correcto: SOAP típicamente usa XML y contratos formales; REST suele usar JSON y contratos más ligeros.  
- Incorrecta: Revisa la comparación: REST no requiere UDDI ni SOAP JSON; se caracteriza por mensajes ligeros y menor rigidez.

10.  
- Correcta: Bien: identificas que SOAP sigue siendo razonable en integraciones reguladas y de largo plazo con contratos muy estructurados.  
- Incorrecta: Recuerda que SOAP encaja mejor donde hay requisitos fuertes de seguridad, contratos estables y WS-Security.

11.  
- Correcta: Correcto: el Body suele contener un elemento que agrupa los datos del producto, como ProductResponse.  
- Incorrecta: Revisa la estructura del Body: no se envuelven datos en EnvelopeProduct ni en elementos de petición si es respuesta.

12.  
- Correcta: Bien: reconoces que debe existir un único Envelope con Header opcional y Body obligatorio.  
- Incorrecta: Recuerda que no se anidan múltiples Envelopes y siempre debe existir un Envelope que contenga Header y Body.

13.  
- Correcta: Correcto: el error indica que el valor no cumple el tipo definido en el XSD, aunque el XML pueda ser bien formado.  
- Incorrecta: Diferencia “bien formado” (sintaxis XML) de “válido” contra XSD; aquí el problema es de tipo de dato, no de sintaxis.

14.  
- Correcta: Bien: sabes que puedes extraer el XSD de `<types>` y usarlo en un validador XML/XSD.  
- Incorrecta: Recuerda que el WSDL sí permite validar mensajes extrayendo o referenciando sus XSD, no se ignoran los `<types>`.

15.  
- Correcta: Correcto: el Fault sirve para comunicar errores de procesamiento con código, motivo y detalles.  
- Incorrecta: Revisa que Fault no transmite datos de negocio ni configuraciones, sino información de error estándar.

16.  
- Correcta: Bien: identificas que el monolito mínimo arranca con rutas GET/POST en memoria para productos y pedidos.  
- Incorrecta: Revisa que inicialmente no hay base de datos ni solo PUT/DELETE; el foco es un CRUD simple en memoria.

17.  
- Correcta: Correcto: `express.json()` permite parsear automáticamente JSON en el cuerpo de la petición.  
- Incorrecta: Recuerda que `express.json()` no es para estáticos ni HTTPS; su función es procesar cuerpos JSON.

18.  
- Correcta: Bien: reconoces que `:id` es un parámetro de ruta en Express.  
- Incorrecta: Diferencia parámetros de ruta (`/recurso/:id`) de query string (`?id=…`) y headers.

19.  
- Correcta: Correcto: `DELETE /productos/:id` es la forma típica de eliminar un recurso específico.  
- Incorrecta: Revisa la convención REST: DELETE sobre la URI del recurso concreto, no sobre rutas genéricas o GETs “borradores”.

20.  
- Correcta: Bien: 404 Not Found es apropiado cuando el recurso solicitado por id no existe.  
- Incorrecta: Recuerda: 200 implica éxito con recurso; 404 es el código estándar cuando el recurso no se encuentra.

21.  
- Correcta: Correcto: PUT `/productos/:id` se usa para actualizar el recurso existente identificado por ese id.  
- Incorrecta: Revisa la semántica de PUT: típicamente actualiza o reemplaza el recurso, no solo “crear siempre” ni retornar sin cambios.

22.  
- Correcta: Bien: usar estructuras en memoria simplifica el laboratorio al evitar configurar una base de datos real.  
- Incorrecta: Recuerda que el objetivo es practicar lógica y rutas, no garantizar persistencia ni transacciones reales.

23.  
- Correcta: Correcto: POST `/productos` con `Content-Type: application/json` y cuerpo JSON es el patrón adecuado.  
- Incorrecta: Revisa que POST sin cuerpo o GET/PUT para crear recurso no son el patrón principal practicado.

24.  
- Correcta: Bien: reconoces la separación de recursos (productos, pedidos) como principio de diseño de la API.  
- Incorrecta: Recuerda que no se trata de tener un solo recurso, sino de tener rutas claras y separadas por tipo de entidad.

25.  
- Correcta: Correcto: en un monolito todo corre en un despliegue; en microservicios se fragmenta en servicios independientes.  
- Incorrecta: Revisa la diferencia de despliegue: monolito un solo artefacto, microservicios varios servicios autónomos.

***

## Examen 2 – Feedback por pregunta

1.  
- Correcta: Bien: identificas la integración punto a punto como conexiones directas que generan “spaghetti” al crecer.  
- Incorrecta: Revisa que en punto a punto no hay bus central; cada par de sistemas construye su propia integración.

2.  
- Correcta: Correcto: SOA agrupa lógica en servicios de negocio con contratos claros, reduciendo spaghetti.  
- Incorrecta: Recuerda que SOA no busca más conexiones, sino servicios reutilizables y contratos bien definidos.

3.  
- Correcta: Bien: REST es un estilo que usa HTTP y trata recursos con métodos GET, POST, PUT, DELETE, etc.  
- Incorrecta: Revisa que REST no es un protocolo binario ni un lenguaje de programación.

4.  
- Correcta: Correcto: REST+JSON aporta mensajes más ligeros y fáciles de consumir que SOAP/XML en muchos casos.  
- Incorrecta: Recuerda que la ventaja típica de REST+JSON es simplicidad y ligereza, no mayor rigidez ni más herramientas pesadas.

5.  
- Correcta: Bien: reconoces la coexistencia de monolitos, SOAP legacy, REST y eventos en organizaciones reales.  
- Incorrecta: Revisa que el mundo real suele mezclar estilos, no eliminar por completo monolitos o SOAP.

6.  
- Correcta: Correcto: cuando se comparte/sincroniza información (como tablas de clientes), se trata de integración de datos.  
- Incorrecta: Recuerda que la integración de datos se enfoca en replicar y sincronizar información, no tanto en invocar funciones.

7.  
- Correcta: Bien: consumir “consultar saldo” remoto es integración funcional, porque usas capacidades de otro sistema.  
- Incorrecta: Diferencia integrar datos (tablas) de integrar funciones (operaciones como consultar o crear).

8.  
- Correcta: Correcto: integración semántica alinea significado de datos y conceptos entre sistemas.  
- Incorrecta: Revisa que el problema semántico es que “balance”, “cliente”, etc., signifiquen lo mismo en todos los sistemas.

9.  
- Correcta: Bien: una integración es crítica si, al fallar, afecta procesos esenciales como pagos o facturación.  
- Incorrecta: Recuerda que lo crítico se define por impacto al negocio, no por ancho de banda ni novedad.

10.  
- Correcta: Correcto: muchas integraciones punto a punto terminan en mayor complejidad, duplicación y acoplamiento.  
- Incorrecta: Revisa que más conexiones punto a punto aumentan el “spaghetti” y hacen el mantenimiento más difícil.

11.  
- Correcta: Bien: SOAP se caracteriza por mensajes XML con Envelope, Header y Body.  
- Incorrecta: Recuerda que SOAP no es JSON; su estructura estándar en XML es una de sus señas de identidad.

12.  
- Correcta: Correcto: WSDL describe operaciones, mensajes y tipos de datos del servicio.  
- Incorrecta: Revisa que WSDL es el contrato; SOAP es el protocolo de mensaje y UDDI es el registro.

13.  
- Correcta: Bien: las especificaciones WS-* extienden SOAP con seguridad, políticas, confianza, transacciones, etc.  
- Incorrecta: Recuerda que WS-* no reemplaza WSDL ni define imágenes; amplía capacidades de la pila SOAP empresarial.

14.  
- Correcta: Correcto: SOAP sigue siendo común en banca, gobierno y salud con requisitos fuertes.  
- Incorrecta: Revisa que estos sectores valoran los contratos formales y WS-Security; no se trata de redes sociales o juegos.

15.  
- Correcta: Bien: si solo hay WSDL/WS-* y el contrato es estable de largo plazo, tiene sentido seguir usando SOAP.  
- Incorrecta: Recuerda que migrar a REST no siempre es prioritario si la integración SOAP es estable y regulada.

16.  
- Correcta: Correcto: SOAP incluye sobre estándar y namespaces; REST/JSON suele enviar directamente datos sin esa envoltura.  
- Incorrecta: Revisa que REST no obliga WS-Security ni UDDI; su formato típico es JSON sin Envelope estándar.

17.  
- Correcta: Bien: una API REST bien diseñada usa URIs de recursos, métodos HTTP y códigos de estado coherentes.  
- Incorrecta: Recuerda que REST no es solo “sin contrato”; debería documentar recursos, métodos y respuestas.

18.  
- Correcta: Correcto: el dilema SOAP vs APIs ligeras se vuelve crítico cuando integras legacy SOAP con nuevos servicios.  
- Incorrecta: Revisa que cuando todo es REST el problema es menor; el reto es convivir con sistemas SOAP existentes.

19.  
- Correcta: Bien: replicar la tabla de clientes cada noche es integración de datos.  
- Incorrecta: Recuerda que aquí no se invoca una función de negocio; solo se copian datos entre sistemas.

20.  
- Correcta: Correcto: la app que invoca “consultar saldo” realiza integración funcional.  
- Incorrecta: Diferencia compartir tablas (datos) de exponer operaciones como “consultar saldo” (funcional).

21.  
- Correcta: Bien: en un WSDL verás elementos como `<portType>`, `<operation>` y `<message>`.  
- Incorrecta: Revisa que JSON y `paths` son típicos de OpenAPI/REST, no de WSDL.

22.  
- Correcta: Correcto: la documentación REST detalla URIs, métodos, estructura de JSON de entrada/salida, etc.  
- Incorrecta: Recuerda que registrar en UDDI y WS-Security pertenecen más al mundo SOAP/WS-*.

23.  
- Correcta: Bien: el objetivo es identificar elementos de contrato en WSDL y REST y discutir ventajas/desventajas.  
- Incorrecta: Revisa que la práctica no busca declarar obsoleto a uno, sino entender ambos enfoques.

24.  
- Correcta: Correcto: el WSDL describe tipos/operaciones en XML; la API REST usa JSON y normalmente OpenAPI u otra doc.  
- Incorrecta: Recuerda que ambos pueden usar HTTPS; la diferencia está en formato y forma de documentar el contrato.

25.  
- Correcta: Bien: el uso distinto de “balance” ilustra un problema de integración semántica.  
- Incorrecta: Revisa que aquí el problema no es de transporte ni sintaxis, sino de significado de los datos.

***

Si quieres, puedo condensar estos textos en versiones aún más cortas pensadas para el límite de caracteres del feedback en Google Forms.