#tkinter window to calculate the product of two input numbers
from tkinter import *




root = Tk()
root.title("Product Calculator")
root.geometry("300x200")

# Create input fields
label1 = Label(root, text="Enter first number:")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = Label(root, text="Enter second number:")
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create result label
result_label = Label(root, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=5)
result_entry = Entry(root)
result_entry.grid(row=2, column=1, padx=10, pady=5)

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_entry.delete(0, END)
        result_entry.insert(0, str(product))
    except ValueError:
        result_entry.delete(0, END)
        result_entry.insert(0, "Invalid input")

# Create button
button = Button(root, text="Calculate Product", command=calculate_product)
button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
