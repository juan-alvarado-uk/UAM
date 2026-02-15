# Mi Presentación


## Introducción

Este es el contenido de introducción.

- Punto 1
- Punto 2
- Punto 3



### Detalles

Aquí hay más detalles específicos.

## Tabla de Datos

| Nombre | Edad | Ciudad |
|--------|------|--------|
| Ana    | 25   | CDMX   |
| Luis   | 30   | GDL    |
| María  | 28   | MTY    |

## Código

```python
def ejemplo():
    print("Hola mundo")
    return True
```


# Estructura básica de XML

XML es un lenguaje de marcado jerárquico donde los datos se organizan en elementos anidados, cada uno delimitado por etiquetas de apertura y cierre, y con atributos opcionales.

Un documento XML bien formado debe tener exactamente un elemento raíz, no puede haber etiquetas cruzadas (ósea que no se abren y cierran sin invadir otras etiquetas) y los atributos deben ir con comillas alrededor de sus valores, en los siguientes ejemplos el primero está correcto y el segundo no. 


```xml
<producto id="1" nombre="Laptop" precio="25000.0" />
<producto id=1 nombre=Laptop />   
```

Para servicios web, XML permite describir mensajes complejos (por ejemplo, una factura con muchísimos campos) de forma estructurada y con nombres explícitos para cada elemento.

Su principal desventaja es el mucho choro que incluye, pero a cambio es muy expresivo y tiene un ecosistema maduro de herramientas de validación, transformación (XSLT) y consulta (XPath, XQuery).  

# Esquemas XSD a nivel conceptual

XSD (XML Schema Definition) es un lenguaje que describe la estructura, los tipos de datos y las reglas de validación de documentos XML asociados.

Conceptualmente, un XSD define qué elementos pueden aparecer, en qué orden, cuántas veces, qué atributos admiten y qué tipos de datos tienen.  

Los tipos simples describen valores atómicos (cadenas, números, fechas, booleanos), mientras que los tipos complejos agrupan elementos y atributos, permitiendo modelar estructuras anidadas.

Cuando un XML se “valida” contra su XSD, se comprueba que cumple tanto las reglas sintácticas de XML como las reglas de contenido (por ejemplo, que un precio sea numérico y obligatorio).  
