from tkinter import *

expr = ""  # Global expression string


def press(key):
    global expr
    expr += str(key)
    display.set(expr)


def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = result  # Allow further calculations
    except (SyntaxError, ZeroDivisionError):
        display.set("Error")
        expr = ""


def clear():
    global expr
    expr = ""
    display.set("")


# Main Window
root = Tk()
root.title("Simple Calculator")
root.configure(bg="light green")
root.geometry("320x280")
root.resizable(False, False)

# Display
display = StringVar()

entry = Entry(
    root,
    textvariable=display,
    font=("Arial", 16),
    justify="right",
    bd=5
)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=8, ipady=8)

# Row 1
Button(root, text='7', width=8, height=2,
       command=lambda: press(7)).grid(row=1, column=0)
Button(root, text='8', width=8, height=2,
       command=lambda: press(8)).grid(row=1, column=1)
Button(root, text='9', width=8, height=2,
       command=lambda: press(9)).grid(row=1, column=2)
Button(root, text='/', width=8, height=2,
       command=lambda: press('/')).grid(row=1, column=3)

# Row 2
Button(root, text='4', width=8, height=2,
       command=lambda: press(4)).grid(row=2, column=0)
Button(root, text='5', width=8, height=2,
       command=lambda: press(5)).grid(row=2, column=1)
Button(root, text='6', width=8, height=2,
       command=lambda: press(6)).grid(row=2, column=2)
Button(root, text='*', width=8, height=2,
       command=lambda: press('*')).grid(row=2, column=3)

# Row 3
Button(root, text='1', width=8, height=2,
       command=lambda: press(1)).grid(row=3, column=0)
Button(root, text='2', width=8, height=2,
       command=lambda: press(2)).grid(row=3, column=1)
Button(root, text='3', width=8, height=2,
       command=lambda: press(3)).grid(row=3, column=2)
Button(root, text='-', width=8, height=2,
       command=lambda: press('-')).grid(row=3, column=3)

# Row 4
Button(root, text='0', width=8, height=2,
       command=lambda: press(0)).grid(row=4, column=0)
Button(root, text='.', width=8, height=2,
       command=lambda: press('.')).grid(row=4, column=1)
Button(root, text='=', width=8, height=2,
       command=equal).grid(row=4, column=2)
Button(root, text='+', width=8, height=2,
       command=lambda: press('+')).grid(row=4, column=3)

# Clear Button
Button(root, text='Clear', width=35, height=2,
       command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()