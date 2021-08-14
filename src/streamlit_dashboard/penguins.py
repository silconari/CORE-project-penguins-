import streamlit as st
import altair as alt
import os
import requests
import pandas as pd
from streamlit_folium import folium_static
import folium


def render_streamlit():

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
    ).properties(width=400, height=300)

    st.altair_chart(sex_chart)

    st.header("*Penguin size by species*")

    body_mass_chart = alt.Chart(penguins_db).mark_circle().encode(
        x="Flipper Length (mm)",
        y="Body Mass (g)",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=900)

    st.altair_chart(body_mass_chart, True)

    st.header("*Penguin flipper lengths*")

    flipper_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="Flipper Length (mm)",
        y="count()",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=300)

    st.altair_chart(flipper_chart, True)

    st.header("*Penguin culmen dimensions*")

    culmen_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="Culmen Length (mm)",
        y="Culmen Depth (mm)",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=600)

    st.altair_chart(culmen_chart, True)

    st.header("*Date egg*")

    egg_chart = alt.Chart(penguins_db).mark_bar().encode(
        x="count()",
        y="Date Egg",
        color=alt.Color("Species", legend=alt.Legend(title="Species by color"))
    ).properties(height=900)

    st.altair_chart(egg_chart, True)

    # Geolocalización de las islas del Archipiélago Palmer

    st.header("Where penguins live?")

    islands = st.radio("Pick a island", ("Torgersen", "Biscoe", "Dream"))

    initial_location = []
    folium_markers = []

    if islands == "Torgersen":

        Torgersen = requests.get(
            "http://127.0.0.1:5000/location?name=Torgersen%20Island,%20Antarctica").json()

        initial_location = [Torgersen["latitude"],
                            Torgersen["longitude"]]

        folium_markers.append(
            folium.Marker(
                [Torgersen["latitude"], Torgersen["longitude"]], popup="Torgersen Island", tooltip="Torgersen Island")
        )

    elif islands == "Biscoe":

        Biscoe = requests.get(
            "http://127.0.0.1:5000/location?name=Biscoe%20Islands,%20Antarctica").json()

        initial_location = [Biscoe["latitude"],
                            Biscoe["longitude"]]

        folium_markers.append(
            folium.Marker(
                [Biscoe["latitude"], Biscoe["longitude"]], popup="Biscoe Island", tooltip="Biscoe Island")
        )

    else:

        Dream = requests.get(
            "http://127.0.0.1:5000/location?name=Dream%20Island,%20Antarctica").json()

        initial_location = [Dream["latitude"],
                            Dream["longitude"]]

        folium_markers.append(
            folium.Marker(
                [Dream["latitude"], Dream["longitude"]], popup="Dream Island", tooltip="Dream Island")
        )

    m = folium.Map(location=initial_location, zoom_start=8)
    for elem in folium_markers:
        elem.add_to(m)

    folium_static(m)
