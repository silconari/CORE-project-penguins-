from altair.vegalite.v4.schema.core import FontStyle, FontWeight
import streamlit as st
import os
import requests
import altair as alt
from streamlit_folium import folium_static
import folium


def render_streamlit():

    cols = st.columns((1, 3, 1))

    cols[1].title("More Antartic penguins...")

    st.write(
        "*Check out this to know more!* 🐧 [link](https://es.wikipedia.org/wiki/Spheniscidae)")

    cols[1].image([os.path.join(os.path.dirname(__file__),
                                "../../assets/Emperor penguin.jpg"),
                   os.path.join(os.path.dirname(__file__),
                                "../../assets/King penguin.jpg"),
                   os.path.join(os.path.dirname(__file__),
                                '../../assets/Macaroni penguin.jpeg'),

                   os.path.join(os.path.dirname(__file__),
                                '../../assets/rockhopper penguin.jpg'),

                   os.path.join(os.path.dirname(__file__),
                                '../../assets/Royal penguin.jpg'),

                   os.path.join(os.path.dirname(__file__),
                                '../../assets/rare penguin.jpg')

                   ], width=300, caption=["Emperor", "King", "Macaroni", "rockhopper", "Royal", "rare"],)

    # Geolocalización de las islas del Archipiélago Palmer

    cols[1].header("**Where penguins live?**")

    initial_location = []
    folium_markers = []

    def icon():
        return folium.features.CustomIcon(
            'https://d29fhpw069ctt2.cloudfront.net/icon/image/49037/preview.svg', icon_size=(30, 30))

    Torgersen = requests.get(
        "http://127.0.0.1:5000/location?name=Torgersen%20Island,%20Antarctica").json()

    initial_location = [-64.968089, -63.551734]

    folium_markers.append(
        folium.Marker(
            [Torgersen["latitude"], Torgersen["longitude"]], popup="Torgersen Island", tooltip="Torgersen Island", icon=icon()
        )

    )

    Biscoe = requests.get(
        "http://127.0.0.1:5000/location?name=Biscoe%20Islands,%20Antarctica").json()

    folium_markers.append(
        folium.Marker(
            [Biscoe["latitude"], Biscoe["longitude"]], popup="Biscoe Island", tooltip="Biscoe Island", icon=icon()
        )
    )

    # En el caso de la isla Dream, la API a la que hago la petición no es capaz de ubicarla correctamente,
    # fuerzo a folium a utilizar las coordenadas reales

    folium_markers.append(
        folium.Marker(
            [-64.7333323, -64.2420877], popup="Dream Island", tooltip="Dream Island", icon=icon()
        )

    )
    m = folium.Map(location=initial_location, zoom_start=7)
    for elem in folium_markers:
        elem.add_to(m)

    with cols[1]:
        folium_static(m)

    st.header("**Which is nearest island from my ubication?**")

    form = st.form(key='my-form')
    coordinates = form.text_input('Enter latitude,longitude')
    submit = form.form_submit_button('Submit')

    st.write('*Press submit to have your nearest island printed below*')

    if submit:
        response = requests.get(
            f"http://127.0.0.1:5000/islands?latlon={coordinates}").json()

        st.write(f'*The nearest island is {response["name"]}*')
