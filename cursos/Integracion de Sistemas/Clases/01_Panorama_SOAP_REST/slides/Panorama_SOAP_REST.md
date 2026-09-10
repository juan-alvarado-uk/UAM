# CLASE: Panorama Histórico y Conceptual de Integración de Sistemas  
## Duración: 2 horas | Dividido en 2 secciones de 1 hora

---

## SECCIÓN 1: EVOLUCIÓN HISTÓRICA (60 minutos)

### I. El Inicio: Integración Punto a Punto (1990s - Principios 2000s)

#### A. El Problema Original

En la década de 1990, las organizaciones enfrentaban un desafío fundamental: tenían múltiples sistemas de información que no podían comunicarse entre sí, generando “islas de información”.[web:6]  
Cada departamento (ventas, recursos humanos, finanzas) operaba sistemas independientes, y para que estos intercambiaran datos se creaban conexiones directas entre cada par de sistemas, lo que escalaba de forma casi exponencial a medida que aumentaba el número de sistemas.[web:6]

Esta complejidad se conoce como el problema de integración **punto a punto** o *spaghetti integration*.[web:6]  

**Características principales:**
- Conexiones directas entre cada par de sistemas (n(n−1)/2 conexiones para n sistemas).[web:6]  
- Duplicación de lógica de transformación de datos en múltiples lugares.[web:6]  
- Mantenimiento difícil: cambiar un sistema impacta muchas conexiones.[web:6]  
- Escalabilidad muy limitada.[web:6]  
- Ausencia de estándares comunes entre aplicaciones.[web:6]  

#### B. Tecnologías Iniciales

Las primeras soluciones típicas incluían:[web:6]  

- Transferencia de archivos planos (CSV, texto delimitado) como intercambios nocturnos o por lote.  
- Llamadas a procedimientos remotos (RPC) con tecnologías propietarias.  
- Conectores específicos para cada par de sistemas, muchas veces hechos “a la medida”.  

El resultado era que **cada conexión** se convertía en un mini–proyecto de ingeniería independiente.[web:6]  

---

### II. Servicios Web y SOA: La Primera Estandarización (2000-2008)

#### A. Surgimiento de SOA (Service-Oriented Architecture)

A finales de los 90 y principios de los 2000 surge **Service-Oriented Architecture (SOA)** como un estilo de arquitectura orientado a **servicios discretos** en lugar de grandes sistemas monolíticos.[web:6][web:17]  
La idea es que cada sistema expone ciertas capacidades de negocio como **servicios**, accesibles de manera estándar e interoperable.[web:17]  

En una arquitectura SOA:[web:17]  

- Cada sistema expone funcionalidad como servicios bien definidos (por ejemplo, “Servicio Clientes”, “Servicio Pagos”).  
- Los servicios son independientes de la implementación interna y del lenguaje de programación.  
- Otras aplicaciones consumen estos servicios sin conocer detalles internos.  
- Se define un **contrato** que describe operaciones, parámetros y formatos de datos.  

Esto reduce la necesidad de conexiones punto a punto entre todos los sistemas, porque cada uno publica sus servicios en un modelo más centralizado o mediado.[web:6]  

#### B. La Pila SOAP/XML

SOA se apoyó fuertemente en una pila de estándares basada en XML y protocolos web:[web:7][web:8][web:6]  

1. **SOAP (Simple Object Access Protocol)**  
   - Protocolo basado en XML para intercambio de mensajes estructurados sobre transportes como HTTP o SMTP.[web:7][web:8]  
   - La estructura básica de un mensaje SOAP incluye:
     - Envelope: elemento raíz que envuelve todo el mensaje.  
     - Header: metadatos opcionales (seguridad, transacciones).  
     - Body: contenido de la solicitud o respuesta.  
     - Fault: descripción estructurada de errores, cuando aplica.  

   Ejemplo conceptual simplificado:

   ```xml
   <soap:Envelope>
     <soap:Header>
       <!-- Autenticación, metadatos -->
     </soap:Header>
     <soap:Body>
       <getCliente>
         <clienteId>12345</clienteId>
       </getCliente>
     </soap:Body>
   </soap:Envelope>

2. **WSDL (Web Services Description Language)**  
   - Lenguaje basado en XML para describir formalmente un servicio web (operaciones, tipos de datos, endpoints).[web:6][web:7]  
   - Permite a herramientas generar clientes automáticamente a partir del contrato.  

3. **UDDI (Universal Description, Discovery and Integration)**  
   - Registros para publicar y descubrir servicios web.[web:6]  
   - Nunca tuvo adopción masiva en la práctica, pero fue importante conceptualmente.  

4. **Familia WS-* (WS-Security, WS-ReliableMessaging, etc.)**  
   - Conjunto de estándares para seguridad, confiabilidad, transacciones y políticas en servicios SOAP.[web:7][web:8]  
   - WS-Security, por ejemplo, define cómo firmar y cifrar mensajes SOAP a nivel de mensaje.  

#### C. Ventajas y Problemas de SOAP/XML

**Ventajas principales:**[web:6][web:7][web:8]  

- Interoperabilidad fuerte entre plataformas gracias al uso de XML y contratos WSDL.  
- Contratos estrictos favorecen integraciones formales en entornos empresariales.  
- Ecosistema amplio de estándares (WS-*) para seguridad y transacciones distribuidas.  

**Limitaciones que se evidenciaron:**[web:7][web:8]  

- Mensajes verbosos: XML produce mensajes relativamente grandes, afectando rendimiento y ancho de banda.  
- Curva de aprendizaje alta por múltiples estándares y herramientas.  
- Uso de HTTP sin explotar del todo la semántica de los métodos (GET, POST, PUT, DELETE).  
- Poco amigable para navegadores y aplicaciones móviles ligeras.  

Aun con estas limitaciones, SOAP permanece en uso en sectores regulados y sistemas legados críticos.[web:8]  

#### D. Vigencia de SOAP

En 2020s, SOAP sigue siendo relevante en:[web:8]  

- Banca y pagos interbancarios, donde se requieren fuertes garantías transaccionales.  
- Integración gubernamental entre instituciones.  
- Salud, seguros y otros sectores regulados con infraestructuras legadas.  

En muchos casos, estas organizaciones combinan SOAP internamente con APIs REST hacia el exterior.[web:8][web:10]  

---

### III. REST: Arquitectura Alineada con la Web

#### A. Orígenes de REST

**REST (Representational State Transfer)** fue descrito por Roy Fielding en su tesis doctoral en 2000 como un estilo arquitectónico para sistemas distribuidos, especialmente la Web.[web:7][web:8]  
Mientras SOAP definía un protocolo de mensajería específico, REST proponía principios generales para diseñar APIs sobre HTTP usando sus capacidades nativas.[web:7]  

#### B. Principios Clave de REST

Los principios fundamentales de REST incluyen:[web:7][web:8]  

- Todo es un **recurso** identificado por una URI (por ejemplo, `/clientes/123`).  
- Se usan los **métodos HTTP** estándar:
  - GET para leer recursos.  
  - POST para crear recursos.  
  - PUT/PATCH para actualizar.  
  - DELETE para eliminar.  
- Las representaciones de recursos suelen ser JSON (aunque pueden ser XML u otros formatos).  
- La comunicación es **sin estado**: el servidor no mantiene sesión entre peticiones, cada solicitud incluye lo necesario.  
- Las respuestas pueden incluir enlaces a otros recursos (hipermedia).  

Ejemplo de uso típico:

- `GET /clientes/123` devuelve el cliente 123 en JSON.  
- `POST /clientes` crea un nuevo cliente enviando un JSON con sus datos.  

#### C. Comparación SOAP vs REST

A nivel general:[web:7][web:8][web:10]  

| Aspecto                 | SOAP                                      | REST                                   |
|-------------------------|-------------------------------------------|----------------------------------------|
| Naturaleza              | Protocolo específico                      | Estilo arquitectónico                  |
| Formato principal       | XML obligatorio                            | Generalmente JSON (u otros)           |
| Mensaje                 | Verboso, sobrecarga alta                  | Ligero, más compacto                   |
| Método de invocación    | Operaciones nombradas (getCliente, etc.)  | Verbos HTTP sobre recursos             |
| Contratos               | WSDL (muy formal)                         | OpenAPI/Swagger (más flexible)        |
| Seguridad avanzada      | WS-Security                               | Normalmente HTTPS + tokens (OAuth/JWT)|
| Casos típicos           | B2B, banca, gobierno                      | Web, mobile, APIs públicas             |

REST se adoptó rápidamente para APIs web por su simplicidad y alineación con HTTP.[web:7]  

#### D. OpenAPI/Swagger como “WSDL para REST”

Para describir APIs REST de forma estructurada, surge **Swagger**, luego estandarizado como **OpenAPI**.[web:10]  

- Permite especificar endpoints, parámetros, cuerpos y respuestas de una API REST.  
- Sirve para generar documentación, validadores y clientes automáticamente.  

No es tan rígido como WSDL, pero es mucho más usable en entornos ágiles de desarrollo.[web:10]  

---

### IV. ACTIVIDAD 1 (10 minutos)  
**Comparación de Eras de Integración**

**Escenario:**  
Una empresa de e‑commerce debe integrar: sistema de inventario, sistema de pagos, sistema de envíos y sistema de correos para notificaciones.

**En grupos pequeños (3-4 estudiantes), responder:**

1. ¿Cuántas conexiones punto a punto se requerirían con 4 sistemas?  
2. ¿Cómo se vería la solución con SOA/SOAP (servicios grandes por función)?  
3. ¿Cómo describirías la misma integración con REST (recursos y URIs)?  
4. ¿Qué sucede si el sistema de envíos cambia su tecnología interna pero mantiene el contrato de servicio (SOAP/WSDL u OpenAPI)?  

Discusión plenaria rápida al final para reforzar:  
- Crecimiento de conexiones en punto a punto.  
- Reducción conceptual de complejidad en SOA/REST.  

---

## SECCIÓN 2: CONCEPTOS ACTUALES DE INTEGRACIÓN (60 minutos)

### V. Cuatro Modelos Arquitectónicos Modernos

#### A. Monolito

**Definición:** Una única aplicación desplegada como unidad, con una base de datos centralizada y código fuertemente acoplado.[web:10]  

**Características:**
- Un solo código base y un solo artefacto de despliegue.[web:10]  
- Base de datos central con todas las tablas del dominio.[web:10]  
- Comunicación interna mediante llamadas a métodos o funciones.  
- Escalamiento vertical (más CPU/RAM) o duplicando todo el monolito.  

**Ventajas y Limitaciones:**
- Rápido de desarrollar inicialmente, sencillo de entender.  
- Se vuelve difícil de mantener cuando crece el equipo y la funcionalidad.  
- Cualquier cambio requiere desplegar todo el sistema.  

#### B. SOA (Service-Oriented Architecture)

**Definición:** Arquitectura con múltiples servicios de negocio de grano medio o grueso (clientes, pedidos, pagos, etc.), usualmente orquestados por un **ESB (Enterprise Service Bus)**.[web:6][web:10]  

**Características:**
- Servicios con responsabilidades amplias pero separadas.  
- Comunicación frecuente mediante SOAP/XML y ESB.[web:6][web:10]  
- Contratos claramente definidos (WSDL).  

**Ventajas:**
- Menos acoplamiento que un monolito.  
- Mayor reutilización de funcionalidades entre aplicaciones.  

**Desafíos:**
- El ESB se vuelve un nodo crítico de complejidad y gobernanza.  
- Latencias más altas debido al procesamiento centralizado.[web:10]  

#### C. Microservicios

**Definición:** Arquitectura basada en servicios **pequeños e independientes**, cada uno desplegable y escalable por separado, típicamente orientados a un contexto de negocio muy específico.[web:4][web:5][web:10]  

**Características clave:**
- Cada microservicio tiene su propia base de datos (desacoplamiento de datos).[web:10]  
- Comunicación usualmente vía HTTP/REST o gRPC.[web:10]  
- Despliegue autónomo por servicio.  
- Propiedad por equipos pequeños y especializados.[web:4]  

**Ventajas:**  
- Escalabilidad granular: escalar solo los servicios que lo requieren.[web:10]  
- Alta resiliencia: fallas aisladas a un servicio específico.[web:10]  
- Permite equipos paralelos con más autonomía.[web:10]  

**Desafíos:**  
- Complejidad operativa: orquestación, monitoreo y trazabilidad distribuidos.[web:10]  
- Gestión de consistencia de datos y transacciones distribuidas.  

#### D. Arquitectura Orientada a Eventos

**Definición:** Estilo en el que los componentes se comunican mediante **eventos** (publicación/suscripción), en lugar de invocaciones directas síncronas.[web:9][web:15]  

**Características:**
- Los productores publican eventos cuando ocurre un cambio relevante (por ejemplo, “PedidoCreado”).[web:9]  
- Los consumidores se suscriben a los eventos de interés y reaccionan cuando los reciben.[web:9][web:15]  
- Hay uno o varios **brokers de eventos** que median la comunicación (Kafka, RabbitMQ, etc.).[web:9][web:15]  

**Ventajas:**
- Desacoplamiento temporal: el productor no espera respuesta inmediata.[web:9][web:15]  
- Escalabilidad y procesamiento en tiempo casi real para flujos de alto volumen.[web:15][web:18]  

**Desafíos:**
- Manejo de orden de eventos, reintentos e idempotencia.[web:9][web:15]  
- Diagnóstico y depuración de flujos distribuidos complejos.[web:15]  

---

### VI. Comparación Integrada de los Cuatro Modelos

| Aspecto                 | Monolito                  | SOA                                | Microservicios                          | Event-Driven                               |
|-------------------------|---------------------------|------------------------------------|------------------------------------------|---------------------------------------------|
| Tamaño de servicios     | Una sola aplicación       | Servicios grandes de negocio       | Servicios pequeños y específicos         | Cualquier tamaño, comunicando por eventos   |
| Comunicación            | Llamadas internas         | SOAP/ESB                           | REST/gRPC entre servicios                | Publicación/suscripción en broker           |
| Base de datos           | Compartida                | Frecuentemente compartida o mixta  | Una por servicio                         | Cada consumidor mantiene su propio estado   |
| Escalabilidad           | Vertical                  | Por servicio en cierto grado       | Altamente granular                       | Altamente elástica en función del broker    |
| Complejidad operativa   | Baja al inicio            | Media (gobernanza SOA)             | Alta (muchos servicios)                  | Alta (gestión de eventos y flujos)          |
| Casos ideales           | Apps pequeñas/medianas    | Grandes organizaciones tradicionales| Plataformas en rápido crecimiento         | IoT, analítica tiempo real, notificaciones  |

---

### VII. Tendencias: Convergencia e Hibridación

En la práctica, las arquitecturas reales son **híbridas**:[web:5][web:10][web:13]  

- Monolitos que extraen partes como microservicios cuando crece la demanda.  
- SOA heredado basado en SOAP coexistiendo con APIs REST modernas.  
- Microservicios que usan eventos para sincronización y procesamiento en tiempo real.  
- Combinaciones de API-first, event-driven y, en algunos casos, serverless.  

Patrones comunes incluyen usar API Gateways frente a servicios legacy y el patrón **Strangler** para migrar gradualmente de sistemas monolíticos o SOAP a arquitecturas más modernas.[web:5][web:10]  

---

### VIII. ACTIVIDAD 2 (15 minutos)  
**Diseño Arquitectónico para Diferentes Contextos**

Dividir la clase en 4 grupos, cada uno con un escenario:

1. Startup de e‑commerce con poco presupuesto y urgencia de salir al mercado.  
2. Banco nacional con sistemas SOAP legados y requerimientos regulatorios fuertes.  
3. Plataforma de red social con crecimiento rápido en usuarios.  
4. Sistema de alertas IoT en tiempo real con miles de dispositivos.  

Cada grupo elige entre: **monolito, SOA, microservicios, eventos (o combinación)** y justifica su decisión.  
Luego exponen brevemente (2 minutos por grupo).  

---

### IX. Integración Semántica (Mención Breve)

Aunque la atención está en la integración técnica (SOAP, REST, eventos), existe el problema de **integración semántica**: que los sistemas compartan no solo datos, sino **significado común**.[file:3]  

Ejemplo: un sistema llama “cliente” a lo que otro llama “usuario”, lo que introduce ambigüedad semántica aunque las APIs funcionen técnicamente.[file:3]  

La solución apunta a vocabularios compartidos y modelos semánticos, que se explorarán en clases posteriores.[file:3]  

---

### X. ACTIVIDAD 3 (10 minutos)  
**Reflexión: Evolucionando una Arquitectura**

Escenario:  
Un sistema bancario diseñado en 2008 con SOA/SOAP ahora debe ser mobile‑first, integrarse con fintechs y soportar pagos en tiempo casi real.

Preguntas para discusión guiada:

1. ¿Cómo introducirías APIs REST sin romper los servicios SOAP existentes?  
2. ¿Dónde tendría sentido añadir eventos para auditoría y monitoreo en tiempo real?  
3. ¿Qué riesgos de seguridad cambian al pasar de WS-Security a REST + OAuth/HTTPS?  
4. ¿Por qué la migración debería ser gradual y no un “big bang”?  

Cierre reforzando que la evolución arquitectónica es un proceso continuo y estratégico.[web:5][web:10]  

---

## REFERENCIAS BIBLIOGRÁFICAS (Sugeridas)

- IBM. “SOA vs. Microservices: What's the Difference?”.[web:6]  
- Treblle. “From SOAP to REST: Tracing The History of APIs”.[web:7]  
- TechChannel. “REST, SOAP, Microservices, Monitoring and Management”.[web:8]  
- Solace. “What is Event-Driven Integration?”.[web:9]  
- DesignGurus / otros. “Monolithic vs Microservices vs SOA – Architecture Comparison”.[web:10]  
- Confluent / otros. Introducciones a Event-Driven Architecture (EDA).[web:15][web:18]  


