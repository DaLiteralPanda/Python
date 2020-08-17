# Importing modules
import streamlit as st

# Title
st.title("Conversion Calculator!")

# Radio button that tells three options
conversion_radio = st.sidebar.radio("Select which conversion unit", ('Distance', 'Mass', 'Volume'))

# If statements for the radio button
if conversion_radio == 'Distance':
    options = st.selectbox(
    "What do you want to convert",
    ('Centimeters to Meters', 'Meters to Centimeters', 'Kilometers to Centimeters', 'Kilometers to Meters', 'Meters to Kilometers', 'Centimeters to Kilometers'))

    if options == 'Centimeters to Meters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num/100)}m')

    if options == 'Meters to Centimeters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 100)}cm')

    if options == 'Kilometers to Centimeters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 100000)}cm')

    if options == 'Kilometers to Meters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 1000)}m')

    if options == 'Meters to Kilometers':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num / 1000)}km')

    if options == 'Centimeters to Kilometers':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num / 100000)}km')

if conversion_radio == 'Mass':
    options = st.selectbox("What do you want to convert",
    ('Grams to Kilograms', 'Kilograms to Grams', 'Tonne to Grams', 'Tonne to Kilograms', 'Kilograms to Tonne', 'Grams to Tonne'))

    if options == 'Grams to Kilograms':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num/1000)}kg')

    if options == 'Kilograms to Grams':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 1000)}gm')

    if options == 'Tonne to Grams':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 1000000)}gm')

    if options == 'Tonne to Kilograms':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 1000)}kg')

    if options == 'Kilograms to Tonne':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num / 1000)}t')

    if options == 'Grams to Tonne':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num / 1000000)}t')

if conversion_radio == 'Volume':
    options = st.selectbox("What do you want to convert: ",
    ('Mililiters to Liters', 'Liters to Mililiters', 'Gallons to Mililiters', 'Gallons to Liters', 'Liters to Gallons', 'Mililiters to Gallons'))

    if options == 'Mililiters to Liters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num/1000)}l')

    if options == 'Liters to Mililiters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 1000)}mil')

    if options == 'Gallons to Mililiters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 3785)}ml')

    if options == 'Gallons to Liters':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num * 3.785)}l')

    if options == 'Liters to Gallons':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num / 3.785)}gal')

    if options == 'Mililiters to Gallons':
        num = st.number_input('Type in the value you want to convert: ')
        st.write(f'Converted Output {str(num / 3785)}gal')
