#tkinter window to calculate the age of a person based on the current year and birth year
from tkinter import *

root = Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Create input fields
label1 = Label(root, text="Enter current year:")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = Label(root, text="Enter birth year:")
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create result label
result_label = Label(root, text="Age:")
result_label.grid(row=2, column=0, padx=10, pady=5)
result_entry = Entry(root)
result_entry.grid(row=2, column=1, padx=10, pady=5)

# Function to calculate age
def calculate_age():
    try:
        current_year = int(entry1.get())
        birth_year = int(entry2.get())
        age = current_year - birth_year
        result_entry.delete(0, END)
        result_entry.insert(0, str(age))
    except ValueError:
        result_entry.delete(0, END)
        result_entry.insert(0, "Invalid input")

# Create button
button = Button(root, text="Calculate Age", command=calculate_age)
button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
