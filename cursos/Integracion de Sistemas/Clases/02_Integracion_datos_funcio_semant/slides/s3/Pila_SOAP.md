#! Integración de sistemas   
##! Pila clásica de servicios web SOAP

# SOAP y XML como base de mensajería

SOAP es un protocolo de mensajería para servicios web que encapsula datos en mensajes XML estructurados y transportados típicamente sobre HTTP o HTTPS. Cada mensaje SOAP sigue una estructura estándar, lo que facilita la interoperabilidad entre plataformas distintas como Java, .NET o sistemas legados. XML actúa como formato de representación, permitiendo describir datos complejos con tipos y estructuras anidadas. 

Más adelante veremos con detalle la estructura de mensajes SOAP y de XML; aquí lo usamos como contexto para entender la pila de servicios web.

# WSDL: contratos estrictos

WSDL es un lenguaje basado en XML que describe qué operaciones ofrece un servicio, qué mensajes acepta y devuelve, qué tipos de datos utiliza y en qué endpoints están disponibles. En la práctica, WSDL funciona como un contrato estricto: las herramientas pueden generar código cliente y servidor a partir del documento WSDL, y los mensajes se validan contra los esquemas definidos. Esta aproximación “contract-first” hace que cualquier desviación en el formato o tipo de dato cause errores claros, lo que da seguridad pero exige disciplina en la evolución del servicio.


# UDDI y la familia WS-

UDDI (Universal Description, Discovery and Integration) es un estándar basado en XML que define un registro o directorio para publicar y descubrir servicios web y la información técnica necesaria para consumirlos.

Aunque los registros UDDI públicos han perdido protagonismo, el concepto de catálogo de servicios sigue vivo en portales de APIs modernos. 

Alrededor de SOAP surgió también la familia de especificaciones WS- para abordar seguridad, confiabilidad, transacciones distribuidas y otros aspectos avanzados. 

---
Algunas de las especificaciones WS- más comunes son:

- WS-Security
- WS-Policy / WS-SecurityPolicy
- WS-Trust
- WS-SecureConversation
- WS-Addressing

---
Estos estándares complementan a SOAP y WSDL para formar lo que se conoce como la pila clásica de servicios web en entornos empresariales.


## Actividad: Diseñar un mini‑contrato verbal

Hacer cuatro equipos y trabajar un servicio de "Consulta de saldo" bancario. Escriban en una hoja o documento: nombre de la operación, parámetros de entrada, estructura simplificada de la salida y posibles códigos de error. Luego discutan qué tan rígido debería ser este "contrato" para que diferentes equipos puedan implementarlo sin malentendidos. Se trata de anticipar el rol de WSDL como contrato formal pero sin clavarse todavía en su sintaxis.
