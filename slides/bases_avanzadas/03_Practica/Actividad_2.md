# Actividad 2: Rediseño semántico usando EER

**Objetivo:** Reutilizar el trabajo de la Actividad "Detectar límites del modelo relacional en sistemas actuales" para rediseñar, con apoyo en EER y conceptos semánticos, las partes del dominio donde el modelo relacional básico mostró mayor tensión.

1. **Elegir un caso previo**  
   Cada equipo retoma el dominios trabajado en la actividad previa donde se identificaron problemas de estructuras complejas, listas variables o columnas vacías. 

2. **Diagnóstico con lenguaje semántico**  
   A partir del diseño relacional que ya hicieron, el equipo debe:  
   - Localizar las entidades que se perciben como “objetos compuestos” (por ejemplo, usuario con dispositivos, sesiones, métodos de autenticación).  
   - Identificar posibles supertipos y subtipos (por ejemplo, contenido como supertipo de video, imagen, transmisión en vivo; persona como supertipo de estudiante, docente, administrativo). 
   - Señalar relaciones complejas que podrían tratarse como agregaciones (por ejemplo, “usuario‑video‑comentario” en una plataforma de video o “cliente‑pedido‑detalle” en comercio electrónico). 

3. **Rediseño en modelo EER**  
   Con esa base, cada equipo elabora un diagrama EER que:  
   - Defina supertipos y subtipos con herencia clara de atributos y relaciones.  
   - Use agregación para encapsular relaciones complejas en entidades de nivel superior.  
   - Muestre dominios de atributos que aclaren el tipo de valores permitidos donde sea relevante. 

4. **Comparación entre modelos**  
   Finalmente, el equipo prepara una breve comparación entre el diseño relacional original y el diseño EER:  
   - ¿Qué síntomas de tensión del modelo relacional se alivian con el rediseño semántico?  
   - ¿En qué partes el EER mejora la comprensión del dominio, y en cuáles el modelo relacional sigue siendo suficiente para la implementación física?  
   - ¿Qué decisiones de generalización, especialización o agregación consideran más importantes para expresar mejor el significado del sistema?


