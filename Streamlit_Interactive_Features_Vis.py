import streamlit as st
import plotly.graph_objs as go
import pandas as pd

try:
    control_group = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/control_group.csv')
    test_group = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/test_group.csv')
except Exception as e:
    st.error(f"Error loading data: {str(e)}")

# Create Streamlit app
st.title('Marketing Campaigns A/B Testing')

# Sidebar widgets for user interaction
Campaign_name_filter = st.selectbox('Select Campaign Name', options=['All'] + control_group['Campaign Name'].unique().tolist())
spend_min = st.slider('Minimum Spend [USD]', min_value=0, max_value=int(control_group['Spend [USD]'].max()), value=0)
spend_max = st.slider('Maximum Spend [USD]', min_value=0, max_value=int(control_group['Spend [USD]'].max()), value=int(control_group['Spend [USD]'].max()))

# Filter the data based on user selections
filtered_control_group = control_group.copy()
filtered_test_group = test_group.copy()

if Campaign_name_filter != 'All':
    filtered_control_group = filtered_control_group[filtered_control_group['Campaign Name'] == Campaign_name_filter]
    filtered_test_group = filtered_test_group[filtered_test_group['Campaign Name'] == Campaign_name_filter]

filtered_control_group = filtered_control_group[(filtered_control_group['Spend [USD]'] >= spend_min) & (filtered_control_group['Spend [USD]'] <= spend_max)]
filtered_test_group = filtered_test_group[(filtered_test_group['Spend [USD]'] >= spend_min) & (filtered_test_group['Spend [USD]'] <= spend_max)]

# Create the box plot based on the filtered data
box_plot_spend = go.Figure()

box_plot_spend.add_trace(go.Box(x=filtered_control_group['Campaign Name'], y=filtered_control_group['Spend [USD]'], name='Control Campaign', boxpoints='all'))
box_plot_spend.add_trace(go.Box(x=filtered_test_group['Campaign Name'], y=filtered_test_group['Spend [USD]'], name='Test Campaign', boxpoints='all'))

box_plot_spend.update_layout(title='Spend Comparison - Control vs. Test Campaign', xaxis_title='Campaign Name', yaxis_title='Spend [USD]')

# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(box_plot_spend)

# Streamlit app footer (optional)
st.sidebar.text("Powered by Streamlit and Plotly")

