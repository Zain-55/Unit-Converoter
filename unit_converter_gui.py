import streamlit as st

# Conversion function
def convert(value, from_unit, to_unit):
    try:
        value = float(value)
        conversions = {
            "Meter to Kilometer": value / 1000,
            "Kilometer to Meter": value * 1000,
            "Kg to Grams": value * 1000,
            "Grams to Kg": value / 1000,
            "Celsius to Fahrenheit": (value * 9/5) + 32,
            "Fahrenheit to Celsius": (value - 32) * 5/9
        }
        
        key = f"{from_unit} to {to_unit}"
        result = conversions.get(key, "Invalid Conversion")
        
        if result != "Invalid Conversion":
            return f"{result:.2f} {to_unit}"
        else:
            return "Invalid Conversion!"
    except ValueError:
        return "Enter a valid number!"

# Streamlit UI
st.title("📏 Unit Converter")

value = st.text_input("Enter value:")
units = ["Meter", "Kilometer", "Kg", "Grams", "Celsius", "Fahrenheit"]

from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)

if st.button("Convert"):
    result = convert(value, from_unit, to_unit)
    st.success(result)
