import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import powerBi
import home
import python
import d3js
import tableau

# Define the CSS style for the iframe
iframe_style = f"""
    width: 100%; 
    height: 600px; 
    border: none;
"""

st.title('Ownership Financial Insights')

#def on_change(key):
    #selection = st.session_state[key]
    #st.write(f"Selection changed to {selection}")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "PowerBI", "Tableau", 'D3.JS', 'Python'], 
    icons=['house', 'reception-4', "table", 'filetype-js', 'filetype-py'], 
    menu_icon="cast", default_index=0, orientation="vertical")
    

DATE_COLUMN = 'post date'
DATA_URL = ('student_accounts_encoded.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")


if selected == "Home":
    home.main(st, data, iframe_style)
elif selected == "PowerBI":
    powerBi.main(st, data, iframe_style)
elif selected == "Python":
    python.main(st, data, iframe_style)
elif selected == "D3.JS":
    d3js.main(st, data, iframe_style)
elif selected == "Tableau":
    tableau.main(st, data, iframe_style)

data_load_state.text("")