# Transición conceptual: de SOAP (WSDL) a REST (OpenAPI) y coexistencia

# De operaciones a recursos

En un contrato SOAP descrito en WSDL, el foco está en **“operaciones”** que se invocan sobre un servicio, cada una con sus mensajes, de entrada y salida, definidos. En REST el foco pasa a ser el **conjunto de recursos expuestos**: entidades como clientes, pedidos o facturas, cada una con una URI y un conjunto estándar de acciones implícitas según el verbo HTTP. Esto implica cambiar el modelo mental: una operación `CrearPedido` se reinterpreta como “crear un recurso pedido con un `POST` a `/pedidos`”, y `ConsultarPedido` como “leer ese recurso con `GET /pedidos/{id}`”. La lógica de negocio puede ser la misma, pero el contrato se organiza alrededor de recursos y representaciones en lugar de llamadas a funciones.

# Coexistencia y envolturas REST sobre SOAP

En muchas organizaciones no se elimina la **infraestructura SOAP existente**, sino que se construyen APIs REST que actúan como **envolturas o adaptadores** lógicos. Un endpoint REST puede recibir una petición JSON ligera, **transformarla internamente** en una llamada SOAP al servicio legado y luego **transformar la respuesta SOAP de regreso a JSON**, sin que el consumidor conozca los detalles. Este patrón permite exponer una cara más moderna y coherente de los servicios existentes, mientras el interior sigue usando SOAP donde sea necesario (por ejemplo, por requisitos regulatorios). En términos conceptuales, **coexistir implica mantener alineados dos contratos: el WSDL del servicio SOAP y el documento OpenAPI de la fachada REST**, para que ambos describan la misma capacidad aunque con estilos distintos.

## Actividad

Se proporciona una lista de tres operaciones SOAP ficticias. Deben escribir para cada una: a) el nombre del recurso REST que la reemplazaría, b) la URI y c) el verbo HTTP. Comentar si alguna operación no encaja bien y qué ajustes de modelado requeriría.

---
1. `ConsultarClientePorId`  
2. `CrearPedidoDeVenta`
3. `GenerarFacturaParaPedido`  
4. (extra) `CancelarFacturaEmitida`

