from tkinter import *


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Armazenamento de Dados")
        self.msg.pack ()

        self.clients = Button(self.widget1)
        self.clients["text"] = "Clientes"
        self.clients["font"] = ("Calibri", "10")
        self.clients["width"] = 10
        self.clients["command"] = self.clientsButton
        self.clients.pack ()

        self.prod = Button(self.widget1)
        self.prod["text"] = "Produtos"
        self.prod["font"] = ("Calibri", "10")
        self.prod["width"] = 10
        # self.prod["command"] = self.widget1.quit
        self.prod.pack ()

    def clientsButton(self, master=None):
        self.widget1.destroy()

        self.widget2 = Frame(master)
        self.widget2.pack()


        self.cad = Button(self.widget2)
        self.cad["text"] = "Cadastrar Clientes"
        self.cad["font"] = ("Calibri", "10")
        self.cad.pack()

        self.show = Button(self.widget2)
        self.show["text"] = "Ver Clientes"
        self.show["font"] = ("Calibri", "10")
        self.show.pack()

        self.back = Button(self.widget2)
        self.back["text"] = "Voltar"
        self.back["font"] = ("Calibri", "10")
        self.back["command"] = self.widget2.destroy()
        self.back.pack()

    def prodButton(self):
        self.clients.destroy()
        self.prod.destroy()

        self.cad = Button(self.widget1)
        self.cad["text"] = "Cadastrar Produtos"
        self.cad["font"] = ("Calibri", "10")
        self.cad.pack()

        self.show = Button(self.widget1)
        self.show["text"] = "Ver Estoque"
        self.show["font"] = ("Calibri", "10")




root = Tk()
Application(root)
root.mainloop()



