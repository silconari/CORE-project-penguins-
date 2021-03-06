# CORE-project-penguins

![Imagen dibujo de especies de pingΓΌinos Palmer](assets/lter_penguins.png)


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://whispering-falls-95097.herokuapp.com/)

## Table of Contents

* [π§ About The Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Folder Structure](#folder-structure)
* [πΎ Dataset](#dataset)
* [Look inside](#look-inside)
* [π  References](#references)

## π§ About The Project <a name="about-the-project"></a>

CORE-project-penguins es mi primer proyecto de CORE. Consiste en una API que hace peticiones a una base de datos con informaciΓ³n sobre los pingΓΌinos del archipiΓ©lago de Palmer y devuelve el resultado en un dashboard de Streamlit. 

## Requisites 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/silconari/core-project-penguins-)

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)




Los siguientes paquetes de cΓ³digo abierto se han usado en este proyecto:

* Pandas
* Mongo DB
* Altair 
* Streamlit 
* json 
* Flask 
* dotenv
* Folium 


## Folder Structure 

``` 

.
βββ LICENSE
βββ README.md
βββ assests
βββ data
β   βββ new_db.csv
β   βββ penguins_lter.csv
βββ requirements.txt
βββ src
β   βββ __pycache__
β   β   βββ app.cpython-39.pyc
β   β   βββ config.cpython-39.pyc
β   β   βββ server.cpython-39.pyc
β   βββ flask
β   β   βββ Dockerfile
β   β   βββ requirements.txt
β   β   βββ src
β   β       βββ app.py
β   β       βββ config.py
β   β       βββ controllers
β   β       β   βββ __init__.py
β   β       β   βββ __pycache__
β   β       β   β   βββ __init__.cpython-39.pyc
β   β       β   β   βββ root_controllers.cpython-39.pyc
β   β       β   βββ root_controllers.py
β   β       βββ main.py
β   β       βββ server.py
β   β       βββ to_new_db.py
β   β       βββ utils
β   β           βββ __pycache__
β   β           β   βββ __init__.cpython-39.pyc
β   β           β   βββ handle_error.cpython-39.pyc
β   β           β   βββ json_response.cpython-39.pyc
β   β           β   βββ mongo_connect.cpython-39.pyc
β   β           βββ handle_error.py
β   β           βββ json_response.py
β   β           βββ mongo_connect.py
β   βββ jupyter-notebook
β   β   βββ creating_df.ipynb
β   β   βββ db_mongo_connect.ipynb
β   βββ streamlit_dashboard
β       βββ Dockerfile
β       βββ __pycache__
β       β   βββ islands.cpython-39.pyc
β       β   βββ multipage.cpython-39.pyc
β       β   βββ penguins.cpython-39.pyc
β       β   βββ streamlit_penguins.cpython-39.pyc
β       βββ assets
β       β   
β       βββ requirements.txt
β       βββ src
β           βββ islands.py
β           βββ main.py
β           βββ multipage.py
β           βββ penguins.py
βββ start.sh

```

## πΎ Dataset <a name="dataset"></a>

[Penguins Palmer dataset]("https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data") π§


## Look inside 

GrΓ‘ficas realizadas a partir de los datos del dataset.

Fecha de la puesta de los pingΓΌinos:

![grΓ‘fica fecha puesta de huevos de especies de pingΓΌinos Palmer](assets/egg.PNG)

Comparativas de la longitud del pico en las diferentes especies:

![grΓ‘fica comparativa de la longitud del pico de especies de pingΓΌinos Palmer](assets/culmen_dimension.PNG)

Marcadores con las islas del archipiΓ©lago:

![Mapa de las islas del archipiΓ©lago de Palmer](assets/maps.PNG)

## π  References <a name="references"></a>

* Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version  0.1.0. https://allisonhorst.github.io/palmerpenguins/. doi: 10.5281/zenodo.3960218. 
   