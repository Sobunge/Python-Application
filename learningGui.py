import tkinter
from tkinter import *

#def quit():
  #  print('Exiting the system.......')
 #   import sys; sys.exit()

#def login():
  #  print('Checking credentials ....... \n')

 #   username = usernameEntry.get()
#    password = passwordEntry.get()

    #if username == 'sobunge' and password == 'merium@kema':
   #     print('Login successful')
  #  else:
 #       print('Login failed')

#top = tkinter.Tk()
#usernameLabel = Label(top,text='Username')
#usernameEntry = Entry(top)

#passwordLabel = Label(top,text='Password')
#passwordEntry = Entry(top,show='*')

#button1 = Button(top,text = 'Login', command = login)
#button2 = Button(top,text = 'Register')
#button = Button(top,text ='Quit',command = quit)

#usernameLabel.pack()
#usernameEntry.pack()

#passwordLabel.pack()
#passwordEntry.pack()

#button2.pack(side = 'left',padx='10',pady='10')
#button.pack(side='left')
#button1.pack(side='left',padx='10',pady='10')

#top.mainloop()

def profil():
    print('Users profil')

def unitRegistration():
    print('Register Units')

def semesterResults():
    print('Semester Results')

def logout():
    print('Loging out.....')

def exit():
    print('Exiting system.........')
    import sys;sys.exit()

top = tkinter.Tk()
top.title("Users Dashboard")

widget = Label(top,text='Users Dashboard',padx=5,pady=5)
widget.pack(side=TOP)

f = Frame(relief=RIDGE,borderwidth=5)
widget1 = Label(f,text='User Name').pack()
widget2 = Label(f,text='Users Role').pack()
widget3 = Button(f,text='Profile',command=profil).pack(padx=10,pady=10)
widget4 = Button(f,text='Unit Registration',command=unitRegistration).pack()
widget5 = Button(f,text='Semester Results',command=semesterResults).pack(padx=10,pady=10)
widget6 = Button(f,text='Logout',command=logout).pack()
widget7 = Button(f,text='Exit',command=exit).pack(padx=10,pady=10)

f.pack(side=LEFT)

top.mainloop()
