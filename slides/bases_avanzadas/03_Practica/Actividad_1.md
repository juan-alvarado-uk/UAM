## Actividad: Detectar límites del modelo relacional en sistemas actuales

**Objetivo:** que los equipos identifiquen, en casos realistas, dónde el modelo relacional básico empieza a tensarse por estructuras complejas, listas variables y jerarquías, usando evidencia en lugar de afirmaciones generales.

1. **Formación de equipos y asignación de dominios**  
   Cada equipo elige un dominio entre los siguientes (o similares):  
   - Red social con publicaciones, historias, comentarios anidados, reacciones y seguidores.  
   - Plataforma de video con listas, subtítulos, recomendaciones, métricas y comentarios jerárquicos.  
   - Comercio electrónico con catálogos heterogéneos, eventos de navegación y perfiles personalizados.  
   - Sistema de autenticación con sesiones, dispositivos, factores múltiples y auditoría de accesos. 

2. **Diseño relacional simple del dominio asignado**  
   - Cada equipo propone un esquema relacional básico: tablas principales, tablas auxiliares y claves externas mínimas necesarias.  
   - El diseño debe intentar ser “limpio” y normalizado en la medida de lo posible (sin concentrarse aún en rendimiento). 
   - Pueden usarse herramientas de IA generativa para auxiliarse en el diseño. 

3. **Detección de síntomas de tensión**  
   Sobre su propio diseño, cada equipo marca y anota:  
   - Dónde se requieren muchas tablas para representar un solo concepto central (por ejemplo, usuario o contenido).  
   - Dónde aparecen listas de tamaño variable que obligan a crear tablas auxiliares adicionales.  
   - Qué columnas se ven opcionales o vacías para muchos registros.  
   - Qué consultas típicas exigirían múltiples uniones para reconstruir una unidad conceptual que en el dominio se percibe como única.  

4. **Presentación**  
   Cada equipo presenta una breve presentación donde responde:   
   - Elementos complejos del dominio (objetos compuestos, listas, jerarquías).  
   - Indicios concretos de tensión del modelo tabular simple (tablas auxiliares, columnas vacías, uniones numerosas).  
   - Mostrar ejemplos específicos de dónde y cómo el diseño relacional comienza a alejarse de la forma natural del dominio.
   - Conclusión: ¿el modelo relacional simple parece suficiente, suficiente solo con muchas adaptaciones, o conceptualmente limitado desde el inicio?
   