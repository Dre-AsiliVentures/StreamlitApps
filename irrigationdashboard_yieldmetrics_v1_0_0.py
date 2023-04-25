import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Set page header
st.header("My Streamlit App")

# Set slider for selecting a value
x_min = st.slider("Select x_min", -10.0, 10.0, -5.0)
x_max = st.slider("Select x_max", -10.0, 10.0, 5.0)

# Generate some data
x = np.linspace(x_min, x_max, 100)
y = np.sin(x)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Sine Wave")
st.pyplot(fig)
