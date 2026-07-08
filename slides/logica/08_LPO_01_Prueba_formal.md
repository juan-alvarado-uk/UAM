# Lógica de primer orden, Prueba formal.

# Alcance

El objetivo práctico de esta sesión consiste en pasar de fórmulas con cuantificadores a expresiones manipulables dentro de una prueba formal, entender bien las reglas de instanciación y generalización, y ver cómo una fórmula universal genera instancias sobre las que se aplican las reglas proposicionales ya conocidas. 

***

# De la prueba formal proposicional a la prueba con cuantificadores

Una prueba formal en lógica de primer orden sigue conservando el mismo concepto ya conocido: una secuencia finita de líneas donde cada fórmula está justificada por una premisa o por una regla válida aplicada a líneas anteriores. La diferencia importante es que ahora las fórmulas pueden contener variables, cuantificadores y términos, por lo que la justificación debe cuidar no solo la forma del conectivo, sino también cómo se sustituyen variables por términos. 

***
Cuando aparece una fórmula como \(\forall x \, Usuario(x) \rightarrow PuedeEntrar(x)\), no se está afirmando algo de una persona específica, sino de cualquiera del dominio. La prueba formal ahora necesita reglas que permitan pasar de lo universal a casos concretos y, en sentido controlado, de un caso arbitrario a una afirmación universal; por eso las reglas de cuantificadores son la extensión natural de la deducción o conclusión lógica ya trabajada en lógica proposicional. 

***
Una analogía útil es pensar en una política de acceso de un sistema. Una regla escrita para “todo usuario autenticado” funciona como una plantilla; una prueba formal debe poder aplicar esa plantilla a Ana, a Luis o a un identificador concreto del sistema, sin perder rigor. La lógica no “adivina” ese paso: lo justifica mediante reglas precisas de instanciación y generalización. 

***

# Instanciación universal

La instanciación universal permite pasar de una afirmación universal a un caso particular. Si se sabe \(\forall x \, P(x)\), entonces puede obtenerse \(P(t)\) para cualquier término \(t\) que tenga sentido en el lenguaje, porque la fórmula universal afirma justamente que la propiedad vale para todos los individuos representables. 

***
Ejemplo: si se tiene \(\forall x \, DispositivoRegistrado(x) \rightarrow PuedeConectarse(x)\), entonces para la constante \(router1\) se puede derivar \(DispositivoRegistrado(router1) \rightarrow PuedeConectarse(router1)\). Si además se cuenta con \(DispositivoRegistrado(router1)\), entonces por modus ponens se concluye \(PuedeConectarse(router1)\); la novedad no está en el MP, sino en que antes fue necesario aterrizar la regla universal a un caso concreto. 

***
Otro ejemplo: de \(\forall x \, Estudiante(x) \rightarrow TieneCredencial(x)\) se puede derivar \(Estudiante(María) \rightarrow TieneCredencial(María)\). Si también se sabe \(Estudiante(María)\), entonces se concluye \(TieneCredencial(María)\); la estructura del razonamiento es la misma, pero ahora trabaja sobre individuos nombrados. 

***
Ejemplo breve de prueba formal:

| Línea | Fórmula                                                | Justificación                |
|-------|--------------------------------------------------------|------------------------------|
| 1     | \(\forall x \, Alumno(x) \rightarrow EntregaTarea(x)\) | Premisa                      |
| 2     | \(Alumno(Elena)\)                                      | Premisa                      |
| 3     | \(Alumno(Elena) \rightarrow EntregaTarea(Elena)\)      | Instanciación universal de 1 |
| 4     | \(EntregaTarea(Elena)\)                                | MP, 2 y 3                    |  

***
La idea importante es que una fórmula universal funciona como una regla reutilizable. En términos de ingeniería, se parece a una plantilla de validación aplicada a distintos registros o nodos de red: la regla es una, pero sus instancias son muchas. 

***

# Generalización universal

La generalización universal permite pasar de una fórmula sobre un individuo arbitrario a una afirmación universal. Si en una prueba se ha razonado sobre una variable que no depende de supuestos especiales sobre un objeto particular, entonces puede cerrarse el paso con \(\forall x\). 

***
La restricción es esencial: no se puede observar algo de un caso especial y luego elevarlo sin control a todos los casos. Dicho en lenguaje cotidiano, comprobar que “este servidor respondió bien” no autoriza concluir “todos los servidores responden bien”; la generalización solo es correcta cuando el razonamiento **no usó rasgos particulares** del elemento elegido. 

***
Ejemplo conceptual: si a partir de una hipótesis arbitraria \(x\) se demuestra \(Proceso(x) \rightarrow RequiereMemoria(x)\), sin usar propiedades particulares de ese \(x\), entonces puede escribirse \(\forall x \, (Proceso(x) \rightarrow RequiereMemoria(x))\). La lógica exige disciplina aquí porque, sin esa condición, aparecerían conclusiones falsas construidas a partir de ejemplos aislados. 

***
**La instanciación universal baja de lo general a lo particular**, mientras que la generalización universal sube de lo arbitrario a lo general. Son movimientos opuestos y complementarios dentro de la prueba formal en lógica de primer orden. 

***

# Cuantificador existencial 

La afirmación existencial expresa que hay al menos un individuo del dominio que satisface cierta propiedad. Cuando se tiene \(\exists x \, P(x)\), no se sabe quién es ese individuo; solo se sabe que existe alguno, por lo que el razonamiento debe evitar tratarlo como si ya estuviera completamente identificado. 

***
En una lectura intuitiva, \(\exists x \, AlarmaActiva(x)\) significa que hay al menos una alarma activa, pero no dice cuál. De manera parecida, si en un campus se afirma “existe una persona con credencial vencida”, todavía no se sabe si es Ana, Bruno o Carla; la información es real, pero incompleta. 

***

Jacques Herbrand (1908–1931) trabajó en los fundamentos de la lógica de primer orden y formuló lo que hoy se conoce como teorema de Herbrand, que conecta las fórmulas con cuantificadores con colecciones de fórmulas proposicionales construidas a partir de sus instancias.

---
Para la preparación del método de Herbrand interesa sobre todo comprender que la existencia tendrá que representarse más adelante de una manera que elimine la vaguedad del “algún individuo”. Por eso la transformación de fórmulas buscará reemplazar existenciales por términos testigo mediante skolemización, no como magia, sino como una técnica para dejar la fórmula en una forma operable con cláusulas. 

---
El nombre skolemización viene del lógico y matemático noruego Thoralf Skolem (1887–1963). Skolem trabajó en lógica de primer orden y en teoría de modelos, y estudió cómo convertir fórmulas en una forma prenexa especial en la que los cuantificadores existenciales se eliminan mediante nuevas funciones, las llamadas funciones de Skolem.

***

# Reglas de inferencia útiles en lógica de primer orden

Además de las reglas proposicionales ya vistas —como modus ponens, conjunción, simplificación o silogismo hipotético—, en lógica de primer orden se agregan reglas ligadas a cuantificadores. La estructura proposicional sigue funcionando dentro de las fórmulas, pero ahora convive con pasos de instanciación y de control sobre variables libres y ligadas. 

***
Un patrón frecuente de prueba tiene esta forma:

1. Fórmula universal.  
2. Instanciación a un término concreto.  
3. Premisa que activa el antecedente.  
4. Aplicación de MP o de otra regla proposicional.  

Ese patrón es importante porque muchas demostraciones en lógica de primer orden son, en realidad, combinaciones de dos niveles: primero se adapta la fórmula cuantificada y luego se aplica inferencia proposicional sobre la instancia obtenida. 

***
Ejemplo de autenticación:

1. \(\forall x \, UsuarioValido(x) \rightarrow AccesoPermitido(x)\)  
2. \(UsuarioValido(ana)\)  
3. \(UsuarioValido(ana) \rightarrow AccesoPermitido(ana)\)  
4. \(AccesoPermitido(ana)\)

---
La línea 3 se obtiene por instanciación universal y la línea 4 por modus ponens. El razonamiento conserva el mismo esqueleto formal de sesiones anteriores, pero ahora aplicado a predicados y términos. 

***

# Sustitución e instancias

Una sustitución reemplaza variables por términos del lenguaje. Esta operación es delicada porque no basta con cambiar símbolos “a ojo”; se debe respetar la estructura de la fórmula y evitar alteraciones indebidas del alcance de cuantificadores. 

***
Si el lenguaje tiene la constante \(a\) y la función \(f\), entonces desde \(\forall x \, P(x)\) pueden derivarse \(P(a)\), \(P(f(a))\), \(P(f(f(a)))\), y así sucesivamente. Esa observación parece sencilla, pero más adelante será decisiva porque el universo de Herbrand se construye precisamente con todos los términos posibles generados a partir de constantes y símbolos de función. 

***
Ejemplo breve:

- Lenguaje: constante \(a\), función unaria \(s\), predicado \(Par\).  
- De \(\forall x \, Par(s(s(x)))\) se obtiene \(Par(s(s(a)))\) si la sustitución toma \(x := a\)..  
- También se obtiene \(Par(s(s(s(a))))\) si la sustitución toma \(x := s(a)\).  

***
**Nota importante**: una afirmación universal no es una sola oración aislada, sino una fuente potencial de muchas instancias. Justamente por eso el trabajo con Herbrand se vuelve manejable cuando se fija un conjunto de términos y se estudian las instancias que nacen de ellos. 

***

# Para llevar...

Se ha visto cómo se insertan los cuantificadores en la prueba formal, cómo se pasa de universal a particular y de un caso arbitrario a una afirmación general, y cómo las sustituciones generan instancias. 

***
Con estas herramientas ya se puede empezar a ver por qué conviene tener fórmulas en formas más estructuradas y cómo, detrás de cada afirmación universal, hay un abanico de instancias que luego se verán reflejadas en términos y átomos dentro del universo de Herbrand. 
