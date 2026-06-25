import streamlit as st
import streamlit.components.v1 as components

# Streamlit sahifasini to'liq kenglikda sozlash
st.set_page_config(layout="wide", page_title="SportMart")

# indexw.html faylini o'qib olish va render qilish
with open("indexw.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTMLni Streamlit ichida ko'rsatish
# height qiymatini sahifangiz uzunligiga qarab o'zgartirishingiz mumkin
components.html(html_content, height=2500, scrolling=True)
