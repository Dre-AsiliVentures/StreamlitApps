""" Seed Rate converter.py
Seed rate refers to the amount of seeds used/needed to plant a specific area of land

This converter application convers the seed rate from seed Rate/ha to Seed Rate/acre and vice versa
"""
import streamlit as st

# Conversion functions
def convert_seed_rate(seed_rate, from_unit, to_unit):
    if from_unit == "seeds/ha" and to_unit == "seeds/acre":
        return seed_rate * 2.47105
    elif from_unit == "seeds/acre" and to_unit == "seeds/ha":
        return seed_rate / 2.47105
    elif from_unit == "kg/ha" and to_unit == "kg/acre":
        return seed_rate * 0.404686
    elif from_unit == "kg/acre" and to_unit == "kg/ha":
        return seed_rate / 0.404686
    elif from_unit == "lbs/ha" and to_unit == "lbs/acre":
        return seed_rate * 0.892179
    elif from_unit == "lbs/acre" and to_unit == "lbs/ha":
        return seed_rate / 0.892179
    else:
        return seed_rate

# Main application code
def main():
    st.title("Seed Rate Converter")
    
    seed_rate = st.number_input("Enter seed rate:")
    from_unit = st.selectbox("Convert from:", ["seeds/ha", "seeds/acre", "kg/ha", "kg/acre", "lbs/ha", "lbs/acre"])
    to_unit = st.selectbox("Convert to:", ["seeds/ha", "seeds/acre", "kg/ha", "kg/acre", "lbs/ha", "lbs/acre"])

    converted_rate = convert_seed_rate(seed_rate, from_unit, to_unit)

    st.write(f"Converted seed rate: {converted_rate} {to_unit}")
    
if __name__ == "__main__":
    main()

