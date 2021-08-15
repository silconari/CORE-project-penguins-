import streamlit as st
import altair as alt
import os
import requests
import pandas as pd


def render_streamlit():

    cols = st.columns((1, 3, 1))

    cols[1].title("Welcome to Palmer penguins")

    cols[1].image([os.path.join(os.path.dirname(__file__),
                                "../../assets/Adelie_penguin.jpg"),
                   os.path.join(os.path.dirname(__file__),
                                "../../assets/Chinstrap_penguin.jpg"),
                   os.path.join(os.path.dirname(__file__), '../../assets/Gentoo_penguin.jpg')], width=200, caption=["Adelie", "Chinstrap", "Gentoo"])

    response = requests.get("http://127.0.0.1:5000/")

    # ¿Cuántos pingüinos hay de cada especie?

    st.header(
        "**How many penguins are there of each species in Palmer Archipelago?**")

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

    ### Estadísticas por especie ###

    st.header("*Penguins by island*")

    islands_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="Island",
        y="count()",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=200)

    st.altair_chart(islands_chart, True)

    # Número de animales de cada sexo por especie

    st.header("*Penguin sex by species*")

    sex_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="Sex",
        y="count()",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(width=400, height=300)

    st.altair_chart(sex_chart)

    # Tamaño de los pingüinos por especie

    st.header("*Penguin size by species*")

    body_mass_chart = alt.Chart(penguins_db).mark_circle().encode(
        x="Flipper Length (mm)",
        y="Body Mass (g)",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=1000)

    st.altair_chart(body_mass_chart, True)

    # Tamaño de las aletas

    st.header("*Penguin flipper lengths*")

    flipper_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="Flipper Length (mm)",
        y="count()",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=300)

    st.altair_chart(flipper_chart, True)

    # Dimensiones del pico por especie

    st.header("*Penguin culmen dimensions*")

    st.image([os.path.join(os.path.dirname(__file__),
                           "../../assets/culmen_depth.png")], width=200)

    culmen_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="Culmen Length (mm)",
        y="Culmen Depth (mm)",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=800)

    st.altair_chart(culmen_chart, True)

    # Fecha de la puesta por especie

    st.header("*Date egg*")

    egg_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="count()",
        y="Date Egg",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=600)

    st.altair_chart(egg_chart, True)
