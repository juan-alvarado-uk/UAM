# Práctica: Instalación de MongoDB y desarrollo de un sistema documental básico en Ubuntu Server dentro de VirtualBox

Esta práctica tiene como propósito construir un entorno funcional de trabajo para bases de datos documentales sobre una máquina virtual con Ubuntu Server en VirtualBox, instalar MongoDB Community Edition mediante paquetes oficiales para Ubuntu, verificar su operación y desarrollar un servicio web mínimo con Express.js que almacene y consulte documentos JSON desde el host. MongoDB distribuye paquetes oficiales para Ubuntu y su instalación recomendada en Linux se realiza precisamente mediante esos paquetes. 

***

## Requisitos previos

Antes de iniciar, se requiere contar con lo siguiente:

- VirtualBox instalado.
- Una imagen ISO de Ubuntu compatible con la arquitectura del equipo.
- Permisos para instalar software en el host y en la máquina virtual.
- Acceso a terminal en el host.
- Conexión a internet para instalar paquetes en Ubuntu.

***

## Parte 1. Preparación de red en VirtualBox

En esta práctica se usará una sola máquina virtual. La VM tendrá dos interfaces de red:

- Una red **NAT** para tener salida a internet y poder instalar paquetes.
- Una red **solo-anfitrión** para permitir la comunicación directa entre el host y la máquina virtual.

### 1. Descargar la imagen de Ubuntu

Descargar la imagen ISO de Ubuntu adecuada para el equipo anfitrión:

- Si el equipo usa procesador Apple Silicon, descargar la versión ARM de Ubuntu.
- Si el equipo usa procesador Intel o AMD, descargar la versión de 64 bits correspondiente.

La arquitectura de la ISO debe coincidir con la arquitectura soportada por el equipo y por VirtualBox.

### 2. Crear la red NAT

1. Abrir VirtualBox.
2. Ir a **Herramientas** o **Preferencias**, según la versión instalada.
3. Entrar al apartado **Red**.
4. Abrir la sección **Redes NAT**.
5. Crear una nueva red NAT con los siguientes parámetros:
   - Nombre: `rednat-bd` (o el default)
   - Prefijo IPv4: `192.168.50.0/24`
   - DHCP: habilitado
6. Guardar la configuración.

La red NAT permitirá que la máquina virtual salga a internet para descargar e instalar paquetes del sistema operativo.

### 3. Crear la red solo-anfitrión

1. En VirtualBox, ir nuevamente al apartado **Red**.
2. Abrir la sección **Redes solo-anfitrión**.
3. Crear una nueva red solo-anfitrión con los todos los parámetros de default
4. Guardar la configuración.

La red solo-anfitrión permitirá la comunicación directa entre el host y la máquina virtual sin depender de internet.

***

## Parte 2. Creación de la máquina virtual

### 4. Crear la única VM

Crear una máquina virtual con las siguientes características:

- Nombre sugerido: `db-vm`
- Memoria RAM: 2 GB
- Disco duro virtual: 20 GB, asignación dinámica
- Medio de instalación: la ISO de Ubuntu descargada previamente.

Completar la instalación de Ubuntu y crear un usuario con contraseña. Tomar nota del nombre del usuario, ya que se utilizará más adelante para conectarse por SSH.

### 5. Configurar los adaptadores de red de la VM

Con la máquina virtual apagada:

1. Entrar a la configuración de la VM.
2. Abrir la sección **Red**.
3. Configurar el **Adaptador 1**:
   - Habilitado.
   - Conectado a: **Red NAT**.
   - Nombre: <La que fue creada previamente>.
4. Configurar el **Adaptador 2**:
   - Habilitado.
   - Conectado a: **Adaptador solo-anfitrión**.
   - Nombre: <La que fue creada previamente>.
5. Guardar los cambios.

La VM usará el adaptador NAT para internet y el adaptador solo-anfitrión para comunicarse con el host.

***

## Parte 3. Verificación de conectividad

### 6. Iniciar la VM y revisar direcciones IP

Iniciar la máquina virtual y abrir una terminal. Ejecutar:

```bash
ip addr
```

Identificar dos direcciones:

- La dirección asociada al adaptador conectado a la red NAT.
- La dirección asociada al adaptador conectado a la red solo-anfitrión, que debe pertenecer al rango `192.168.56.x`.

Anotar la IP de la red solo-anfitrión, ya que se utilizará para la comunicación entre host y VM.

### 7. Probar conectividad entre host y VM

Desde la VM, hacer ping a la IP del host (192.168.56.1) en la red solo-anfitrión:

```bash
ping 192.168.56.1
```

Desde el host, hacer ping a la IP de la VM en la red solo-anfitrión:

```bash
ping 192.168.56.X
```

Sustituir `192.168.56.X` por la IP real obtenida por la VM. La comunicación entre ambos debe funcionar correctamente.

***

## Parte 4. Instalación y configuración básica de SSH en la VM

### 8. Actualizar paquetes del sistema

En la VM, ejecutar:

```bash
sudo apt update
sudo apt upgrade -y
```

### 9. Instalar el servidor SSH

En la VM, ejecutar:

```bash
sudo apt install openssh-server -y
```

### 10. Habilitar e iniciar SSH

En la VM, ejecutar:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh
```

Verificar que el estado del servicio aparezca como `active (running)`.

### 11. Probar acceso por SSH desde el host

Desde el host, abrir una terminal y ejecutar:

```bash
ssh usuario@192.168.56.X
```

Sustituir `usuario` por el nombre del usuario creado en Ubuntu y `192.168.56.X` por la IP host-only de la VM.

***

## Parte 5. Propósito técnico de la práctica

**Definición.** Una base documental almacena información como documentos con estructura flexible, normalmente JSON, lo que permite representar objetos con listas, subdocumentos y atributos variables de forma más natural que una tabla rígida en ciertos escenarios.  

***

En esta práctica se construirá un entorno donde la VM funciona como servidor de base de datos y servidor de aplicación, mientras el host opera como equipo cliente. La separación entre host y VM permite observar una forma básica de despliegue distribuido: un nodo ofrece servicio y otro lo consume por red. 

***

## Parte 6. Instalación de MongoDB Community Edition en Ubuntu Server

**Definición.** MongoDB es una base de datos documental NoSQL que trabaja con documentos tipo BSON, muy cercanos conceptualmente a JSON, y MongoDB recomienda en Ubuntu usar sus paquetes oficiales `mongodb-org` mantenidos para este sistema. 

***

### 12. Confirmar la versión de Ubuntu

En la VM, verificar primero la versión instalada:

```bash
cat /etc/os-release
```

***

Tomar nota de la versión LTS de Ubuntu, ya que la instalación oficial de MongoDB Community Edition en Ubuntu está documentada para versiones LTS soportadas mediante el administrador de paquetes `apt`. 

***

### 13. Instalar utilidades necesarias (si fuera necesario)

Ejecutar:

```bash
sudo apt update
sudo apt install -y gnupg curl
```

Estas utilidades permiten agregar la llave GPG del repositorio oficial y registrar el repositorio de MongoDB en el sistema. La documentación oficial de MongoDB en Ubuntu parte precisamente de la incorporación de su repositorio y de la instalación del paquete `mongodb-org`. 

***

### 14. Agregar la llave GPG oficial de MongoDB

Ejecutar:

```bash
curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
--dearmor
```

MongoDB publica una guía oficial para instalar MongoDB Community Edition en Ubuntu LTS usando el paquete oficial y su repositorio firmado. 

***

### 15. Registrar el repositorio oficial de MongoDB

```bash
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
```

***

### 16. Actualizar índice de paquetes

Ejecutar:

```bash
sudo apt update
```

Si el repositorio se agregó correctamente, el sistema debe leer también el origen de MongoDB.

***

### 17. Instalar MongoDB

Ejecutar:

```bash
sudo apt install -y mongodb-org
```

La instalación oficial de MongoDB Community Edition en Ubuntu usa el paquete `mongodb-org` mantenido por MongoDB. 

***

### 18. Habilitar e iniciar el servicio de MongoDB

Ejecutar:

```bash
sudo systemctl enable mongod
```
Se requiere autenticar con el usuario vboxuser para los dos siguientes casos
- Authentication is required to manage system service or unit files.
- Authentication is required to reload the systemd state.

```bash
sudo systemctl start mongod
sudo systemctl status mongod
```

El servicio debe aparecer como `active (running)` cuando la instalación se realizó correctamente. La documentación oficial de MongoDB en Ubuntu usa el servicio `mongod` como proceso principal del servidor. 

***

### 19. Verificar que MongoDB responde localmente

Ejecutar una de las siguientes opciones, según lo que tenga disponible la instalación:

```bash
mongosh
```

o consultar estado con:

```bash
sudo systemctl status mongod
```

Dentro de `mongosh`, probar:

```javascript
db.runCommand({ ping: 1 })
```

La respuesta esperada incluye `"ok" : 1`, lo que indica que el servidor está activo y respondiendo a comandos.

***

## Parte 7. Preparación inicial de la base de datos documental

**Definición.** En una base documental, una colección agrupa documentos relacionados, pero no obliga a que todos tengan exactamente la misma forma. Esto permite almacenar variaciones naturales del dominio sin rediseñar tablas cada vez que aparece un nuevo atributo. 

***

### 20. Crear una base de datos para la práctica

Entrar a la consola:

```bash
mongosh
```

Crear y seleccionar una base:

```javascript
use practica_nosql
```

***

### 21. Insertar documentos de ejemplo

Crear una colección llamada `productos` con documentos de estructura variable:

```javascript
db.productos.insertMany([
  {
    nombre: "Laptop",
    categoria: "electronica",
    precio: 18999,
    atributos: {
      ram: "16 GB",
      procesador: "Ryzen 7",
      almacenamiento: "1 TB SSD"
    },
    etiquetas: ["computo", "oficina", "estudiantes"]
  },
  {
    nombre: "Tenis deportivos",
    categoria: "calzado",
    precio: 1299,
    atributos: {
      talla: 27,
      color: "negro",
      material: "malla"
    },
    etiquetas: ["deporte", "moda"]
  },
  {
    nombre: "Cereal integral",
    categoria: "alimentos",
    precio: 78,
    atributos: {
      peso: "500 g",
      caducidad: "2026-12-31",
      ingredientes: ["avena", "trigo", "miel"]
    },
    etiquetas: ["despensa", "salud"]
  }
])
```

***

Estos documentos muestran una ventaja central de los datos semiestructurados: comparten una base común, pero cada uno conserva atributos específicos del tipo de producto sin obligar a columnas vacías o tablas auxiliares excesivas. Ese problema ya había sido señalado en el curso al discutir catálogos con ropa, dispositivos y alimentos con propiedades distintas. 

***

### 22. Consultar los documentos insertados

Ejecutar:

```javascript
db.productos.find().pretty()
```

Consultar solo electrónicos:

```javascript
db.productos.find({ categoria: "electronica" }).pretty()
```

Consultar por un atributo anidado:

```javascript
db.productos.find({ "atributos.ram": "16 GB" }).pretty()
```

Consultar por una etiqueta:

```javascript
db.productos.find({ etiquetas: "deporte" }).pretty()
```

***

### 23. Insertar documentos con estructura diferente

Agregar ahora una colección `usuarios`:

```javascript
db.usuarios.insertMany([
  {
    nombre: "Ana",
    correo: "ana@ejemplo.com",
    roles: ["alumna", "becaria"],
    configuracion: {
      notificaciones: true,
      idioma: "es"
    }
  },
  {
    nombre: "Luis",
    correo: "luis@ejemplo.com",
    roles: ["alumno"],
    telefonos: ["7221111111", "7222222222"],
    direccion: {
      ciudad: "Toluca",
      colonia: "Centro"
    }
  }
])
```

Consultar:

```javascript
db.usuarios.find().pretty()
```

***

Aquí se observa otra idea importante del curso: el dato semiestructurado conserva organización jerárquica y anidada mediante objetos, arreglos y pares atributo‑valor, muy cercano a JSON, lo cual facilita representar información real como configuraciones, listas de roles, teléfonos y direcciones. 

***

## Parte 8. Operaciones básicas sugeridas para la práctica

### 24. Búsqueda por condición numérica

Ejecutar:

```javascript
db.productos.find({ precio: { $gt: 1000 } }).pretty()
```

***

### 25. Actualización de un documento

Actualizar el precio de un producto:

```javascript
db.productos.updateOne(
  { nombre: "Tenis deportivos" },
  { $set: { precio: 1399 } }
)
```

Verificar:

```javascript
db.productos.find({ nombre: "Tenis deportivos" }).pretty()
```

***

### 26. Agregar un nuevo atributo sin rediseñar la colección

```javascript
db.productos.updateOne(
  { nombre: "Laptop" },
  { $set: { garantiaMeses: 12 } }
)
```

Consultar:

```javascript
db.productos.find({ nombre: "Laptop" }).pretty()
```

***

Este paso es especialmente importante porque ejemplifica la flexibilidad de esquema que motiva el uso de tecnologías NoSQL en contextos donde los datos cambian con frecuencia o cada entidad presenta variantes. La flexibilidad de esquema fue una de las motivaciones destacadas en el temario de la sesión. 

***

### 27. Eliminar un documento

```javascript
db.usuarios.deleteOne({ nombre: "Ana" })
```

Verificar:

```javascript
db.usuarios.find().pretty()
```

***

### 28. Crear un índice simple

```javascript
db.productos.createIndex({ nombre: 1 })
```

Listar índices:

```javascript
db.productos.getIndexes()
```

***

### 29. Obtener estadísticas básicas de la colección

```javascript
db.productos.stats()
```

***

## Parte 9. Instalación de Node.js para el sistema de ejemplo

**Definición.** Express.js es un framework ligero para Node.js orientado a construir servicios web y APIs. Un sistema pequeño con Express y MongoDB permite observar cómo una aplicación web produce y consume JSON de manera natural, que es uno de los contextos donde JSON se volvió dominante. 

***

### 30. Instalar Node.js y npm desde Ubuntu

Ejecutar:

```bash
sudo apt install -y nodejs npm
```

Verificar versiones:

```bash
node -v
npm -v
```

***

Aunque existen varias formas de instalar Node.js, esta vía es suficiente para una práctica académica y permite construir un servicio sencillo sobre la VM para ser accedido desde el host.

***

## Parte 10. Creación de un sistema pequeño con Express.js y MongoDB

### 31. Crear carpeta del proyecto

```bash
mkdir -p ~/mini-api-mongo
cd ~/mini-api-mongo
```

Inicializar el proyecto:

```bash
npm init -y
```

Instalar dependencias:

```bash
npm install express mongodb cors
```

La combinación Express + driver de MongoDB permite construir una API REST sencilla sobre una base documental. MongoDB incluso ofrece material oficial de tutorial para Express.js y MongoDB como combinación común para aplicaciones web. 

***

### 32. Crear el archivo principal del servidor

Crear el archivo `app.js`:

```bash
nano app.js
```

Pegar el siguiente contenido:

```javascript
const express = require('express');
const { MongoClient, ObjectId } = require('mongodb');
const cors = require('cors');

const app = express();
const PORT = 3000;
const MONGO_URL = 'mongodb://127.0.0.1:27017';
const DB_NAME = 'practica_nosql';

app.use(cors());
app.use(express.json());

let db;

MongoClient.connect(MONGO_URL)
  .then(client => {
    db = client.db(DB_NAME);
    console.log('Conectado a MongoDB');
  })
  .catch(err => {
    console.error('Error al conectar a MongoDB:', err);
  });

app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Mini sistema MongoDB</title>
      </head>
      <body style="font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto;">
        <h1>Mini sistema con Express y MongoDB</h1>
        <p>Servidor funcionando correctamente.</p>
        <ul>
          <li><a href="/api/productos">Ver productos en JSON</a></li>
          <li><a href="/front">Abrir interfaz simple</a></li>
        </ul>
      </body>
    </html>
  `);
});

app.get('/api/productos', async (req, res) => {
  const productos = await db.collection('productos').find().toArray();
  res.json(productos);
});

app.get('/api/productos/:id', async (req, res) => {
  const producto = await db.collection('productos').findOne({
    _id: new ObjectId(req.params.id)
  });
  res.json(producto);
});

app.post('/api/productos', async (req, res) => {
  const nuevo = req.body;
  const resultado = await db.collection('productos').insertOne(nuevo);
  res.json({ mensaje: 'Producto insertado', id: resultado.insertedId });
});

app.put('/api/productos/:id', async (req, res) => {
  const cambios = req.body;
  const resultado = await db.collection('productos').updateOne(
    { _id: new ObjectId(req.params.id) },
    { $set: cambios }
  );
  res.json({ mensaje: 'Producto actualizado', resultado });
});

app.delete('/api/productos/:id', async (req, res) => {
  const resultado = await db.collection('productos').deleteOne({
    _id: new ObjectId(req.params.id)
  });
  res.json({ mensaje: 'Producto eliminado', resultado });
});

app.get('/front', (req, res) => {
  res.send(`
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Front simple</title>
      </head>
      <body style="font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto;">
        <h1>Consulta de productos</h1>
        <button onclick="cargar()">Cargar productos</button>
        <h2>Agregar producto</h2>
        <input id="nombre" placeholder="Nombre">
        <input id="categoria" placeholder="Categoría">
        <input id="precio" type="number" placeholder="Precio">
        <button onclick="agregar()">Guardar</button>
        <pre id="salida" style="background:#f4f4f4; padding:16px; margin-top:20px;"></pre>

        <script>
          async function cargar() {
            const r = await fetch('/api/productos');
            const datos = await r.json();
            document.getElementById('salida').textContent =
              JSON.stringify(datos, null, 2);
          }

          async function agregar() {
            const producto = {
              nombre: document.getElementById('nombre').value,
              categoria: document.getElementById('categoria').value,
              precio: Number(document.getElementById('precio').value)
            };

            const r = await fetch('/api/productos', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(producto)
            });

            const datos = await r.json();
            alert(JSON.stringify(datos));
            cargar();
          }
        </script>
      </body>
    </html>
  `);
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(\`Servidor escuchando en puerto \${PORT}\`);
});
```

Guardar y salir.

***

### 33. Ejecutar el sistema

Desde la carpeta del proyecto:

```bash
node app.js
```

La aplicación quedará escuchando en el puerto `3000` sobre `0.0.0.0`, lo que permite que el servicio sea consumido desde el host a través de la interfaz solo‑anfitrión.

***

## Parte 11. Probar el sistema desde la propia VM

En la VM, abrir otra terminal y ejecutar:

```bash
curl http://127.0.0.1:3000/api/productos
```

También se puede abrir desde un navegador en la VM si se cuenta con interfaz gráfica, aunque en Ubuntu Server normalmente bastará con `curl`.

***

## Parte 12. Consumir el sistema desde el host

### 34. Identificar la IP host-only de la VM

Revisar nuevamente en la VM:

```bash
ip addr
```

Ubicar la IP del adaptador solo‑anfitrión, por ejemplo `192.168.56.10`.

***

### 35. Probar la API desde el host

Desde el navegador del host, abrir:

```text
http://192.168.56.X:3000/
```

Para abrir la interfaz sencilla:

```text
http://192.168.56.X:3000/front
```

Para consultar la API en JSON:

```text
http://192.168.56.X:3000/api/productos
```

***

### 36. Probar inserción desde el host usando terminal

Desde el host, ejecutar:

```bash
curl -X POST http://192.168.56.X:3000/api/productos \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Mouse inalambrico","categoria":"electronica","precio":399}'
```

Consultar nuevamente:

```bash
curl http://192.168.56.X:3000/api/productos
```

***

Este comportamiento permite observar un patrón muy importante en aplicaciones modernas: el frontend o cliente consume documentos JSON expuestos por una API, y esos documentos se almacenan en una base documental sin tener que transformar todo a un modelo tabular rígido. Esa cercanía entre JSON de aplicación y documento persistente es una de las razones por las que las bases documentales se volvieron tan útiles en aplicaciones web. 

***

## Parte 13. Hacer persistente el servicio con systemd

### 37. Crear un servicio para Express

Crear el archivo:

```bash
sudo nano /etc/systemd/system/mini-api.service
```

Pegar:

```ini
[Unit]
Description=Mini API Express con MongoDB
After=network.target mongod.service

[Service]
User=TU_USUARIO
WorkingDirectory=/home/TU_USUARIO/mini-api-mongo
ExecStart=/usr/bin/node /home/TU_USUARIO/mini-api-mongo/app.js
Restart=always
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

Sustituir `TU_USUARIO` por el usuario real de Ubuntu.

***

### 38. Habilitar el servicio

```bash
sudo systemctl daemon-reload
sudo systemctl enable mini-api
sudo systemctl start mini-api
sudo systemctl status mini-api
```

***

Ahora el sistema quedará disponible tras reiniciar la VM, siempre que MongoDB y la red estén operando correctamente.

***

## Parte 14. Verificaciones finales

### 39. Verificar MongoDB

```bash
sudo systemctl status mongod
```

Debe aparecer `active (running)`.

***

### 40. Verificar la API

```bash
sudo systemctl status mini-api
curl http://127.0.0.1:3000/api/productos
```

***

### 41. Verificar desde el host

Abrir:

```text
http://192.168.56.X:3000/front
```

Agregar un producto desde la interfaz y confirmar que aparece en la lista.

***

## Parte 15. Evidencias mínimas solicitadas

- Captura de `ip addr` donde se vean ambas interfaces.
- Captura de `systemctl status ssh`.
- Captura de `systemctl status mongod`.
- Captura de `db.productos.find().pretty()` en `mongosh`.
- Captura del navegador del host accediendo a `/front`.
- Captura del JSON devuelto por `/api/productos`.

***

## Parte 16. Actividades de análisis

### 42. Identificar estructura semiestructurada

Responder con base en los documentos insertados:

- ¿Qué atributos están anidados?
- ¿Qué campos son arreglos?
- ¿Qué ventaja ofrece que un producto tenga `atributos` distintos según su categoría? 

***

### 43. Comparar con un esquema relacional

Responder:

- Si `productos` se almacenara en una sola tabla relacional, ¿qué columnas quedarían vacías para muchos registros?
- ¿Qué tablas auxiliares aparecerían si se quisieran modelar etiquetas, ingredientes o listas variables? 

***

### 44. Relacionar con escalabilidad y distribución

Responder:

- ¿Qué papel juega la red solo‑anfitrión en esta práctica como forma básica de separación entre cliente y servidor?
- ¿Por qué esta práctica ya muestra un esquema simple de servicio distribuido, aunque solo exista una VM? 

***

## Parte 17. Preguntas de cierre

- ¿Qué diferencia práctica se observa entre almacenar un documento flexible en MongoDB y diseñar una tabla rígida para todos los casos? 
- ¿Por qué JSON resulta natural para una API web y para una base documental? 
- ¿Qué ventaja ofrece que el host consuma el servicio de la VM por red? 
- ¿Qué cambios mínimos permitirían convertir este sistema en una API CRUD más completa? 

***

## Parte 18. Resultado esperado

Al finalizar la práctica, la máquina virtual debe cumplir con lo siguiente:

- Ubuntu Server instalado y accesible por SSH.
- MongoDB Community Edition instalado desde el repositorio oficial y ejecutándose como servicio. 
- Base `practica_nosql` creada con colecciones y documentos de ejemplo.
- Sistema Express.js funcional en el puerto `3000`.
- Interfaz web simple accesible desde el host mediante la IP host-only de la VM.
- Operaciones básicas de inserción y consulta funcionando sobre documentos JSON.

***

## Parte 19. Observaciones técnicas

MongoDB recomienda instalar Community Edition en Ubuntu mediante sus paquetes oficiales para distribuciones Linux soportadas y usar el servicio `mongod` para administrar el servidor. Además, MongoDB mantiene documentación específica para Ubuntu LTS y material de integración con Express.js para construir APIs REST sobre datos documentales. 

***

## Parte 20. Problemas comunes y solución rápida

- **No hay internet en la VM:** revisar que el Adaptador 1 esté en red NAT y que la red NAT tenga DHCP habilitado.
- **No responde la IP host-only:** revisar que el Adaptador 2 esté conectado al adaptador solo-anfitrión y confirmar la IP con `ip addr`.
- **`mongod` no inicia:** revisar `sudo systemctl status mongod` y confirmar que el repositorio corresponde a la versión real de Ubuntu. 
- **La API no responde desde el host:** verificar que Express escuche en `0.0.0.0` y no solo en `127.0.0.1`.
- **El puerto 3000 no abre:** revisar `sudo systemctl status mini-api` o ejecutar temporalmente `node app.js` para detectar errores.
- **No conecta SSH:** confirmar `systemctl status ssh` y que la IP usada sea la de la interfaz solo-anfitrión.

***

Si quieres, en el siguiente mensaje la convierto a un formato todavía más académico con secciones de **objetivo, introducción, desarrollo, evidencias y rúbrica**, o te la adapto para entrega directa a alumnado en Markdown con separadores `---` cada cierto bloque.