from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import messagebox

import mysql.connector as mysql


def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id == "" or name == "" or phone == ""):
        messagebox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="mydb")
        cursor = con.cursor()
        cursor.execute("insert into student values('" + id + "', '" + name + "', '" + phone + "')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        messagebox.showinfo("Insert Status", "All Fields are required")
        con.close()


def delete():
    pass


def update():
    pass


def get():
    pass


root = Tk()
root.geometry("600x300")
root.title("Python+Thinter+Mysql")

id = Label(root, text='Enter ID', font=('bold', 10))
id.place(x=20, y=30)

id = Label(root, text='Enter Name', font=('bold', 10))
id.place(x=20, y=60)

id = Label(root, text='Enter Phone', font=('bold', 10))
id.place(x=20, y=90)


e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text="Insert", font=("san-sarif", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("san-sarif", 10), bg="white", command=delete)
delete.place(x=80, y=140)

update = Button(root, text="Update", font=("sarif", 10), bg="white", command=update)
update.place(x=145, y=140)

get = Button(root, text="Get", font=("sarif", 10), bg="white", command=get)
get.place(x=250, y=140)

root.mainloop()

