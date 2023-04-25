import numpy as np
import streamlit as st
import plotly.graph_objs as go

# Prompt:
# Use numpy to generate crop, irrigation values. But don't use matplotlib. Then use Streamlit to display these irrigation metrics:
# - Crop yield per acre
# - Water use efficiency (WUE)
# - Water productivity (WP)
# - Irrigation efficiency
# - Gross margin
# The irrigation input values are the irrigation intervals and irrigation application depth.

# Generate random crop and irrigation values using NumPy
crop_yield = np.random.randint(50, 100, size=10)  # Crop yields per acre (in bushels)
irrigation_intervals = st.slider("Irrigation intervals (days)", 1, 10, 5, 1)  # Irrigation intervals (in days)
irrigation_depths = st.slider("Gross irrigation depth (inches)", 1, 10, 5, 1)  # Irrigation application depth (in inches)

# Calculate the various irrigation metrics
water_applied = irrigation_depths * 0.623  # Convert inches to millimeters using a conversion factor of 0.623
crop_production = crop_yield * 25.4  # Convert bushels to millimeters using a conversion factor of 25.4
wue = crop_production / water_applied  # Water use efficiency (in mm/mm)
crop_value = np.random.randint(10, 20, size=10)  # Crop values (in dollars)
wp = crop_production / (water_applied * crop_value)  # Water productivity (in mm/mm/$)
water_lost = np.random.randint(10, 20, size=10)  # Water lost (in percent)
irrigation_efficiency = (100 - water_lost) / 100  # Irrigation efficiency (dimensionless)
variable_costs = np.random.randint(500, 1000, size=10)  # Variable costs (in dollars)
revenue = crop_yield * crop_value  # Revenue (in dollars)
gross_margin = revenue - variable_costs  # Gross margin (in dollars)

# Create a bar chart to compare the different irrigation metrics
metrics = ["Crop Yield per Acre (bushels)", "Water Use Efficiency (mm/mm)", "Water Productivity (mm/mm/$)", "Irrigation Efficiency", "Gross Margin ($/acre)"]
metric_values = [crop_yield.mean(), wue.mean(), wp.mean(), irrigation_efficiency.mean(), gross_margin.mean()]

fig = go.Figure(data=[go.Bar(x=metrics, y=metric_values)])
fig.update_layout(title="Irrigation Metrics Comparison", xaxis_title="Metric", yaxis_title="Value")

# Display the irrigation metrics and the bar chart using Streamlit
st.write("Irrigation Metrics:")
st.write("Crop Yield per Acre (bushels/acre):", crop_yield)
st.write("Water Use Efficiency (mm/mm):", wue)
st.write("Water Productivity (mm/mm/$):", wp)
st.write("Irrigation Efficiency (dimensionless):", irrigation_efficiency)
st.write("Gross Margin ($/acre):", gross_margin)

st.plotly_chart(fig)
