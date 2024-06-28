# %%writefile  webapp.py 

import streamlit as st 
# import pandas as pd 
# import requests
# from st_aggrid import AgGrid
#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')
# #read json file dari data covid 
# flight_passanger_api = requests.post('https://forecastpassengerapi.herokuapp.com/forecast_timeseries',json={
#   "month_limit": "2020-01-01",
#   "window_size": 12
# }).json()

def main() : 

  st.write('Minimal Example By Edison Marpaung')

  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

  
  st.write('Contoh dataframe')
  st.dataframe(house)

  

if __name__ == '__main__' : 
  main()
