# Práctica 

Implementar un escenario de bases de datos distribuidas usando tres nodos virtuales (`db-nodo1`, `db-nodo2`, `db-nodo3`) con diferentes motores de base de datos y un motor adicional en el host, aplicando fragmentación horizontal, vertical e híbrida, ejecutando consultas locales y globales, y representando replicación de catálogos compartidos. 

***

## Parte 1. Preparación de máquinas virtuales y redes

1. **Descargar Ubuntu apropiado al host**  
   - Si el host es Mac con procesador M1/M2/M3: descargar Ubuntu ARM (ARM 64‑bit). 
   - Si el host es PC o laptop con procesador Intel/AMD (Windows o Linux): descargar Ubuntu “Intel or AMD 64‑bit architecture”. 
   - La arquitectura de la ISO debe coincidir con la arquitectura que soporta el hipervisor en ese host. 

2. **Configurar redes en modo experto en VirtualBox**  
   - Abrir VirtualBox y entrar a **Preferencias → Red** en modo experto. 

3. **Crear red solo‑anfitrión**  
   - En la sección de redes “Host‑only”:  
     - Nombre: `default` (o el que se muestre por defecto).  
     - Máscara: `255.255.255.0`.  
     - IP del anfitrión: `192.168.56.1`.  
     - Rango DHCP: desde `192.168.56.1` hasta `192.168.56.199`.  
     - DHCP habilitado. 

4. **Crear red NAT**  
   - En la sección de redes NAT:  
     - Nombre: `default`.  
     - Prefijo IPv4: `192.168.50.0/24`.  
     - DHCP habilitado. 

5. **Crear las tres máquinas virtuales**  
   - Crear tres VMs en VirtualBox con nombres:  
     - `db-nodo1`  
     - `db-nodo2`  
     - `db-nodo3`  
   - Tipo: Linux, Ubuntu (ARM o Intel/AMD según la ISO). 
   - RAM: 2 GB.  
   - Disco: 20 GB, **dinamically allocated**. 
   - Adjuntar la ISO de Ubuntu y completar la instalación, creando un usuario y contraseña.

6. **Configurar adaptadores de red en cada VM**  
   - Para `db-nodo1`, `db-nodo2` y `db-nodo3`, en **Settings → Network**:  
     - Adaptador 1:  
       - Activado.  
       - Conectado a: **Red NAT**.  
       - Nombre: `default` (192.168.50.0/24). 
     - Adaptador 2:  
       - Activado.  
       - Conectado a: **Red solo‑anfitrión**.  
       - Nombre: `default` (host‑only, 192.168.56.0/24). 

7. **Obtener las IP de cada VM y probar conectividad**  
   - En cada VM, ejecutar:  
     ```bash
     ip addr
     ```  
   - Tomar nota de:
     - IP del adaptador host‑only (192.168.56.x). 
   - Desde cada VM, hacer `ping` a las otras VMs usando las IP host‑only (192.168.56.x) para confirmar conectividad. 
   - Desde el host, hacer `ping` a las IP host‑only de cada VM (por ejemplo 192.168.56.3, 192.168.56.4, 192.168.56.5) para verificar comunicación host ↔ nodos. 

8. **Actualizar y preparar SSH en cada VM**  
   - En cada VM (`db-nodo1`, `db-nodo2`, `db-nodo3`), ejecutar:  
     ```bash
     sudo apt update
     sudo apt upgrade
     sudo apt install openssh-server
     ```  
   - Habilitar y arrancar SSH:  
     ```bash
     sudo systemctl enable ssh
     sudo systemctl start ssh
     sudo systemctl status ssh
     ```  
   - El estado debe mostrar “active (running)”. 

9. **Conectar por SSH desde el host a cada VM**  
   - Desde el host, conectarse a cada nodo usando su IP host‑only:  
     ```bash
     ssh usuario@192.168.56.3   # db-nodo1
     ssh usuario@192.168.56.4   # db-nodo2
     ssh usuario@192.168.56.5   # db-nodo3
     ```  
   - `usuario` es el usuario creado durante la instalación de Ubuntu. 

***

## Parte 2. Instalación de motores de base de datos

### Nodo1: PostgreSQL (`db-nodo1`)

10. Conectarse a `db-nodo1`:
    ```bash
    ssh usuario@192.168.56.3
    ```

11. Instalar PostgreSQL:
    ```bash
    sudo apt update
    sudo apt install postgresql
    sudo systemctl enable postgresql
    sudo systemctl start postgresql
    ```

12. Verificar PostgreSQL:
    ```bash
    sudo -u postgres psql -c "SELECT version();"
    ```
    - Confirmar que se muestra la versión de PostgreSQL. 

### Nodo2: MySQL (`db-nodo2`)

13. Conectarse a `db-nodo2`:
    ```bash
    ssh usuario@192.168.56.4
    ```

14. Instalar MySQL Server:
    ```bash
    sudo apt update
    sudo apt install mysql-server
    sudo systemctl enable mysql
    sudo systemctl start mysql
    ```

15. Entrar a MySQL como root usando socket:
    ```bash
    sudo mysql
    ```
    - Dentro del prompt, ejecutar:
      ```sql
      SELECT VERSION();
      ```
    - Confirmar que se muestra la versión de MySQL. 

### Nodo3: MariaDB (`db-nodo3`)

16. Conectarse a `db-nodo3`:
    ```bash
    ssh usuario@192.168.56.5
    ```

17. Instalar MariaDB:
    ```bash
    sudo apt update
    sudo apt install mariadb-server
    sudo systemctl enable mariadb
    sudo systemctl start mariadb
    ```

18. Entrar a MariaDB:
    ```bash
    sudo mysql
    ```
    - Dentro del prompt, ejecutar:
      ```sql
      SELECT VERSION();
      ```
    - Confirmar que se muestra la versión de MariaDB. 

### Host: PostgreSQL (coordinador)

19. Instalar PostgreSQL en el host (ejemplo en Linux):
    ```bash
    sudo apt update
    sudo apt install postgresql
    sudo systemctl enable postgresql
    sudo systemctl start postgresql
    ```

20. Verificar PostgreSQL en el host:
    ```bash
    sudo -u postgres psql -c "SELECT version();"
    ```
    - Confirmar que se muestra la versión. 

***

## Parte 3. Modelo lógico y creación de bases/esquemas

Modelo lógico global de referencia: 

- `alumno(id_alumno, nombre, correo, telefono, campus, carrera, promedio)`  
- `curso(id_curso, nombre, campus, creditos)`  
- `inscripcion(id_inscripcion, id_alumno, id_curso, periodo, calificacion, fecha_inscripcion)`  
- `profesor(id_profesor, nombre, correo, telefono, campus, salario, grado)`  
- `departamento(id_depto, nombre, edificio, extension)`

La implementación física se repartirá en fragmentos horizontales, verticales e híbridos, más un catálogo replicado.

### Nodo1 (PostgreSQL): fragmentos horizontales de alumno y curso

21. Conectarse a PostgreSQL de `db-nodo1`:
    ```bash
    ssh usuario@192.168.56.3
    sudo -u postgres psql
    ```

22. Crear base de datos del nodo:
    ```sql
    CREATE DATABASE bd_nodo1;
    \c bd_nodo1;
    ```

23. Crear tablas fragmentadas horizontalmente por campus:
    ```sql
    CREATE TABLE alumno_centro (
        id_alumno      INT PRIMARY KEY,
        nombre         VARCHAR(100),
        correo         VARCHAR(120),
        telefono       VARCHAR(20),
        campus         VARCHAR(20),
        carrera        VARCHAR(100),
        promedio       NUMERIC(4,2),
        CHECK (campus = 'CENTRO')
    );

    CREATE TABLE alumno_norte (
        id_alumno      INT PRIMARY KEY,
        nombre         VARCHAR(100),
        correo         VARCHAR(120),
        telefono       VARCHAR(20),
        campus         VARCHAR(20),
        carrera        VARCHAR(100),
        promedio       NUMERIC(4,2),
        CHECK (campus = 'NORTE')
    );

    CREATE TABLE curso_centro (
        id_curso       INT PRIMARY KEY,
        nombre         VARCHAR(100),
        campus         VARCHAR(20),
        creditos       INT,
        CHECK (campus = 'CENTRO')
    );

    CREATE TABLE curso_norte (
        id_curso       INT PRIMARY KEY,
        nombre         VARCHAR(100),
        campus         VARCHAR(20),
        creditos       INT,
        CHECK (campus = 'NORTE')
    );
    ```

24. Insertar datos de ejemplo:
    ```sql
    INSERT INTO alumno_centro VALUES
    (1, 'Ana',  'ana@uni.mx',  '555-0001', 'CENTRO', 'Computación', 8.5),
    (2, 'Luis', 'luis@uni.mx', '555-0002', 'CENTRO', 'Matemáticas', 9.0);

    INSERT INTO alumno_norte VALUES
    (3, 'Juan',  'juan@uni.mx',  '555-0003', 'NORTE', 'Física',    8.2),
    (4, 'María', 'maria@uni.mx', '555-0004', 'NORTE', 'Biología',  8.8);

    INSERT INTO curso_centro VALUES
    (101, 'BD Avanzadas', 'CENTRO', 8),
    (102, 'Algoritmos',   'CENTRO', 6);

    INSERT INTO curso_norte VALUES
    (201, 'Redes',        'NORTE', 8),
    (202, 'Programación', 'NORTE', 6);
    ```

### Nodo2 (MySQL): fragmentos horizontales y catálogo replicado

25. Conectarse a `db-nodo2`:
    ```bash
    ssh usuario@192.168.56.4
    sudo mysql
    ```

26. Crear base de datos:
    ```sql
    CREATE DATABASE bd_nodo2;
    USE bd_nodo2;
    ```

27. Crear fragmentos horizontales para campus SUR:
    ```sql
    CREATE TABLE alumno_sur (
        id_alumno      INT PRIMARY KEY,
        nombre         VARCHAR(100),
        correo         VARCHAR(120),
        telefono       VARCHAR(20),
        campus         VARCHAR(20),
        carrera        VARCHAR(100),
        promedio       DECIMAL(4,2),
        CHECK (campus = 'SUR')
    );

    CREATE TABLE curso_sur (
        id_curso       INT PRIMARY KEY,
        nombre         VARCHAR(100),
        campus         VARCHAR(20),
        creditos       INT,
        CHECK (campus = 'SUR')
    );
    ```

28. Crear catálogo `departamento` replicado:
    ```sql
    CREATE TABLE departamento (
        id_depto       INT PRIMARY KEY,
        nombre         VARCHAR(100),
        edificio       VARCHAR(50),
        extension      VARCHAR(10)
    );
    ```

29. Insertar datos:
    ```sql
    INSERT INTO alumno_sur VALUES
    (5, 'Paco',  'paco@uni.mx',  '555-0005', 'SUR', 'Química',      8.0),
    (6, 'Elena', 'elena@uni.mx', '555-0006', 'SUR', 'Computación',  9.1);

    INSERT INTO curso_sur VALUES
    (301, 'Seguridad', 'SUR', 8),
    (302, 'Linux',     'SUR', 6);

    INSERT INTO departamento VALUES
    (1, 'Computación', 'Edif A', '1001'),
    (2, 'Matemáticas', 'Edif B', '1002'),
    (3, 'Física',      'Edif C', '1003');
    ```

### Nodo3 (MariaDB): fragmentación vertical e híbrida

30. Conectarse a `db-nodo3`:
    ```bash
    ssh usuario@192.168.56.5
    sudo mysql
    ```

31. Crear base de datos:
    ```sql
    CREATE DATABASE bd_nodo3;
    USE bd_nodo3;
    ```

32. Crear fragmentos verticales de `profesor`:
    ```sql
    CREATE TABLE profesor_datos (
        id_profesor    INT PRIMARY KEY,
        nombre         VARCHAR(100),
        correo         VARCHAR(120),
        telefono       VARCHAR(20),
        campus         VARCHAR(20),
        grado          VARCHAR(50)
    );

    CREATE TABLE profesor_nomina (
        id_profesor    INT PRIMARY KEY,
        salario        DECIMAL(10,2)
    );
    ```

33. Insertar datos:
    ```sql
    INSERT INTO profesor_datos VALUES
    (1, 'Dr. López', 'lopez@uni.mx', '555-0101', 'CENTRO', 'Doctorado'),
    (2, 'Mtra. Ruiz', 'ruiz@uni.mx', '555-0102', 'SUR',    'Maestría');

    INSERT INTO profesor_nomina VALUES
    (1, 35000.00),
    (2, 28000.00);
    ```

34. Crear fragmentación híbrida de `inscripcion` (académica/operativa):
    ```sql
    CREATE TABLE inscripcion_centro_academica (
        id_inscripcion     INT PRIMARY KEY,
        id_alumno          INT,
        id_curso           INT,
        periodo            VARCHAR(20),
        calificacion       DECIMAL(4,2)
    );

    CREATE TABLE inscripcion_centro_operativa (
        id_inscripcion     INT PRIMARY KEY,
        fecha_inscripcion  DATE
    );
    ```

35. Insertar datos:
    ```sql
    INSERT INTO inscripcion_centro_academica VALUES
    (1001, 1, 101, '2026-1', 9.0),
    (1002, 2, 102, '2026-1', 8.5);

    INSERT INTO inscripcion_centro_operativa VALUES
    (1001, '2026-02-01'),
    (1002, '2026-02-02');
    ```

***

## Parte 4. Consultas locales de reconstrucción

### Profesor (fragmentación vertical, nodo3)

36. En `db-nodo3`:
    ```sql
    USE bd_nodo3;

    SELECT d.id_profesor,
           d.nombre,
           d.campus,
           d.grado,
           n.salario
    FROM profesor_datos d
    JOIN profesor_nomina n
      ON d.id_profesor = n.id_profesor;
    ```
    - Esta consulta reconstruye la vista lógica de `profesor`. 

### Inscripcion (fragmentación híbrida, nodo3)

37. En `db-nodo3`:
    ```sql
    USE bd_nodo3;

    SELECT a.id_inscripcion,
           a.id_alumno,
           a.id_curso,
           a.periodo,
           a.calificacion,
           o.fecha_inscripcion
    FROM inscripcion_centro_academica a
    JOIN inscripcion_centro_operativa o
      ON a.id_inscripcion = o.id_inscripcion;
    ```
    - Esta consulta reconstruye `inscripcion` para el campus CENTRO. 

***

## Parte 5. Consultas cruzadas desde el host

### Preparación en el host

38. En el host, asegurarse de tener los clientes:
    - `psql` para PostgreSQL (host y nodo1). 
    - `mysql` para MySQL (nodo2) y MariaDB (nodo3). 

39. Conectarse al PostgreSQL del host:
    ```bash
    sudo -u postgres psql
    ```

40. Crear base de datos coordinadora:
    ```sql
    CREATE DATABASE bd_coordinador;
    \c bd_coordinador;
    ```

### Obtener datos de alumnos desde los nodos

41. Alumnos CENTRO y NORTE (nodo1), desde el host:
    ```bash
    ssh -t usuario@192.168.56.3 \
    "sudo -u postgres psql -d bd_nodo1 -c \
    \"SELECT id_alumno, nombre, campus, carrera, promedio
       FROM alumno_centro
       UNION ALL
       SELECT id_alumno, nombre, campus, carrera, promedio
       FROM alumno_norte;\""
    ```
    - Este comando ejecuta la consulta en `db-nodo1` y muestra el resultado en el host. 

42. Alumnos SUR (nodo2), desde el host:
    ```bash
    ssh -t usuario@192.168.56.4 \
    "sudo mysql -D bd_nodo2 -e \
    \"SELECT id_alumno, nombre, campus, carrera, promedio
       FROM alumno_sur;\""
    ```
    - Se usa `sudo mysql` en la VM para no requerir contraseña por socket. 

### Registrar resultados en `bd_coordinador` (host)

43. En el host, dentro de `bd_coordinador`, crear tabla de apoyo:
    ```sql
    CREATE TABLE alumno_global (
        id_alumno  INT PRIMARY KEY,
        nombre     VARCHAR(100),
        campus     VARCHAR(20),
        carrera    VARCHAR(100),
        promedio   NUMERIC(4,2)
    );
    ```

44. Insertar en `alumno_global` los datos obtenidos desde los nodos.  
    - Esta inserción puede hacerse manualmente copiando los resultados o mediante scripts adicionales que no forman parte del núcleo de la práctica (requiere código para automatizar la transferencia).  
    - Es importante aclarar que a partir de este punto la consolidación en `alumno_global` es manual o requiere programación de apoyo.

45. Consultas globales sobre `alumno_global`:
    - Listar todos los alumnos:
      ```sql
      SELECT * FROM alumno_global;
      ```
    - Contar alumnos por campus:
      ```sql
      SELECT campus, COUNT(*) AS total
      FROM alumno_global
      GROUP BY campus;
      ```

46. De forma similar, se pueden obtener desde nodo3 las vistas reconstruidas de `profesor` e `inscripcion`, registrar los resultados en tablas `profesor_global` e `inscripcion_global` en `bd_coordinador`, y luego hacer joins globales:

   - Ejemplo de consulta global:
     ```sql
     SELECT a.nombre AS alumno,
            a.campus,
            COUNT(i.id_inscripcion) AS total_inscripciones
     FROM alumno_global a
     LEFT JOIN inscripcion_global i
       ON a.id_alumno = i.id_alumno
     GROUP BY a.nombre, a.campus;
     ```

***

## Parte 6. Ejemplo de catálogo replicado requerido en varios nodos

47. El catálogo `departamento` representa información que todas las sedes necesitan consultar (por ejemplo, nombres de departamentos académicos). Para simular replicación: 

   - En `db-nodo2` (MySQL), ya se creó la tabla:
     ```sql
     CREATE TABLE departamento (
         id_depto       INT PRIMARY KEY,
         nombre         VARCHAR(100),
         edificio       VARCHAR(50),
         extension      VARCHAR(10)
     );
     ```

   - En `db-nodo1` (PostgreSQL), crear una tabla equivalente:
     ```bash
     ssh usuario@192.168.56.3
     sudo -u postgres psql
     ```

     ```sql
     \c bd_nodo1;

     CREATE TABLE departamento (
         id_depto       INT PRIMARY KEY,
         nombre         VARCHAR(100),
         edificio       VARCHAR(50),
         extension      VARCHAR(10)
     );
     ```

   - Insertar en `db-nodo1` los mismos registros que en `db-nodo2`:
     ```sql
     INSERT INTO departamento VALUES
     (1, 'Computación', 'Edif A', '1001'),
     (2, 'Matemáticas', 'Edif B', '1002'),
     (3, 'Física',      'Edif C', '1003');
     ```

   De este modo, el catálogo `departamento` está **replicado** en al menos dos nodos (PostgreSQL nodo1 y MySQL nodo2), permitiendo que consultas locales en cada nodo usen la misma información de referencia sin necesidad de solicitarla a un nodo central. 

48. Verificar replicación:
   - En `db-nodo1`:
     ```sql
     SELECT * FROM departamento;
     ```
   - En `db-nodo2`:
     ```sql
     SELECT * FROM departamento;
     ```
   - Confirmar que el contenido es idéntico en ambos nodos.

Con esta práctica se cubre: preparación de nodos, instalación de motores, diseño de fragmentación horizontal/vertical/híbrida, ejecución de consultas de reconstrucción en cada nodo, aproximación a consultas globales desde el host y representación de replicación de catálogos compartidos. 