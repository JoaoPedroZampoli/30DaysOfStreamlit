import streamlit as st

# Adding a title to the app
st.title("Day 03: Buttons")

# 
st.header("Buttons - st.button")

# Create a button and check if it is clicked
if st.button('Click me to say "Hello!"'):
    st.success("You clicked the button!")
    st.write("Well, hello there! :)")
    st.balloons()  # Show balloons animation
else:
    st.write("You haven't clicked the button yet. :(")