

import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Load your data for the control and test sets
control_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/control_group.csv')
test_data = pd.read_csv('test_group.csv')

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

# Streamlit app footer (optional)
st.sidebar.text("Powered by Streamlit and Plotly")
