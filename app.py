import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit.components.v1 as components

st.title('Ownership Financial Insights')

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


st.subheader('Raw data')
st.write(data)

st.subheader('Total number of charges w.r.t Program')

# Calculate the number of pickups by hour
hourly_pickups = data.groupby(data['program']).size()

st.bar_chart(hourly_pickups)


def load_d3js_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

d3js_code = load_d3js_file('d3.html')  # Replace with the path to your D3.js HTML file

st.components.v1.html(d3js_code, height=600) 

# Load the D3.js library
d3_script = """
<script src="https://d3js.org/d3.v6.min.js"></script>
"""

# Define the D3.js visualization code
d3_visualization = """
<div id="chart"></div>
<script>
  // D3.js visualization code goes here
  const data = [10, 20, 30, 40, 50];

  const svg = d3.select("#chart")
    .append("svg")
    .attr("width", 400)
    .attr("height", 400);

  svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", (d, i) => i * 50 + 123)
    .attr("cy", 200)
    .attr("r", d => d)
    .attr("fill", "steelblue");
</script>
"""

# Render the D3.js visualization in Streamlit
components.html(d3_script + d3_visualization, height=500)
