from tkinter import *;

<<<<<<< HEAD

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
=======
class Window(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
>>>>>>> f20f3aa2037b5b89a92df455e43b46ef5b4070c2
        self.master = master

        self.init_window()

    def init_window(self):
<<<<<<< HEAD
        self.master.title("Gui")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit")

        quitButton.place(x=0, y=0)


root = Tk()
root.geometry("400x400")
app = Window(root)

root.mainloop()
=======
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit")
        quitButton.place(x=0,y=0)

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
>>>>>>> f20f3aa2037b5b89a92df455e43b46ef5b4070c2
