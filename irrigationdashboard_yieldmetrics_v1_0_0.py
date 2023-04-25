# Import necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
years = np.arange(2010, 2023)
interval_values = np.random.choice([3, 7, 14, 21], size=len(years))
depth_values = np.random.randint(50, 200, size=len(years))
yield_values = np.round(np.random.uniform(1, 4, size=len(years)), decimals=2)
wue_values = np.round(np.random.uniform(1, 3, size=len(years)), decimals=2)
wp_values = np.round(np.random.uniform(0.5, 2, size=len(years)), decimals=2)
efficiency_values = np.round(np.random.uniform(0.5, 1, size=len(years)), decimals=2)
margin_values = np.round(np.random.uniform(2000, 6000, size=len(years)), decimals=2)

# Combine data into a Pandas DataFrame
data = pd.DataFrame({
    'Year': years,
    'Irrigation Interval (days)': interval_values,
    'Irrigation Application Depth (mm)': depth_values,
    'Crop Yield per Acre': yield_values,
    'Water Use Efficiency (WUE)': wue_values,
    'Water Productivity (WP)': wp_values,
    'Irrigation Efficiency': efficiency_values,
    'Gross Margin': margin_values
})

# Create the dashboard
st.title('Irrigation Metrics Dashboard')

# Display the data
st.write(data)

# Create a sidebar for filtering the data
interval = st.sidebar.slider('Select Irrigation Interval (days)', 3, 21, 7, step=1)
depth = st.sidebar.slider('Select Irrigation Application Depth (mm)', 50, 200, 100, step=10)

# Filter the data based on the selected interval and depth
filtered_data = data[(data['Irrigation Interval (days)'] == interval) & (data['Irrigation Application Depth (mm)'] == depth)]

# Display the filtered data
st.write(filtered_data)

# Create a bar chart to display the metrics
metrics = ['Crop Yield per Acre', 'Water Use Efficiency (WUE)', 'Water Productivity (WP)', 'Irrigation Efficiency', 'Gross Margin']
selected_metric = st.selectbox('Select a Metric', metrics)

# Filter the data based on the selected metric
metric_data = filtered_data[['Year', selected_metric]]

# Set the Year column as the index
metric_data = metric_data.set_index('Year')

# Create a bar chart
fig, ax = plt.subplots()
metric_data.plot(kind='bar', ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel(selected_metric)
st.pyplot(fig)
