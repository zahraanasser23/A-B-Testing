import streamlit as st
import pandas as pd

# Set the Streamlit app title
st.title('Marketing Campaigns A/B Testing')

# Load the control campaign dataset with a semicolon (;) delimiter
control_group = pd.read_csv('control_group.csv', delimiter=';')

# Load the test campaign dataset with a semicolon (;) delimiter
test_group = pd.read_csv('test_group.csv', delimiter=';')

# Display the column names of the control and test data frames
#st.subheader('Column Names:')
#st.write("Control Campaign Column Names:", control_group.columns.tolist())
#st.write("Test Campaign Column Names:", test_group.columns.tolist())

import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Streamlit app title
st.title('Spend Comparison - Control vs. Test Campaigns')

# Create two separate box plots for Control and Test Campaigns
fig = go.Figure()

# Box Plot for Control Campaign
fig.add_trace(go.Box(x=control_data['Campaign Name'], y=control_data['Spend [USD]'], name='Control Campaign', boxpoints='all'))

# Box Plot for Test Campaign
fig.add_trace(go.Box(x=test_data['Campaign Name'], y=test_data['Spend [USD]'], name='Test Campaign', boxpoints='all'))

# Update layout
fig.update_layout(title='Spend Comparison - Control vs. Test Campaigns', xaxis_title='Campaign Name', yaxis_title='Spend [USD]')

# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(fig)



