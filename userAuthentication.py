import tkinter
from tkinter import *
from tkinter import messagebox

def leave():
    print('Successful Exiting the system..........')
    import sys;sys.exit()

def signup():
    messagebox.showinfo('Signing Up','Signig Up succesful')

def login():

    username = 'samuel'
    password = 'samuel'

    uname = usernameEntry.get()
    pword = passwordEntry.get()

    if uname == username and pword == password:
        messagebox.showinfo('Login','Login successful........')
    else:
        messagebox.showinfo('Login','Login failed.........')

def register():

    root = tkinter.Tk()

    name = Label(root,text='Name').pack()
    nameEntry = Entry(root)
    nameEntry.pack()
    username = Label(root,text='Username').pack()
    usernameEntry = Entry(root)
    usernameEntry.pack()
    password = Label(root,text='Password').pack()
    password = Entry(root)
    password.pack()
    date = Label(root,text='entryDate').pack()
    date = Entry(root)
    date.pack()
    role = Label(root,text='Role').pack()
    roleEntry = Entry(root)
    roleEntry.pack()
    gender = Label(root,text='Gender').pack()
    genderEntry = Entry(root)
    genderEntry.pack()
    age = Label(root,text='Age').pack()
    age = Entry(root)
    age.pack()
    address = Label(root,text='Address').pack()
    address = Entry(root)
    address.pack()

    register = Button(root,text='Register',width=7).pack(side=LEFT)
    exit = Button(root,text='Exit',width=7,command=leave)
    exit.pack()

    root.mainloop()

top = tkinter.Tk()

username = Label(top,text='Username').pack()
usernameEntry = Entry(top)
usernameEntry.pack()
password = Label(top,text='Password').pack()
passwordEntry = Entry(top)
passwordEntry.pack()

login = Button(top,text='Signin',command=login).pack(side=LEFT,padx=10,pady=10)
register = Button(top,text='Register',command=register).pack(side=LEFT)
exit = Button(top,text='Exit',command=exit).pack(side=LEFT,padx=10,pady=10)

top.mainloop()