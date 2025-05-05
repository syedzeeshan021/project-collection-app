import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title('Sample Data Dashboard')

    uploaded_file = st.file_uploader("Choose a file", type="csv")

    if uploaded_file is not None:
        st.write("File uploaded...")
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Previewer")
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
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y-axis column", columns)

        if st.button("Generate Plot"):
            if filtered_df.empty:
                st.write("Cannot generate plot because filtered data is empty.")
            elif x_column not in filtered_df.columns or y_column not in filtered_df.columns:
                st.write("Selected columns for plotting are not in filtered data.")
            else:
                try:
                    st.line_chart(filtered_df.set_index(x_column)[y_column])
                except Exception as e:
                    st.write(f"An error occurred while generating the plot: {e}")

    else:
        st.write("Waiting on file upload...")


