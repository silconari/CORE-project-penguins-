import streamlit as st
import os
import requests
import pandas as pd


def render_streamlit():

    st.title("More Antartic penguins...")

    images = st.image([os.path.join(os.path.dirname(__file__),
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

                       ], width=300, caption=["Emperor", "King", "Macaroni", "rockhopper", "Royal", "rare"])

    st.title("Which is nearest island from my ubication?")

    form = st.form(key='my-form')
    coordinates = form.text_input('Enter latitude,longitude')
    submit = form.form_submit_button('Submit')

    st.write('Press submit to have your nearest island printed below')

    if submit:
        response = requests.get(
            f"http://127.0.0.1:5000/islands?latlon={coordinates}").json()

        st.write(f'The nearest island is {response["name"]}')
