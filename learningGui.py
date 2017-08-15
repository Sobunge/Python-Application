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

top = tkinter.Tk()

frame1 = Frame(top)
frame1.pack(side='left',relief='RAISED')

frame2 = Frame(top)
frame2.pack(side='left')

widget1 = Label(frame1,text='Profile')

widget2 = Label(frame2,text='Welcome to your portal')

widget1.pack()
widget2.pack()

top.mainloop()