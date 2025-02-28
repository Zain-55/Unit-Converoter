import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

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
            label_result.config(text=f"Result: {result:.2f} {to_unit}")
        else:
            label_result.config(text="Invalid Conversion!")
    except ValueError:
        label_result.config(text="Enter a valid number!")

# GUI Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Title Label
label_title = tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Entry Field
entry_value = tk.Entry(root, width=20)
entry_value.pack(pady=5)

# From Unit Dropdown
units = ["Meter", "Kilometer", "Kg", "Grams", "Celsius", "Fahrenheit"]
combo_from = ttk.Combobox(root, values=units)
combo_from.pack(pady=5)
combo_from.set("Select From")

# To Unit Dropdown
combo_to = ttk.Combobox(root, values=units)
combo_to.pack(pady=5)
combo_to.set("Select To")

# Convert Button
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

# Run App
root.mainloop()
