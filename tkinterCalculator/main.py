import tkinter
from tkinter import *

root = Tk()
root.title("My Tkinter Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text="", font=("arial", 30), justify="right")
label_result.pack()

Button(root, command=lambda: clear(), text="C", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#3697f5").place(x=10, y=100)
Button(root, command=lambda: show("/"), text="/", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=100)
Button(root, command=lambda: show("%"), text="%", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=100)
Button(root, command=lambda: show("*"), text="*", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=100)


Button(root, command=lambda: show("7"), text="7", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=200)
Button(root, command=lambda: show("8"), text="8", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=200)
Button(root, command=lambda: show("9"), text="9", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=200)
Button(root, command=lambda: show("-"), text="-", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=200)


Button(root, command=lambda: show("4"), text="4", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=300)
Button(root, command=lambda: show("5"), text="5", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=300)
Button(root, command=lambda: show("6"), text="6", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=300)
Button(root, command=lambda: show("+"), text="+", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=300)


Button(root, command=lambda: show("1"), text="1", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=400)
Button(root, command=lambda: show("2"), text="2", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=400)
Button(root, command=lambda: show("3"), text="3", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=400)
Button(root, command=lambda: show("0"), text="0", width=11, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=500)


Button(root, command=lambda: show("."), text=".", width=5, height=1, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=500)
Button(root, command=lambda: calculate(), text="=", width=5, height=3, font=("arial", 30, "bold"), justify="center", bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=400)


root.mainloop()