# -*- coding: utf-8 -*-
pip install streamlit plotly


import streamlit as st
import pandas as pd
import plotly.express as px



# Load your data for the control and test sets
# Load your data for the control and test sets from raw GitHub URLs
control_data_url = "https://raw.githubusercontent.com/zahraanasser23/A-B-Testing/main/control_group.csv"
test_data_url = "https://raw.githubusercontent.com/zahraanasser23/A-B-Testing/main/test_group.csv"

control_data = pd.read_csv(control_data_url)
test_data = pd.read_csv(test_data_url)

#control_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/blob/main/control_group.csv')
#test_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/blob/main/test_group.csv')

# Streamlit app title
st.title('Clicks vs. Purchase Correlation')

# Sidebar filters
st.sidebar.header('Filter Data')
campaign_selection = st.sidebar.radio('Select Campaign', ('Control', 'Test'))

import pandas as pd
if campaign_selection == 'Control':
    data = control_data
    title = 'Control Campaign'
else:
    data = test_data
    title = 'Test Campaign'

x_column = st.sidebar.selectbox('X-axis', ['# of Website Clicks'])
y_column = st.sidebar.selectbox('Y-axis', ['# of Purchase'])

# Scatterplot
fig = px.scatter(
    data,
    x=x_column,
    y=y_column,
    color_discrete_sequence=['blue' if campaign_selection == 'Control' else 'red'],
    symbol='Campaign Name',
    size='# of Website Clicks',
    size_max=20,
    title=f'Clicks vs. Purchase Correlation - {title}'
)

# Show the plot
st.plotly_chart(fig, use_container_width=True)

# Streamlit app footer (optional)
st.sidebar.text("Powered by Streamlit and Plotly")


