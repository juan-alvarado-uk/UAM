#! Integración de sistemas   
##! Panorama histórico y concepto actual de integración


# Punto a punto: el “cableado spaghetti”

La integración punto a punto fue la forma dominante de conectar sistemas en los primeros años de la informática empresarial. 
Consistía en que cada par de aplicaciones que necesitaba hablar entre sí establecía su propio canal de comunicación con protocolos y formatos hechos a la medida. 
Cada vez que aparecía un nuevo sistema, se agregaban más conexiones directas, lo que generaba una red cada vez más compleja y difícil de mantener. 
En organizaciones grandes esto producía un efecto “spaghetti”: muchas conexiones cruzadas, lógica de integración duplicada y alta dependencia entre sistemas. 
Cambiar o reemplazar una aplicación se volvía costoso, porque había que reescribir múltiples integraciones. 

---

**Actividad – Mapa de spaghetti**  
En equipos de 3–4, elijan un escenario sencillo y que dibujen en pizarrón (no borrar) las conexiones punto a punto entre sistemas si cada par se conecta directamente.  

---
Después, cada equipo identifica:  
- Cuántas integraciones habría si se agregan nuevos sistemas (por ejemplo, CRM, app móvil).  
- Qué pasaría si se cambia el sistema de pagos.  
Discutir brevemente cómo crece la complejidad en función del número de sistemas.  

---

# SOA: servicios y buses de integración

Para reducir el caos de las integraciones punto a punto surgió la Arquitectura Orientada a Servicios (SOA). 
En SOA, la lógica de negocio se agrupa en servicios bien definidos que representan capacidades (por ejemplo, “Servicio de Clientes”, “Servicio de Facturación”), en lugar de conexiones ad hoc entre aplicaciones. 
Los servicios se comunican mediante mensajes estándar y suelen utilizar un middleware de integración como un ESB (Enterprise Service Bus) para orquestar, transformar y enrutar mensajes. 
SOA enfatiza contratos claros entre productor y consumidor de servicios, lo que facilita la reutilización de funcionalidades en diferentes aplicaciones. 
Sin embargo, muchas implementaciones de SOA se volvieron pesadas, con gobernanza compleja y dependencia fuerte del ESB. 

---

**Actividad – Reorganizar el spaghetti en servicios**  
En los mismos equipos, reutilicen el escenario elegido y ya dibujado.  
Ahora deben:  
- Proponer de 3 a 5 servicios de negocio (por ejemplo, Clientes, Pedidos, Pagos, Inventario).  
- Dibujar cómo los sistemas existentes (web, ERP, pasarela de pago) consumirían esos servicios en vez de conectarse entre sí directamente.  

---
Contrastar el nuevo diagrama con el anterior y notar el cambio en:  
- Número de conexiones.  
- Facilidad para agregar un nuevo canal (por ejemplo, app móvil).  

---

# Servicios web SOAP/XML en la era SOA

En la época de auge de SOA, los servicios web basados en SOAP (Simple Object Access Protocol) y XML se convirtieron en el estándar dominante para la integración entre sistemas heterogéneos. 

SOAP define un formato de mensaje estructurado en XML que viaja normalmente sobre HTTP, pero el protocolo no está limitado a HTTP. 
Los mensajes SOAP incluyen un sobre (Envelope) que contiene un encabezado (Header) y un cuerpo (Body), más una sección de error (Fault) cuando algo falla. 
Alrededor de SOAP se construyó todo un ecosistema: WSDL para describir servicios, UDDI para registrarlos y la familia de especificaciones WS-* (seguridad, confiabilidad, transacciones, etc.). 
Esta pila fue adoptada con fuerza en sectores como banca, gobierno y salud, donde se requerían contratos estrictos, tipos de datos muy detallados y fuertes garantías de seguridad. 

*(Estos temas se retomarán con más detalle en clases dedicadas a SOAP/XML, por lo que aquí solo se mencionan de manera muy general.)*  

---

# Surgimiento de REST y las APIs modernas

A comienzos de los 2000, Roy Fielding formuló REST (Representational State Transfer) como estilo arquitectónico para la Web, proponiendo una forma simple y uniforme de diseñar servicios usando HTTP como protocolo de aplicación. 

REST plantea que los recursos de una aplicación se identifiquen con URIs y se manipulen con los métodos estándar de HTTP (GET, POST, PUT, DELETE, etc.). 
La combinación de REST con formatos ligeros como JSON hizo que las APIs fueran más fáciles de consumir desde navegadores, apps móviles y servicios en la nube. 
Muchas empresas de Internet (por ejemplo, redes sociales y servicios de mapas) popularizaron las APIs REST públicas, lo que impulsó aplicaciones de terceros. 
REST no reemplazó automáticamente a SOAP, pero sí se volvió el enfoque dominante para integraciones web nuevas, sobre todo cuando se privilegian simplicidad y agilidad sobre contratos muy rígidos. 

---

# Concepto actual de integración: visión general

Hoy la integración de sistemas incluye múltiples estilos y arquitecturas que coexisten: monolitos, SOA “clásico”, microservicios y arquitecturas dirigidas por eventos. 

La elección de un estilo depende de factores como tamaño de la organización, velocidad de cambio del negocio, restricciones regulatorias y madurez técnica del equipo. 
En la práctica, muchas empresas combinan varios enfoques: por ejemplo, un monolito principal con algunos microservicios alrededor, o servicios legacy SOAP conectados con APIs REST y colas de mensajes. 
La tendencia reciente es construir sistemas API-first, donde las interfaces se diseñan antes del código, y aprovechar eventos para integrar componentes de forma desacoplada. 
El reto para futuros sistemas, es saber cuándo conviene cada estilo y cómo hacerlos coexistir sin repetir errores de integración del pasado. 

---

**Actividad – Debate: “esto no es blanco/negro”**  
Hacer dos grandes grupos:  
- Equipo A: “Todo debería ser microservicios y eventos”.  
- Equipo B: “Un buen monolito bien diseñado sigue siendo suficiente en muchos casos”.  

Cada equipo discute para preparar 3 argumentos que defiendan su postura.  

---
Luego los equipos presentarán sus argumentos al equipo contrario (tratando de convencerlos).  

