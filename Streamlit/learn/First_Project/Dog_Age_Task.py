import streamlit as st
st.title("Dog Age Converter")

username = st.text_input("What is Your Name :- ")

human_age = int(st.slider('What is your Age :- '))

first_2years_age = (human_age - (human_age - 2)) * 10.5
rest_years = (human_age - 2) * 4

st.write(f"Your Age in Dog Years is {first_2years_age + rest_years}")
