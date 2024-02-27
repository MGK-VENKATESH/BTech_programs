import tkinter as tk
from tkinter import messagebox


def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        messagebox.showinfo("Result", f"The result is: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create the main window
window = tk.Tk()
window.title("Expression Calculator")

# Create an entry field for the expression
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button to calculate the expression
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Run the GUI
window.mainloop()
