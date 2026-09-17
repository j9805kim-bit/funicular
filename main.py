import streamlit as st 

#git add main.py requirements.txt
#git commit -m "Update app"
#git push

st.header("Hello World!!~" )

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")