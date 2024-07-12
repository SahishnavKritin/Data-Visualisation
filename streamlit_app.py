import streamlit as st
import pandas as pd

def downsample(data, factor):
    return data[::factor]

def moving_average(data, window_size):
    return data.rolling(window=window_size).mean()

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

        # Select downsampling factor
        downsample_factor = st.selectbox("Select Downsampling Factor", [None, 2, 3, 4, 6])

        # Select moving average window size
        moving_avg_window = st.number_input("Select Moving Average Window Size (4 or above)", min_value=4, step=1, value=4)

        # Downsampling
        if downsample_factor:
            data[selected_column] = downsample(data[selected_column], downsample_factor)

        # Moving average
        data[selected_column] = moving_average(data[selected_column], moving_avg_window)

        # Select plot segment
        start_index = st.number_input("Start Index", min_value=0, max_value=len(data)-1, step=1, value=0)
        end_index = st.number_input("End Index", min_value=0, max_value=len(data)-1, step=1, value=len(data)-1)

        # Plot the data
        if st.button("Plot Data"):
            st.line_chart(data[selected_column][start_index:end_index])

if __name__ == "__main__":
    main()
