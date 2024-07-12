import streamlit as st
import pandas as pd

def main():
    st.title("CSV File Upload")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)
        
        # Display the CSV file
        st.write(data)

if __name__ == "__main__":
    main()
