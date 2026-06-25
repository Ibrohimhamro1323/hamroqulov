import streamlit as st
import streamlit.components.v1 as components

# Sahifa sozlamalari
st.set_page_config(page_title="SportMart — Sport Oziq-Ovqatlari", layout="wide")

# HTML kodini o'zgaruvchiga yuklaymiz
# Eslatma: JS funksiyalari (addToCart, switchCat) ham shu string ichida bo'lishi kerak.
html_content = f"""
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8" />
    <style>
        /* BU YERGA O'ZINGIZNING CSS KODINGIZNI QO'YASIZ */
        /* Yuqoridagi <style>...</style> qismini to'liq shu yerga ko'chiring */
    </style>
</head>
<body>
    <script>
        // JS funksiyalaringizni shu yerga joylang
        function switchCat(cat) {{
            // Tablar almashinuvi logikasi
        }}
        function addToCart(btn, name, cat, img, price) {{
            // Savatga qo'shish logikasi
        }}
    </script>
</body>
</html>
"""

# Streamlit orqali ko'rsatish
components.html(html_content, height=4500, scrolling=True)
