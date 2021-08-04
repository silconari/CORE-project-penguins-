import streamlit as st
import altair as alt
import os

st.title("Palmer penguins")

images = st.image([os.path.join(os.path.dirname(__file__),
                   "../../assets/Adelie_penguin.jpg"),
                   os.path.join(os.path.dirname(__file__),
                                "../../assets/Chinstrap_penguin.jpg"),
                   os.path.join(os.path.dirname(__file__), '../../assets/Gentoo_penguin.jpg')], caption=["Adelie", "Chinstrap", "Gentoo"])


# Elegir pingüino por ID

id_number = st.text_input("Which penguin am I? (ID_number)")

# Escoger una especie

species = st.radio("Pick a specie", ("Adelie", "Chinstrap", "Gentoo"))


# Comparar medidas entre especies o machos y hembras

# source = data.penguins()

# alt.Chart(source).mark_circle(size=60).encode(
# x='',
# y='',
#  color='',
#   tooltip=[']
# ).interactive()
