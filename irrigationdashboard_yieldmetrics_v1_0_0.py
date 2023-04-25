import streamlit as st
import numpy as np

# Define a dictionary of crops and their yield ranges
crops = {
    "Wheat": (2000, 5000),
    "Corn": (3000, 8000),
    "Rice": (4000, 10000)
}

# Define a function to generate random values for the selected crop
def generate_values(crop):
    yield_range = crops[crop]
    crop_yield = np.random.randint(yield_range[0], yield_range[1]+1, size=1)[0]  # kg/ha
    water_use_efficiency = np.random.uniform(1, 4, size=1)[0]  # kg/m3
    water_productivity = np.random.randint(2, 10, size=1)[0]  # kg/m3
    irrigation_efficiency = np.random.uniform(50, 90, size=1)[0]  # %
    gross_margin = np.random.randint(1000, 5000, size=1)[0]  # USD/ha
    return crop_yield, water_use_efficiency, water_productivity, irrigation_efficiency, gross_margin

# Set up the Streamlit app
st.title("Irrigation Dashboard")
st.header("Select a Crop")
selected_crop = st.selectbox("Select a crop", list(crops.keys()))

# Generate the values for the selected crop
crop_yield, water_use_efficiency, water_productivity, irrigation_efficiency, gross_margin = generate_values(selected_crop)

# Display the selected crop and its generated values
st.header(selected_crop)
st.write("- Crop yield (kg/ha)")
st.write("- Water use efficiency (kg/m3)")
st.write("- Water productivity (kg/m3)")
st.write("- Irrigation efficiency (%)")
st.write("- Gross margin (USD/ha)")
st.write("")
st.write("Randomly Generated Values:")
st.write(f"- Crop yield: {crop_yield} kg/ha")
st.write(f"- Water use efficiency: {water_use_efficiency:.2f} kg/m3")
st.write(f"- Water productivity: {water_productivity} kg/m3")
st.write(f"- Irrigation efficiency: {irrigation_efficiency:.2f}%")
st.write(f"- Gross margin: {gross_margin} USD/ha")
