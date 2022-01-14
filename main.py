from tkinter import *
from index import *


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Armazenamento de Dados")
        self.msg.pack()

        self.clients = Button(self.widget1)
        self.clients["text"] = "Clientes"
        self.clients["font"] = ("Calibri", "10")
        self.clients["width"] = 10
        self.clients["command"] = self.clientsButton
        self.clients.pack()

        self.prod = Button(self.widget1)
        self.prod["text"] = "Produtos"
        self.prod["font"] = ("Calibri", "10")
        self.prod["width"] = 10
        # self.prod["command"] = self.widget1.quit
        self.prod.pack()

    def clientsButton(self, master=None):
        self.widget2 = Frame(master)
        self.widget2.pack()

        self.msg = Label(self.widget1, text="Clientes")
        self.msg.pack()





    def prodButton(self, master=None):
        self.widget2 = Frame(master)
        self.widget2.pack()




root = Tk()
Application(root)
root.mainloop()



