import streamlit as st

# Conversion functions
def convert_seed_rate(seed_rate, from_unit, to_unit):
    if from_unit == "seeds/ha" and to_unit == "seeds/acre":
        return seed_rate * 2.47105
    elif from_unit == "seeds/acre" and to_unit == "seeds/ha":
        return seed_rate / 2.47105
    else:
        return seed_rate

# Main application code
def main():
    st.title("Seed Rate Converter")
    
    seed_rate = st.number_input("Enter seed rate:")
    from_unit = st.selectbox("Convert from:", ["seeds/ha", "seeds/acre"])
    to_unit = st.selectbox("Convert to:", ["seeds/ha", "seeds/acre"])

    converted_rate = convert_seed_rate(seed_rate, from_unit, to_unit)

    st.write(f"Converted seed rate: {converted_rate} {to_unit}")
    
if __name__ == "__main__":
    main()
