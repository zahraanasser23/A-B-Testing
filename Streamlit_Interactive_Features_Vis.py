
#control_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/control_group.csv')
#test_data = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/test_group.csv')


import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# Load your data for the control and test sets
#control_group = pd.read_csv('/kaggle/input/ab-testing-dataset/control_group.csv', delimiter=';')
#test_group = pd.read_csv('/kaggle/input/ab-testing-dataset/test_group.csv', delimiter=';')

#control_group = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/control_group.csv')
#test_group = pd.read_csv('https://github.com/zahraanasser23/A-B-Testing/raw/main/test_group.csv')


# Create Streamlit app
st.title('Marketing Campaigns A/B Testing')

# Create the box plot
box_plot_spend = go.Figure()

box_plot_spend.add_trace(go.Box(x=control_group['Campaign Name'], y=control_group['Spend [USD]'], name='Control Campaign', boxpoints='all'))
box_plot_spend.add_trace(go.Box(x=test_group['Campaign Name'], y=test_group['Spend [USD]'], name='Test Campaign', boxpoints='all'))

box_plot_spend.update_layout(title='Spend Comparison - Control vs. Test Campaign', xaxis_title='Campaign Name', yaxis_title='Spend [USD]')

# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(box_plot_spend)


# Filter out rows with missing or invalid data in control campaign
control_group_cleaned = control_group.dropna(subset=['# of Website Clicks', '# of Purchase'])

# Filter out rows with missing or invalid data in test campaign
test_group_cleaned = test_group.dropna(subset=['# of Website Clicks', '# of Purchase'])

# Create scatter plots for Clicks vs. Purchase correlation for both campaigns
scatter_control = px.scatter(control_group_cleaned, x='# of Website Clicks', y='# of Purchase',
                             color_discrete_sequence=['blue'],
                             symbol='Campaign Name',
                             size='# of Website Clicks', size_max=20,
                             title='Clicks vs. Purchase Correlation - Control Campaign')

scatter_test = px.scatter(test_group_cleaned, x='# of Website Clicks', y='# of Purchase',
                          color_discrete_sequence=['red'],
                          symbol='Campaign Name',
                          size='# of Website Clicks', size_max=20,
                          title='Clicks vs. Purchase Correlation - Test Campaign')

# Combine the two scatter plots
scatter_combined = px.scatter()

# Add traces from control and test scatter plots to the combined plot
for trace in scatter_control.data:
    scatter_combined.add_trace(trace)
for trace in scatter_test.data:
    scatter_combined.add_trace(trace)

# Set layout for the combined plot
scatter_combined.update_layout(title='Clicks vs. Purchase Correlation - Control vs. Test Campaign',
                               xaxis_title='# of Website Clicks', yaxis_title='# of Purchase')

# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(scatter_combined)
