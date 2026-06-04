import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        result_label.config(text=f"Area = {area}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
rectangle = tk.Tk()
rectangle.title("Rectangle Area Calculator")
rectangle.geometry("360x200")
tk.Label(rectangle, text="Enter Length:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(rectangle, text="Enter Width:").grid(row=1, column=0, padx=10, pady=10)
entry_length = tk.Entry(rectangle)
entry_length.grid(row=0, column=1, padx=10, pady=10)
entry_width = tk.Entry(rectangle)
entry_width.grid(row=1, column=1, padx=10, pady=10)
tk.Button(rectangle, text="Calculate Area", command=calculate_area).grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(rectangle, text="")
result_label.grid(row=3, column=0, columnspan=2)
rectangle.mainloop()

