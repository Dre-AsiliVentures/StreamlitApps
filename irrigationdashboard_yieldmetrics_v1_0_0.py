import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

# Define constants
CROP_TYPES = ["Wheat", "Corn", "Soybeans"]
IRRIGATION_INTERVALS = ["Daily", "Weekly", "Monthly"]
GROSS_APPLICATION_DEPTHS = ["2 inches", "4 inches", "6 inches"]

# Define function to generate data
def generate_data(crop_type, irrigation_interval, gross_application_depth):
    # Generate random data using NumPy
    days = np.arange(1, 366)
    yield_per_acre = np.random.normal(loc=100, scale=10, size=365)
    water_use = np.random.normal(loc=10, scale=1, size=365)
    economic_value = np.random.normal(loc=500, scale=50, size=365)
    irrigation_efficiency = np.random.normal(loc=0.8, scale=0.1, size=365)
    gross_margin = np.random.normal(loc=10000, scale=1000, size=365)

    # Calculate water use efficiency and water productivity
    wue = yield_per_acre / water_use
    wp = yield_per_acre / (water_use * economic_value)

    # Filter data based on selected crop type, irrigation interval, and gross application depth
    if crop_type == "Wheat":
        yield_per_acre = yield_per_acre * 1.2
    elif crop_type == "Soybeans":
        yield_per_acre = yield_per_acre * 0.8

    if irrigation_interval == "Weekly":
        water_use = water_use * 7
    elif irrigation_interval == "Monthly":
        water_use = water_use * 30

    if gross_application_depth == "4 inches":
        gross_margin = gross_margin * 0.9
    elif gross_application_depth == "6 inches":
        gross_margin = gross_margin * 1.1

    return days, yield_per_acre, wue, wp, irrigation_efficiency, gross_margin

# Set page title and layout
#st.set_page_config(page_title="Irrigation Dashboard", page_layout="wide")

# Add page header
st.title("Irrigation Dashboard")

# Add sliders for selecting crop type, irrigation interval, and gross application depth
crop_type = st.select_slider("Select Crop Type", options=CROP_TYPES)
irrigation_interval = st.select_slider("Select Irrigation Interval", options=IRRIGATION_INTERVALS)
gross_application_depth = st.select_slider("Select Gross Application Depth", options=GROSS_APPLICATION_DEPTHS)

# Generate data based on selected sliders
days, yield_per_acre, wue, wp, irrigation_efficiency, gross_margin = generate_data(crop_type, irrigation_interval, gross_application_depth)

# Add line chart for yield per acre
st.subheader("Crop Yield per Acre")
yield_chart_data = {"Days": days, "Yield per Acre": yield_per_acre}
yield_chart_df = pd.DataFrame(yield_chart_data)
yield_chart = sns.lineplot(data=yield_chart_df, x="Days", y="Yield per Acre", color="green")
yield_chart.set(xlabel="Days", ylabel="Yield per Acre (bushels)")

# Add scatter plot for water use efficiency
st.subheader("Water Use Efficiency (WUE)")
wue_chart_data = {"Yield per Acre": yield_per_acre, "Water Use": wue}
wue_chart_df = pd.DataFrame(wue_chart_data)
wue_chart = sns.scatterplot(data=wue_chart_df, x="Water Use", y="Yield per Acre", color="blue")
wue_chart.set(xlabel="Water Use (gallons)", ylabel="Yield per Acre (bushels)")

# Add bar chart for water productivity
st.subheader("Water Productivity (WP)")
wp_chart_data = {"Days": days, "Water Productivity": wp}
wp_chart_df = pd.DataFrame(wp_chart_data)
wp_chart = sns.barplot(data=wp_chart_df, x="Days", y="Water Productivity", color="purple")
wp_chart.set(xlabel="Days", ylabel="Water Productivity (bushels/gallon)")

# Add line chart for irrigation efficiency
st.subheader("Irrigation Efficiency")
irrigation_chart_data = {"Days": days, "Irrigation Efficiency": irrigation_efficiency}
irrigation_chart_df = pd.DataFrame(irrigation_chart_data)
irrigation_chart = sns.lineplot(data=irrigation_chart_df, x="Days", y="Irrigation Efficiency", color="orange")
irrigation_chart.set(xlabel="Days", ylabel="Irrigation Efficiency")

# Add line chart for gross margin
st.subheader("Gross Margin")
gross_margin_chart_data = {"Days": days, "Gross Margin": gross_margin}
gross_margin_chart_df = pd.DataFrame(gross_margin_chart_data)
gross_margin_chart = sns.lineplot(data=gross_margin_chart_df, x="Days", y="Gross Margin", color="red")
gross_margin_chart.set(xlabel="Days", ylabel="Gross Margin ($)")

# Display charts
st.pyplot(yield_chart.figure)
st.pyplot(wue_chart.figure)
st.pyplot(wp_chart.figure)
st.pyplot(irrigation_chart.figure)
st.pyplot(gross_margin_chart.figure)

