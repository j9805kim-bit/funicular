import streamlit as st 

#git add main.py requirements.txt
#git commit -m "Update app"
#git push

st.header("Hello World!!~" )

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
        st.write("You selected comedy.")
else:
        st.write("You didn't select comedy.")


color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)