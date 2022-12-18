import streamlit as st
import plotly.express as px
from backend import get_data
# st.set_page_config(layout="wide",page_title="Weather-forecast")

st.title("Weather forecast for the next days")
place=st.text_input("Enter place:")
days=st.slider("Forecast days:",min_value=1,max_value=5,help="Select the number of days")
option=st.selectbox("Select data to view",("Temperature","Sky"))

st.subheader(f'{option} for the next {days} days in {place}')
if place:
    try:
        filtered_data=get_data(place,days)

        if option=="Temperature":
            temperatures = [dic['main']['temp']/10 for dic in filtered_data]
            dates=[dic['dt_txt'] for dic in filtered_data]
            figure=px.line(x=dates,y=temperatures,labels={"x":"time","y":"temperatures"})
            st.plotly_chart(figure)

        if option=="Sky":
            # codes = [dic['weather'][0]['icon'] for dic in filtered_data]
            # images=["http://openweathermap.org/img/wn/"+code+"@2x.png" for code in codes]
            weather=[dic['weather'][0]['main'] for dic in filtered_data]
            images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            image_path=[images[i] for i in weather]
            dates=[dic['dt_txt'] for dic in filtered_data]
            st.image(image_path,width=100)
    except KeyError:
        st.write("This place does not exist")