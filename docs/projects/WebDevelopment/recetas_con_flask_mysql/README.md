# Recipes

## Carpetas

* flask_app
  * config
    * mysqlconnection.py
  * controllers
    * recipes.py
    * users.py
  * models
    * recipes.py
    * user.py
  * templates
    * dashboard.html
    * edit_recipe.html
    * index.html
    * new_recipe.html
    * onerecipe.html
  * __init__.py  
* Pipfile
* Pipfile.lock
* recipes_schema.mwb
* server.py

### Pipenv

Los archivos `Pipfile` y `Pipfile.lock` son genrados al momentos de crear el ambiente
virtual con **Pipenv**.

### recipes_schema.mwb
Es un archivo que representa el esquema de **recipes_schema** y se debe leer con
**MySQL**. El esquema luce como:

<img src="../belt_review/recipes/images/esquema.png" alt="Girl in a jacket" >

Las instrucciones para que funcione correctamente el esquema es:

1. Abrir **MySQL**.
2. En **Models** abrir el archivo `recipes_schema.mwb`.
3. Para guardar el esquema en la Base de datos local (**root**) debemos hacer lo siguiente:
   * Hacer Click en Database/Forward Engineer
   * Luego aceptar cada una de las condiciones.
4. Finalmente. ir a  **MySQL Connection** y debería ver algo de este estilo:

<img src="../belt_review/recipes/images/db.png" alt="Girl in a jacket" >

> **Nota**: Si no puede hacer **el paso 3** es porque necesita configurar su base de datos correctamente.


### server.py

Este es el archivo que corre la aplicación (mediante `flask`).

### flask_app

En esta carpeta van todas las cosas relacionadas a nuestra aplicación

#### config
    
Esta Carpeta contiene el archivo `mysqlconnection.py`, el que tiene la función de crear 
la connección entre **Python** y **MySQL**. Además, en este archivo se debe especificar 
cuando se quiere hacer una consulta *SELECT*, *INSERT* o *DELETE*.


### models

Esta carpeta toma como referencia el esquema de **recipes_schema** y lo transforma en 
clases de Python, es decir:

* `user.py`: crea la clase **User** para tabla **user**.
* `recipe.py`: crea la clase **Recipe** para tabla **recipe**.

Además, en cada una de estas clases se definiran **métodos de clases** para poder guardar
la información del esquema **recipes_schema** en Python (mediante el archivo `mysqlconnection.py`).

### controllers

Esta carpeta tiene los archivos para construir la página web mediante `flask`, es decir, renderizar 
apropiadamente los archivos `.html` de la carpeta **templates**.

-> `users.py`: Administra todo lo relacionado a usuarios, ya sea para registrarlo (**Register**) o para logearlo (**Login**). 
Este archivo ocupa:
  * `index.html`
  * `dashboard.html`

-> `recipes.py`: Administra todo lo relacionado a las recetas, ya sea para crear, modificar recetas.
Este archivo ocupa:
  * `edit_recipe.html`
  * `new_recipe.html`
  * `onerecipe.html`

####  templates

Archivos `.html` utilizados para construir la página web.

* `index.html`: página inicial donde se registra o logea el usuario objetivo.
* `dashboard.html`: página donde se muestran todas las recetas.
* `edit_recipe.html`: página donde se edita una receta en particular.
* `new_recipe.html`: página donde se crea una nueva receta.
* `onerecipe.html`:  página donde se muestra una receta en particular.