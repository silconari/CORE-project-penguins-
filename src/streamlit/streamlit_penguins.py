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


response = requests.get("http://127.0.0.1:5000/")


# ¿Cuántos pingüinos hay de cada especie?

st.header("How many penguins are there of each species in Palmer Archipelago?")

species = st.radio("Pick a species", ("Adelie", "Chinstrap", "Gentoo"))

penguins_db = pd.DataFrame.from_records(response.json())

if species == "Adelie":

    st.write(len(penguins_db[(penguins_db["Species"] ==
                             "Adelie Penguin (Pygoscelis adeliae)")]))

elif species == "Chinstrap":

    st.write(len(penguins_db[(penguins_db["Species"] ==
                             "Chinstrap penguin (Pygoscelis antarctica)")]))
else:

    st.write(len(penguins_db[(penguins_db["Species"] ==
                             "Gentoo penguin (Pygoscelis papua)")]))


# Estadísticas por especie


st.header("*Penguin sex by species*")

sex_chart = alt.Chart(penguins_db).mark_bar().encode(
    x="Sex",
    y="count()",
    color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
).properties(width=300, height=300)

st.altair_chart(sex_chart)

st.header("*Penguin size by species*")

body_mass_chart = alt.Chart(penguins_db).mark_circle().encode(
    x="Flipper Length (mm)",
    y="Body Mass (g)",
    color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
).properties(width="container", height=300)

st.altair_chart(body_mass_chart)
