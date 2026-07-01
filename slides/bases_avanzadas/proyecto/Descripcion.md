## Anuncio del proyecto final

Título del anuncio  
Proyecto final – Bases de datos avanzadas: aplicación con Db4o. 

Objetivo general  
Desarrollar una aplicación en Java que utilice una base de datos orientada a objetos implementada con Db4o, aplicando los conceptos vistos en clase (almacenamiento de objetos, consultas, herencia y relaciones entre objetos). 

Características del proyecto  
- Trabajo en equipo.  
- La aplicación puede funcionar en línea de comandos o con interfaz gráfica sencilla; el equipo decide la opción.  
- La funcionalidad debe ser alcanzable en un periodo de 3 semanas, pero suficientemente rica para requerir diseño de clases, operaciones CRUD y algunas consultas no triviales.  
- La aplicación debe usar exclusivamente Db4o como motor de base de datos orientada a objetos (no se permiten motores relacionales para la persistencia principal). 

Requisitos técnicos mínimos  
- Lenguaje: Java (versión 8 o superior). 
- Uso de Db4o: integración del jar de Db4o en el proyecto y manejo de `ObjectContainer` para abrir, cerrar y operar sobre la base de datos. 
- Definir al menos 5 clases de dominio con relaciones entre ellas (por ejemplo, herencia y asociaciones uno-a-muchos similares a `Persona`, `Alumno` y `Curso`). 
- Implementar operaciones CRUD completas sobre al menos dos de las clases principales. 
- Incluir consultas por atributos específicos usando mecanismos como Query By Example, consultas nativas o SODA, siguiendo los ejemplos vistos en la práctica `DB4O.md`. 

Alcance funcional sugerido  
Cada equipo elegirá el tema de su aplicación (por ejemplo, gestión de cursos, biblioteca, reservaciones, inventario sencillo, etc.), pero debe incluir:  
- Registro (alta) de objetos principales y relacionados. 
- Listado de todos los objetos de una clase desde la base Db4o. 
- Búsqueda filtrada por al menos dos criterios (por ejemplo, nombre y ciudad, análogo a las consultas de `Persona`). 
- Actualización de atributos (por ejemplo, cambiar ciudad, descripción, estatus). 
- Eliminación controlada de objetos (baja lógica o física, según el diseño del equipo). 

Entrega y evidencias  
- Código fuente completo del proyecto (organizado en paquetes y con nombres de clases claros). 
- Archivo(s) de la base Db4o generada(s) por la aplicación. 
- Breve documento (1–2 páginas) que describa:  
  - Modelo de clases (clases principales y relaciones).  
  - Funcionalidad implementada.  
  - Consultas soportadas y cómo se realizan (QBE, nativas, etc.). 
- Breve video (máx. 5 minutos) donde se muestren las principales operaciones de la aplicación.  

Fechas  
- Periodo de desarrollo: 3 semanas a partir de la publicación de este anuncio.  
- Fecha límite de entrega: 17 de julio 2026.  

Apoyo y recursos  
- La práctica `DB4O.md` disponible en los archivos del curso sirve como guía de integración de Db4o, diseño de clases y ejemplos de CRUD y consultas. 
- Se recomienda revisar las secciones del tutorial donde se trabajan las clases `Persona`, `Alumno` y `Curso`, y las consultas sobre `personas.db4o` y `cursos.db4o` como referencia. 
- También está el jar necesario para la práctica.
- Si necesitaran mayor detalle de db4o, pueden usar este repositorio: https://github.com/pegurnee/db4o


## Rúbrica de evaluación propuesta

Puntos (sobre 100):

1. Modelo de objetos y uso de OODB – 30 puntos  
   - Definición clara de clases de dominio, con atributos adecuados.  
   - Uso de herencia y/o relaciones uno-a-muchos similar al ejemplo de `Alumno` y `Curso`. 
   - Correcta persistencia de objetos completos en Db4o (los objetos relacionados se almacenan y recuperan completos). 

2. Operaciones CRUD y manejo de Db4o – 30 puntos  
   - Implementación correcta de alta, consulta, actualización y eliminación sobre al menos dos entidades principales. 
   - Apertura y cierre adecuados de la base (manejo de `ObjectContainer` y control de errores). 
   - Uso explícito de `db.store`, consultas sobre la base y actualización de objetos ya almacenados. 

3. Consultas y filtrado de datos – 20 puntos  
   - Implementación de listados generales (equivalentes a `ListarPersonas`). 
   - Implementación de búsquedas filtradas por uno o más campos (similar a `BuscarPorNombre`, `BuscarPorCiudad` o combinaciones). 
   - Uso de al menos una técnica de consulta vista en el tutorial (QBE, nativa o SODA). 

4. Calidad de la aplicación y entrega – 20 puntos  
   - Interfaz clara (consola o gráfica) y flujo de uso coherente.  
   - Código organizado, legible y sin errores de compilación.  
   - Documento explicativo y video que permiten comprender el diseño y verificar el funcionamiento.
