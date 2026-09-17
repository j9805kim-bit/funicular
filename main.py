import streamlit as st 

st.header("Hello World!!~" )

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")