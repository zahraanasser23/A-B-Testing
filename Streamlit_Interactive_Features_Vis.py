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

# Assuming you have control_group and test_group DataFrames defined

# Create Streamlit app
st.title('Interactive Box Plot - Campaign Spend Comparison')

# Sidebar widgets for user interaction
campaign_name_filter = st.selectbox('Select Campaign Name', options=['All'] + control_group['Campaign Name'].unique().tolist())
spend_min = st.slider('Minimum Spend [USD]', min_value=0, max_value=int(control_group['Spend [USD]'].max()), value=0)
spend_max = st.slider('Maximum Spend [USD]', min_value=0, max_value=int(control_group['Spend [USD]'].max()), value=int(control_group['Spend [USD]'].max()))

# Filter the data based on user selections
filtered_control_group = control_group.copy()
filtered_test_group = test_group.copy()

if campaign_name_filter != 'All':
    filtered_control_group = filtered_control_group[filtered_control_group['Campaign Name'] == campaign_name_filter]
    filtered_test_group = filtered_test_group[filtered_test_group['Campaign Name'] == campaign_name_filter]

filtered_control_group = filtered_control_group[(filtered_control_group['Spend [USD]'] >= spend_min) & (filtered_control_group['Spend [USD]'] <= spend_max)]
filtered_test_group = filtered_test_group[(filtered_test_group['Spend [USD]'] >= spend_min) & (filtered_test_group['Spend [USD]'] <= spend_max)]

# Create the box plot based on the filtered data
box_plot_spend = go.Figure()

box_plot_spend.add_trace(go.Box(x=filtered_control_group['Campaign Name'], y=filtered_control_group['Spend [USD]'], name='Control Campaign', boxpoints='all'))
box_plot_spend.add_trace(go.Box(x=filtered_test_group['Campaign Name'], y=filtered_test_group['Spend [USD]'], name='Test Campaign', boxpoints='all'))

box_plot_spend.update_layout(title='Spend Comparison - Control vs. Test Campaign', xaxis_title='Campaign Name', yaxis_title='Spend [USD]')

# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(box_plot_spend)



