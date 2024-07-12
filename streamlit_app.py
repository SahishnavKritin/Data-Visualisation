import streamlit as st
import pandas as pd
import numpy as np

# Generate some sample data
np.random.seed(0)
data = pd.DataFrame({
    'x': range(100),
    'y': np.random.randint(0, 1000, 100)
})

# Display the line chart with manually set y-axis range
st.line_chart(data.set_index('x'), use_container_width=True, y_axis_auto_range=False, y_axis_range=[0, 1000])
