# Análisis y diseño para integración

## Fuentes de datos y límites de sistemas

En una integración real es muy importante identificar qué sistemas participan, qué tipo de datos manejan y quién es responsable de cada entidad de negocio (cliente, pedido, factura, etc.). Esto implica listar sistemas origen (por ejemplo, e‑commerce, ERP, facturación, inventarios) y determinar para cada uno qué operaciones ofrece (**consultar**, **crear**, **actualizar**) y qué tan “oficiales” son sus datos. A partir de esta identificación se definen los **puntos de integración**: qué APIs REST se deben exponer, qué servicios existentes se reutilizarán (incluyendo posibles servicios SOAP) y qué datos deben sincronizarse o solo consultarse bajo demanda. Tener claros estos límites evita que varias APIs modifiquen el mismo dato de forma descoordinada, lo que generaría inconsistencias difíciles de resolver.

**Actividad**  
Dibujar un mapa de sistemas para un escenario e‑commerce + facturación + inventarios con cajas con nombres de sistemas y flechas indicando qué datos fluyen entre ellos. Analizar casos como el siguiente: “si hay conflicto en el nombre de un cliente, ¿qué sistema gana?”, con ello determinar quien es el sistema “dueño” del dato.

## Latencia y granularidad de servicios

La latencia aceptable entre sistemas condiciona cuán “finas” o “gruesas” deben ser las operaciones expuestas. Si un flujo requiere respuestas casi en **tiempo real** (por ejemplo, validación de pago en línea), conviene exponer servicios relativamente **compactos y evitar secuencias largas** de llamadas síncronas entre muchos sistemas, ya que cada salto añade retraso. Cuando la **latencia tolerable es mayor** (por ejemplo, integración nocturna de reportes), se puede optar por **llamadas más pesadas** o incluso por mecanismos por lotes. En el diseño de APIs REST, esta reflexión se traduce en decidir si un cliente hace **muchas llamadas pequeñas o menos llamadas más ricas**, equilibrando simplicidad, rendimiento y claridad.

## Requisitos de seguridad en la integración

Desde el análisis se deben capturar requerimientos de **confidencialidad** (qué datos deben viajar siempre cifrados), **integridad** (qué mensajes necesitan firma o verificación) y **trazabilidad** (qué operaciones deben dejar rastro detallado). Para cada flujo de integración se puede describir quién llama a quién, qué identidad usa y qué información mínima se necesita para autorizar la operación, sin entrar aún en protocolos concretos. Esto sirve de base para más adelante elegir mecanismos específicos de autenticación y autorización en las APIs REST o, donde corresponda, perfiles de seguridad en servicios SOAP existentes.

