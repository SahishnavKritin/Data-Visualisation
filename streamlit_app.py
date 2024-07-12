import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("CSV File Upload and Data Processing")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)

        # Drop the first three rows
        data = data.iloc[3:].reset_index(drop=True)

        # Display the CSV file
        st.write("### CSV File Content (First 5 rows)")
        st.write(data.head())

        # Select column to plot
        columns = data.columns
        selected_column = st.selectbox("Select Column to Plot", columns)

        # Checkbox for downsampling
        downsample_option = st.checkbox("Apply Downsampling")

        # Show downsampling options if checked
        if downsample_option:
            downsample_factor = st.selectbox("Select Downsampling Factor", [2, 3, 4, 6])
            data[selected_column] = data[selected_column][::downsample_factor]

        # Checkbox for moving average
        moving_avg_option = st.checkbox("Apply Moving Average")

        # Show moving average options if checked
        if moving_avg_option:
            moving_avg_window = st.number_input("Select Moving Average Window Size (4 or above)", min_value=4, step=1, value=4)
            data[selected_column] = data[selected_column].rolling(window=moving_avg_window).mean()

        # Select plot segment
        start_index = st.number_input("Start Index", min_value=0, max_value=len(data)-1, step=1, value=0)
        end_index = st.number_input("End Index", min_value=0, max_value=len(data)-1, step=1, value=len(data)-1)

        # Get the range of transformed data to plot
        plot_data = data.iloc[start_index:end_index]

        # Plot the data using Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(plot_data.index, plot_data[selected_column], label=selected_column)
        ax.set_xlabel("Index")
        ax.set_ylabel(selected_column)
        ax.set_title(f"Plot of {selected_column}")

        # Set y-axis limits based on data range
        y_min = plot_data[selected_column].min()
        y_max = plot_data[selected_column].max()
        ax.set_ylim(y_min, y_max)

        # Display plot in Streamlit
        st.pyplot(fig)

if __name__ == "__main__":
    main()
