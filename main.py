import streamlit as st
import streamlit.components.v1 as components

# Sahifa sozlamalari
st.set_page_config(layout="wide", page_title="SportMart")

# HTML kodini yozib olamiz
html_code = """
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8" />
  <title>SportMart</title>
  <style>
    body { background: #0f0f0f; color: white; font-family: sans-serif; }
    /* Qolgan CSS kodlaringizni shu yerga joylashtiring */
  </style>
</head>
<body>
  <h1>SportMart — Sport Oziq-Ovqatlari</h1>
  <p>Xush kelibsiz!</p>
</body>
</html>
"""

# HTMLni render qilish
components.html(html_code, height=1000, scrolling=True)