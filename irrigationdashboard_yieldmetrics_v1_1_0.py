import pandas as pd
import streamlit as st

# Read crop details from Excel file
crop_details = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/04/FYR-07-DATABASE-ANALYTICS-COMPLETE.xlsx', sheet_name='Crop Details')

# Extract crop names and Kc values
CROP_TYPES = {}
for i, row in crop_details.iterrows():
    crop_name = row['Crop Name']
    kc = row['Kc Ini']
    CROP_TYPES[crop_name] = {'kc': kc, 'yield_coeff': 3.5, 'price': 300}

def compute_irrigation_info(crop_type, irrigation_interval, gross_irrigation_depth):
    crop_params = CROP_TYPES[crop_type]
    kc = crop_params['kc']
    yield_coeff = crop_params['yield_coeff']
    price = crop_params['price']

    depth_values = [gross_irrigation_depth / 2, gross_irrigation_depth / 2]
    interval_values = [irrigation_interval, irrigation_interval]

    water_applied = sum(depth_values) * kc
    yield_per_ha = yield_coeff * water_applied
    wue = yield_per_ha / sum(depth_values)
    wp = yield_per_ha / (sum(depth_values) * price)
    irrigation_efficiency = sum(depth_values) / (sum(depth_values) + water_applied)

    gross_margin = yield_per_ha * price

    return {
        'Irrigation Interval (days)': interval_values,
        'Irrigation Application Depth (mm)': depth_values,
        'Crop Yield per Acre (kg/ha)': yield_per_ha,
        'Water Use Efficiency (WUE) in percentage': wue * 100,
        'Water Productivity (WP)': wp,
        'Irrigation Efficiency in percentage': irrigation_efficiency * 100,
        'Gross Margin (Dollars)': gross_margin
    }

st.sidebar.title('Irrigation Calculator')

crop_type = st.sidebar.selectbox('Crop type', list(CROP_TYPES.keys()))
irrigation_interval = st.sidebar.slider('Irrigation Interval (days)', 1, 30, 7)
gross_irrigation_depth = st.sidebar.slider('Gross Irrigation Depth (mm)', 100, 500, 250)

results = compute_irrigation_info(crop_type, irrigation_interval, gross_irrigation_depth)

st.title(f'Irrigation Information for {crop_type}')
st.write(results)
