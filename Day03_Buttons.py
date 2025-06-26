import streamlit as st

# Adding a title to the app
st.title("Day 03: Buttons")

# 
st.header("Buttons - st.button")

# Create a button and check if it is clicked
if st.button('Click me to say "Hello!"', help="Tip: Click this button to see a greeting!", icon="👋", type="primary"):
    st.success("You clicked the button!")
    st.write("Well, hello there! :)")
    st.balloons()  # Show balloons animation
else:
    st.write("You haven't clicked the button yet. :(")

if st.button("Why not another button?", help="I couldn't think about leaving a button alone in here!", icon="🍰", type="secondary"):
    st.write("Another button clicked! Wow!  You are on a roll!")

if st.button("Don't click this one", help="This button is just here for decoration.  Do not click it!", icon="🚫", type="tertiary"):
    st.write("You clicked the 'Don't click' button! Well, you did it anyway.  I guess you are a rebel!")