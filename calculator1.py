# Professional Calculator App in Python (Tkinter)
# Run in VS Code

import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Main Window Setup
# -----------------------------
root = tk.Tk()
root.title("Professional Calculator")
root.geometry("380x550")
root.resizable(False, False)
root.configure(bg="#1E1E2F")

# -----------------------------
# Entry Display
# -----------------------------
expression = ""

input_text = tk.StringVar()

input_frame = tk.Frame(root, bg="#1E1E2F")
input_frame.pack(pady=20)

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=("Arial", 24, "bold"),
    width=18,
    bd=0,
    bg="#2D2D44",
    fg="white",
    justify="right",
    insertbackground="white"
)
input_field.grid(row=0, column=0)
input_field.pack(ipady=15)


# -----------------------------
# Functions
# -----------------------------
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        expression = ""
        input_text.set("")
    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        input_text.set("")


def clear():
    global expression
    expression = ""
    input_text.set("")


def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


# -----------------------------
# Button Styling
# -----------------------------
button_frame = tk.Frame(root, bg="#1E1E2F")
button_frame.pack()

btn_font = ("Arial", 16, "bold")
btn_bg = "#3A3A5A"
btn_fg = "white"
operator_bg = "#FF8C42"
equal_bg = "#00C896"
clear_bg = "#FF4C4C"

def create_button(text, row, col, command, bg=btn_bg):
    button = tk.Button(
        button_frame,
        text=text,
        width=7,
        height=2,
        font=btn_font,
        bg=bg,
        fg=btn_fg,
        bd=0,
        activebackground="#555",
        activeforeground="white",
        command=command
    )
    button.grid(row=row, column=col, padx=5, pady=5)


# -----------------------------
# Buttons Layout
# -----------------------------
buttons = [
    ('C', 0, 0, clear, clear_bg),
    ('⌫', 0, 1, backspace, clear_bg),
    ('%', 0, 2, lambda: press('%'), operator_bg),
    ('/', 0, 3, lambda: press('/'), operator_bg),

    ('7', 1, 0, lambda: press('7')),
    ('8', 1, 1, lambda: press('8')),
    ('9', 1, 2, lambda: press('9')),
    ('*', 1, 3, lambda: press('*'), operator_bg),

    ('4', 2, 0, lambda: press('4')),
    ('5', 2, 1, lambda: press('5')),
    ('6', 2, 2, lambda: press('6')),
    ('-', 2, 3, lambda: press('-'), operator_bg),

    ('1', 3, 0, lambda: press('1')),
    ('2', 3, 1, lambda: press('2')),
    ('3', 3, 2, lambda: press('3')),
    ('+', 3, 3, lambda: press('+'), operator_bg),

    ('0', 4, 0, lambda: press('0')),
    ('.', 4, 1, lambda: press('.')),
    ('(', 4, 2, lambda: press('(')),
    (')', 4, 3, lambda: press(')')),

    ('=', 5, 0, equal, equal_bg),
]

for btn in buttons:
    if len(btn) == 5:
        create_button(btn[0], btn[1], btn[2], btn[3], btn[4])
    else:
        create_button(btn[0], btn[1], btn[2], btn[3])

# Make "=" button wider
equal_button = tk.Button(
    button_frame,
    text="=",
    width=32,
    height=2,
    font=btn_font,
    bg=equal_bg,
    fg="white",
    bd=0,
    command=equal
)
equal_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# -----------------------------
# Run App
# -----------------------------
root.mainloop()