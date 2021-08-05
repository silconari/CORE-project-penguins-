from dotenv import load_dotenv
from altair.vegalite.v4.schema.core import MultiSelectionConfig
import streamlit as st
import altair as alt
import os
from pymongo import MongoClient

load_dotenv()

username = os.getenv("ATLAS_USER")
password = os.getenv("ATLAS_PASSWORD")

url = f"mongodb+srv://{username}:{password}@cluster0.enltd.mongodb.net/test?authSource=admin&replicaSet=atlas-mrg0dm-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"

penguins = MongoClient(url).get_database("penguins-data").penguins


st.title("Welcome to Palmer penguins")

images = st.image([os.path.join(os.path.dirname(__file__),
                                "../../assets/Adelie_penguin.jpg"),
                  os.path.join(os.path.dirname(__file__),
                               "../../assets/Chinstrap_penguin.jpg"),
                  os.path.join(os.path.dirname(__file__), '../../assets/Gentoo_penguin.jpg')], width=200, caption=["Adelie", "Chinstrap", "Gentoo"])


# Elegir pingüino por ID

id_number = st.text_input("Which penguin am I? (ID_number)")

individual_id = list(penguins.find(
    {"Individual ID": id_number}, {"Individual ID": 1, "_id": 0}))

if len(individual_id):
    st.write(f"{id_number} yes, I'm a Palmer penguin")
else:
    st.write(f"{id_number} sorry, I'm not a Palmer penguin")

# Escoger una especie

species = st.radio("Pick a specie", ("Adelie", "Chinstrap", "Gentoo"))


# Comparar medidas entre especies o machos y hembras


# alt.Chart(penguins).mark_circle(size=60).encode(
#   x=penguins.find({}, {"Species": 1}),
#  y=penguins.find({}, {"Body Mass (g)": 1})
# ).interactive()
