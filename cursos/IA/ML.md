# Introducción al Aprendizaje de Máquina

---

## ¿Qué es el Aprendizaje Automático?

---

El **aprendizaje automático** (Machine Learning o ML) es una rama de la inteligencia artificial que permite a las máquinas **aprender de datos** sin ser programadas explícitamente para cada tarea específica.[1][2]

***

A diferencia de la programación tradicional donde el desarrollador escribe reglas específicas para cada problema, en machine learning la máquina identifica **patrones complejos** en millones de datos y es capaz de usar esos patrones para predecir comportamientos futuros.[3][4]

***

La idea central del ML es que existe una **relación matemática** entre cualquier combinación de datos de entrada y salida. El modelo no conoce esta relación de antemano, pero puede descubrirla si se le brindan suficientes ejemplos.[4]

***

Como si se tratara de un ser humano, las máquinas de aprendizaje deben ser capaces de **generalizar conceptos** a partir de ejemplos.[5]

***

## Relación con la Inteligencia Artificial y Deep Learning

***

Es importante comprender la relación jerárquica entre estos conceptos:[2][6]

***

**Inteligencia Artificial (IA):** Es el campo más amplio, relacionado con la creación de computadoras y máquinas que pueden razonar, aprender y actuar de manera similar a la inteligencia humana.

***

Incluye muchas disciplinas: análisis de datos, estadística, ingeniería de hardware y software, neurociencia y filosofía.[2]

***

**Machine Learning (ML):** Es un subconjunto de la IA que se enfoca en entrenar máquinas para ejecutar tareas sin estar programadas específicamente para ellas.

***

Utiliza técnicas como redes neuronales, aprendizaje supervisado y no supervisado, árboles de decisión y regresión lineal.[2]

***

**Deep Learning (DL):** Es un subconjunto del machine learning que utiliza redes neuronales profundas con múltiples capas (generalmente tres o más, pero normalmente cientos o miles) para representar los datos mediante diferentes niveles de abstracción.[7][8][3]

***

Requiere menos intervención humana que el ML tradicional, ya que puede aprender automáticamente las características relevantes de los datos.[9][7]

***

## Componentes Principales del Machine Learning

***

Para que el aprendizaje automático funcione, se requieren tres elementos fundamentales:[10]

***

**Conjunto de datos:** Los datos son la materia prima de la cual las máquinas aprenden. Sin datos de alta calidad y en cantidad suficiente, no es posible entrenar un modelo efectivo.[11][10]

***

**Algoritmo:** Es el conjunto de instrucciones y lógica que procesa los datos para extraer patrones. El estudio del machine learning se puede reducir al estudio de sus algoritmos, ya que representan las diversas técnicas para operar sobre datos y obtener modelos matemáticos.[10]

---

**Modelo:** Es el resultado de entrenar un algoritmo con datos. El modelo es lo que finalmente se usa en casos reales para hacer predicciones o clasificaciones.[11]

***

## Tipos de Aprendizaje Automático

***

Existen principalmente **cuatro tipos** de aprendizaje automático, clasificados según la naturaleza de los datos y el objetivo:[12][11][2]

***

### Aprendizaje Supervisado

***

En el aprendizaje supervisado, el algoritmo trabaja con **datos etiquetados**, es decir, datos donde ya conocemos la respuesta correcta.[13][12]

***

El modelo intenta encontrar una función que, dadas las variables de entrada, asigne la etiqueta de salida adecuada. El algoritmo aprende de un "histórico" de datos y así puede predecir el valor de salida para nuevos datos no vistos.[13]

***

Este tipo de aprendizaje es similar al aprendizaje humano bajo la supervisión de un maestro, donde el profesor proporciona ejemplos correctos que el alumno memoriza y a partir de los cuales deduce reglas generales.[14]

---

Dentro del aprendizaje supervisado existen dos categorías principales:[13]

---

- **Modelos de clasificación:** Generan una etiqueta discreta (ejemplo: identificar si un correo es spam o no spam)

***

- **Modelos de regresión:** Producen un valor numérico continuo (ejemplo: predecir el precio de una casa)

***

### Aprendizaje No Supervisado

---

En el aprendizaje no supervisado, los datos **no están etiquetados**, por lo que el algoritmo debe encontrar patrones y estructura en los datos por sí mismo.[12][13]

***

No hay respuestas correctas proporcionadas; la máquina determina correlaciones y relaciones mediante el análisis de los datos disponibles.[15]

***

El método más común es el **análisis de clústeres** (clustering), que utiliza algoritmos de agrupamiento para categorizar puntos de datos según similitudes en sus valores.[12]

***

También incluye algoritmos de asociación que identifican relaciones entre objetos dentro de grandes bases de datos.[12]

---

Este tipo de aprendizaje es especialmente valioso porque los datos no etiquetados son mucho más abundantes que los etiquetados.[14]

***

### Aprendizaje por Refuerzo

***

El aprendizaje por refuerzo trabaja mediante un sistema de **recompensa y castigo**.[16][12]

***

Un agente toma acciones en un entorno específico para alcanzar una meta predeterminada. El agente recibe retroalimentación (positiva o negativa) por sus acciones, lo que le permite perfeccionar su proceso de toma de decisiones mediante **ensayo y error**.[16][11]

***

Este método no se basa estrictamente en un conjunto de datos etiquetados (por lo que no es supervisado), pero tampoco es completamente no supervisado, ya que conocemos de antemano cuál es la recompensa esperada.[16]

***

### Aprendizaje Semi-supervisado

***

Ofrece una **combinación** entre aprendizaje supervisado y no supervisado.[12]

***

Los algoritmos se entrenan con un pequeño conjunto de datos etiquetados y un gran conjunto de datos sin etiquetar. Los datos etiquetados guían el proceso de aprendizaje para el cuerpo más grande de datos sin etiquetar.[12]

---

## El Flujo de Trabajo del Machine Learning

***

Un proyecto típico de machine learning sigue una serie de pasos sistemáticos:[17][14]

***

**Definición del problema:** Se define claramente el problema a resolver y se establecen los objetivos del proyecto. Esto implica entender el contexto, identificar las fuentes de datos relevantes y definir las métricas de rendimiento clave.[17]

***

**Recolección y compilación de datos:** Se reúnen datos de diversas fuentes (bases de datos, sensores, archivos externos), asegurando un conjunto de datos completo y representativo.[11][17]

***

**Preparación y preprocesamiento de datos:** Esta es una de las fases más importantes y consume hasta el 80% del tiempo en un proyecto real. Incluye:[18][19]

***

- **Limpieza de datos:** Manejar valores faltantes, eliminar duplicados y abordar valores atípicos[19][18]

***

- **Transformación de datos:** Normalizar, escalar y codificar variables para que estén en un formato consistente[19]

***

- **Reducción de datos:** Seleccionar las características más relevantes para reducir la complejidad[19]

***

**Análisis exploratorio de datos (EDA):** Se exploran los datos para obtener información, identificar patrones, tendencias y relaciones que ayuden a tomar decisiones sobre la selección de características y modelos.[17]

***

**Selección y entrenamiento del modelo:** Se eligen algoritmos de machine learning adecuados según los requisitos del problema. El modelo se entrena usando los datos preparados, ajustando sus parámetros mediante un proceso iterativo.[4][17]

***

Durante el entrenamiento, el algoritmo ajusta el modelo mediante una **función de pérdida** que mide los errores del modelo y técnicas de optimización como el descenso de gradientes para minimizar esos errores.[2]

***

**Evaluación y ajuste del modelo:** Se evalúa el rendimiento usando técnicas como la validación cruzada y se ajustan los **hiperparámetros** para optimizar el rendimiento.[17]

***

**Despliegue y monitoreo:** Se despliega el modelo entrenado en el entorno de producción, se integra en los sistemas existentes y se monitorea su rendimiento continuamente.[17]

***

## Conjuntos de Datos: Entrenamiento, Validación y Prueba

***

Para evaluar correctamente un modelo de machine learning, es fundamental dividir los datos en tres conjuntos distintos:[20][21][22]

***

**Conjunto de entrenamiento (Training Set):** Representa aproximadamente el 70-80% de los datos totales. Se utiliza para entrenar el modelo, es decir, para que el algoritmo ajuste sus parámetros internos.[21][20]

---

**Conjunto de validación (Validation Set):** Representa aproximadamente el 10-15% de los datos. Se usa para realizar pruebas iniciales del modelo durante el entrenamiento y para ajustar los hiperparámetros del modelo (como el número de capas en una red neuronal, la tasa de aprendizaje, etc.).[23][20]

---

Permite detectar problemas como el sobreajuste antes de la evaluación final.[20]

***

**Conjunto de prueba (Test Set):** Representa aproximadamente el 10-15% de los datos. Proporciona una evaluación final e imparcial del modelo entrenado con datos que nunca han sido vistos durante el entrenamiento ni la validación.[22][23][20]

***

La separación de estos conjuntos es crucial para verificar que el modelo pueda **generalizar** correctamente a datos nuevos y no solo memorizar los datos de entrenamiento.[21]

***

## Problemas Comunes: Underfitting y Overfitting

***

Dos de los problemas más importantes en machine learning relacionados con la capacidad de generalización son:[24][5]

***

**Underfitting (Subajuste):** Ocurre cuando el modelo es **demasiado simple** y no puede capturar los patrones importantes en los datos. El modelo tiene un desempeño pobre tanto en el conjunto de entrenamiento como en el de validación.[5][24]

***

Es como mostrarle a alguien solo una raza de perros y pretender que reconozca todas las demás razas existentes.[5]

***

**Overfitting (Sobreajuste):** Ocurre cuando el modelo es **demasiado complejo** y aprende no solo los patrones reales sino también el ruido y las particularidades específicas de los datos de entrenamiento.

***

El modelo tiene un excelente desempeño en el conjunto de entrenamiento (error cercano a cero) pero un desempeño deficiente en el conjunto de validación.[24][5]

***

Es como memorizar datos específicos sin poder aplicar el conocimiento a situaciones nuevas.[5]

***

El objetivo es encontrar un **punto medio** entre ambos extremos, donde el modelo tenga un buen desempeño tanto en el conjunto de entrenamiento como en el de validación.[24][5]

***

## Sesgo y Varianza

---

Relacionados con los problemas anteriores están los conceptos de sesgo y varianza:[25][26]

***

**Sesgo (Bias):** Se refiere a errores sistemáticos en las predicciones, donde un modelo simple puede no capturar la verdadera relación entre los datos debido a suposiciones simplistas. Un alto sesgo está asociado con el underfitting.[26][27][25]

***

**Varianza:** Describe cuánto varían las predicciones del modelo ante nuevos datos, reflejando un modelo excesivamente complejo que memoriza los datos de entrenamiento pero falla en generalizar. Una alta varianza está asociada con el overfitting.[27][25][26]

***

El **dilema sesgo-varianza** es el conflicto al intentar minimizar simultáneamente estas dos fuentes de error. Disminuir el sesgo suele aumentar la varianza y viceversa.[26][27]

***

El objetivo es encontrar un equilibrio óptimo que minimice el error total en datos no vistos.[27]

***

## Métricas de Evaluación

***

Para medir el desempeño de los modelos de machine learning, especialmente en problemas de clasificación, utilizamos varias métricas:[28][29]

***

**Accuracy (Exactitud):** Representa el porcentaje total de valores correctamente clasificados. Es útil cuando los datos están balanceados, pero puede ser engañosa con datos desbalanceados.[28]

***

**Precision (Precisión):** Indica qué porcentaje de los valores clasificados como positivos son realmente positivos. Mide la relevancia de nuestras predicciones.[30][28]

***

**Recall (Exhaustividad):** Indica cuántos valores positivos son correctamente clasificados del total de valores positivos reales. Mide qué tan completa es nuestra detección.[30][28]

***

**F1 Score:** Es la media armónica entre precisión y recall, proporcionando un balance entre ambas métricas. Es especialmente útil cuando trabajamos con datos desbalanceados.[29][28]

***

## Ejemplos Cotidianos de Machine Learning

***

El machine learning está presente en nuestra vida diaria de múltiples formas:[31][32]

---

**Motores de recomendación:** Netflix, Amazon y Spotify utilizan ML para recomendar contenido basándose en nuestros hábitos de consumo y los de millones de usuarios con perfiles similares.[32]

***

**Asistentes de voz:** Siri y Alexa utilizan ML para limpiar ruido ambiental, comprender el idioma e interpretar órdenes. Aprenden de sus errores para mejorar continuamente.[32]

***

**Detección de spam y fraude:** Twitter usa ML para combatir el spam, Facebook para detectar noticias falsas, y los bancos para detectar fraudes con tarjetas de crédito.[32]

***

**Plataformas de aprendizaje de idiomas:** Duolingo utiliza ML tanto para el reconocimiento de voz como para priorizar qué reportes de errores necesitan revisión humana mediante regresión logística.[31]

***

**Navegación y ubicación:** Los mapas utilizan ML para predecir tráfico, sugerir rutas óptimas y estimar tiempos de llegada basándose en patrones históricos.[31]

***

## Actividades Lúdicas para Comprender Machine Learning

***

Para facilitar la comprensión de estos conceptos en clase, se proponen las siguientes actividades interactivas:

***

### Actividad 1: "Aprende como una máquina" (20 minutos)

---

**Objetivo:** Experimentar el proceso de aprendizaje supervisado de forma tangible.

***

**Materiales:** Tarjetas con imágenes de diferentes frutas (manzanas, plátanos, naranjas).

***

**Desarrollo:**

***

1. Divida a los estudiantes en parejas. Uno será el "algoritmo" (con ojos vendados) y otro el "entrenador"

***

2. **Fase de entrenamiento:** El entrenador muestra físicamente varias frutas al "algoritmo" mientras dice su nombre. El estudiante vendado debe tocar cada fruta y sentir sus características (textura, forma, tamaño)

***

3. **Fase de prueba:** El entrenador entrega una fruta al azar y el "algoritmo" debe identificarla basándose en lo aprendido

***

4. **Reflexión grupal:** Discutir cómo el número de ejemplos (frutas) afecta la precisión, relacionándolo con la importancia de datos de entrenamiento suficientes

***

### Actividad 2: "La frontera de decisión" (25 minutos)

***

**Objetivo:** Visualizar los conceptos de clasificación, overfitting y underfitting.

***

**Materiales:** Pizarrón, marcadores de dos colores, cinta adhesiva de colores para el piso.

***

**Desarrollo:**

***

1. Coloque puntos de dos colores en el piso del salón representando dos clases (ejemplo: círculos rojos = estudiantes que prefieren café, círculos azules = estudiantes que prefieren té)

***

2. Pida a un voluntario que trace una línea (usando cinta adhesiva) que separe ambos grupos lo mejor posible

***

3. Muestre tres escenarios diferentes:

***

   - **Línea muy simple** (recta que no separa bien los grupos) → Underfitting

***

   - **Línea muy compleja** (zigzagueando entre cada punto individual) → Overfitting

---

   - **Línea balanceada** (curva suave que separa razonablemente ambos grupos) → Modelo adecuado

***

4. Agregue nuevos puntos (datos de validación) y verifique qué línea generaliza mejor

***

5. Discutir la importancia de encontrar el balance correcto

***

### Actividad 3: "Clasificador humano de Spam" (20 minutos)

***

**Objetivo:** Comprender el aprendizaje supervisado y las métricas de evaluación.

***

**Materiales:** Tarjetas con mensajes reales (algunos spam, otros legítimos).

***

**Desarrollo:**

***

1. Forme equipos de 3-4 estudiantes

***

2. **Fase de entrenamiento:** Muestre 10 ejemplos etiquetados (5 spam, 5 legítimos) y pida que identifiquen patrones comunes (palabras clave, urgencia excesiva, errores ortográficos)

***

3. **Fase de prueba:** Entregue 10 nuevos mensajes sin etiquetar para que los clasifiquen

***

4. Revele las etiquetas correctas y calculen juntos:

***

   - Accuracy: ¿Cuántos clasificaron correctamente del total?

***

   - Precision: De los que marcaron como spam, ¿cuántos realmente eran spam?

***

   - Recall: Del total de spam real, ¿cuántos detectaron?

***

5. Discutir qué es más importante: no perder emails importantes (alto recall) o no molestar con falsas alarmas (alta precisión)

***

### Actividad 4: "El juego de la predicción" (15 minutos)

***

**Objetivo:** Entender la diferencia entre aprendizaje supervisado y no supervisado.

***

**Materiales:** Ninguno (solo observación).

***

**Desarrollo:**

***

1. **Escenario supervisado:** Muestre una secuencia de números con etiquetas: 2→4, 5→10, 8→16. Pregunte: ¿Qué sigue para 11? (Los estudiantes deducen la regla: multiplicar por 2)

---

2. **Escenario no supervisado:** Muestre objetos mezclados de la mochila de varios estudiantes (lápices, cuadernos, celulares, llaves). Pida que los agrupen sin darles criterios. Diferentes grupos pueden agrupar por material, función, tamaño, etc.

---

3. Discutir cómo en el primer caso había una "respuesta correcta" y en el segundo caso el objetivo era encontrar estructura en los datos sin guía previa

***

### Actividad 5: Exploración con "Machine Learning for Kids" (opcional, si hay acceso a computadoras)

***

**Plataforma:** machinelearningforkids.co.uk/

***

Esta herramienta gratuita de IBM permite a los estudiantes crear proyectos interactivos donde entrenan modelos de ML para reconocer texto, imágenes, números o sonidos, y luego conectan esos modelos con juegos en Scratch.[33][34][35]

***

Es una forma práctica y visual de experimentar todo el proceso de entrenamiento y prueba de un modelo.

***

## Nota Importante sobre Algoritmos Específicos

***

En esta introducción hemos establecido los **fundamentos conceptuales** del aprendizaje automático sin profundizar en algoritmos específicos.

***

Los siguientes temas se cubrirán en clases posteriores con el detalle necesario:

***

- Zero Rule, One Rule y Naïve Bayes (algoritmos de clasificación básicos)
- Árboles de Decisión y K-Vecinos más cercanos
- Redes Neuronales (Perceptrón y Redes Multicapa)
- Máquinas de Soporte Vectorial (SVM)
- Algoritmo K-means para agrupamiento

***

Por ahora, lo importante es comprender que todos estos algoritmos son **técnicas específicas** que implementan los tipos de aprendizaje que hemos discutido (supervisado, no supervisado, etc.) y que cada uno tiene fortalezas particulares para diferentes tipos de problemas.

***

## Referencias

1. Microsoft Learn. (2025). Introducción a los conceptos de aprendizaje automático.
2. IBM. (2021). ¿Qué es machine learning?
3. Google Cloud. (2025). ¿Qué es el aprendizaje automático? Tipos y usos.
4. ISGlobal-BRGE. (2023). Introducción al Aprendizaje Automático.
5. Oracle México. (2024). ¿Qué es el machine learning?
6. Telefónica Tech. (2023). Tipos de aprendizaje en Machine Learning: supervisado y no supervisado.
7. Pure Storage. (2024). ¿Qué es un flujo de trabajo de aprendizaje automático?
8. AWS. (2025). ¿Qué es el machine learning? - Explicación de la inteligencia artificial.
9. IBM. (2023). Tipos de machine learning.
10. InvGate Blog. (2022). Machine learning: definición, métodos y ejemplos.
11. Dialektico. (2025). Machine Learning para principiantes.
12. AI Lab School. (2022). ¿Cuáles son los tipos de machine learning?
21. Machine Learning for Kids. Proyectos de aprendizaje automático. machinelearningforkids.co.uk
22. IEXE. (2023). 4 Juegos para entender la inteligencia artificial.
24. Tools CR. (2020). 8 juegos en línea que pueden enseñar ciencia de datos a los niños durante la cuarentena.
27. Algotive. (2022). 5 ejemplos de Machine Learning que usas en tu día a día y no lo sabías.
30. Universidad Europea. (2021). Ejemplos de Machine Learning.
40. Atria Innovation. Diferencias entre Inteligencia Artificial, Machine Learning y Deep Learning.
41. Coursera. (2023). Deep learning vs. Machine learning: Guía para principiantes.
42. Bismart Blog. (2019). ¿Cuál es la diferencia entre el machine learning y el deep learning?
43. UOC Blogs. (2024). Diferencia entre machine learning y deep learning.
44. BBVA. (2024). 'Deep learning' y 'machine learning': en qué se diferencian.
45. Pure Storage. (2024). ¿Qué es el preprocesamiento de datos para el aprendizaje automático?
46. Aprende Machine Learning. (2021). Qué es overfitting y underfitting y cómo solucionarlo.
47. Zendesk. (2021). Diferencia entre Machine Learning y Deep Learning.
48. Arkon Data. (2024). Preprocesamiento de datos: pasos, técnicas y su influencia en el machine learning.
49. Codificando Bits. (2024). Underfitting y Overfitting en las Redes Neuronales.
50. IBM. (2024). ¿Qué es el deep learning?
51. OpenWebinars. (2023). Importancia del preprocesamiento de datos en Data Science.
62. The Machine Learners. (2024). Métricas de Clasificación - Aprende a EVALUAR tu modelo.
64. Juan Barrios. (2024). La matriz de confusión y sus métricas.
65. Google Developers. (2025). División del conjunto de datos original | Machine Learning.
66. Mindful ML. (2024). El Sesgo y la Varianza en el Machine Learning.
67. Codificando Bits. (2025). Precision, recall y F-score para la clasificación binaria.
68. Aprende Machine Learning. (2020). Sets de Entrenamiento, Test y Validación.
69. Codelabs Academy. (2024). El equilibrio entre sesgo y varianza en el aprendizaje automático.
71. Wikipedia. (2023). Conjuntos de datos de entrenamiento, validación y prueba.
72. Wikipedia. (2024). Dilema sesgo-varianza.
77. Codificando Bits. (2024). Los sets de entrenamiento, validación y prueba.

[1](https://www.ibm.com/mx-es/think/topics/machine-learning)
[2](https://cloud.google.com/learn/what-is-machine-learning?hl=es-419)
[3](https://isglobal-brge.github.io/Aprendizaje_Automatico_1/introducci%C3%B3n-al-aprendizaje-autom%C3%A1tico.html)
[4](https://aws.amazon.com/es/what-is/machine-learning/)
[5](https://www.aprendemachinelearning.com/que-es-overfitting-y-underfitting-y-como-solucionarlo/)
[6](https://www.coursera.org/mx/articles/ai-vs-deep-learning-vs-machine-learning-beginners-guide)
[7](https://www.bbva.com/es/innovacion/deep-learning-y-machine-learning-en-que-se-diferencian-los-dos-grandes-cerebros-de-la-era-digital/)
[8](https://www.ibm.com/mx-es/think/topics/deep-learning)
[9](https://www.zendesk.com.mx/blog/machine-learning-deep-learning-diferencias/)
[10](https://dialektico.com/introduccion-machine-learning/)
[11](https://www.oracle.com/mx/artificial-intelligence/machine-learning/what-is-machine-learning/)
[12](https://www.ibm.com/mx-es/think/topics/machine-learning-types)
[13](https://ailabschool.com/cuales-son-los-tipos-de-machine-learning/)
[14](https://blog.invgate.com/es/machine-learning)
[15](https://www.apd.es/algoritmos-del-machine-learning/)
[16](https://telefonicatech.com/blog/que-algoritmo-elegir-en-ml-aprendizaje)
[17](https://www.purestorage.com/es/knowledge/machine-learning-workflow.html)
[18](https://www.purestorage.com/es/knowledge/what-is-data-preprocessing.html)
[19](https://blog.arkondata.com/es-mx/preprocesamiento-de-datos-pasos-t%C3%A9cnicas-y-su-influencia-en-el-machine-learning)
[20](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets?hl=es-419)
[21](https://www.aprendemachinelearning.com/sets-de-entrenamiento-test-validacion-cruzada/)
[22](https://codificandobits.com/blog/sets-entrenamiento-validacion-y-prueba/)
[23](https://es.wikipedia.org/wiki/Conjuntos_de_datos_de_entrenamiento,_validaci%C3%B3n_y_prueba)
[24](https://codificandobits.com/blog/underfitting-y-overfitting/)
[25](https://mindfulml.vialabsdigital.com/post/el-sesgo-y-la-varianza-en-el-machine-learning/)
[26](https://es.wikipedia.org/wiki/Dilema_sesgo-varianza)
[27](https://codelabsacademy.com/es/blog/the-bias-variance-trade-off-in-machine-learning)
[28](https://www.themachinelearners.com/metricas-de-clasificacion/)
[29](https://codificandobits.com/blog/precision-recall-f-score/)
[30](https://www.juanbarrios.com/la-matriz-de-confusion-y-sus-metricas/)
[31](https://www.algotive.ai/es-mx/blog/5-ejemplos-de-machine-learning-que-usas-en-tu-dia-a-dia-y-no-lo-sabias)
[32](https://universidadeuropea.com/blog/ejemplos-machine-learning/)
[33](https://machinelearningforkids.co.uk/?lang=es)
[34](https://www.iexe.edu.mx/desarrollo-humano/juegos-para-que-aprendan-de-inteligencia-artificial/)
[35](http://toolscr.com/blog/2020/08/13/8-juegos-en-linea-que-pueden-ensenar-ciencia-de-datos-a-los-ninos-durante-la-cuarentena/)
