from dotenv import load_dotenv
import penguins as penguins
import islands as islands
import streamlit as st
from multipage import MultiPage

load_dotenv()

page_manager = MultiPage()

page_manager.add_page(title="Palmer penguins",
                      func=penguins.render_streamlit)


page_manager.add_page(title="Antartic info",
                      func=islands.render_streamlit)


page_manager.run()
