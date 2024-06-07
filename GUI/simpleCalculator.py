# Instruction: Create a Python Tkinter program for a simple calculator
import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(operand1_entry.get())
        num2 = float(operand2_entry.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        elif operation == "^":
            result = num1 ** num2
        elif operation == "Mod":
            result = num1 % num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Invalid input")

def clear():
    operand1_entry.delete(0, tk.END)
    operand2_entry.delete(0, tk.END)
    result_label.config(text="Result:")
    operation_var.set("")

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Simple Calculator")

# Operator frame
operators_frame = ttk.Frame(window)
operators_frame.pack(side=tk.LEFT, padx=10, pady=10)

operators = ["+", "-", "*", "/", "^", "Mod"]
for i, operator in enumerate(operators):
    ttk.Button(operators_frame, text=operator, command=lambda op=operator: operation_var.set(op)).grid(row=i, column=0, padx=5, pady=5)

# Operation frame
operation_frame = ttk.Frame(window)
operation_frame.pack(side=tk.LEFT, padx=10, pady=10)

operation_label = ttk.Label(operation_frame, text="Operation:")
operation_label.grid(row=0, column=0, columnspan=2)

operation_var = tk.StringVar(value="")
operation_entry = ttk.Entry(operation_frame, textvariable=operation_var, state="readonly")
operation_entry.grid(row=1, column=0, columnspan=2)

operand1_label = ttk.Label(operation_frame, text="Operand 1:")
operand1_label.grid(row=2, column=0)
operand1_entry = ttk.Entry(operation_frame)
operand1_entry.grid(row=2, column=1)

operand2_label = ttk.Label(operation_frame, text="Operand 2:")
operand2_label.grid(row=3, column=0)
operand2_entry = ttk.Entry(operation_frame)
operand2_entry.grid(row=3, column=1)

result_label = ttk.Label(operation_frame, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

# Button frame
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear)
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = ttk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=10)

calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

window.mainloop()