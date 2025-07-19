import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Simple Streamlit Dashboard")
st.subheader("An interactive demo dashboard")

st.sidebar.header("Settings")
num_points = st.sidebar.slider("Number of Data Points", min_value=10, max_value=100, value=50)
chart_type = st.sidebar.selectbox("Chart Type", ["Line Chart", "Bar Chart"])

data = pd.DataFrame({
    'x': np.arange(num_points),
    'y': np.random.randn(num_points).cumsum()
})


st.markdown("### Chart")
if chart_type == "Line Chart":
    st.line_chart(data.set_index('x'))
else:
    st.bar_chart(data.set_index('x'))


st.markdown("### Raw Data")
st.dataframe(data)

st.markdown("### My Quote")
st.image("tvb-moonlight-resonance.gif", caption="Life is hard!")


