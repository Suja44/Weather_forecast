import streamlit as st

st.set_page_config(layout="wide",page_title="Weather-forecast")

st.title("Weather forecast for the next days")
place=st.text_input("Enter place:")
days=st.slider("Forecast days:",min_value=1,max_value=5,help="Select the number of days")
option=st.selectbox("Select data to view",("Temperature","Sky"))

st.subheader(f'{option} for the next {days} days in {place}')