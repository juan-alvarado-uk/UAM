6. Cómo queda el editor después de todos los pasos

El contenido completo del panel izquierdo debe verse así:

```yaml
openapi: 3.0.0
info:
  title: Catalogo de Productos
  version: 1.0.0
servers:
  - url: https://api.example.com
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