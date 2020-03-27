'''
- First Name (Text Input)
- Last Name (Text Input)
- Gender (Radio Input)
- Coding Experience (Text Input)
'''

import streamlit as st

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.radio("Gender", ["Male", "Female", "Other"])
coding_experience = st.radio("Coding Experience", ["Bad", "Neutral", "Good", "Excellent"])
additional_experience = st.text_input("Additional Coding Experience (Optional)")

file = open("form_file.txt", "w+")
file.write(f"First Name : {first_name} \nLast Name : {last_name} \nGender : {gender} \nCoding Experience : {coding_experience} \nAdditional Coding Experience : {additional_experience}")
file.close()
