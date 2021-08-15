import streamlit_dashboard.penguins as penguins
import streamlit_dashboard.islands as islands
import streamlit as st
from streamlit_dashboard.multipage import MultiPage

page_manager = MultiPage()

page_manager.add_page(title="Palmer penguins",
                      func=penguins.render_streamlit)


page_manager.add_page(title="Antartic info",
                      func=islands.render_streamlit)


page_manager.run()
