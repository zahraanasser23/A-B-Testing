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

import streamlit as st
import pandas as pd
import plotly.express as px


# Interactive feature: Select parameter for animation
animation_parameter = st.selectbox('Select Animation Parameter', ['# of Website Clicks', '# of Purchase'])

# Create scatter plot for Control Group
fig_control = px.scatter(control_group, x=animation_parameter, y='# of Purchase', color='Campaign Name',
                         size_max=20, title='Clicks vs. Purchase Correlation - Control Campaign',
                         labels={animation_parameter: 'Clicks', '# of Purchase': 'Purchase'},
                         animation_frame='Campaign Name')

# Set color scale for the Control Group
fig_control.update_traces(marker=dict(size=12, opacity=0.7), selector=dict(mode='markers+text'))

# Create scatter plot for Test Group
fig_test = px.scatter(test_group, x=animation_parameter, y='# of Purchase', color='Campaign Name',
                      size_max=20, title='Clicks vs. Purchase Correlation - Test Campaign',
                      labels={animation_parameter: 'Clicks', '# of Purchase': 'Purchase'},
                      animation_frame='Campaign Name')

# Set color scale for the Test Group
fig_test.update_traces(marker=dict(size=12, opacity=0.7), selector=dict(mode='markers+text'))

# Display the Control and Test plots side by side
st.plotly_chart(fig_control, use_container_width=True)
st.plotly_chart(fig_test, use_container_width=True)



