# Práctica: Fragmentación horizontal y vertical en una base de datos distribuida

## Objetivo

Implementar un escenario básico de base de datos distribuida usando dos nodos:

- El **host** como nodo principal con **PostgreSQL**.
- Una **máquina virtual** como segundo nodo con **MySQL**.

En esta práctica se aplicarán dos tipos de fragmentación:

- **Fragmentación horizontal** de la tabla `alumno`.
- **Fragmentación vertical** de la tabla `profesor`.

Al finalizar, se debe poder observar que una misma base lógica puede distribuirse entre dos nodos distintos, manteniendo la posibilidad de reconstruir la información original por medio de operaciones de union y join. 

## Competencias a desarrollar

Al completar esta práctica, se deberá ser capaz de:

- Configurar una red virtual con conectividad entre host y máquina virtual.
- Instalar y verificar PostgreSQL en el host y MySQL en una máquina virtual.
- Implementar fragmentación horizontal mediante distribución de filas entre nodos.
- Implementar fragmentación vertical mediante distribución de columnas entre nodos.
- Ejecutar consultas locales y consultas de reconstrucción de la información lógica.

## Requisitos previos

Antes de iniciar, se requiere contar con lo siguiente:

- VirtualBox instalado.
- Una imagen ISO de Ubuntu compatible con la arquitectura del equipo.
- Permisos para instalar software en el host y en la máquina virtual.
- Acceso a terminal en el host.
- Conexión a internet para instalar paquetes en Ubuntu.

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

## Parte 5. Instalación de PostgreSQL en el host

### 12. Instalar PostgreSQL

Instalar PostgreSQL en el host. El procedimiento puede variar según el sistema operativo, pero en un host con Ubuntu o Debian puede realizarse con:

```bash
sudo apt update
sudo apt install postgresql -y
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

Si el host es Windows o Mac, consultar la forma de instalación apropiada.

### 13. Verificar PostgreSQL

Comprobar que PostgreSQL está disponible een el host, en un host con Ubuntu o Debian puede realizarse con:

```bash
sudo -u postgres psql -c "SELECT version();"
```

Se debe observar la versión instalada de PostgreSQL.
En otros sistemas operativos, consultar la documentación apropiada

## Parte 6. Instalación de MySQL en la VM

### 14. Instalar MySQL Server

Dentro de la VM, ejecutar:

```bash
sudo apt update
sudo apt install mysql-server -y
sudo systemctl enable mysql
sudo systemctl start mysql
```

### 15. Verificar el estado del servicio MySQL

En la VM, ejecutar:

```bash
sudo systemctl status mysql
```

Verificar que el servicio aparezca como `active (running)`.

### 16. Entrar a MySQL

Dentro de la VM, ejecutar:

```bash
sudo mysql
```

Una vez dentro del cliente MySQL, ejecutar:

```sql
SELECT VERSION();
```

Confirmar que se muestra correctamente la versión del motor. Para salir de MySQL, ejecutar:

```sql
exit
```

## Parte 7. Modelo lógico global

Para esta práctica se tomará como referencia el siguiente modelo lógico global del sistema académico:

- `alumno(id_alumno, nombre, correo, telefono, campus, carrera, promedio)`
- `profesor(id_profesor, nombre, correo, telefono, campus, grado, salario)`

Estas tablas no se implementarán completas en un solo nodo, sino fragmentadas entre el host y la VM. La fragmentación tiene como objetivo dividir una relación en fragmentos que puedan almacenarse en nodos diferentes y reconstruirse posteriormente.

## Parte 8. Fragmentación horizontal de la tabla alumno

La fragmentación horizontal divide una tabla por filas, de forma que cada fragmento contiene un subconjunto de registros determinado por una condición sobre un atributo.

En esta práctica, la tabla lógica `alumno` se distribuirá por campus de la siguiente manera:

- En el **host** se almacenarán los alumnos de `CENTRO` y `NORTE`.
- En la **VM** se almacenarán los alumnos de `SUR`.

La reconstrucción lógica de la tabla completa se expresa como:

$$
alumno = alumno\_centro \cup alumno\_norte \cup alumno\_sur
$$

Esta distribución permite observar que cada nodo almacena un subconjunto distinto de filas de la misma tabla lógica.

### 17. Crear la base de datos en el host

En el host, entrar a PostgreSQL:

```bash
sudo -u postgres psql
```

Crear la base de datos del nodo principal:

```sql
CREATE DATABASE bd_host;
\c bd_host;
```

### 18. Crear los fragmentos horizontales en el host

Ejecutar en PostgreSQL:

```sql
CREATE TABLE alumno_centro (
    id_alumno INT PRIMARY KEY,
    nombre    VARCHAR(100),
    correo    VARCHAR(120),
    telefono  VARCHAR(20),
    campus    VARCHAR(20),
    carrera   VARCHAR(100),
    promedio  NUMERIC(4,2),
    CHECK (campus = 'CENTRO')
);

CREATE TABLE alumno_norte (
    id_alumno INT PRIMARY KEY,
    nombre    VARCHAR(100),
    correo    VARCHAR(120),
    telefono  VARCHAR(20),
    campus    VARCHAR(20),
    carrera   VARCHAR(100),
    promedio  NUMERIC(4,2),
    CHECK (campus = 'NORTE')
);
```

### 19. Insertar datos en los fragmentos del host

Ejecutar:

```sql
INSERT INTO alumno_centro VALUES
(1, 'Ana', 'ana@uni.mx', '555-0001', 'CENTRO', 'Computación', 8.5),
(2, 'Luis', 'luis@uni.mx', '555-0002', 'CENTRO', 'Matemáticas', 9.0);

INSERT INTO alumno_norte VALUES
(3, 'Juan', 'juan@uni.mx', '555-0003', 'NORTE', 'Física', 8.2),
(4, 'María', 'maria@uni.mx', '555-0004', 'NORTE', 'Biología', 8.8);
```

### 20. Crear la base de datos en la VM

Conectarse a la VM y entrar a MySQL:

```bash
ssh usuario@192.168.56.X
sudo mysql
```

Crear la base de datos:

```sql
CREATE DATABASE bd_vm;
USE bd_vm;
```

### 21. Crear el fragmento horizontal en la VM

Ejecutar en MySQL:

```sql
CREATE TABLE alumno_sur (
    id_alumno INT PRIMARY KEY,
    nombre    VARCHAR(100),
    correo    VARCHAR(120),
    telefono  VARCHAR(20),
    campus    VARCHAR(20),
    carrera   VARCHAR(100),
    promedio  DECIMAL(4,2),
    CHECK (campus = 'SUR')
);
```

### 22. Insertar datos en el fragmento de la VM

Ejecutar:

```sql
INSERT INTO alumno_sur VALUES
(5, 'Paco', 'paco@uni.mx', '555-0005', 'SUR', 'Química', 8.0),
(6, 'Elena', 'elena@uni.mx', '555-0006', 'SUR', 'Computación', 9.1);
```

## Parte 9. Fragmentación vertical de la tabla profesor

La fragmentación vertical divide una tabla por columnas. Para poder reconstruir la tabla original, cada fragmento debe conservar el identificador común.

En esta práctica, la tabla lógica `profesor` se distribuirá así:

- En el **host** se almacenarán los datos generales del profesor.
- En la **VM** se almacenará la información de nómina.

La reconstrucción lógica de la tabla completa se expresa como:

$$
profesor = profesor\_datos \bowtie profesor\_nomina
$$

El atributo común para reunir ambos fragmentos será `id_profesor`.

### 23. Crear el fragmento vertical en el host

En PostgreSQL, dentro de `bd_host`, ejecutar:

```sql
CREATE TABLE profesor_datos (
    id_profesor INT PRIMARY KEY,
    nombre      VARCHAR(100),
    correo      VARCHAR(120),
    telefono    VARCHAR(20),
    campus      VARCHAR(20),
    grado       VARCHAR(50)
);
```

### 24. Insertar datos en el fragmento del host

Ejecutar:

```sql
INSERT INTO profesor_datos VALUES
(1, 'Dr. López', 'lopez@uni.mx', '555-0101', 'CENTRO', 'Doctorado'),
(2, 'Mtra. Ruiz', 'ruiz@uni.mx', '555-0102', 'SUR', 'Maestría');
```

### 25. Crear el fragmento vertical en la VM

En MySQL, dentro de `bd_vm`, ejecutar:

```sql
CREATE TABLE profesor_nomina (
    id_profesor INT PRIMARY KEY,
    salario     DECIMAL(10,2)
);
```

### 26. Insertar datos en el fragmento de la VM

Ejecutar:

```sql
INSERT INTO profesor_nomina VALUES
(1, 35000.00),
(2, 28000.00);
```

## Parte 10. Consultas locales

### 27. Consultar los fragmentos horizontales en el host

En PostgreSQL, ejecutar:

```sql
SELECT * FROM alumno_centro;
SELECT * FROM alumno_norte;
```

### 28. Consultar el fragmento horizontal en la VM

En MySQL, ejecutar:

```sql
SELECT * FROM alumno_sur;
```

### 29. Consultar el fragmento vertical en el host

En PostgreSQL, ejecutar:

```sql
SELECT * FROM profesor_datos;
```

### 30. Consultar el fragmento vertical en la VM

En MySQL, ejecutar:

```sql
SELECT * FROM profesor_nomina;
```

Estas consultas permiten observar que cada nodo contiene solamente una parte de la base lógica global.

## Parte 11. Reconstrucción lógica de la información

### 31. Reconstrucción conceptual de `alumno`

La tabla `alumno` se reconstruye combinando todos los fragmentos horizontales. Desde el punto de vista teórico, la reconstrucción se realiza con una unión de registros provenientes de los tres campus.

En el host, crear una tabla de apoyo para visualizar la reconstrucción global:

```sql
CREATE TABLE alumno_global (
    id_alumno INT PRIMARY KEY,
    nombre    VARCHAR(100),
    campus    VARCHAR(20),
    carrera   VARCHAR(100),
    promedio  NUMERIC(4,2)
);
```

Insertar primero los datos del host:

```sql
INSERT INTO alumno_global
SELECT id_alumno, nombre, campus, carrera, promedio
FROM alumno_centro;

INSERT INTO alumno_global
SELECT id_alumno, nombre, campus, carrera, promedio
FROM alumno_norte;
```

Después, recuperar desde la VM los datos del fragmento `alumno_sur` con el siguiente comando ejecutado en el host:

```bash
ssh -t usuario@192.168.56.X "sudo mysql -D bd_vm -e \"SELECT id_alumno, nombre, campus, carrera, promedio FROM alumno_sur;\""
```

Con base en el resultado mostrado, insertar manualmente esos registros en `alumno_global`:

Verificar el contenido global:

```sql
SELECT * FROM alumno_global;
```

### 32. Reconstrucción conceptual de `profesor`

La tabla `profesor` se reconstruye reuniendo los fragmentos verticales por medio del atributo `id_profesor`, ya que ambos fragmentos comparten la llave primaria.

Crear en el host una tabla global de apoyo:

```sql
CREATE TABLE profesor_global (
    id_profesor INT PRIMARY KEY,
    nombre      VARCHAR(100),
    correo      VARCHAR(120),
    telefono    VARCHAR(20),
    campus      VARCHAR(20),
    grado       VARCHAR(50),
    salario     NUMERIC(10,2)
);
```

Consultar desde el host el contenido local del fragmento `profesor_datos`:

```sql
SELECT * FROM profesor_datos;
```

Recuperar desde la VM el contenido del fragmento `profesor_nomina`:

```bash
ssh -t usuario@192.168.56.X "sudo mysql -D bd_vm -e \"SELECT * FROM profesor_nomina;\""
```

Con base en los datos observados, insertar manualmente los registros completos en `profesor_global`:

Verificar el resultado:

```sql
SELECT * FROM profesor_global;
```

## Parte 12. Consultas finales

### 33. Consultas globales sobre alumnos

En el host, ejecutar:

```sql
SELECT * FROM alumno_global;
```

```sql
SELECT campus, COUNT(*) AS total_alumnos
FROM alumno_global
GROUP BY campus;
```

### 34. Consultas globales sobre profesores

En el host, ejecutar:

```sql
SELECT * FROM profesor_global;
```

```sql
SELECT campus, AVG(salario) AS salario_promedio
FROM profesor_global
GROUP BY campus;
```

## Parte 13. Actividades de análisis

Responder las siguientes preguntas en el reporte:

1. ¿Qué parte de la práctica corresponde a fragmentación horizontal y por qué?
2. ¿Qué parte de la práctica corresponde a fragmentación vertical y por qué?
3. ¿Qué atributo permite reconstruir la tabla `profesor`?
4. ¿Por qué `alumno` se reconstruye con unión y `profesor` con reunión (JOIN)?
5. ¿Qué ventajas ofrece almacenar en el host fragmentos que la VM no contiene y viceversa?

## Entregables

Entregar un archivo comprimido con los siguientes elementos:

1. **Reporte en PDF** con:
   - Portada.
   - Objetivo de la práctica.
   - Respuestas a las preguntas de análisis.

2. **Capturas de pantalla** integradas en el reporte que muestren al menos:
   - La verificación de versión de PostgreSQL en el host.
   - La verificación de versión de MySQL en la VM.
   - Las consultas finales. (Parte 12)
