De 08_lpo_herbrand 


# Ejercicios insertados en la exposición

Una práctica consiste en construir el universo de Herbrand hasta profundidad 2 para el lenguaje con constante \(c\), función unaria \(s\) y predicado binario \(Conecta(x,y)\). El resultado esperado comienza con \(c\), luego \(s(c)\) y después \(s(s(c))\); a partir de esos términos, la base se forma con todos los átomos \(Conecta(t_1,t_2)\) donde \(t_1\) y \(t_2\) pertenecen al universo truncado. 

***
Otra práctica consiste en tomar el lenguaje con constantes \(ana\) y \(luis\), sin funciones, y predicados \(Alumno(x)\) y \(TrabajaCon(x,y)\). El universo de Herbrand queda formado solo por \(\{ana, luis\}\), mientras que la base incluye \(Alumno(ana)\), \(Alumno(luis)\) y las cuatro combinaciones posibles para \(TrabajaCon\); este caso es útil porque permite ver la construcción completa sin crecimiento explosivo. 

***
Una tercera práctica consiste en analizar satisfacibilidad para el conjunto:
- \(P(a) \lor Q(a)\)
- \(\neg P(a)\)
- \(\neg Q(a)\)

La primera cláusula exige que al menos uno de los dos átomos sea verdadero, pero las otras dos obligan a que ambos sean falsos; por tanto, el conjunto es insatisfacible en cualquier interpretación de Herbrand sobre esa base. 

***
Otra práctica:
- \(\neg Disponible(s1) \lor Responde(s1)\)
- \(Disponible(s1)\)

Aquí cualquier interpretación que satisfaga ambas debe hacer verdadero \(Responde(s1)\). El patrón es exactamente el mismo que en una cláusula proposicional, pero ya expresado como átomo de primer orden cerrado. 

***
