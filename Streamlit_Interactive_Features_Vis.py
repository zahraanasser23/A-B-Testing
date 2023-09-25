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


# Combine control and test data into a single DataFrame with a label column
control_group['Campaign Type'] = 'Control'
test_group['Campaign Type'] = 'Test'
combined_data = pd.concat([control_group, test_group])

# Create scatter plot
fig = px.scatter(combined_data, x='# of Website Clicks', y='# of Purchase', color='Campaign Type',
                 animation_frame='Campaign Name', size_max=20,
                 title='Clicks vs. Purchase Correlation - Control vs. Test Campaign',
                 labels={'# of Website Clicks': 'Clicks', '# of Purchase': 'Purchase'})

# Set color scale for Control (blue) and Test (red)
fig.update_traces(marker=dict(size=12, opacity=0.7),
                  selector=dict(mode='markers+text'))

# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(fig)


