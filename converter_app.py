import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert_units():
    try:
        input_value = float(entry_input.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()
        result = None

        if category == "Rupee Converter":
            rupee_factors = {"INR": 1, "USD": 0.012, "EUR": 0.011, "GBP": 0.0097}
            result = input_value * rupee_factors[to_unit] / rupee_factors[from_unit]
        
        elif category == "Currency Converter":
            currency_factors = {"USD": 1, "EUR": 0.92, "GBP": 0.77, "INR": 82.5}
            result = input_value * currency_factors[to_unit] / currency_factors[from_unit]
        
        elif category == "Distance Converter":
            distance_factors = {"Kilometers": 1, "Miles": 0.621371, "Meters": 1000, "Yards": 1093.61}
            result = input_value * distance_factors[to_unit] / distance_factors[from_unit]
        
        elif category == "Temperature Converter":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (input_value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (input_value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = input_value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = input_value - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (input_value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (input_value - 273.15) * 9/5 + 32
            else:
                result = input_value  # Same unit

        if result is not None:
            label_result.config(text=f"Result: {result:.4f} {to_unit}")
        else:
            label_result.config(text="Conversion not supported.")
    except ValueError:
        label_result.config(text="Please enter a valid number.")

# Update unit options based on category
def update_units(event):
    category = combo_category.get()
    units = []
    
    if category == "Rupee Converter":
        units = ["INR", "USD", "EUR", "GBP"]
    elif category == "Currency Converter":
        units = ["USD", "EUR", "GBP", "INR"]
    elif category == "Distance Converter":
        units = ["Kilometers", "Miles", "Meters", "Yards"]
    elif category == "Temperature Converter":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    
    combo_from["values"] = units
    combo_to["values"] = units
    combo_from.current(0)
    combo_to.current(0)

# GUI setup
root = tk.Tk()
root.title("Multi-Converter App")
root.geometry("500x400")

# Category selection
label_category = tk.Label(root, text="Select Converter Category:", font=("Arial", 12))
label_category.pack(pady=10)

combo_category = ttk.Combobox(root, values=["Rupee Converter", "Currency Converter", "Distance Converter", "Temperature Converter"], state="readonly")
combo_category.pack(pady=10)
combo_category.current(0)
combo_category.bind("<<ComboboxSelected>>", update_units)

# From unit selection
label_from = tk.Label(root, text="From:", font=("Arial", 10))
label_from.pack(pady=5)

combo_from = ttk.Combobox(root, state="readonly")
combo_from.pack(pady=5)

# To unit selection
label_to = tk.Label(root, text="To:", font=("Arial", 10))
label_to.pack(pady=5)

combo_to = ttk.Combobox(root, state="readonly")
combo_to.pack(pady=5)

# Input field
label_input = tk.Label(root, text="Enter Value:", font=("Arial", 10))
label_input.pack(pady=5)

entry_input = tk.Entry(root, font=("Arial", 12))
entry_input.pack(pady=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_units, font=("Arial", 12), bg="blue", fg="white")
btn_convert.pack(pady=20)

# Result display
label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.pack(pady=20)

# Initialize default units
update_units(None)

# Start GUI loop
root.mainloop()
