#! Integración de sistemas   
##! SOAP hoy...

# Sectores donde SOAP sigue vigente

Aunque muchas integraciones nuevas usan APIs REST o variantes modernas, SOAP sigue siendo relevante en sectores con fuertes requisitos regulatorios y de seguridad. En banca, numerosos servicios de pago, compensación y reporteo se apoyan en servicios web SOAP por sus contratos formales, soporte para WS-Security y herramientas maduras. En gobierno, muchas plataformas de interoperabilidad entre dependencias se estandarizaron hace años en torno a SOAP, y migrar toda esa infraestructura es costoso y arriesgado. En salud, estándares como HL7 y ciertas pasarelas de intercambio clínico han utilizado SOAP y WS- para garantizar trazabilidad, autenticación y cifrado robusto.


# APIs modernas: REST y más allá

Las APIs modernas suelen exponer recursos a través de HTTP usando REST y formatos ligeros como JSON, lo que simplifica el consumo desde navegadores, apps móviles y microservicios. Estas APIs favorecen ciclos de desarrollo rápidos, menores dependencias de herramientas específicas y una curva de aprendizaje más suave para desarrolladores. Nuevos enfoques como GraphQL, gRPC o arquitecturas basadas en eventos amplían el repertorio. 

No obstante, es importante entender que en la práctica conviven servicios SOAP heredados con APIs modernas, y muchos proyectos requieren integrar ambos mundos. 


# Cuándo SOAP sigue siendo una opción razonable

SOAP puede seguir siendo una opción razonable cuando se necesitan contratos **altamente estructurados**, **transacciones distribuidas complejas o cumplimiento de estándares existentes** que ya asumen la pila SOAP. 

Esto es frecuente en integraciones **interorganizacionales** donde el contrato se negocia una vez y debe mantenerse **estable durante muchos años**. 

También puede ser más sencillo consumir un servicio SOAP existente que reescribirlo en REST, sobre todo si el proveedor solo ofrece WSDL y documentación WS-. 

El reto para el arquitecto es decidir cuándo convivir con SOAP y encapsularlo, y cuándo impulsar una migración hacia APIs más ligeras. 

# Práctica

**Explorando un WSDL y comparándolo con una API REST**

En esta práctica inspeccionarán un archivo WSDL y lo compararán conceptualmente con la documentación de una API REST, identificando elementos de contrato en ambos casos.
