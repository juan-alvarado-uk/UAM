# Práctica: contrato de API en Swagger Editor online

## Objetivo

Definir un contrato simple de API para un catálogo de productos usando OpenAPI en Swagger Editor online, con operaciones CRUD básicas sobre `/products`.  

## Paso a paso detallado

1. Acceso a Swagger Editor  
   - Abrir `https://editor.swagger.io` en el navegador.   

2. Limpiar el contenido  
   - Seleccionar todo el YAML en el panel izquierdo y borrar el contenido.  

3. Esqueleto inicial de OpenAPI  

   Escribir lo siguiente:

   ```yaml
   openapi: 3.0.0
   info:
     title: Catalogo de Productos
     version: 1.0.0
   servers:
     - url: https://api.example.com
   paths: {}
   components: {}
   ```

4. Definir el recurso `/products` y operaciones básicas  

   Sustituir `paths: {}` por:

   ```yaml
   paths:
     /products:
       get:
         summary: Listar productos
         responses:
           '200':
             description: Lista de productos
             content:
               application/json:
                 schema:
                   type: array
                   items:
                     $ref: '#/components/schemas/Product'
       post:
         summary: Crear producto
         requestBody:
           required: true
           content:
             application/json:
               schema:
                 $ref: '#/components/schemas/Product'
         responses:
           '201':
             description: Producto creado
     /products/{id}:
       get:
         summary: Obtener producto por ID
         parameters:
           - in: path
             name: id
             required: true
             schema:
               type: integer
         responses:
           '200':
             description: Producto encontrado
             content:
               application/json:
                 schema:
                   $ref: '#/components/schemas/Product'
           '404':
             description: Producto no encontrado
       put:
         summary: Actualizar producto
         parameters:
           - in: path
             name: id
             required: true
             schema:
               type: integer
         requestBody:
           required: true
           content:
             application/json:
               schema:
                 $ref: '#/components/schemas/Product'
         responses:
           '200':
             description: Producto actualizado
       delete:
         summary: Eliminar producto
         parameters:
           - in: path
             name: id
             required: true
             schema:
               type: integer
         responses:
           '204':
             description: Producto eliminado
   ```

5. Definir el esquema `Product`  

   Sustituir `components: {}` por:

   ```yaml
   components:
     schemas:
       Product:
         type: object
         required:
           - id
           - name
           - price
         properties:
           id:
             type: integer
             example: 1
           name:
             type: string
             example: Laptop
           price:
             type: number
             format: float
             example: 25000.0
   ```


6. Exploración en la interfaz de Swagger  
   - En el panel derecho, revisar cómo aparecen las operaciones agrupadas por `/products`.  
   - Usar “Try it out” para ver ejemplos de cuerpos JSON basados en el esquema `Product`.  

