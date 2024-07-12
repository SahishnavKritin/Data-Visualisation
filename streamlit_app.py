import streamlit as st
import pandas as pd
import altair as alt

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

        # Checkbox for downsampling
        downsample_option = st.checkbox("Apply Downsampling")

        # Show downsampling options if checked
        if downsample_option:
            downsample_factor = st.selectbox("Select Downsampling Factor", [2, 3, 4, 6])
            data[selected_column] = downsample(data[selected_column], downsample_factor)

        # Checkbox for moving average
        moving_avg_option = st.checkbox("Apply Moving Average")

        # Show moving average options if checked
        if moving_avg_option:
            moving_avg_window = st.number_input("Select Moving Average Window Size (4 or above)", min_value=4, step=1, value=4)
            data[selected_column] = moving_average(data[selected_column], moving_avg_window)

        # Select plot segment
        start_index = st.number_input("Start Index", min_value=0, max_value=len(data)-1, step=1, value=0)
        end_index = st.number_input("End Index", min_value=0, max_value=len(data)-1, step=1, value=len(data)-1)

        # Get the range of transformed data to plot
        plot_data = data[selected_column][start_index:end_index]

        # Compute y-axis range based on the transformed data
        y_min = plot_data.min()
        y_max = plot_data.max()

        # Create Altair chart
        chart = alt.Chart(data.iloc[start_index:end_index]).mark_line().encode(
            x='index',
            y=alt.Y(selected_column, scale=alt.Scale(domain=[y_min, y_max]))
        ).properties(
            width=600,
            height=400
        )

        # Display Altair chart using st.altair_chart
        st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    main()
