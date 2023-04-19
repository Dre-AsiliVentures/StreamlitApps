import numpy as np
import pandas as pd

# Define sample farm size
farm_size = 1000  # in acres

# Generate sample data for crop yield
crop_yield = np.random.normal(loc=10, scale=2, size=farm_size)
crop_yield_data = pd.DataFrame({'Crop Yield': crop_yield})
crop_yield_data.to_csv('crop_yield.csv', index=False)

# Generate sample data for water use efficiency
water_use = np.random.normal(loc=20, scale=5, size=farm_size)
crop_yield = crop_yield * crop_yield.max() / crop_yield.mean()
water_use_efficiency = crop_yield / water_use
water_use_data = pd.DataFrame({'Water Use Efficiency': water_use_efficiency})
water_use_data.to_csv('water_use.csv', index=False)

# Generate sample data for water productivity
water_productivity = crop_yield * crop_yield.max() / (water_use * 1000)  # assume 1000 liters of water per acre
water_prod_data = pd.DataFrame({'Water Productivity': water_productivity})
water_prod_data.to_csv('water_productivity.csv', index=False)

# Generate sample data for irrigation efficiency
irrigation_efficiency = np.random.normal(loc=0.8, scale=0.1, size=farm_size)
irrigation_eff_data = pd.DataFrame({'Irrigation Efficiency': irrigation_efficiency})
irrig_eff_data.to_csv('irrigation_efficiency.csv', index=False)

# Generate sample data for gross margin
crop_value = crop_yield * 2  # assume a crop value of $2 per unit
water_cost = water_use * 0.5  # assume a water cost of $0.5 per unit
labor_cost = np.random.normal(loc=5, scale=1, size=farm_size)  # assume labor cost of $5 per acre
gross_margin = crop_value - water_cost - labor_cost
gross_margin_data = pd.DataFrame({'Crop': range(1, farm_size+1), 'Gross Margin': gross_margin})
gross_margin_data.to_csv('gross_margin.csv', index=False)

#In this example code, we use NumPy to generate sample data for each of the five metrics (crop yield, water use efficiency, water productivity, irrigation efficiency, and gross margin) based on a farm size of 1000 acres. The generated data is stored in individual CSV files.
#Note that this is just an example code, and you would need to adjust the parameters (such as mean and standard deviation) and assumptions (such as crop value and water cost) to match your specific farm and irrigation management practices.
