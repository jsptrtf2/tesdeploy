import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simple Dashboard", layout="wide")

st.title("🚲 Bike Sharing Dashboard (Demo)")
st.write("Ini adalah dashboard Streamlit sederhana untuk demo deploy.")

# Generate data dummy
st.subheader("Random Data")
df = pd.DataFrame({
    "Waktu": pd.date_range(start="2023-01-01", periods=30),
    "Jumlah Penyewaan": np.random.randint(100, 500, size=30)
})

st.line_chart(df.set_index("Waktu"))

# Chart tambahan
st.subheader("Distribusi")
fig, ax = plt.subplots()
ax.hist(df["Jumlah Penyewaan"], bins=10, color="skyblue", edgecolor="black")
st.pyplot(fig)
