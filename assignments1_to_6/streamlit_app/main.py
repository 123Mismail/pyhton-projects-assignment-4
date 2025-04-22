import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Plot"])
    
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)
    
    
    plot_filtered = st.checkbox("Plot filtered data only", value=False)
    
    data_to_plot = filtered_df if plot_filtered else df

    if st.button("Generate Plot"):
        try:
            if plot_type == "Line Chart":
                st.line_chart(data_to_plot.set_index(x_column)[y_column])
            elif plot_type == "Bar Chart":
                st.bar_chart(data_to_plot.set_index(x_column)[y_column])
            elif plot_type == "Scatter Plot":
                fig, ax = plt.subplots()
                ax.scatter(data_to_plot[x_column], data_to_plot[y_column])
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)
        except Exception as e:
            st.error(f"Error generating plot: {str(e)}")
            st.info("Please check that your selected columns contain appropriate data types for plotting.")
else:
    st.write("Waiting on file upload...")