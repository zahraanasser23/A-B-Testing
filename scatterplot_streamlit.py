# Check if data loaded successfully
if control_data is not None and test_data is not None:
    # Streamlit app title
    st.title('Clicks vs. Purchase Correlation')

    # Sidebar filters (if needed)
    st.sidebar.header('Filter Data')
    # Add filter options if necessary

    # Scatterplot
    st.subheader('Scatterplot')
    
    # Create a scatterplot for control_data
    fig_control = px.scatter(
        control_data,
        x='# of Website Clicks',
        y='# of Purchase',
        color_discrete_sequence=['blue'],
        symbol='Campaign Name',
        size='# of Website Clicks',
        size_max=20,
        title='Clicks vs. Purchase Correlation - Control Campaign'
    )
    
    # Create a scatterplot for test_data
    fig_test = px.scatter(
        test_data,
        x='# of Website Clicks',
        y='# of Purchase',
        color_discrete_sequence=['red'],
        symbol='Campaign Name',
        size='# of Website Clicks',
        size_max=20,
        title='Clicks vs. Purchase Correlation - Test Campaign'
    )
    
    # Display the scatterplots
    st.plotly_chart(fig_control, use_container_width=True)
    st.plotly_chart(fig_test, use_container_width=True)

    # Additional data analysis or visualizations can be added here

else:
    st.error("Data loading failed. Please check your data files and format.")

# Streamlit app footer (optional)
st.sidebar.text("Powered by Streamlit and Plotly")

