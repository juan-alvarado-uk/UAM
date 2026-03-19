# Catálogos de APIs y términos de uso

# Portales de APIs modernos
Los catálogos modernos evolucionan la idea de UDDI hacia portales de APIs que concentran documentación, ejemplos, consola de pruebas y administración de claves. 
En empresas grandes, estos portales actúan como “tienda interna” de servicios, donde los equipos descubren qué APIs existen antes de crear una nueva. 
También pueden incluir buscadores por dominio de negocio, tags y versiones, y paneles de uso para monitorear consumo por aplicación cliente. 

# Documentación y contratos publicados
Los portales exponen contratos REST (OpenAPI) o de otros estilos y pueden incluir variantes enriquecidas con semántica (ejemplo: JSON-LD o enlaces a vocabularios). 
Es normal que compartan porciones de código listos para copiar en varios lenguajes, SDK generados automáticamente y guías para iniciar a usar la API. 
Para integradores, el portal es la primera fuente para entender límites de uso, formatos, errores y ciclos de vida (versionado, deprecaciones). 

# Términos de uso y políticas
Los términos de uso de APIs definen qué se puede hacer con los datos y con la infraestructura, incluyendo límites de cuota y restricciones legales. 
Ejemplos típicos incluyen no exceder ciertas tasas de llamadas, no almacenar datos más allá de cierto nivel permitido, no revender datos ni el acceso a la API, y cumplir normativas de privacidad aplicables. 
Ignorar estos términos puede tener consecuencias legales o la revocación de claves (o llaves), por lo que deben considerarse parte del diseño de integración. 

# Actividad – “API detective”
Cada equipo selecciona un portal público (Microsoft, Google, GitHub, etc.) y localiza:  
Nombre de la API, enlace a documentación, límites de uso básicos y al menos una cláusula relevante de términos de uso. 
Compartir las restricciones que impactarían más el diseño de un sistema distribuido (por ejemplo, reintentos, volumen de llamadas, etc.). 

# APIs internas, externas y de socios
En una organización hay APIs sólo internas, APIs públicas abiertas y APIs de socios con acuerdos específicos. 
Las internas normalmente priorizan la velocidad de entrega y pueden asumir más conocimiento compartido; las públicas necesitan contratos muy claros, versionado cuidadoso y límites de consumo. 
Las APIs de socios incorporan acuerdos de negocio (seguridad, privacidad, etc.) que afectan la forma de hacer la integración y el monitoreo. 
