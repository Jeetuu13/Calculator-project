import tkinter as tk


# Function to update the expression in the entry widget
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the current entry field
    entry.insert(tk.END, current + key)  # Insert the key pressed


# Function to evaluate the expression and display the result
def evaluate():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression using eval
        entry.delete(0, tk.END)  # Clear the current entry field
        entry.insert(tk.END, result)  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Show error if the expression is invalid


# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)


# Function to add opening bracket to the expression
def add_open_bracket():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "(")


# Function to add closing bracket to the expression
def add_close_bracket():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + ")")


# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")  # Set the window size
root.config(bg="skyblue")  # Sky blue background color for the window

# Entry widget for showing the expression or result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#f0f0f0",
                 fg="#333")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
]

# Define a simple color scheme for buttons: white for numbers, light green for operations
button_colors = [
    "#FFFFFF", "#FFFFFF", "#FFFFFF", "#90EE90",  # Row 1
    "#FFFFFF", "#FFFFFF", "#FFFFFF", "#90EE90",  # Row 2
    "#FFFFFF", "#FFFFFF", "#FFFFFF", "#90EE90",  # Row 3
    "#FFFFFF", "#FFFFFF", "#FFFFFF", "#90EE90",  # Row 4
    "#FFFFFF", "#90EE90", "#90EE90"  # Row 5
]

# Create and place buttons in the grid with simple color design
button_style = {
    "width": 5,
    "height": 2,
    "font": ("Arial", 18),
    "bd": 4,
    "relief": "raised",
}

for (text, row, col), color in zip(buttons, button_colors):
    if text == '=':
        button = tk.Button(root, text=text, **button_style, bg=color, fg="black", command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, **button_style, bg=color, fg="black", command=clear)
    elif text == '(':
        button = tk.Button(root, text=text, **button_style, bg=color, fg="black", command=add_open_bracket)
    elif text == ')':
        button = tk.Button(root, text=text, **button_style, bg=color, fg="black", command=add_close_bracket)
    else:
        button = tk.Button(root, text=text, **button_style, bg=color, fg="black", command=lambda t=text: press(t))

    button.grid(row=row, column=col, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
