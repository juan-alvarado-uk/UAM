Clasifico cada escenario suponiendo buenas prácticas de diseño de sistemas distribuidos. [happihacking](https://www.happihacking.com/blog/posts/2025/asynchp/)

***

1. **Validar una contraseña en tiempo real**  
   - Clasificación: **Síncrono**.  
   - Razón: El usuario no puede avanzar sin saber si las credenciales son correctas; se requiere respuesta inmediata para decidir si mostrar el sistema o un error. [dev](https://dev.to/manonaga2188/async-vs-sync-apis-a-developers-complete-guide-11io)

2. **Calcular el costo de envío en checkout**  
   - Clasificación: **Síncrono**.  
   - Razón: El usuario necesita ver el costo total antes de confirmar la compra; la UI debe esperar la respuesta para mostrar el importe final. [openapi](https://openapi.com/blog/synchronous-and-asynchronous-apis)

3. **Registrar un pedido y mostrar confirmación**  
   - Clasificación: **Mixto**.  
   - Razón: El registro mínimo del pedido y validaciones críticas (pago, stock) deben ser síncronas, pero tareas como actualizar analíticos o enviar correos pueden dispararse asíncronamente después. [useparagon](https://www.useparagon.com/blog/synchronous-vs-asynchronous-integration-use-cases)

4. **Generar un reporte mensual pesado de ventas**  
   - Clasificación: **Asíncrono**.  
   - Razón: Es un proceso de larga duración y pesado; conviene lanzarlo en background, devolver un acuse rápido y notificar cuando esté listo (por email, notificación, polling). [nordicapis](https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/)

5. **Enviar un correo de bienvenida al crear una cuenta**  
   - Clasificación: **Asíncrono**.  
   - Razón: El usuario sólo necesita saber que la cuenta se creó; el envío del correo no debe bloquear la respuesta y puede fallar/reintentar sin afectar la creación de cuenta. [openapi](https://openapi.com/blog/synchronous-and-asynchronous-apis)

6. **Actualizar el stock en tiempo real tras confirmar un pago**  
   - Clasificación: **Mixto**.  
   - Razón: La decisión de confirmar el pedido debe asegurar que no se sobrevende (parte síncrona), pero la propagación del stock a otros canales o sistemas puede hacerse por eventos/colas en background. [appseconnect](https://www.appseconnect.com/how-ecommerce-brands-automate-inventory-order-management-sync-across-systems/)

7. **Procesar una importación masiva de clientes desde CSV**  
   - Clasificación: **Asíncrono**.  
   - Razón: Involucra miles de registros y puede tardar mucho; se inicia el proceso, se devuelve un “job id” y se consulta/avisa cuando termine para no bloquear la UI ni timeouts. [nordicapis](https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/)

8. **Mostrar el balance actualizado de una cartera digital al abrir la app**  
   - Clasificación: **Síncrono**.  
   - Razón: El usuario necesita ver un saldo confiable antes de tomar decisiones (enviar dinero, invertir); la llamada debe devolver el dato actual o casi actual en el momento. [cloud.google](https://cloud.google.com/blog/topics/developers-practitioners/differences-between-synchronous-web-apis-and-asynchronous-stateful-apis/)

9. **Enviar notificaciones push simultáneas ante inicio de sesión sospechoso**  
   - Clasificación: **Asíncrono**.  
   - Razón: La autenticación ya se resolvió; el disparo de notificaciones a múltiples dispositivos es secundario y puede orquestarse por colas/eventos con reintentos, sin bloquear el login. [dev](https://dev.to/ayaninsights/mastering-synchronous-vs-asynchronous-integration-patterns-in-salesforce-5ao8)

10. **Recalcular recomendaciones personalizadas tras una compra o nueva visualización**  
    - Clasificación: **Mixto**.  
    - Razón: Puedes mostrar recomendaciones “buenas pero no perfectas” de forma síncrona usando un modelo previo y lanzar un recalculo más costoso de forma asíncrona para futuras sesiones/páginas. [commercev3](https://commercev3.com/resources/blog/real-time-sync-strategies-for-ecommerce-inventory-management/)

¿Quieres que convierta esto en una mini-tabla corta en markdown para pegarla directo en tus diapositivas?