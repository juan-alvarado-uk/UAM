# Práctica: Creación de un servicio web SOAP con JAX‑WS y Maven

En esta práctica se mostrará paso a paso cómo crear, implementar y probar un servicio web SOAP en Java usando IntelliJ IDEA, Maven y JAX‑WS.

# 1. Preparación del entorno

## 1.1 Crear cuenta en JetBrains

- Crear una cuenta en JetBrains usando su cuenta institucional:  
  https://www.jetbrains.com/  

Esto sirve para tener de una licencia educativa gratuita para IntelliJ IDEA y otras herramientas de JetBrains. En esta práctica usaremos IntelliJ IDEA para que funcione bien entre diferentes sistemas operativos.

## 1.2 Instalar IntelliJ IDEA

- Descargar IntelliJ IDEA Ultimate
  - Para esto, inicia sesión con tu cuenta de JetBrains y haz click en el ícono de usuario en la parte superior derecha de la pantalla.
  - En las herramientas disponibles selecciona IntelliJ IDEA Ultimate y descarga la versión compatible con tu sistema operativo.
- Instalar IntelliJ IDEA siguiendo las instrucciones de instalación del sitio de JetBrains o de tu descarga.

## 1.3 Activar la licencia educativa

- Abrir IntelliJ IDEA.  
- Ir al menú `Help` → `Manage subscriptions`.  
- Iniciar sesión con tu cuenta de JetBrains.  

Con esto activarás la licencia educativa y desbloquearás todas las funcionalidades del IDE.

# 2. Crear el proyecto Maven base

## 2.1 Crear un nuevo proyecto Maven

- En IntelliJ IDEA, elegir `New Project`.  
- En el panel izquierdo, seleccionar la opción de **Maven Archetype**. 
- En el panel derecho, establecer el nombre del proyecto como `soap`.  
- En la sección de _Archetype_, seleccionar `maven-archetype-quickstart`.  
- Hacer clic en `Create` (o `Finish`).

Con esto usamos el archetype `maven-archetype-quickstart` para generar automáticamente la estructura mínima de un proyecto Java con Maven, evitando crear carpetas y archivos a mano.

## 2.2 Revisar la estructura inicial del proyecto

- Verificar que el proyecto contiene:
  - El directorio `src`
  - El archivo `pom.xml` (archivo de configuración de Maven)  
- Dentro de `src`, observar que existen:
  - `src/main/java` (código fuente principal)
  - `src/test/java` (código de pruebas; en esta práctica no se utilizará)

Esto nos da la estructura estándar de un proyecto Maven, donde `pom.xml` define dependencias y plugins, y la carpeta `src/main` contiene el código fuente del proyecto.

## 2.3 Crear la carpeta para el WSDL

- Dentro de `src/main`, crear la ruta de directorios: `resources/wsdl`.  
  - Es decir: `src/main/resources/wsdl`.  
- Copiar a la carpeta `wsdl` el archivo WSDL proporcionado para la práctica.

Esto sirve para tener el archivo WSDL dentro de los recursos del proyecto para que Maven y el plugin de JAX‑WS puedan localizarlo y generar código Java necesario para el servicio SOAP.

# 3. Configurar Maven y generar clases a partir del WSDL

## 3.1 Reemplazar el contenido de `pom.xml`

- Abrir el archivo `pom.xml` en el editor de IntelliJ IDEA.  
- Reemplazar todo su contenido por el siguiente:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>org.example</groupId>
  <artifactId>soap</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>soap</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
    <!-- API JAX-WS (javax.xml.ws.*) -->
    <dependency>
      <groupId>javax.xml.ws</groupId>
      <artifactId>jaxws-api</artifactId>
      <version>2.3.1</version>
    </dependency>

    <!-- Implementación Metro (runtime JAX-WS) -->
    <dependency>
      <groupId>com.sun.xml.ws</groupId>
      <artifactId>rt</artifactId>
      <version>2.3.7</version>
      <exclusions>
        <exclusion>
          <groupId>com.sun.mail</groupId>
          <artifactId>jakarta.mail</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- Plugin para ejecutar wsimport desde Maven -->
      <plugin>
        <groupId>com.sun.xml.ws</groupId>
        <artifactId>jaxws-maven-plugin</artifactId>
        <version>2.3.7</version>

        <executions>
          <execution>
            <id>wsimport-hello</id>
            <goals>
              <goal>wsimport</goal>
            </goals>
            <!-- Se ejecuta antes de compilar -->
            <phase>generate-sources</phase>

            <configuration>
              <!-- Ruta al WSDL dentro del proyecto -->
              <wsdlFiles>
                <wsdlFile>
                  ${project.basedir}/src/main/resources/wsdl/HelloService.wsdl
                </wsdlFile>
              </wsdlFiles>

              <!-- Paquete Java para nuestras clases generadas -->
              <packageName>com.ejemplo.hello</packageName>

              <!-- Directorio donde se colocan las fuentes auto-generadas -->
              <sourceDestDir>
                ${project.build.directory}/generated-sources/wsimport
              </sourceDestDir>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- Plugin estándar de compilación -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.11.0</version>
        <configuration>
          <release>17</release>
        </configuration>
      </plugin>
    </plugins>
  </build>

</project>
```

**Propósito:**  
- Declarar las dependencias de JAX‑WS (API y runtime Metro) que permiten trabajar con servicios SOAP en Java.  
- Configurar el plugin `jaxws-maven-plugin` para ejecutar `wsimport` durante la fase `generate-sources`, tomando el WSDL del proyecto y generando las clases Java necesarias (interfaces, requests, responses, etc.).

## 3.2 Sincronizar los cambios de Maven

- En IntelliJ, en la pestaña del `pom.xml`, localizar el ícono de Maven (una `m` con flechas formando un bucle) en la parte superior derecha o en la ventana de Maven.  
- Hacer clic en el ícono para **sincronizar** el proyecto con el nuevo contenido de `pom.xml`.  

Esto es para indicar a IntelliJ que vuelva a leer la configuración de Maven, descargue las nuevas dependencias configuradas en el archivo `pom.xml` y reconfigure el proyecto de acuerdo con ellas. En este paso podría solicitar la configuración de plugins y esto implicará una instalación (jakarta...). Hay que aceptar la instalación para continuar. 

## 3.3 Abrir la ventana de Maven

- Ir a `View` → `Tool Windows` → `Maven`.  
- En la ventana de Maven (generalmente al lado derecho), localizar el proyecto actual y desplegar sus opciones.  
- Dentro de las opciones del proyecto, desplegar la sección `Lifecycle`.  

Utilizamos la interfaz de Maven integrada en IntelliJ para ejecutar fases del ciclo de vida (como `clean` y `compile`) sin usar la línea de comandos.

## 3.4 Ejecutar `clean` y `compile`

- En la sección `Lifecycle`:
  - Hacer doble clic en `clean`.  
  - Hacer doble clic en `compile`.  
 
- `clean`: para borrar resultados de compilaciones anteriores y garantizar que el proyecto se recompila desde cero.  
- `compile`: durante esta fase, el plugin `jaxws-maven-plugin` ejecutará el objetivo `wsimport` en la fase `generate-sources`, generando el código Java a partir del WSDL y compilando después todo el código.

## 3.5 Revisar el código generado

- Después de compilar, verificar que se ha creado el directorio:  
  `target/generated-sources/wsimport`  
- Confirmar que dentro de ese directorio están las clases Java generadas para el servicio.  
- No mover esas clases de esa carpeta, y tampoco las clases compiladas de `target/classes`.  

**Nota**: Este código es generado automáticamente a partir del WSDL y Maven lo gestiona; no se debe editar ni mover manualmente, porque se regenerará cada vez que se ejecute `wsimport`.

## 3.6 Identificar la interfaz generada

- Buscar y abrir el archivo `HelloPortType.java` dentro de las clases generadas.  
- Observar que esta interfaz contiene las firmas de los métodos que representan las operaciones definidas en el WSDL (por ejemplo, `sayHello`, `sayGoodbye`).  

`HelloPortType.java` es la interfaz que describe el contrato del servicio SOAP: qué operaciones expone, qué parámetros recibe y qué respuestas devuelve.

# 4. Implementar la lógica del servicio

## 4.1 Crear el paquete de implementación

- En `src/main/java`, crear la ruta de subdirectorios `com/ejemplo/hello`.  
  - En IntelliJ, se verá como el paquete `com.ejemplo.hello`.  

Esto sirve para crear el paquete donde se ubicará la implementación del servicio y otras clases relacionadas, alineado con el `packageName` configurado en el plugin de JAX‑WS.

## 4.2 Crear la clase `HelloPortTypeImpl`

- En el paquete `com.ejemplo.hello`, crear una nueva clase Java con el nombre `HelloPortTypeImpl.java`.  
- Colocar el siguiente contenido:

```java
package com.ejemplo.hello;

import javax.jws.WebService;

@WebService(
        serviceName = "HelloService",
        portName = "HelloPort",
        targetNamespace = "http://www.examples.com/wsdl/HelloService.wsdl",
        endpointInterface = "com.ejemplo.hello.HelloPortType"
)
public class HelloPortTypeImpl implements HelloPortType {

    @Override
    public SayHelloResponse sayHello(SayHelloRequest parameters) {
        SayHelloResponse resp = new SayHelloResponse();
        String name = parameters.getFirstName();
        resp.setGreeting("Hola " + name + "!" );
        return resp;
    }

    @Override
    public SayGoodbyeResponse sayGoodbye(SayGoodbyeRequest parameters) {
        SayGoodbyeResponse resp = new SayGoodbyeResponse();
        String name = parameters.getFirstName();
        resp.setFarewell("Adiós " + name + "!");
        return resp;
    }
}
```

**Propósito:**  
- Implementar la interfaz generada `HelloPortType`, con la lógica de negocio real del servicio (en este caso qué texto devolver al saludar y despedir).  
- Mediante la anotación `@WebService`, indicar a JAX‑WS qué interfaz se está implementando (`endpointInterface`), qué nombre tiene el servicio, el puerto y el espacio de nombres, de modo que el runtime pueda publicar este servicio de acuerdo con el WSDL.

## 4.3 Resolver errores de referencias (si aparecen)

- Es posible que, tras crear `HelloPortTypeImpl`, aparezcan errores en el código porque IntelliJ aún no reconoce correctamente las clases generadas y las dependencias Maven.  
- Ir a la ventana de Maven.  
- En la barra superior de la ventana de Maven, hacer clic en el ícono de flechas circulares y elegir `Reload All Maven Projects`.  

Lo anterior es para forzar a IntelliJ a recargar la configuración y las dependencias de Maven, de modo que reconozca las clases generadas por `wsimport` y desaparezcan los errores de referencia.

# 5. Crear el servidor y el cliente SOAP

## 5.1 Crear la clase `HelloServer`

- En el paquete `com.ejemplo.hello`, crear una nueva clase Java llamada `HelloServer.java`.  
- Usar el siguiente contenido:

```java
package com.ejemplo.hello;

import javax.xml.ws.Endpoint;

public class HelloServer {

    public static void main(String[] args) {
        String address = "http://localhost:8080/HelloService";

        HelloPortTypeImpl implementacion = new HelloPortTypeImpl();

        Endpoint.publish(address, implementacion);

        System.out.println("HelloService publicado en " + address);
        System.out.println("Pulsa Ctrl+C para detener.");
    }
}
```

Esto sirve para...  
- Publicar el servicio SOAP en una URL local (`http://localhost:8080/HelloService`) usando la clase `Endpoint` de JAX‑WS.  
- Asociar la URL con la implementación `HelloPortTypeImpl`, de modo que las peticiones SOAP que lleguen a esa dirección se atiendan con la lógica programada.

## 5.2 Crear la clase `HelloClient`

- En el mismo paquete `com.ejemplo.hello`, crear una nueva clase Java llamada `HelloClient.java`.  
- Usar el siguiente contenido:

```java
package com.ejemplo.hello;

public class HelloClient {

    public static void main(String[] args) {
        // Crear el "service" a partir de la clase generada
        HelloService service = new HelloService();

        // Obtener el port que implementa HelloPortType
        HelloPortType port = service.getHelloPort();

        // Construir solicitud sayHello
        SayHelloRequest helloReq = new SayHelloRequest();
        helloReq.setFirstName("Juan");

        SayHelloResponse helloResp = port.sayHello(helloReq);
        System.out.println("Respuesta sayHello: " + helloResp.getGreeting());

        // Construir solicitud sayGoodbye
        SayGoodbyeRequest byeReq = new SayGoodbyeRequest();
        byeReq.setFirstName("Juan");

        SayGoodbyeResponse byeResp = port.sayGoodbye(byeReq);
        System.out.println("Respuesta sayGoodbye: " + byeResp.getFarewell());
    }
}
```

Esto sirve para...  
- Crear un cliente Java que use las clases generadas (`HelloService`, `HelloPortType`, `SayHelloRequest`, etc.) para consumir el servicio SOAP publicado por `HelloServer`.  
- Construir solicitudes para las operaciones `sayHello` y `sayGoodbye` y mostrar en la consola las respuestas devueltas por el servicio.

## 5.3 Guardar cambios y recompilar

- Guardar todos los archivos Java modificados o creados.  
- En la ventana de Maven, en `Lifecycle`, hacer doble clic nuevamente en `compile`.  

Esto es para recompilar el proyecto incluyendo las nuevas clases de implementación, servidor y cliente, asegurándose de que no haya errores de compilación antes de ejecutar.

# 6. Ejecutar y probar el servicio SOAP

## 6.1 Ejecutar el servidor

- Abrir la pestaña del archivo `HelloServer.java`.  
- Hacer clic en el ícono de ejecución (triángulo verde) junto a la declaración de `main`, y seleccionar `Run HelloServer.main()`.  
- Se abrirá una ventana o pestaña de terminal dentro de IntelliJ que mostrará algo similar a:

  ```
  HelloService publicado en http://localhost:8080/HelloService
  Pulsa Ctrl+C para detener.
  ```

Con esto ponemos en marcha el servidor que expone el servicio SOAP; mientras esta consola esté activa, el servicio estará disponible para que otros clientes (como `HelloClient`) lo consuman.

**Nota:** cualquier cambio en las clases generadas o en la implementación del servicio requerirá detener el servidor y volver a ejecutarlo para aplicar los cambios.

## 6.2 Ejecutar el cliente

- Con el servidor aún en ejecución, abrir la pestaña del archivo `HelloClient.java`.  
- Hacer clic en el ícono de ejecución y seleccionar `Run HelloClient.main()`.  
- Se abrirá otra pestaña de terminal (además de la del servidor) que debería mostrar:

  ```
  Respuesta sayHello: Hola Juan!
  Respuesta sayGoodbye: Adiós Juan!
  Process finished with exit code 0
  ```

Con esto verificamos que el cliente puede conectarse correctamente al servicio SOAP, enviar mensajes según el contrato definido en el WSDL y recibir respuestas válidas de la implementación del servidor.

## 6.3 Algunas modificaciones

Nuestra implementación SOAP ya funciona bien, pero analizando el comportamiento en pruebas de esta implementación, se ha decidido que las operaciones `sayHello` y `sayGoodbye`, además del `firstname`, pidan el `lastname`. 

También se ha pedido que se compruebe si `firstname` y `lastname` llegan vacíos (o nulos), en cuyo caso el sistema lo detecte y pueda enviar un saludo y despedida que haga esta situación evidente, por ejemplo, "¡Hola usuario anónimo!". 

En caso de que solo alguno de los nombres esté presente saludar o despedirse 
1) si solo `firstname`, saludar o despedirse coloquialmente, 
2) si solo `lastname`, saludar o despedirse formalmente

Si están ambos, saludar coloquialmente y usar ambos nombres. 
