import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression in the entry widget
def evaluate_expression(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

# Function to append a character to the entry widget
def append_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear_expression(): 
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Balaji's Calculator")

# Create an entry widget
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=10, command=evaluate_expression)
        root.bind('<Return>', evaluate_expression)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: append_to_expression(t))
    button.grid(row=row, column=col)

# Add a clear button
clear_button = tk.Button(root, text='C', padx=20, pady=10, command=clear_expression)
clear_button.grid(row=4, column=1)

# Start the main event loop
root.mainloop()