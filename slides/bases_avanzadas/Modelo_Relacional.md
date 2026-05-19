# Modelo Relacional


(0.53,0.1)
[wd=8.5cm,ht=7.3cm,sep=0.5cm]hvidbox
10
0.4pt
(0.53,0.1)
[wd=8.5cm,sep=0.5cm]hvidbox
Modelo Relacional
Para el diseño de bases de datos.
Juan Alvarado
1(14.5,11.38)
%


[hvid]
## OBJETIVOS
- Conocer el modelo relacional y conocer el proceso para pasar de una representación Entidad-Relación a una representación en el modelo Relacional.


[fragile, hvid]
## Modelo relacional
# Modelo relacional


[fragile, hvid]
## Modelo relacional
Una base de datos relacional consiste en un conjunto de tablas, a cada una de las cuales se le asigna un nombre exclusivo.
Cada fila de la tabla representa una relación entre un conjunto de valores.
Dado que cada tabla es un conjunto de dichas relaciones, hay una fuerte correspondencia entre el concepto de tabla y el concepto matemático de relación, del que toma su nombre el modelo de datos relacional.


[fragile, hvid]
## Transformación de un Diagrama E-R a tablas
# REDUCCIÓN DE UN ESQUEMA E-R A TABLAS


[fragile, hvid]
## Transformación de un Diagrama E-R a tablas
Una base de datos que se ajusta a un esquema de bases de datos E-R se puede representar por una colección de tablas.
Los modelos E-R y el de bases de datos relacionales son representaciones abstractas y lógicas de empresas del mundo real.


[fragile, hvid]
## Transformación de un Diagrama E-R a tablas
Debido a que los dos modelos emplean principios de diseño similares, se puede convertir un diseño E-R en un diseño relacional.
Convertir una representación de bases de datos de un diagrama E-R a un formato de tablas es la base para la derivación de un diseño de bases de datos relacional desde un diagrama E-R.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
# Representación tabular de los conjuntos de entidades fuertes


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
Sea E un conjunto de entidades fuertes con los atributos descriptivos `a_1 , a_2,…,a_n`.
Esta entidad se representa mediante una tabla llamada `E` con `n` columnas distintas, cada una de las cuales corresponde a uno de los atributos de `E`.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
Cada fila de la tabla corresponde a una entidad del conjunto de entidades E.
Considérese el conjunto de entidades préstamo del diagrama E-R siguiente.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
![](modelo_relacional_imgs/img_01.png)


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
![](modelo_relacional_imgs/img_02.png)


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
`D_1` denota el conjunto de todos los números de préstamo y `D_2` denota el conjunto de todos los saldos.
Cualquier fila de la tabla préstamo debe consistir en una tupla(`v_1`,`v_2`), donde `v_1` es un número de préstamo (es decir, `v_1` está en el conjunto `D_1`) y `v_2` es un importe (es decir, `v_1` está en el conjunto `D_2`).


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
En general, la tabla préstamo contendrá sólo un subconjunto del conjunto de todas las filas posibles.
El conjunto de todas las filas posibles de préstamo es el producto cartesiano de `D_1` y `D_2`, denotado por
`D_1` × `D_2`


[fragile, hvid]
## Representación tabular de los conjuntos de entidades fuertes
En general, si se tiene una tabla de n columnas, se denota el producto cartesiano de `D_1, D_2,…,D_n` por
`D_1` × `D_2` × … × `D_n-1` × `D_n`


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
# Representación tabular de los conjuntos de entidades débiles


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
A es un conjunto de entidades débiles con los atributos `a_1, a_2,…,a_m`.
B es el conjunto de entidades fuertes del que A depende.
La clave primaria de B es el conjunto de atributos `b_1, b_2,…,b_n`.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
Se representa el conjunto de entidades A mediante una tabla llamada *A* con una columna por cada uno de los atributos del conjunto:
`(a_1, a_2,…,a_m)  (b_1, b_2,…,b_n)`


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
Por ejemplo, considérese el conjunto de entidades pago del siguiente diagrama E-R.
Este conjunto de entidades tiene tres atributos: ***número-pago***, ***fecha-pago*** e ***importe-pago***.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
![](modelo_relacional_imgs/img_03.png)


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
La clave primaria del conjunto de entidades préstamo, de la que pago depende, es ***número-préstamo***.
Entonces, pago se representa mediante una tabla con cuatro columnas **número-préstamo, número-pago, fecha-pago e importe-pago**


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
![](modelo_relacional_imgs/img_04.png)


[fragile, hvid]
## Representación tabular de los conjuntos de relaciones
# Representación tabular de
# los conjuntos de relaciones


[fragile, hvid]
## Representación tabular de los conjuntos de relaciones
Sea R un conjunto de relaciones,
sean `a_1, a_2,…,a_m` el conjunto de atributos formados por la unión de las claves primarias de cada uno de los conjuntos de entidades que participan en R, y
sean `b_1, b_2,…,b_n` los atributos descriptivos de R (si los hay).


[fragile, hvid]
## Representación tabular de los conjuntos de relaciones
El conjunto de relaciones se representa mediante una tabla llamada R con una columna por cada uno de los atributos del conjunto:
`(a_1, a_2,…,a_m)  (b_1, b_2,…,b_n)`


[fragile, hvid]
## Representación tabular de los conjuntos de relaciones
Como ejemplo, considérese el conjunto de relaciones **prestatario** del siguiente diagrama E-R.
Este conjunto de relaciones involucra los dos siguientes conjuntos de entidades:
- cliente, con la clave primaria **id-cliente**.
- préstamo, con la clave primaria **número-préstamo**.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
![](modelo_relacional_imgs/img_01.png)


[fragile, hvid]
## Representación tabular de los conjuntos de relaciones
Como el conjunto de relaciones no tiene atributos, la tabla prestatario se forma con dos columnas **id-cliente** y **número-préstamo**.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
![](modelo_relacional_imgs/img_05.png)


[fragile, hvid]
%     ## Representación tabular de los conjuntos de relaciones
%
%
% ################# Figura 2.26 Tabla prestatario
%
%
%
% 
%
%
%


[fragile, hvid]
## Redundancia de tablas
# Redundancia de tablas


[fragile, hvid]
## Redundancia de tablas
Un conjunto de relaciones uniendo un conjunto de entidades débiles con el correspondiente conjunto de entidades fuertes es un caso especial.
Estas relaciones son muchos a uno y no tienen atributos descriptivos.


[fragile, hvid]
## Redundancia de tablas
Además, la clave primaria de un conjunto de entidades débiles incluye la clave primaria del conjunto de entidades fuertes.
En el diagrama E-R (siguiente), el conjunto de entidades débiles pago depende del conjunto de entidades fuertes préstamo a través del conjunto de relaciones pago-préstamo.


[fragile, hvid]
## Representación tabular de los conjuntos de entidades débiles
![](modelo_relacional_imgs/img_03.png)


[fragile, hvid]
## Redundancia de tablas
La clave primaria de pago es \**número-préstamo, número-pago**\ y
la clave primaria de préstamo es \**número-préstamo**\.
Como **pago-préstamo** no tiene atributos descriptivos, la tabla para **pago-préstamo** tendría dos columnas, **número-préstamo** y **número-pago**.


[fragile, hvid]
## Redundancia de tablas
La tabla para el conjunto de entidades pago tiene cuatro columnas, **número-préstamo, número-pago, fecha-pago e importe-pago**.
Cada combinación (**número-préstamo, número-pago**) en **pago-préstamo** también se encontraría en la tabla **pago**, y viceversa.


[fragile, hvid]
## Redundancia de tablas
Por tanto, la tabla (para la relación) pago-préstamo es redundante.
En general, la tabla para el **conjunto de relaciones** que une un **conjunto de entidades débiles** con su correspondiente **conjunto de entidades fuertes** es redundante y no necesita representación tabular.


[fragile, hvid]
## Redundancia de tablas
Combinación de tablas: Considérese el siguiente diagrama E-R
![](modelo_relacional_imgs/img_06.png)


[fragile, hvid]
%     ## Redundancia de tablas
%
%  ######################  de la Figura 2.27.
%
%
%
% 
%
%
%


[fragile, hvid]
## Redundancia de tablas
La doble línea del diagrama E-R indica que la participación de **cuenta** en **cuenta-sucursal** es total.
Entonces, una cuenta no puede existir sin estar asociada con una sucursal particular.


[fragile, hvid]
## Redundancia de tablas
Además, el conjunto de relaciones **cuenta-sucursal** es muchos a uno desde **cuenta** a **sucursal**.
Por lo tanto, se puede combinar la tabla para **cuenta-sucursal** con la tabla para **cuenta** y se necesitan sólo las dos tablas siguientes:


[fragile, hvid]
## Redundancia de tablas
- **cuenta**, con los atributos **número-cuenta**, **saldo** y **nombre-sucursal**
- **sucursal**, con los atributos **nombre-sucursal**, **ciudad-sucursal** y **activo**


[fragile, hvid]
## Atributos compuestos
Los atributos compuestos se manejan creando un atributo separado para cada uno de los atributos componentes; no se crea una columna separada para el propio atributo compuesto.


[fragile, hvid]
## Atributos compuestos
Por ejemplo, si dirección es un atributo compuesto del conjunto de entidades cliente y los componentes de dirección son **ciudad** y **calle**.
La tabla generada de **cliente** contendría las columnas **calle-dirección** y **ciudad-dirección**; no hay una columna separada para dirección.


[fragile, hvid]
## Atributos multivalorados
En los ejemplos mostrados se ha visto que los atributos en un diagrama E-R generalmente se asocian directamente en columnas para las tablas apropiadas.
Los atributos multivalorados, sin embargo, son una excepción; para estos atributos se crean tablas nuevas.


[fragile, hvid]
## Atributos multivalorados
La creación de estas tablas para atributos multivalorados es simple.
Para un atributo multivalorado M se crea una tabla T con una columna C que corresponde a la clave primaria del conjunto de entidades o conjunto de relaciones del que M es atributo.
Por ejemplo, (otra vez) el atributo dirección, pero suponiendo el escenario en el que un cliente puede tener muchas direcciones.


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
# Estructura básica de Bases de datos relacionales


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
Considérese la tabla cuenta siguiente:
![](modelo_relacional_imgs/img_07.png)


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
La tabla tiene tres encabezados para cada columna: **número-cuenta**, **nombre-sucursal** y **saldo**.
Siguiendo la terminología del modelo relacional se puede hacer referencia a estas cabeceras como atributos.


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
Para cada atributo hay un conjunto de valores permitidos, llamado dominio de ese atributo.
En general, **cuenta** sólo contendrá un subconjunto del conjunto de todas las filas posibles.
Por tanto, **cuenta** es un subconjunto de
`D_1 × D_2 × D_3`


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
En general, una tabla de n atributos debe ser un subconjunto de
`D_1 × D_2 × … × D_n – 1 × D_n`


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
Como las tablas son esencialmente relaciones, se suelen utilizar los términos matemáticos relación y tupla en lugar de los términos tabla y fila.


[fragile, hvid]
%     ## Estructura básica de Bases de datos relacionales
%
% **Esquema de la base de datos**
%
% Cuando se habla de bases de datos se debe diferenciar entre el **esquema de la base de datos**, o diseño lógico de la misma, y el **ejemplar de la base de datos**, que es una captura instantánea de los datos de ella en un momento dado.
%
%
%


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
**Claves**
Los conceptos de superclave, de clave candidata y de clave primaria, también son aplicables en el modelo relacional. (ver diagrama cuenta-sucursal )
Tanto \nombre-sucursal\ como \nombre-sucursal, ciudad-sucursal\ son superclaves.
\nombre-sucursal, ciudad-sucursal\ no es una clave candidata porque \nombre-sucursal\ es un subconjunto de \nombre-sucursal, ciudad-sucursal\ y \nombre-sucursal\ es una superclave.


[fragile, hvid]
## Estructura básica de Bases de datos relacionales
Por lo tanto, (como ya hemos encontrado las llaves mínimas) nombre-sucursal es una clave candidata, y será la elección de clave primaria para el diseño de la tabla.
El atributo ciudad-sucursal no es una superclave, dado que dos sucursales de la misma ciudad pueden tener nombres diferentes (y diferentes volúmenes de activos).


[fragile, hvid]
## Diagramas de esquema
# Diagramas de esquema relacional


[fragile, hvid]
## Diagramas de esquema
Un esquema de bases de datos, junto con las dependencias de clave primaria y externa, se puede mostrar gráficamente mediante diagramas de esquema relacional.
No se debe confundir un diagrama de esquema relacional con un diagrama Entidad-Relación.
No son la misma cosa.


[fragile, hvid]
## Diagramas de esquema
En particular, los diagramas E-R no muestran explícitamente los atributos clave externa, mientras que los diagramas de esquema relacional sí lo hacen.


[fragile, hvid]
## Ejemplo: Diagrama E-R (bancario)
Transformar a Diagrama de esquema relacional
![](modelo_relacional_imgs/img_08.png)


[fragile, hvid]
## Ejemplo: Diagrama esquema relacional (bancario)
![](modelo_relacional_imgs/img_09.png)


[hvid]
%## Requerimientos
%
%
%        - Un requerimiento es una declaración de cómo un producto futuro será o cómo se comportará.
%        - Deben ser específicos, claros y no ambiguos.
%        - Los requerimientos de software se clasifican en
%
%                - Requerimientos de negocio (**funcionales**) y
%                - Requerimientos técnicos (**no funcionales**)
%
%
%
%
%            
%
%


[hvid]
%## Requerimientos
%
%
%        - Los requerimientos funcionales tienen que ver con las operaciones que realiza el sistema, con sus funciones.
%        - Los requerimientos no funcionales se relacionan con las restricciones o condiciones a las que el sistema debe apegarse.
%
%
%
%            
%
%


[hvid]
%## CMMI
%
%
%        - Existen estándares que se pueden usar para mantener un control del desarrollo de software no solo en la definición de requerimientos, sino en todo el proceso.
%        - CMMI (Capability Maturity Model Integration) para Desarrollo, Versión 1.3
enciteProductCMMIfor2010 es un ejemplo de este tipo de estándares.
%        - En lo particular, en CMMI para desarrollo en el nivel 3 de madurez, podemos encontrar las siguientes áreas de proceso
%
%
%    - Desarrollo de requerimientos (RD) (proceso de ingeniería)
%    - Gestión de requerimientos (REQM) (proceso de administración)
%
%
%
%
%


[hvid]
%## CMMI
%     El propósito del desarrollo de requerimientos (RD) es obtener, analizar y establecer los requerimientos. Incluye las siguientes metas específicas (Specific Goals, **SG**) y prácticas específicas (Specific Practice, **SP**) para el logro de estas metas.
%
%
%    - [SG 1] Desarrollar los requerimientos del cliente.
%
%        - [SP 1.1] Obtener necesidades.
%        - [SP 1.2] Transformar las necesidades de las partes.
%
%    - [SG 2] Desarrollar los requerimientos del producto.
%
%        - [SP 2.1] Establecer requerimientos de productos y componentes de productos.
%        - [SP 2.2] Asignar requerimientos de componentes de productos.
%        - [SP 2.3] Identificar los requerimientos de la interfaz.
%
%
%
%
%


[hvid]
%## CMMI
%
%
%    - [SG 3] Analizar y validar requerimientos.
%
%        - [SP 3.1] Establecer conceptos y escenarios operativos.
%        - [SP 3.2] Establecer una definición de los atributos de calidad y funcionalidad requeridos.
%        - [SP 3.3] Analizar requerimientos.
%        - [SP 3.4] Analizar los requerimientos para lograr el equilibrio.
%        - [SP 3.5] Validar requerimientos.
%
%
%
%
%


[hvid]
%## Recolección de datos
%Para la definición de requerimientos es necesario conseguir información apropiada.  señalan que para ello se pueden utilizar; métodos tradicionales, de grupo, prototipos, técnicas cognitivas, entre otras. Un paso previo a la recolección de datos es la identificación de las partes interesadas.
%
%Tanto la identificación de partes interesadas, así como la recolección de datos y análisis de actividades corresponden a actividades del análisis sociotécnico.
%
%El éxito en la definición de requerimientos depende de varios factores, entre ellos, las técnicas de recolección de datos y su correcta aplicación.
%
%


[hvid]
%## Análisis de requerimientos
%Debe considerarse cuidadosamente cómo registrar los datos, así como el análisis, interpretación y presentación de los mismos. Este análisis debe ocurrir poco después de que se recopilen los datos, incluyendo sesiones piloto posteriores o prototipos para mostrar funcionalidades.
%
%El objetivo de estas tareas es identificar criterios importantes de las partes interesadas. Para ello los resultados y datos recopilados se deben discutir y presentar. Dentro de las opciones de presentación se pueden incluir: diagramas de flujo de datos, diagramas de flujo de trabajo, gráficos, diagramas, nubes de palabras, etc.
%
%


[hvid]
% ## Análisis de requerimientos
% El propósito de este trabajo es entender los resultados. Separar lo que dicen los datos (números, hechos) y lo que se cree que significan (interpretación) es crucial.
%
% La ambigüedad de las necesidades de las partes interesadas ocurre cuando el personal asume que comprende las necesidades y no las analiza con la intención de eliminar declaraciones que pueden tener más de un posible significado o interpretación
enciteSchmidt13.
%
% Debe asegurarse de que las interpretaciones son razonables y creíbles, ¿Por qué significa lo que se cree que significa?, ¿Cómo se puede racionalizar esta conclusión?
%


[hvid]
% ## Slide with 2 coloumns
%
%
%             - Bullet 1
%             - Bullet 2
%
%
%
%
%             - Bullet 3
%             - Bullet 4
%             - Bullet 5
%
%
%


[hvid]
% ## Slide with a coloumn and an image
%
%
%             - Bullet 1
%             - Bullet 2
%
%
%
%             
%
%


[hvid]
% ## Slide with large image
%
%     
%


[billede]
(0,0.77)
[wd=7.8cm,sep=0.3cm]rodbox
¡Gracias!


[billede]
%     (0.57,0.4)
%         [wd=7.8cm,sep=0.3cm]rodbox
%         Here is some text and a list.
%
%                 - Bullet 1
%                 - Bullet 2
%                 - Bullet 3
%                 - Bullet 4
%
%
%
%


[rod]
%     0 ``
%     \\
%
%     0 Prediction is very difficult, especially if it's about the future.
%     \\
%
%     0 Niels Bohr
%


[rod]
%
%     !
%         r l
%             **Research** & Forskning \\
%             **Education** & Uddannelse \\
%             **Exchange of knowdledge** & Forskningsformidling \\
%
%
%


[hvid, allowframebreaks]
% ## Referencias
%
%
