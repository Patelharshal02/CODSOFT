import tkinter as tk

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def mod(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    else:
        return a % b

def calculate():
    operation = operation_var.get()
    val1 = int(val1_entry.get())
    val2 = int(val2_entry.get())

    if operation == "Addition":
        result_var.set(add(val1, val2))
    elif operation == "Subtraction":
        result_var.set(sub(val1, val2))
    elif operation == "Multiplication":
        result_var.set(mul(val1, val2))
    elif operation == "Division":
        result_var.set(div(val1, val2))
    elif operation == "Modulus":
        result_var.set(mod(val1, val2))

root = tk.Tk()
root.title("Simple Calculator")

default_font = ("Helvetica", 12)

val1_label = tk.Label(root, text="Enter 1st number:", font=default_font)
val1_entry = tk.Entry(root, font=default_font)
val2_label = tk.Label(root, text="Enter 2nd number:", font=default_font)
val2_entry = tk.Entry(root, font=default_font)
operation_label = tk.Label(root, text="Select operation:", font=default_font)
operation_var = tk.StringVar(root)
operation_var.set("Addition")
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Modulus")
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=default_font)
result_label = tk.Label(root, text="Result:", font=default_font)
result_var = tk.StringVar(root)
result_entry = tk.Entry(root, textvariable=result_var, state="readonly", font=default_font)

entry_width = 20
val1_entry.config(width=entry_width)
val2_entry.config(width=entry_width)
result_entry.config(width=entry_width)


val1_label.grid(row=0, column=0, padx=5, pady=5)
val1_entry.grid(row=0, column=1, padx=5, pady=5)
val2_label.grid(row=1, column=0, padx=5, pady=5)
val2_entry.grid(row=1, column=1, padx=5, pady=5)
operation_label.grid(row=2, column=0, padx=5, pady=5)
operation_menu.grid(row=2, column=1, padx=5, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=4, column=0, padx=5, pady=5)
result_entry.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()
