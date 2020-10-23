import streamlit as st
import pandas as pd

# Root folder is Rishov-Task
df = pd.read_csv('./Date-Recogniser/data/shootings.csv')

possible_date_names = ['date', 'dates', 'DATE', 'DATES', 'Date', 'Dates']

def date_finder(data_set):
    for names in possible_date_names:
        if True in list(data_set.columns.str.contains(names)):
            print(f"The date column has been found its data_set")
        else:
            pass

print(date_finder(df))

print(list(df.columns.str.contains(possible_date_names[0])))
