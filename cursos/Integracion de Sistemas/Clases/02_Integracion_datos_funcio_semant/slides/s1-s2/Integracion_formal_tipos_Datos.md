#! Integración de sistemas   
##! Integración Formal, Tipos de integración

# Visión general de la integración

En una organización típica conviven múltiples aplicaciones: ERP, CRM, portal web, apps móviles, sistemas legados, etc., cada una con su propia base de datos y lógica de negocio. La **integración** de sistemas busca que todos esos componentes se coordinen como si fueran un solo sistema coherente, sin que el usuario tenga que saber qué aplicación está "detrás" de cada operación. Esto implica que los sistemas puedan intercambiar datos, invocar funciones remotas y compartir una interpretación común de la información clave del negocio. 

# Tipos de integración: datos, funcional y semántica

Hay tres categorías básicas para clasificar los problemas de integración. 
- **Integración de datos**: cuando el reto principal es mover o sincronizar datos entre fuentes distintas, como bases relacionales, archivos planos o APIs de terceros. 
- **Integración funcional**: cuando el objetivo es coordinar funciones o servicios de sistemas diferentes para construir procesos de negocio completos, por ejemplo, un flujo de "pago en línea" que llama a un procesador bancario externo. 
- **Integración semántica**: cuando hay que alinear el significado de los datos, resolviendo diferencias en vocabulario, estructura o modelos conceptuales entre aplicaciones. 


# Integración de datos

La integración de **datos** se centra en unificar información dispersa para que se pueda consultar o analizar como un todo. Esto incluye tareas como consolidar catálogos de clientes que están duplicados en varios sistemas, o mantener sincronizados inventarios entre la tienda en línea y el sistema de almacén. Las soluciones típicas incluyen procesos ETL (Extract, Transform, Load), replicación de bases de datos y APIs de lectura/escritura que exponen vistas unificadas. Aquí nos interesa distinguir cuándo el problema principal es “datos incoherentes” frente a otros tipos de problemas de integración.

## Actividad: Mapa rápido de integraciones de datos

En equipos, elijan un contexto cercano (la universidad, un e‑commerce simple, un hospital pequeño). Enumeren al menos cinco sistemas o aplicaciones que podrían existir en ese contexto y dibujen flechas cuando haya un intercambio de datos claro (por ejemplo, calificaciones de un LMS hacia el sistema institucional). Marquen con un color las flechas donde el **principal reto sería que los datos sean consistentes** (mismo alumno, mismos IDs, mismas fechas). 


# Integración funcional

La integración **funcional** se trata de coordinar capacidades de distintos sistemas para lograr un flujo de negocio completo. Por ejemplo, un flujo de "compra en línea" puede orquestar funciones de catálogo, carrito, pagos, facturación y envío, cada una ofrecida por sistemas diferentes. En este escenario, el foco no está solo en copiar datos, sino en invocar operaciones remotas (servicios) con entradas y salidas bien definidas. Estilos como SOA y microservicios son variaciones de cómo organizar esa integración funcional.


# Integración semántica

La integración **semántica** intenta resolver el problema de que “no hablamos el mismo idioma” aunque los sistemas intercambien datos. Dos aplicaciones pueden usar el campo “cliente” con significados distintos, o representar direcciones, productos o diagnósticos médicos con modelos incompatibles. Las técnicas semánticas introducen modelos compartidos (ontologías, vocabularios controlados, esquemas bien definidos) para que el dato pueda interpretarse de la misma manera en contextos diferentes. Es importante reconocer que sin una capa semántica, integrar solo por campos y tipos puede generar errores sutiles. 


# Relación entre los tres tipos

En proyectos reales, los tres tipos de integración aparecen mezclados. Un portal de autoservicio para clientes puede requerir: datos integrados (historial de compras), funciones integradas (proceso de pago y entrega) y semántica común (qué significa “cliente activo”, “pedido entregado” o “saldo vencido”). Identificar explícitamente qué tipo de integración predomina en cada parte del proyecto ayuda a elegir tecnologías y estrategias adecuadas, como priorizar mapeos de datos, orquestación de servicios o alineación de vocabularios. 


# Práctica

**Detectando tipos de integración en un caso sencillo**

En esta práctica se analizará un escenario de una pequeña empresa y se etiquetarán las necesidades de integración como de datos, funcionales o semánticas. El trabajo se puede realizar con herramientas colaborativas digitales. 
