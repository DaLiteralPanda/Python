'''
Imagine you want to create an app that can match people to be friends if they listened to the same song.
Create a Python program that will create a list of songs for 5 different users and then output which of the users will be friends.
You are allowed to use .txt files, input(), JSON files, or whatever you feel can help you to solve this problem.
'''

import streamlit as st

song_list_str = st.text_area("Type in your songs sepreated with a comma")

with open('songs.txt','w') as f:
    for line in song_list_str.split(","):
        f.write(f'{line}\n')
    f.close()
