import streamlit as st
st.title("min færste økonomiapp")
omsætning = st.number_input("omsætning",value=100000)
omkostninger = st.number_input("omkostninger", value=50000)
resultat = omsætning - omkostninger
st.write("resultat:", resultat, "kr.")












