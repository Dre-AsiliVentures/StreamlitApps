#Shows the impact of precision agriculture on crop yield and quality, modified V1.0.0 with the existing code 
# includes visualizations such as line charts or scatter plots. 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load crop data from CSV file
csv_url= "https://raw.githubusercontent.com/ElectronicsDr/StreamlitApps/main/crop_data.csv"
crop_data = pd.read_csv(csv_url)

# Set up sidebar for selecting crop
crop = st.sidebar.selectbox('Select a crop', crop_data['crop'].unique())

# Filter data to selected crop
crop_subset = crop_data[crop_data['crop'] == crop]

# Calculate yield mean and standard deviation for selected crop
yield_mean = crop_subset['yield'].mean()
yield_std = crop_subset['yield'].std()

# Calculate fertilizer mean and standard deviation for selected crop
fert_mean = crop_subset['fertilizer'].mean()
fert_std = crop_subset['fertilizer'].std()

# Generate random yield and fertilizer values based on selected crop
n_samples = st.slider('Number of samples', 10, 1000, 100)
yield_samples = np.random.normal(yield_mean, yield_std, size=n_samples)
fert_samples = np.random.normal(fert_mean, fert_std, size=n_samples)

# Display histogram of yield and fertilizer values
fig, ax = plt.subplots()
ax.hist(yield_samples)
ax.set_xlabel('Crop Selected Yields')
ax.set_ylabel('Frequency')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(fert_samples)
ax.set_xlabel('Fertilizer Usage')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Calculate the correlation between fertilizer and yield
correlation = crop_subset['yield'].corr(crop_subset['fertilizer'])

# Create a line chart to display the relationship between fertilizer and yield
fig, ax = plt.subplots()
ax.plot(crop_subset['fertilizer'], crop_subset['yield'], 'o')
ax.set_xlabel('Fertilizer Usage')
ax.set_ylabel('Crop Yields')
ax.set_title('Impact of Fertilizer Usage on Crop Yields')
ax.text(0.1, 0.9, f'Correlation: {correlation:.2f}', transform=ax.transAxes)
st.pyplot(fig)
