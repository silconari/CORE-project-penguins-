# CORE-project-penguins

![Imagen dibujo de especies de pingüinos Palmer](assets/lter_penguins.png)


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://whispering-falls-95097.herokuapp.com/)

## Table of Contents

* [🐧 About The Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Folder Structure](#folder-structure)
* [💾 Dataset](#dataset)
* [Look inside](#look-inside)
* [📚  References](#references)

## 🐧 About The Project <a name="about-the-project"></a>

CORE-project-penguins es mi primer proyecto de CORE. Consiste en una API que hace peticiones a una base de datos con información sobre los pingüinos del archipiélago de Palmer y devuelve el resultado en un dashboard de Streamlit. 

## Requisites 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/silconari/core-project-penguins-)

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)




Los siguientes paquetes de código abierto se han usado en este proyecto:

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
├── LICENSE
├── README.md
├── assests
├── data
│   ├── new_db.csv
│   └── penguins_lter.csv
├── requirements.txt
├── src
│   ├── __pycache__
│   │   ├── app.cpython-39.pyc
│   │   ├── config.cpython-39.pyc
│   │   └── server.cpython-39.pyc
│   ├── flask
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── src
│   │       ├── app.py
│   │       ├── config.py
│   │       ├── controllers
│   │       │   ├── __init__.py
│   │       │   ├── __pycache__
│   │       │   │   ├── __init__.cpython-39.pyc
│   │       │   │   └── root_controllers.cpython-39.pyc
│   │       │   └── root_controllers.py
│   │       ├── main.py
│   │       ├── server.py
│   │       ├── to_new_db.py
│   │       └── utils
│   │           ├── __pycache__
│   │           │   ├── __init__.cpython-39.pyc
│   │           │   ├── handle_error.cpython-39.pyc
│   │           │   ├── json_response.cpython-39.pyc
│   │           │   └── mongo_connect.cpython-39.pyc
│   │           ├── handle_error.py
│   │           ├── json_response.py
│   │           └── mongo_connect.py
│   ├── jupyter-notebook
│   │   ├── creating_df.ipynb
│   │   └── db_mongo_connect.ipynb
│   └── streamlit_dashboard
│       ├── Dockerfile
│       ├── __pycache__
│       │   ├── islands.cpython-39.pyc
│       │   ├── multipage.cpython-39.pyc
│       │   ├── penguins.cpython-39.pyc
│       │   └── streamlit_penguins.cpython-39.pyc
│       ├── assets
│       │   
│       ├── requirements.txt
│       └── src
│           ├── islands.py
│           ├── main.py
│           ├── multipage.py
│           └── penguins.py
└── start.sh

```

## 💾 Dataset <a name="dataset"></a>

[Penguins Palmer dataset]("https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data") 🐧


## Look inside 

Gráficas realizadas a partir de los datos del dataset.

Fecha de la puesta de los pingüinos:

![gráfica fecha puesta de huevos de especies de pingüinos Palmer](assets/egg.PNG)

Comparativas de la longitud del pico en las diferentes especies:

![gráfica comparativa de la longitud del pico de especies de pingüinos Palmer](assets/culmen_dimension.PNG)

Marcadores con las islas del archipiélago:

![Mapa de las islas del archipiélago de Palmer](assets/maps.PNG)

## 📚  References <a name="references"></a>

* Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version  0.1.0. https://allisonhorst.github.io/palmerpenguins/. doi: 10.5281/zenodo.3960218. 
   