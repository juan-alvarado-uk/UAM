# Práctica: API REST con FastAPI, cliente Python y cliente Java generado

## 1. Preparación del entorno con conda (para FastAPI y cliente Python)

### 1.1 Instalar/Verificar instalación de conda

1. Abrir una terminal:  
   - Windows: Anaconda Prompt o terminal.  
   - macOS / Linux: Terminal.  
2. Ejecutar:

   ```bash
   conda --version
   ```
   
Si aparece un número de versión, conda está instalado.

Si no aparece un número de versión hay que instalar miniconda desde [aquí](https://www.anaconda.com/download)

**NOTA:** Asegúrense de que es miniconda y no Anaconda porque Anaconda es muy grande y tiene demasiadas cosas que tal vez no necesiten por ahora.

Usaremos conda para crear un entorno aislado de trabajo, y no estropear el ambiente base (de python) de sus máquinas.

***

### 1.2 Crear y activar el entorno de la práctica

```bash
conda create -n fastapi-client -y
conda activate fastapi-client
```

Con esto tendremos un entorno virtual dedicado a esta práctica (`fastapi-client`), evitando contaminar otras instalaciones de Python. 


### 1.3 Instalar dependencias dentro del entorno

```bash
conda install -y fastapi uvicorn requests
```

Esto es para instalar los paquetes necesarios para desarrollar la API y el cliente Python:  
- FastAPI (framework web). 
- Uvicorn (servidor ASGI). 
- Requests (cliente HTTP en Python). 

***

## 2. Estructura del proyecto

En la carpeta donde guardarás la práctica, crear la siguiente estructura de directorios:

```text
fastapi-client-practica/
  server/
  client/
```

***

## 3. Implementar la API REST con FastAPI

### 3.1 Definir la API básica (CRUD de productos)

Dentro de `fastapi-client-practica/server/` crear un archivo `main.py` con el siguiente contenido.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

# "Base de datos" en memoria
products_db: list[Product] = []

@app.get("/products", response_model=List[Product])
def list_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for p in products_db:
        if p.id == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product):
    if product.price < 0.0:
        raise HTTPException(status_code=400, detail="Price must be positive")

    for p in products_db:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product ID already exists")

    products_db.append(product)
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated: Product):
    for idx, p in enumerate(products_db):
        if p.id == product_id:
            products_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    for idx, p in enumerate(products_db):
        if p.id == product_id:
            products_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Product not found")
```

Con esto hemos definido un conjunto de endpoints REST (GET, POST, PUT, DELETE) sobre un recurso `Product`, con validación básica y códigos HTTP adecuados.

***

### 3.2 Ejecutar el servidor FastAPI

Desde `fastapi-client-practica`:

```bash
cd server
uvicorn main:app --reload
```

El servidor quedará en `http://127.0.0.1:8000`.

Con esto hemos expuesto la API como un servicio HTTP real que otros clientes podrán consumir. 

***

### 3.3 (Opcional) Explorar Swagger UI / ReDoc

- `http://127.0.0.1:8000/docs` → Swagger UI interactivo. 
- `http://127.0.0.1:8000/redoc` → vista tipo documento (ReDoc). 

FastAPI genera automáticamente documentación OpenAPI. 

***

## 4. Implementar el cliente programático en Python

### 4.1 Cliente síncrono con requests

Dentro de `fastapi-client-practica/client/` crear un archivo `client_sync.py` con el siguiente contenido.

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

def create_product():
    product = {"id": 1, "name": "Laptop", "price": 19999.99}
    resp = requests.post(f"{BASE_URL}/products", json=product)
    print("CREATE:", resp.status_code, resp.json())

def list_products():
    resp = requests.get(f"{BASE_URL}/products")
    print("LIST:", resp.status_code, resp.json())

def get_product(product_id: int):
    resp = requests.get(f"{BASE_URL}/products/{product_id}")
    print(
        f"GET {product_id}:",
        resp.status_code,
        resp.json() if resp.headers.get("content-type", "").startswith("application/json") else resp.text,
    )

def update_product(product_id: int):
    updated = {"id": product_id, "name": "Laptop Pro", "price": 25999.99}
    resp = requests.put(f"{BASE_URL}/products/{product_id}", json=updated)
    print("UPDATE:", resp.status_code, resp.json() if resp.content else "")

def delete_product(product_id: int):
    resp = requests.delete(f"{BASE_URL}/products/{product_id}")
    print("DELETE:", resp.status_code)

def main():
    print("---- Creating product ----")
    create_product()

    print("\n---- Listing products ----")
    list_products()

    print("\n---- Getting existing product ----")
    get_product(1)

    print("\n---- Updating product ----")
    update_product(1)
    get_product(1)

    print("\n---- Deleting product ----")
    delete_product(1)
    list_products()

    print("\n---- Getting non-existing product (should be 404) ----")
    get_product(1)

if __name__ == "__main__":
    main()
```



Con esto tenemos un cliente programático que usa la API (CRUD) mediante peticiones HTTP reales.

***

### 4.2 Ejecutar el cliente Python

1. Dejar corriendo el servidor (`uvicorn main:app --reload`).  
2. En otra terminal:

   ```bash
   conda activate fastapi-client
   cd fastapi-client-practica/client
   python client_sync.py
   ```

Se observa el intercambio real de peticiones/respuestas entre el cliente Python y el servidor FastAPI. 

***

## 5. Exportar la especificación OpenAPI (openapi.json)

Con el servidor FastAPI aún corriendo, desde otra terminal (puede ser fuera del entorno conda):

```bash
cd fastapi-client-practica
curl http://127.0.0.1:8000/openapi.json -o openapi.json
```

**Propósito:** obtener localmente la descripción formal de la API en formato OpenAPI, que usaremos para generar el cliente Java.

***

## 6. Generar cliente Java con OpenAPI Generator

### 6.1 Descargar OpenAPI Generator CLI (JAR)

Ejemplo de descarga:

```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.6.0/openapi-generator-cli-7.6.0.jar -O openapi-generator-cli.jar
```

Esto es para disponer de la herramienta de línea de comandos que transforma OpenAPI en código Java.

***

### 6.2 Generar el cliente Java

Desde `fastapi-client-practica` (donde está `openapi.json` y el JAR):

En Windows (cmd o PowerShell)
```bash
java -jar openapi-generator-cli.jar generate ^
  -i openapi.json ^
  -g java ^
  -o java-client
```
En Linux/MacOS
```bash
java -jar openapi-generator-cli.jar generate \
  -i openapi.json \
  -g java \
  -o java-client
```



- `-i openapi.json`: archivo con la especificación de la API FastAPI.  
- `-g java`: tipo de cliente a generar. [openapi-generator](https://openapi-generator.tech/docs/generators/)
- `-o java-client`: carpeta de salida con el proyecto Maven.  

Con esto tenemos un proyecto Java (con `pom.xml`) que contiene las clases de modelo y el cliente para llamar a tu API. 

***

## 7. Instalar el cliente Java en el repositorio Maven local

### 7.1 Abrir el proyecto generado e instalar localmente el proyecto del paso anterior

Abrir el directorio `java-client` en IntelliJ. Se detectará que es un proyecto Maven y así lo abrimos. Luego podemos revisar el código. La instalación de este cliente se puede hacer en la línea de comandos, pero la haremos con el maven que tiene IntelliJ IDEA seleccionando del `Lifecycle` la opción `install`.

Esto compila el cliente y lo instala en el repositorio Maven local. 

Con esto permitimos que cualquier otro proyecto Maven de nuestra máquina pueda usar este cliente como dependencia.

***

## 8. Crear un nuevo proyecto Java consumidor en IntelliJ IDEA

### 8.1 Crear proyecto Maven

1. Abrir IntelliJ IDEA.  
2. “File → New → Project…”.  
3. Elegir “Maven”.  
4. Configurar:  
   - GroupId: `mx.uam.integracion`.  
   - ArtifactId: `fastapi-consumer`.  
5. Finalizar.

Con esto tendremos un proyecto separado que actuará como consumidor de la API FastAPI usando el cliente generado.

***

### 8.2 Agregar dependencia al cliente generado

1. Abrir `java-client/pom.xml` y anotar:

   ```xml
   <groupId>...</groupId>
   <artifactId>...</artifactId>
   <version>...</version>
   ```

2. En el `pom.xml` del proyecto `fastapi-consumer`, agregar:

   ```xml
   <dependencies>
       <!-- otras dependencias... -->

       <dependency>
         <groupId>org.openapitools</groupId>
         <artifactId>openapi-java-client</artifactId>
         <version>0.1.0</version>
       </dependency>
   </dependencies>
   ```

3. En IntelliJ, recargar Maven (icono de “reload” en la ventana “Maven” o clic derecho → “Maven → Reload project”).  

Con esto le decimos a Maven/IntelliJ que este proyecto depende del SDK Java, el generado desde OpenAPI. 

***

## 9. Consumir la API FastAPI desde el proyecto Java

### 9.1 Crear clase `Main` que use el cliente

En `src/main/java`, crear paquetes y clase:

- Paquete: `mx.uam.integracion`.  
- Clase: `Main`.


```java
package mx.uam.integracion;

public class Main {
    public static void main(String[] args) {
        try {
            org.openapitools.client.ApiClient client = new org.openapitools.client.ApiClient();
            client.setBasePath("http://127.0.0.1:8000"); // URL de tu API FastAPI
            
            org.openapitools.client.api.DefaultApi api = new org.openapitools.client.api.DefaultApi(client);

            // Ejemplo: llamar a GET /products
            java.util.List<org.openapitools.client.model.Product> products = api.listProductsProductsGet(); 

            System.out.println("Productos obtenidos desde FastAPI:");
            System.out.println(products);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

***

### 9.2 Ejecutar la integración completa

1. Asegurarse de que el servidor FastAPI está corriendo (`uvicorn main:app --reload`). 
2. En IntelliJ, en el proyecto `fastapi-consumer`, ejecutar `Main.main()` (clic derecho → “Run 'Main.main()'”, o clic sobre el icono verde y seleccionar “Run 'Main.main()'”).  
3. Ver en consola los productos devueltos (al inicio probablemente vacía; se pueden crear productos primero con el cliente Python o con la propia API).  

Con esto hemos probado de extremo a extremo la cadena: FastAPI → OpenAPI → OpenAPI Generator → cliente Java → app Java que consume la API.

## 10. Modificaciones

- Hacer que la API responda con error si el precio al crear un producto es negativo.
- En general, hacer que responda con error si los datos no son correctos o faltan.
- 