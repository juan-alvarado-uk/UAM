# Síncrono vs asíncrono, colas y eventos
# Integración síncrona
En integración síncrona un cliente envía una petición y espera la respuesta para continuar, típico en HTTP/REST. 
Es adecuado cuando se necesita feedback inmediato (consultar saldo, validar credenciales) y la latencia es aceptable y predecible. 
Sin embargo, acopla la disponibilidad del cliente y el servidor: si el servicio está caído, la operación falla en ese momento. 

# Integración asíncrona: colas y eventos
En integración asíncrona, un productor envía un mensaje o evento a una cola o bus, y los consumidores lo procesan más tarde sin bloquear al emisor. 
Esto desacopla temporalmente a los sistemas, mejora tolerancia a fallas y permite procesar picos de carga de forma más suave. 
Tecnologías habituales incluyen colas de mensajes, logs de eventos y servicios de mensajería en la nube, pero el concepto se mantiene incluso con herramientas sencillas.

# Actividad – “Clasifica el escenario”
En equipos, etiqueten cada escenario siguiente como “síncrono”, “asíncrono” o “mixto (REST + eventos)” y preparen una justificación de su decisión. 
Discutir dónde cambiarían de enfoque si la carga o los requerimientos de experiencia de usuario aumentan. 

- **Validar una contraseña** cuando el usuario escribe sus credenciales en el formulario de login. 

- **Calcular el costo de envío** cuando el usuario introduce su código postal en la pantalla de checkout. 

- **Registrar un pedido y mostrar confirmación** cuando el usuario presiona “Comprar ahora”. 

- **Generar un reporte mensual pesado** de ventas (miles de filas) que tarda varios minutos en calcularse. 

- **Enviar un correo de bienvenida** después de que un usuario crea su cuenta en la plataforma. 

- **Actualizar el stock** cuando se confirma un pago, para evitar sobrevender productos en la tienda en línea. 

- **Procesar una importación masiva de clientes desde un archivo CSV** subido por un administrador (decenas de miles de registros). 

- **Mostrar el balance actualizado de una cartera digital** cuando el usuario abre la aplicación.

- **Enviar notificaciones push simultáneas** a todos los dispositivos de un usuario cuando se detecta un inicio de sesión desde un país inusual. 

- **Recalcular recomendaciones personalizadas** (productos, cursos, artículos) cada vez que el usuario completa una compra o ve nuevo contenido.


# API-first y event-driven
API-first (que ya hemos mencionado) implica diseñar primero los contratos de API (incluyendo semántica) antes de implementar, de modo que sirvan de base común para equipos de desarrollo y stakeholders externos. 
La arquitectura dirigida por eventos (event-driven) enfatiza que los cambios significativos del sistema se publican como eventos, que otros servicios observan y manejan de forma reactiva. 
Juntas, estas ideas permiten sistemas más modulares, escalables y alineados con el negocio, pero exigen mayor disciplina en diseño de contratos y en gobernanza. 
