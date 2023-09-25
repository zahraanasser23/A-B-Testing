
#control_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/control_group.csv')
#test_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/test_group.csv')



import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Load your data for the control and test sets
control_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/control_group.csv')
test_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/test_group.csv')

# Streamlit app title
st.title('Clicks vs. Purchase Correlation')

# Sidebar filters for Clicks vs. Purchase Correlation
st.sidebar.header('Clicks vs. Purchase Correlation')

campaign_selection = st.sidebar.radio('Select Campaign', ('Control', 'Test'))

if campaign_selection == 'Control':
    data = control_data
    title = 'Control Campaign'
else:
    data = test_data
    title = 'Test Campaign'

x_column = st.sidebar.selectbox('X-axis', ['# of Website Clicks'])
y_column = st.sidebar.selectbox('Y-axis', ['# of Purchase'])

# Scatterplot for Clicks vs. Purchase Correlation
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data[x_column],
    y=data[y_column],
    mode='markers',
    marker=dict(
        size=12,
        color='blue' if campaign_selection == 'Control' else 'red',
        symbol='circle',
        line=dict(
            width=2,
            color='DarkSlateGrey'
        )
    ),
    name=title
))

fig.update_layout(
    title=f'Clicks vs. Purchase Correlation - {title}',
    xaxis_title=x_column,
    yaxis_title=y_column
)

# Sidebar filters for Spend Comparison
st.sidebar.header('Spend Comparison')

# Add the code for Spend Comparison here (from the previous response)

# Show the selected visualization (Clicks vs. Purchase Correlation or Spend Comparison)
visualization_selection = st.sidebar.radio('Select Visualization', ['Clicks vs. Purchase Correlation', 'Spend Comparison'])

if visualization_selection == 'Clicks vs. Purchase Correlation':
    st.plotly_chart(fig, use_container_width=True)
else:
    # Add the code for Spend Comparison visualization here (from the previous response)
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

# Streamlit app footer (optional)
st.sidebar.text("Powered by Streamlit and Plotly")
