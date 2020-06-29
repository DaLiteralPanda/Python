import streamlit as st
from random import choice

st.title("Coin Flip WebApp")

# Variable with choices
coin_choice = ["Heads","Tails"]

# Asking user for heads or Tails
user_input = st.text_input("Choose Heads or Tails :- ")

end_choice = choice(coin_choice)

if str(user_input) == str(end_choice) :
    st.write(f"Congrats You Got {end_choice}!")
else :
    st.write(f"Whump Whump Whump, Better Luck Next Time")
