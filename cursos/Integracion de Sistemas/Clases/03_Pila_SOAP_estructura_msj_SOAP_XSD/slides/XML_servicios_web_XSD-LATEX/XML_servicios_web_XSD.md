#! Integración de sistemas   
##! XML para servicios web y XSD

# Estructura básica de XML

XML es un lenguaje de marcado jerárquico donde los datos se organizan en elementos anidados, cada uno delimitado por etiquetas de apertura y cierre, y con atributos opcionales.

Un documento XML bien formado debe tener exactamente un elemento raíz, no puede haber etiquetas cruzadas (ósea que no se abren y cierran sin invadir otras etiquetas) y los atributos deben ir con comillas alrededor de sus valores, en los siguientes ejemplos el primero está correcto y el segundo no. 


```xml
<producto id="1" nombre="Laptop" precio="25000.0" />
<producto id=1 nombre=Laptop />   
```

---  
Para servicios web, XML permite describir mensajes complejos (por ejemplo, una factura con muchísimos campos) de forma estructurada y con nombres explícitos para cada elemento.

Su principal desventaja es el mucho choro que incluye, pero a cambio es muy expresivo y tiene un ecosistema maduro de herramientas de validación, transformación (XSLT) y consulta (XPath, XQuery).  

# Esquemas XSD a nivel conceptual

XSD (XML Schema Definition) es un lenguaje que describe la estructura, los tipos de datos y las reglas de validación de documentos XML asociados.

Conceptualmente, un XSD define qué elementos pueden aparecer, en qué orden, cuántas veces, qué atributos admiten y qué tipos de datos tienen.  

---  
Los tipos simples describen valores atómicos (cadenas, números, fechas, booleanos), mientras que los tipos complejos agrupan elementos y atributos, permitiendo modelar estructuras anidadas.

Cuando un XML se “valida” contra su XSD, se comprueba que cumple tanto las reglas sintácticas de XML como las reglas de contenido (por ejemplo, que un precio sea numérico y obligatorio).  

# XSD y WSDL

En WSDL, las definiciones de tipos de datos de los mensajes SOAP normalmente se expresan mediante XSD, ya sea embebidos en el propio WSDL o referenciados desde archivos externos.

Cada mensaje de entrada o salida se asocia con elementos definidos en el esquema, de modo que el contrato queda fuertemente tipificado a nivel de XML. 

Esto facilita que herramientas de generación de código generen clases o estructuras en lenguajes como Java, C# o PHP que cumplen el contrato XSD/WSDL.  

# Ejemplo de XSD simple

Un XSD minimalista para un producto podría verse como sigue:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            targetNamespace="http://example.com/products"
            xmlns="http://example.com/products"
            elementFormDefault="qualified">

  <xsd:element name="Product" type="ProductType"/>

  <xsd:complexType name="ProductType">
    <xsd:sequence>
      <xsd:element name="id" type="xsd:int"/>
      <xsd:element name="name" type="xsd:string"/>
      <xsd:element name="price" type="xsd:decimal"/>
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

# Ejemplo en línea: validar XML contra XSD

Utiliza el archivo `product.xml` y el esquema `product.xsd` y usa una herramienta online como:  
- https://www.freeformatter.com/xml-validator-xsd.html  
- https://xmlformatter.org/xsd-validator/  

Procedimiento:  
1. Abrir el validador online en el navegador.  
2. Copiar y pegar el contenido de `product.xml` en el área de XML.  
3. Copiar y pegar el contenido de `product.xsd` en el área de XSD (si la herramienta lo separa) o subir ambos archivos.  
4. Pulsar el botón de “Validar” o equivalente.  
5. Revisar si el XML es válido; si no, leer los mensajes de error para corregir la estructura o los valores.  

También se puede validar desde línea de comandos con `xmllint` (en Linux/macOS):

```bash
xmllint --noout --schema product.xsd product.xml
```

Si el XML cumple el esquema, el comando termina sin errores; de lo contrario, muestra las violaciones encontradas.  

# Validar un XML que representa un contrato WSDL

Hay dos escenarios distintos:  
- Validar la instancia de mensaje SOAP que usa tipos definidos en el WSDL (lo habitual).  
- Validar el propio documento WSDL como XML y contra los esquemas oficiales de WSDL.  

Para el primer caso, muchos entornos extraen automáticamente los XSD definidos en el WSDL o referenciados, y luego permiten validar mensajes contra esos tipos.  

Para el segundo caso, existen validadores específicos de WSDL que:  
1. Verifican que el WSDL es XML bien formado.  
2. Lo comparan con los esquemas de WSDL 1.1 o 2.0 para asegurar que su estructura es correcta.  






# Ejemplo de validación contra los esquemas de WSDL: 

Un editor/validador de WSDL en línea  
- WSDL Analyzer: https://wsdl-analyzer.net  

## WSDL simple con errores para validar

Ejemplo de archivo `HelloService-with-errors.wsdl`

# Ejemplo de validación con XSD desde el WSDL

## Cómo obtener los XSD desde el WSDL

El WSDL tiene los tipos en la sección `<types>`. Ahí puede haber:

1. Esquemas XSD embebidos (dentro del propio WSDL).  
2. Esquemas XSD importados o incluidos mediante `xsd:import` o `xsd:include`.  

## Tipos embebidos

En un WSDL sencillo, podríamos tener algo como lo siguiente:

```xml
<types>
  <xsd:schema
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      targetNamespace="http://example.com/hello"
      elementFormDefault="qualified">
    <xsd:element name="sayHelloRequest" type="xsd:string"/>
    <xsd:element name="sayHelloResponse" type="xsd:string"/>
  </xsd:schema>
</types>
```

Para obtener el XSD:  
- Se copia el contenido de `<xsd:schema>...</xsd:schema>` y se pega en un archivo nuevo, por ejemplo `hello.xsd`.  
- Se le puede agregar cabecera XML (línea 1):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    targetNamespace="http://example.com/hello"
    elementFormDefault="qualified">

  <xsd:element name="sayHelloRequest" type="xsd:string"/>
  <xsd:element name="sayHelloResponse" type="xsd:string"/>

</xsd:schema>
```

`hello.xsd` se puede usar en cualquier validador XML–XSD para validar mensajes de ejemplo.

## Tipos importados

En otros WSDL, podría haber algo como:

```xml
<types>
  <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:import namespace="http://example.com/hello/types"
                schemaLocation="http://example.com/schemas/hello-types.xsd"/>
  </xsd:schema>
</types>
```

Aquí no está el XSD completo adentro, sino referenciado:  
- `schemaLocation` señala la URL (o ruta) del XSD real.  
- Para obtenerlo, hay que abrir esa URL en el navegador o descargar el archivo `hello-types.xsd`.  
- Ese archivo se usa como esquema para validación XML–XSD.


## Usar el XSD extraído con un validador XML–XSD

Supongamos que tenemos el archivo `hello.xsd` y un mensaje XML, `helloRequest.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sayHelloRequest xmlns="http://example.com/hello">
  Hola mundo
</sayHelloRequest>
```

... y esto se valida con el xml y xsd como ya se había visto.



# Actividad: XML sencillo para analizar

Fragmento con errores intencionales:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<products>
  <product id=1>
    <name>Laptop</name>
    <price>25000.00</price>
  </product>
  <product>
    <name>Mouse</name>
  </product>
</items>
```


# Mensajes SOAP: estructura y comparación con REST/JSON

## Estructura de un mensaje SOAP

Un mensaje SOAP típico es un documento XML con esta estructura general:

---
```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:prod="http://example.com/products">
  <soap:Header>
    <!-- Metadatos, seguridad, tracking, etc. -->
  </soap:Header>
  <soap:Body>
    <prod:GetProductResponse>
      <prod:Product>
        <prod:id>1</prod:id>
        <prod:name>Laptop</prod:name>
        <prod:price>25000.00</prod:price>
      </prod:Product>
    </prod:GetProductResponse>
  </soap:Body>
</soap:Envelope>
```

---
Componentes:  
- Envelope: elemento raíz que identifica el mensaje como SOAP y define namespaces.  
- Header (opcional): metadatos que pueden procesar intermediarios (autenticación, direccionamiento, políticas).  
- Body (obligatorio): contiene la operación invocada y los datos de negocio.  
- Fault (opcional dentro de Body): describe errores de procesamiento en formato estándar (código, motivo, detalles).  

## Ejemplo de Fault

```xml
<soap:Body>
  <soap:Fault>
    <faultcode>soap:Client</faultcode>
    <faultstring>Invalid product ID</faultstring>
    <detail>
      <prod:InvalidId>0</prod:InvalidId>
    </detail>
  </soap:Fault>
</soap:Body>
```

Este tipo de Fault permite a los consumidores manejar errores de manera uniforme, independientemente de la implementación interna del servicio.  

# Comparación con mensajes REST/JSON ligeros

Un JSON equivalente al ejemplo de producto sería:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 25000.0
}
```

Comparación conceptual:  
- En REST/JSON, el cuerpo suele contener directamente los datos, sin una envoltura estándar como Envelope/Body ni namespaces XML.  
- SOAP introduce capas adicionales que facilitan extensiones (seguridad, intermediarios, transacciones), pero aumentan tamaño y complejidad de parsing.  
- En REST/JSON, los contratos pueden estar descritos en OpenAPI, pero el formato JSON en sí es más flexible y menos fuertemente tipado que un XML + XSD típico.  
