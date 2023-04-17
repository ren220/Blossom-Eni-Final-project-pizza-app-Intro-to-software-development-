import tkinter as tk
from tkinter import messagebox

# Define pizza prices
pizza_prices = {
    "Pepperoni": 6.99,
    "Mushroom": 7.00,
    "Detroit Pizza": 17.00,
    "Greek Pizza": 20.00,
    "New York Pizza": 10.00
}

# Define tax rate
tax_rate = 0.08

# Create main window
root = tk.Tk()
root.title("Pizza App")

# Create login window
login_window = tk.Toplevel(root)
login_window.title("Login")

# Create login label and entry
login_label = tk.Label(login_window, text="Login:")
login_label.pack()
login_entry = tk.Entry(login_window)
login_entry.pack()

# Create pizza selection frame
pizza_frame = tk.Frame(root)
pizza_frame.pack(pady=10)

# Create pizza selection labels and checkboxes
for pizza, price in pizza_prices.items():
    checkbox = tk.Checkbutton(pizza_frame, text=f"{pizza} - ${price:.2f}")
    checkbox.pack(anchor=tk.W)

# Create total price label and variable
total_price_var = tk.StringVar()
total_price_label = tk.Label(root, textvariable=total_price_var)
total_price_label.pack()

# Calculate total price function
def calculate_total_price():
    total_price = 0.0
    for pizza, price in pizza_prices.items():
        if pizza_vars[pizza].get():
            total_price += price
    total_price_with_tax = total_price * (1 + tax_rate)
    total_price_var.set(f"Total Price (with Tax): ${total_price_with_tax:.2f}")

# Create pizza vars to store the states of the checkboxes
pizza_vars = {}
for pizza in pizza_prices.keys():
    pizza_vars[pizza] = tk.BooleanVar()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_total_price)
calculate_button.pack(pady=10)

# Create display button
display_button = tk.Button(root, text="Display", command=lambda: messagebox.showinfo("Selected Pizzas", "\n".join([pizza for pizza, var in pizza_vars.items() if var.get()])))
display_button.pack()

# Run main loop
root.mainloop()
