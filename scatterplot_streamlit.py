import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data for the control and test sets with the correct delimiter
try:
    control_data = pd.read_csv('control_data.csv', delimiter=';')
    test_data = pd.read_csv('test_data.csv', delimiter=';')
except Exception as e:
    st.error(f"An error occurred while loading data: {str(e)}")
    control_data = None
    test_data = None

# Check if data loaded successfully
if control_data is not None and test_data is not None:
    # Streamlit app title
    st.title('Clicks vs. Purchase Correlation')

    # ... (Rest of your Streamlit code)
else:
    st.error("Data loading failed. Please check your data files and format.")

# Streamlit app footer (optional)
st.sidebar.text("Powered by Streamlit and Plotly")
