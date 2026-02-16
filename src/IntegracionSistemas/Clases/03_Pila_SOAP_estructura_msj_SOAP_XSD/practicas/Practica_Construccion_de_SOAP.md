# Práctica: SOAP/XML básico

## Objetivo

Dado un mensaje REST/JSON sencillo, escribir el equivalente como mensaje SOAP/XML básico, centrado en la estructura Envelope–Header–Body y en la traducción de campos.  

## Paso a paso detallado

1. Preparación del entorno  
   - Verificar que cada alumno tenga un editor de texto (VS Code, Notepad++, Sublime, etc.) y un navegador.  
   - Crear una carpeta local `soap_lab/` donde se guardarán los archivos del ejercicio.  

2. JSON de partida  
   - Usar el siguiente JSON y guardarlo como `producto.json`:

     ```json
     {
       "id": 1,
       "name": "Laptop",
       "price": 25000.0
     }
     ```

3. Análisis del JSON  
   - Identificar el recurso principal (Product) y sus campos: id (entero), name (cadena), price (número).  
   - Discutir brevemente qué tipo de operación podría estar representando (p. ej., respuesta a “obtener producto”).  

4. Crear el archivo XML  
   - En el editor, crear `producto_soap.xml` con la declaración XML:

     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     ```

5. Definir el Envelope y namespaces  
   - Agregar el elemento raíz:

     ```xml
     <soap:Envelope
         xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
         xmlns:prod="http://example.com/products">
     ```

   - Mantener sangrías claras para facilitar la lectura.  

6. Añadir Header (vacío para esta práctica)  
   - Dentro de Envelope, añadir:

     ```xml
       <soap:Header>
         <!-- Sin contenido en este ejercicio -->
       </soap:Header>
     ```

7. Añadir Body con operación y datos  

   Fragmento completo del Body esperado:

   ```xml
       <soap:Body>
         <prod:ProductResponse>
           <prod:Product>
             <prod:id>1</prod:id>
             <prod:name>Laptop</prod:name>
             <prod:price>25000.0</prod:price>
           </prod:Product>
         </prod:ProductResponse>
       </soap:Body>
   ```

8. Cerrar el Envelope  

   ```xml
     </soap:Envelope>
   ```

   - Verificar que las etiquetas estén correctamente anidadas y cerradas.  

9. Validación básica  
   - Copiar el XML y pegarlo en un validador de XML online para confirmar que es bien formado.  
   - Corregir cualquier error de anidamiento o de nombres de etiqueta.

10. ¿Cómo sería el body para la petición (Request) de un producto?

11. ¿Cómo se sería el WSDL considerando sólo la operación de request?

12. Revisión en parejas  
    - Intercambiar archivos y revisar que:  
      - Exista un solo Envelope.  
      - Header y Body estén presentes.  
      - Los datos sean equivalentes al JSON original.
      - Que el WSDL sea correcto

