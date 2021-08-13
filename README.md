# CORE-project-penguins
First project in CORE school 

🐧🐧 -- PREPARANDO EL DATASET -- 🐧🐧

El dataset elegido en este proyecto ha sido "Palmer Archipelago Penguins" que contenía una serie de datos sobre varias colonias de pinguinos de la Antártida. 

En la limpieza de datos he eliminado aquellas columnas que hacían referencia a los análisis de sangre ('Delta 15 N (o/oo');'Delta 13 C (o/oo)') y la columna 'Comments' por tener gran cantidad de filas vacías. También he eliminado una columna con datos duplicados ('Stage') y otra con el código de cada estudio ('studyName').

Además, he eliminado las filas de la columna 'Sex' que contenían nulos. 

Todos estos pasos los he realizado en el archivo to_new_db.py 

Con este limpiado de datos, me he centrado en las medidas que diferencian a cada pinguino, la especie e isla a donde pertenece. 

La base de datos "limpia" la he subido a MongoDB Atlas y he accedido a ella a través de MongoCompass. 

Está compuesta por dos colecciones, una con la información del dataset de los pinguinos y otra con el nombre y coordenadas de la isla a la que pertenecen.

 🐧🐧 -- ORGANIZACIÓN DEL CÓDIGO -- 🐧🐧

El proyecto está dividido en tres carpetas diferentes de un mismo repositorio (CORE-project-penguins):

- assets. 
 
    Contiene las imágenes utilizadas en el dashboard de Streamlit

 - data.

    Con los datos originales y limpiados de los que parte el proyecto. 

 - src.

    Es la carpeta raíz y en ella se desglosa prácticamente todo el código.

 
 Por otro lado se encuentran los archivos que no son código python: .env, readme, .gitignore, requerirements.


 🐧🐧--CREANDO API EN FLASK -- 🐧🐧

Flask está repartido en varios:

    - controllers. root_controllers. La carpeta controllers contiene el archivo con las funciones controladoras que implementan los endpoints, son cuatro:

            1. La primera hace una petición a la base de datos de los pinguinos en formato json. Es la "raíz" de los endpoints. 

            2. La segunda contiene una petición a la segunda colección de la base de datos de los pinguinos donde guardo cada una de las coordenadas de las islas. Devuelve un json con una geoquery que marca la isla más cercana a las coordenadas dadas por el usuario en streamlit. 

            3. La tercera función hace una petición a una API que devuelve un json con las coordenadas del lugar que elija el usuario (en este caso son las islas de los pinguinos).
    - app. 

    Crea la aplicación de flask. 

    - config. 

    Contiene el puerto donde se va a ejecutar la API. 

    - server. 

    Inicia el servidor que expone la API.

    - main.

    Contiene el page_manager que gestiona las diferentes páginas de mi dashboard en streamlit. 


 🐧🐧 -- CREANDO DASHBOARD -- 🐧🐧

    Streamlit se reparte también en diferentes archivos. 

    - islands.

    Con el contenido que se muestra en la segunda página del dashboard:

        - Imágenes de las diferentes especies de pingüinos antárticos.
        - una request a la función controladora que muestra al usuario la isla más cercana a las coordenadas que indica por una casilla de texto. 

    - penguins.

    Muestra el contenido de la página principal del dashboard, con las imágenes de los pingüinos del archipiélago de Palmer, algunas estadísticas y un mapa que marca en el mapa las diferentes islas del archipiélago. 

    - multipage. 

    Contiene la clase y métodos que crean diferentes páginas en el dashboard de Streamlit. 

    - utils 
        - hanndle_error. Devuelve un texto con un error en caso de que se produzca un fallo en la ejecución de la API. 

        - json_response. Devuelve las respuestas en formato json. 

        - mongo_connect. Conecta con la base de datos en MongoAtlas. 


                🧊🧊🧊🧊🧊        🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧                🧊🧊🧊🧊🧊 




 😥 -- COSAS PENDIENTES --

Además de cumplir con los siguientes levels del proyecto... me han quedado tareas pendientes que me gustaría haber realizado con el dataset.

    - Añadir más gráficas a partir de los datos de las medidas del pico de los pingüinos de cada especie.
    - Crear más contenido en otras páginas del dashboard
    - Añadir botones con funcionalidades
    - Mejorar la estética y organización del readme. 


📚 -- REFERENCES --

* 

Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version  0.1.0. https://allisonhorst.github.io/palmerpenguins/. doi: 10.5281/zenodo.3960218. 
   