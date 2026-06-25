import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SportMart",
    page_icon="💪",
    layout="wide"
)

with open("indexw.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(
    html_content,
    height=5000,
    scrolling=True
)
