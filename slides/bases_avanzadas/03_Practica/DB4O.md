# Tutorial DB4O

## Parte 0 – Preparar el entorno en VS Code

Antes de escribir código con Db4o, es necesario tener un entorno Java funcional y asegurarse de que la librería de Db4o está correctamente integrada.

### 0.1. Instalar Java y comprobar la versión

Java es el lenguaje que se utilizará para escribir el código que se conecta a Db4o. Conviene comprobar que la JDK está instalada y disponible en línea de comandos.

En una terminal (bash, zsh, PowerShell o CMD) se ejecuta:

```bash
java -version
```

La salida debe mostrar una versión de Java instalada (por ejemplo, 8, 11 o superior). Esto confirma que:

- Hay una JVM disponible para ejecutar programas Java.
- El sistema reconoce el comando `java`, lo que será necesario cuando VS Code intente compilar y ejecutar el código.

Si no aparece ninguna versión o el comando no se reconoce, se debe instalar una JDK (por ejemplo, OpenJDK) antes de continuar.

Este tutorial ha sido probado con la versión 18.0.2

### 0.2. Instalar la extensión de Java en VS Code

VS Code, por sí solo, no sabe compilar ni ejecutar Java. La extensión **“Extension Pack for Java”** (de Microsoft) añade soporte para:

- Compilar proyectos Java.
- Ejecutar clases con `main`.
- Gestionar librerías y dependencias.

Esta extensión se instala desde la pestaña de extensiones de VS Code, buscando “Extension Pack for Java” y pulsando en “Install”.

Una vez instalada, se puede crear un proyecto Java simple y ejecutar un programa “Hola Mundo” para confirmar que todo está configurado correctamente.

### 0.3. Crear un proyecto Java en VS Code

Desde la paleta de comandos de VS Code (Ctrl+Shift+P), se ejecuta:

- `Java: Create Java Project`.

Se puede elegir la opción “No build tools” para un proyecto simple (sin Maven o Gradle) y darle un nombre, por ejemplo: `HolaOODB`.

VS Code crea una estructura con una carpeta `src` y una clase inicial (por ejemplo `App.java`). Se puede reemplazar o complementar esa clase con una clase como:

```java
public class App {
    public static void main(String[] args) {
        System.out.println("Hola Mundo desde VS Code");
    }
}
```

Ejecutar esta clase confirma que:

- El proyecto compila.
- La extensión de Java funciona correctamente.
- La salida aparece en la terminal integrada.

### 0.4. Incorporar el jar de Db4o al proyecto

Db4o se distribuye como un archivo `.jar` que contiene el motor de base de datos orientada a objetos. La idea es que el programa Java incluya ese jar en su classpath para poder usar clases como `Db4oEmbedded` y `ObjectContainer`.

Los pasos generales son:

1. Descargar el jar correspondiente (por ejemplo, `db4o-8.0.276.16149-all-java5.jar`) y guardarlo en una carpeta del proyecto, por ejemplo `lib/`.
2. Asegurarse de que VS Code incluye ese jar en el classpath. En proyectos simples, la extensión de Java detecta jars en ciertas rutas o se puede configurar el classpath según la estructura. En proyectos Maven, se usaría una dependencia declarada.
3. Una forma de comprobar que el jar está correctamente integrado es escribir una clase que importe `com.db4o.Db4oEmbedded` y `com.db4o.ObjectContainer` y ver si compila.

El objetivo de este paso es que el código Java “vea” la API de Db4o y pueda invocar sus métodos.

***

## Parte 1 – Primer contacto con Db4o

En esta parte se abre y se cierra una base de datos Db4o desde Java, para comprobar que la integración con el jar funciona.

### 1.1. Verificar los imports de Db4o

Se crea la clase `PruebaDb4oImports`:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;

public class PruebaDb4oImports {
    public static void main(String[] args) {
        System.out.println("Imports de Db4o compilando correctamente");
    }
}
```

Si esta clase compila, significa que:

- El jar de Db4o está correctamente añadido.
- El compilador encuentra las clases de Db4o.
- Se puede seguir adelante con el uso del motor de base de datos.

Este paso es importante porque evita avanzar con problemas de configuración de librerías.

### 1.2. Abrir y cerrar una base de datos: `HolaOODB`

Se crea la clase `HolaOODB`:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;

public class HolaOODB {
    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("holaOODB.db4o");
            System.out.println("Base de datos Db4o abierta correctamente.");
        } finally {
            if (db != null) {
                db.close();
                System.out.println("Base de datos Db4o cerrada.");
            }
        }
    }
}
```

En este programa:

- `Db4oEmbedded.openFile("holaOODB.db4o")` abre (o crea) un archivo de base de datos con ese nombre.
- `ObjectContainer db` representa la conexión a esa base de datos.
- El bloque `finally` garantiza que la base se cierra aunque ocurra alguna excepción.

El propósito de este paso es que el alumno vea cómo se establece la conexión con una base de datos orientada a objetos y cómo se gestiona su ciclo de vida básico (abrir y cerrar).

***

## Parte 2 – Definir `Persona` y almacenar objetos

En esta parte se introduce una clase de dominio (`Persona`) y se aprende a almacenar instancias en la base de datos Db4o.

### 2.1. Definir la clase `Persona`

Se crea `Persona.java`:

```java
public class Persona {

    private int id;
    private String nombre;
    private String ciudad;

    // Constructor sin argumentos (Db4o lo exige para instanciar objetos al recuperar)
    public Persona() {
    }

    public Persona(int id, String nombre, String ciudad) {
        this.id = id;
        this.nombre = nombre;
        this.ciudad = ciudad;
    }

    public int getId(){
        return id;
    }

    public void setId(int id){
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }

    @Override
    public String toString() {
        return "Persona{ID= " + id + ", nombre='" + nombre + "', ciudad='" + ciudad + "'}";
    }
}
```

Esta clase representa el “modelo de datos” en el mundo de objetos. Db4o almacenará instancias de esta clase directamente, sin necesidad de transformarlas a tablas.

El constructor sin argumentos permite que Db4o cree objetos `Persona` cuando los recupera de la base. El método `toString` facilita la visualización de los datos al imprimirlos.

### 2.2. Insertar varias personas: `DBPersonas`

Se crea `DBPersonas.java`:

```java
import java.util.ArrayList;
import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class DBPersonas {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta.");

            // Recuperar todas las instancias de Persona solo para contar y asignar IDs
            ObjectSet resultado = db.queryByExample(Persona.class);

            // Crear objetos Persona
            String[] nombres = { "Juan", "Ana", "Luis", "Pedro", "Paco" };
            String[] ciudades = { "Guadalajara", "Madrid", "Granada", "Asturias", "Madrid" };

            List personas = new ArrayList<>();

            int ids = resultado.size() + 1;
            for (int i = 0; i < nombres.length; i++) {
                Persona p = new Persona(ids, nombres[i], ciudades[i]);
                personas.add(p);
                ids++; // id incremental
                // Almacenar objetos Persona
                db.store(p);
            }

            System.out.println("Personas almacenadas en la BD.");

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Este programa:

- Abre la base `personas.db4o`.
- Recupera las personas ya existentes para saber cuántas hay y calcular ids nuevos.
- Crea varias `Persona` con ids consecutivos, nombres y ciudades.
- Llama a `db.store(p)` para guardar cada persona.
- Cierra la base de datos.

El objetivo aquí es que el alumno vea cómo se insertan objetos en una OODB de manera muy directa: se crean objetos en Java y se almacenan tal cual, con una llamada a `store`.

***

## Parte 3 – Consultas sobre `Persona`

En esta parte se exploran distintas formas de recuperar información: listar todo, buscar por nombre, ciudad, combinación de campos, prefijos y rangos.

### 3.1. Listar todas las personas

La clase `ListarPersonas` muestra todas las personas almacenadas:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class ListarPersonas {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para lectura.");

            // Recuperar todas las instancias de Persona
            ObjectSet resultado = db.queryByExample(Persona.class);

            System.out.println("Total de personas: " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

La clase `ListarTodasQBE` hace lo mismo usando un prototipo vacío:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class ListarTodasQBE {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para listar todas las personas.");

            Persona prototipo = new Persona(); // todos los campos en valor por defecto
            ObjectSet resultado = db.queryByExample(prototipo);

            System.out.println("Total de personas (QBE): " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Estos ejemplos muestran cómo recuperar todos los objetos de una clase, lo que sirve para comprobar el contenido de la base y entender qué se ha almacenado.

### 3.2. Consultas QBE: prototipos

#### 3.2.1. Buscar por nombre

`BuscarPorNombre` usa un prototipo con el nombre rellenado:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class BuscarPorNombre {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para consulta por nombre.");

            // Prototipo: sólo establecemos el nombre
            Persona prototipo = new Persona();
            prototipo.setNombre("Juan");

            ObjectSet resultado = db.queryByExample(prototipo);

            System.out.println("Personas con nombre 'Juan': " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

En QBE (Query By Example), el prototipo define qué campos se consideran en la búsqueda. Aquí se busca cualquier `Persona` cuyo `nombre` sea “Juan”.

#### 3.2.2. Buscar por ciudad

`BuscarPorCiudad` usa un prototipo con la ciudad:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class BuscarPorCiudad {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para consulta por ciudad.");

            Persona prototipo = new Persona();
            prototipo.setCiudad("Madrid");

            ObjectSet resultado = db.queryByExample(prototipo);

            System.out.println("Personas en 'Madrid': " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

#### 3.2.3. Buscar por nombre y ciudad

`BuscarPorNombreYCiudad` combina ambos campos:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class BuscarPorNombreYCiudad {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para consulta por nombre y ciudad.");

            Persona prototipo = new Persona();
            prototipo.setNombre("Juan");
            prototipo.setCiudad("Guadalajara");

            ObjectSet resultado = db.queryByExample(prototipo);

            System.out.println("Personas 'Juan' en 'Guadalajara': " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Aquí se busca a quienes coincidan simultáneamente en nombre y ciudad, mostrando cómo QBE permite combinar criterios.

### 3.3. Consultas nativas: predicados en Java

`BuscarPorPrefijoNombre` muestra cómo escribir una consulta que filtra por un criterio más complejo, en este caso, un prefijo en el nombre:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Predicate;

public class BuscarPorPrefijoNombre {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para consulta por prefijo de nombre.");

            ObjectSet resultado = db.query(new Predicate() {
                @Override
                public boolean match(Persona p) {
                    return p.getNombre() != null && p.getNombre().startsWith("A");
                }
            });

            System.out.println("Personas cuyo nombre empieza por 'A': " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Esta forma de consulta permite expresar condiciones usando el propio lenguaje Java, lo que resulta natural cuando se quieren filtros más expresivos (como prefijos, subcadenas, rangos, etc.).

### 3.4. Consultas SODA: filtros estructurados

#### 3.4.1. Buscar por nombre

`BuscarConSODA` utiliza la API SODA:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Query;

public class BuscarConSODA {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para consulta SODA.");

            Query query = db.query();
            query.constrain(Persona.class);
            query.descend("nombre").constrain("Juan");

            ObjectSet resultado = query.execute();

            System.out.println("Personas 'Juan' (SODA): " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

SODA permite construir consultas de manera estructurada, indicando la clase, el campo y las condiciones sobre ese campo.

#### 3.4.2. Buscar por rango de id

`BuscarPorRango` muestra cómo filtrar por un rango de `id`:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Constraint;
import com.db4o.query.Query;

public class BuscarPorRango {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para consulta SODA por rango de id.");

            // Definimos límites (no inclusivos)
            int idMin = 2;
            int idMax = 5;

            // Crear consulta SODA
            Query query = db.query();

            // Restringir a la clase Persona
            query.constrain(Persona.class);

            // Bajar al campo "id"
            Query subQuery = query.descend("id");

            // Añadir restricciones >= idMin y <= idMax
            Constraint cMin = subQuery.constrain(idMin).greater();
            Constraint cMax = subQuery.constrain(idMax).smaller();

            // Combinar (la combinación AND es implícita cuando se aplican sobre el mismo descend)
            cMin.and(cMax);

            // Ejecutar
            ObjectSet resultado = query.execute();

            System.out.println("Personas con id entre " + idMin + " y " + idMax + ": " + resultado.size());
            for (Persona p : resultado) {
                System.out.println(p);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Con SODA se observa cómo se pueden expresar condiciones de tipo “mayor que” y “menor que” directamente sobre campos numéricos, utilizando `greater()` y `smaller()`.

***

## Parte 4 – Actualizar y eliminar personas usando `id`

En esta parte se completan las operaciones de actualización y eliminación, utilizando el `id` como identificador lógico de las personas.

### 4.1. Actualizar ciudad de una persona por `id`

La clase `ActualizarPersonaPorId` busca una persona por `id`, modifica su ciudad y guarda de nuevo el objeto:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class ActualizarPersonaPorId {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para actualización por id.");

            // Prototipo con sólo el id
            Persona prototipo = new Persona();
            prototipo.setId(1);

            ObjectSet<Persona> resultado = db.queryByExample(prototipo);

            if (resultado.isEmpty()) {
                System.out.println("No se encontró ninguna persona con id=1.");
            } else {
                Persona encontrada = resultado.next();
                System.out.println("Persona encontrada: " + encontrada);

                // Modificar la ciudad en memoria
                encontrada.setCiudad("Monterrey");

                // Guardar de nuevo (update)
                db.store(encontrada);
                System.out.println("Persona actualizada: " + encontrada);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Aquí se observa que Db4o no requiere un comando especial para “update”: basta con recuperar el objeto, modificarlo y volver a llamar a `store`.

### 4.2. Ajustar datos utilizando `id` como criterio

La clase `IncrementarEdadDesdeId` ilustra una operación masiva basada en `id`. Aunque en el código actual `Persona` no tiene `edad`, el patrón sigue siendo válido para cualquier atributo:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class IncrementarEdadDesdeId {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para actualización de edades.");

            int idMinimo = 2;

            // Prototipo sin id (para traer todas y filtrar en memoria)
            Persona prototipo = new Persona();
            ObjectSet<Persona> resultado = db.queryByExample(prototipo);

            while (resultado.hasNext()) {
                Persona p = resultado.next();
                if (p.getId() >= idMinimo) {
                    System.out.println("Antes: " + p);
                    // Aquí se incrementaría un atributo como edad si existiera
                    // p.setEdad(p.getEdad() + 1);
                    System.out.println("Después: " + p);
                    db.store(p);
                }
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

Este ejemplo muestra cómo se puede recorrer un conjunto de objetos y aplicar cambios según condiciones sobre el `id`.

### 4.3. Eliminar una persona por `id`

`EliminarPersonaPorId` elimina a una persona específica:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class EliminarPersonaPorId {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("personas.db4o");
            System.out.println("BD personas.db4o abierta para eliminación por id.");

            int idBuscado = 3;

            Persona prototipo = new Persona();
            prototipo.setId(idBuscado);

            ObjectSet<Persona> resultado = db.queryByExample(prototipo);

            if (resultado.isEmpty()) {
                System.out.println("No se encontró ninguna persona con id=" + idBuscado);
            } else {
                Persona encontrada = resultado.next();
                System.out.println("Persona a eliminar: " + encontrada);
                db.delete(encontrada);
                System.out.println("Persona eliminada.");
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD personas.db4o cerrada.");
            }
        }
    }
}
```

De este modo, se completa el CRUD:

- Create: `DBPersonas`.
- Read: `ListarPersonas`, consultas QBE, Native y SODA.
- Update: `ActualizarPersonaPorId`, `IncrementarEdadDesdeId` (adaptable a cualquier atributo).
- Delete: `EliminarPersonaPorId`.

***

## Parte 5 – Herencia y relaciones: `Alumno` y `Curso`

El siguiente paso consiste en ampliar el modelo para representar no sólo personas aisladas, sino relaciones más complejas, como alumnos inscritos en cursos, aprovechando que Db4o almacena grafos de objetos.

### 5.1. Subclase `Alumno`

`Alumno` extiende `Persona` y añade campos específicos:

```java
public class Alumno extends Persona {

    private String matricula;
    private String carrera;

    public Alumno() {
        super();
    }

    public Alumno(int id, String nombre, String ciudad,
                  String matricula, String carrera) {
        super(id, nombre, ciudad);
        this.matricula = matricula;
        this.carrera = carrera;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    @Override
    public String toString() {
        return "Alumno{" +
               "id=" + getId() +
               ", nombre='" + getNombre() + '\'' +
               ", ciudad='" + getCiudad() + '\'' +
               ", matricula='" + matricula + '\'' +
               ", carrera='" + carrera + '\'' +
               '}';
    }
}
```

Esto muestra cómo Db4o puede trabajar con jerarquías de clases, almacenando tanto la parte común (`Persona`) como la parte específica (`Alumno`).

### 5.2. Clase `Curso` con lista de alumnos

`Curso` contiene un `id`, un nombre, una descripción y una lista de `Alumno`:

```java
import java.util.ArrayList;
import java.util.List;

public class Curso {

    private int id;
    private String nombre;
    private String descripcion;
    private List<Alumno> alumnos;

    public Curso() {
        this.alumnos = new ArrayList<>();
    }

    public Curso(int id, String nombre, String descripcion) {
        this.id = id;
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.alumnos = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public List<Alumno> getAlumnos() {
        return alumnos;
    }

    public void agregarAlumno(Alumno alumno) {
        this.alumnos.add(alumno);
    }

    @Override
    public String toString() {
        return "Curso{" +
               "id=" + id +
               ", nombre='" + nombre + '\'' +
               ", descripcion='" + descripcion + '\'' +
               ", alumnos=" + alumnos +
               '}';
    }
}
```

Esta clase sirve para ilustrar cómo se representan relaciones uno-a-muchos en una base de datos orientada a objetos: el curso mantiene referencias directas a los alumnos.

### 5.3. Crear un curso con alumnos y guardarlo

La clase `CrearCursoConAlumnos` crea alumnos y un curso, los relaciona y persiste el grafo:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;

public class CrearCursoConAlumnos {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("cursos.db4o");
            System.out.println("BD cursos.db4o abierta.");

            // Crear alumnos
            Alumno a1 = new Alumno(1, "Juan", "Guadalajara",
                                   "A001", "Ingeniería en Computación");
            Alumno a2 = new Alumno(2, "Ana", "Madrid",
                                   "A002", "Matemáticas");
            Alumno a3 = new Alumno(3, "Luis", "Granada",
                                   "A003", "Física");

            // Crear curso
            Curso curso = new Curso(101, "Bases de Datos OO",
                                    "Introducción a bases de datos orientadas a objetos");

            // Asociar alumnos al curso
            curso.agregarAlumno(a1);
            curso.agregarAlumno(a2);
            curso.agregarAlumno(a3);

            // Persistir curso (y, con él, los alumnos relacionados)
            db.store(curso);

            System.out.println("Curso y alumnos almacenados en la BD.");

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD cursos.db4o cerrada.");
            }
        }
    }
}
```

Aquí el curso es el “objeto raíz” que se almacena. Db4o se encarga de registrar también los alumnos asociados.

### 5.4. Listar cursos y alumnos

`ListarCursosYAlumnos` muestra los cursos y sus listas de alumnos:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;

public class ListarCursosYAlumnos {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("cursos.db4o");
            System.out.println("BD cursos.db4o abierta para lectura.");

            // Recuperar todos los cursos
            Curso prototipo = new Curso();
            ObjectSet<Curso> resultado = db.queryByExample(prototipo);

            System.out.println("Total de cursos: " + resultado.size());
            while (resultado.hasNext()) {
                Curso c = resultado.next();
                System.out.println("Curso: " + c.getNombre() +
                                   " (id=" + c.getId() + ")");
                System.out.println("Alumnos inscritos:");
                for (Alumno a : c.getAlumnos()) {
                    System.out.println("  " + a);
                }
                System.out.println("------------------------");
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD cursos.db4o cerrada.");
            }
        }
    }
}
```

Este ejemplo muestra cómo se navega el grafo de objetos: se recupera el curso y, a través de su lista interna, se recorren los alumnos.

### 5.5. Consultar alumnos de un curso por `id` de curso

La clase `AlumnosDeCursoPorId` utiliza una Native Query para localizar un curso por `id` y mostrar sus alumnos:

```java
import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Predicate;

public class AlumnosDeCursoPorId {

    public static void main(String[] args) {
        ObjectContainer db = null;
        try {
            db = Db4oEmbedded.openFile("cursos.db4o");
            System.out.println("BD cursos.db4o abierta para consulta.");

            int idCursoBuscado = 101;

            ObjectSet<Curso> resultado = db.query(new Predicate<Curso>() {
                @Override
                public boolean match(Curso c) {
                    return c.getId() == idCursoBuscado;
                }
            });

            if (resultado.isEmpty()) {
                System.out.println("No se encontró curso con id=" + idCursoBuscado);
                return;
            }

            Curso curso = resultado.next();
            System.out.println("Curso encontrado: " + curso.getNombre());
            System.out.println("Alumnos inscritos:");
            for (Alumno a : curso.getAlumnos()) {
                System.out.println("  " + a);
            }

        } finally {
            if (db != null) {
                db.close();
                System.out.println("BD cursos.db4o cerrada.");
            }
        }
    }
}
```

Con esta última parte, se completa un ejemplo donde:

- Se define un modelo orientado a objetos con herencia.
- Se representa una relación uno-a-muchos mediante una lista.
- Se almacena y se consulta un grafo de objetos completo en una base de datos orientada a objetos.