import tkinter as tk
from tkinter import ttk
import math

# Root window design
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Set icon
try:
    icon = tk.PhotoImage(file="icon/calculator.png")
    root.iconphoto(False, icon)
except:
    print("Icon file not found or failed to load")

# Color definitions
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

# Font definitions
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

# Style creation
style = ttk.Style(root)
root.configure(bg=LIGHT_GRAY)

# Frame creation
display_frame = tk.Frame(root, bg=LIGHT_GRAY)
button_frame = tk.Frame(root, bg=LIGHT_GRAY)
display_frame.pack(expand=True, fill="both")
button_frame.pack(expand=True, fill="both")

# Display creation
display = tk.Entry(display_frame, font=LARGE_FONT_STYLE, justify=tk.RIGHT, bg=LIGHT_GRAY, fg=LABEL_COLOR, bd=0)
display.pack(expand=True, fill="both", pady=10, padx=10)

# Global variables
last_was_operator = False
operator_buttons = []

# Functions
def clear_display():
    display.delete(0, tk.END)
    enable_operator_buttons()
    global last_was_operator
    last_was_operator = False

def add_to_display(value):
    global last_was_operator
    current = display.get()
    
    if value in ['+', '-', '*', '/']:
        if last_was_operator or not current:
            return
        last_was_operator = True
        disable_operator_buttons()
    else:
        last_was_operator = False
        enable_operator_buttons()
    
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
    global last_was_operator
    last_was_operator = False
    enable_operator_buttons()

def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def percentage():
    try:
        result = float(display.get()) / 100
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def backspace():
    current = display.get()
    if current and current[-1] in ['+', '-', '*', '/']:
        enable_operator_buttons()
    display.delete(len(current)-1, tk.END)
    global last_was_operator
    last_was_operator = False

def disable_operator_buttons():
    for button in operator_buttons:
        button.config(state=tk.DISABLED)

def enable_operator_buttons():
    for button in operator_buttons:
        button.config(state=tk.NORMAL)

# Button creation
def create_button(parent, text, command, bg_color, fg_color, is_operator=False):
    btn = tk.Button(parent, text=text, command=command, bg=bg_color, fg=fg_color, font=DIGITS_FONT_STYLE, bd=0, activebackground=bg_color)
    if is_operator:
        operator_buttons.append(btn)
    return btn

buttons = [
    ("C", LIGHT_BLUE, LABEL_COLOR, clear_display, False),
    ("√", LIGHT_BLUE, LABEL_COLOR, square_root, False),
    ("%", LIGHT_BLUE, LABEL_COLOR, percentage, False),
    ("⌫", LIGHT_BLUE, LABEL_COLOR, backspace, False),
    ("7", WHITE, LABEL_COLOR, lambda: add_to_display("7"), False),
    ("8", WHITE, LABEL_COLOR, lambda: add_to_display("8"), False),
    ("9", WHITE, LABEL_COLOR, lambda: add_to_display("9"), False),
    ("/", "#455a64", WHITE, lambda: add_to_display("/"), True),
    ("4", WHITE, LABEL_COLOR, lambda: add_to_display("4"), False),
    ("5", WHITE, LABEL_COLOR, lambda: add_to_display("5"), False),
    ("6", WHITE, LABEL_COLOR, lambda: add_to_display("6"), False),
    ("x", "#2096f3", WHITE, lambda: add_to_display("*"), True),
    ("1", WHITE, LABEL_COLOR, lambda: add_to_display("1"), False),
    ("2", WHITE, LABEL_COLOR, lambda: add_to_display("2"), False),
    ("3", WHITE, LABEL_COLOR, lambda: add_to_display("3"), False),
    ("-", "#ffc10e", WHITE, lambda: add_to_display("-"), True),
    ("0", WHITE, LABEL_COLOR, lambda: add_to_display("0"), False),
    (".", WHITE, LABEL_COLOR, lambda: add_to_display("."), False),
    ("=", LIGHT_BLUE, LABEL_COLOR, calculate, False),
    ("+", "#4daf50", WHITE, lambda: add_to_display("+"), True)
]

# Button layout
row, col = 0, 0
for (text, bg_color, fg_color, command, is_operator) in buttons:
    btn = create_button(button_frame, text, command, bg_color, fg_color, is_operator)
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make buttons expand with window size
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()