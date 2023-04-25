import numpy as np
import streamlit as st

# Objective: Display these Metrics from the inputs of the Irrigation Intervals and Gross Irrigation Depth
#  Irrigation metrics:
# - Crop yield per acre
# - Water use efficiency (WUE)
# - Water productivity (WP)
# - Irrigation efficiency
# - Gross margin
# The irrigation input values are the irrigation intervals and irrigation application depth.

# Generate random crop and irrigation values using NumPy
crop_yield = np.random.randint(50, 100, size=10)  # Crop yields per acre (in bushels)
irrigation_intervals = np.random.randint(2, 5, size=10)  # Irrigation intervals (in days)
irrigation_depths = np.random.randint(1, 4, size=10)  # Irrigation application depth (in inches)

# Calculate the various irrigation metrics
water_applied = irrigation_depths * 0.623  # Convert inches to millimeters using a conversion factor of 0.623
crop_production = crop_yield * 25.4  # Convert bushels to millimeters using a conversion factor of 25.4
wue = crop_production / water_applied  # Water use efficiency
crop_value = np.random.randint(10, 20, size=10)  # Crop values (in dollars)
wp = crop_production / (water_applied * crop_value)  # Water productivity
water_lost = np.random.randint(10, 20, size=10)  # Water lost (in percent)
irrigation_efficiency = (100 - water_lost) / 100  # Irrigation efficiency
variable_costs = np.random.randint(500, 1000, size=10)  # Variable costs (in dollars)
revenue = crop_yield * crop_value  # Revenue (in dollars)
gross_margin = revenue - variable_costs  # Gross margin (in dollars)

# Display the irrigation metrics using Streamlit
st.write("Crop Yield per Acre:")
st.write(crop_yield)
st.write("Water Use Efficiency (WUE):")
st.write(wue)
st.write("Water Productivity (WP):")
st.write(wp)
st.write("Irrigation Efficiency:")
st.write(irrigation_efficiency)
st.write("Gross Margin:")
st.write(gross_margin)
