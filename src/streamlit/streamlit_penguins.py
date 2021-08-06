from altair.vegalite.v4.schema.core import MultiSelectionConfig
import streamlit as st
import altair as alt
import os
import requests
import pandas as pd


st.title("Welcome to Palmer penguins")

images = st.image([os.path.join(os.path.dirname(__file__),
                                "../../assets/Adelie_penguin.jpg"),
                  os.path.join(os.path.dirname(__file__),
                               "../../assets/Chinstrap_penguin.jpg"),
                  os.path.join(os.path.dirname(__file__), '../../assets/Gentoo_penguin.jpg')], width=200, caption=["Adelie", "Chinstrap", "Gentoo"])


response = requests.get("http://127.0.01:5000/")


# ¿Cuántos pingüinos hay de cada especie?

st.header("How many penguins are there of each species in Palmer Archipelago?")

species = st.radio("Pick a species", ("Adelie", "Chinstrap", "Gentoo"))

species_db = pd.DataFrame.from_records(response.json())

if species == "Adelie":

    st.write(len(species_db[(species_db["Species"] ==
                             "Adelie Penguin (Pygoscelis adeliae)")]))

elif species == "Chinstrap":

    st.write(len(species_db[(species_db["Species"] ==
                             "Chinstrap penguin (Pygoscelis antarctica)")]))
else:

    st.write(len(species_db[(species_db["Species"] ==
                             "Gentoo penguin (Pygoscelis papua)")]))

# ¿macho o hembra?


############### Estadísticas por especie ############################

# alt.Chart(penguins).mark_circle(size=60).encode(
#   x=penguins.find({}, {"Species": 1}),
#  y=penguins.find({}, {"Body Mass (g)": 1})
# ).interactive()
