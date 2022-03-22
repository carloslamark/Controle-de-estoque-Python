from import_aux import *
import clients as cli
import products as prod
import money_to_receive as mtr


clients = cli.Application()
products = prod.Application()
mtR = mtr.Application()
root = Tk()

class Funcs():
    def startRoot(self):
        self.root2 = Toplevel()
        return self.root2

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.menu_screen()
        self.menu_widgets_frame_1()
        root.mainloop()

    def menu_screen(self):
        self.root.title("Menu Principal")
        self.root.configure(background= '#582f0e')
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        root.wm_state('zoomed')
        self.root.geometry("%dx%d+0+0" % (width, height))
        self.root.resizable(True, True)
        self.root.minsize(width=600, height=500)
        self.frame_1 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)
        

    def menu_widgets_frame_1(self):
        #Criação da label Nova Ótica
        self.codigo_prod = Label(self.frame_1, text="Menu Principal", bg='#a68a64', fg='#582f0e', font=('Arial', 25, BOLD))
        self.codigo_prod.place(relx=0.415, rely=0.2)

        #clientes
        self.bt_clients = Button(self.frame_1, text="Clientes", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: clients.start(self.startRoot()))
        self.bt_clients.place(relx=0.35, rely=0.40, relwidth=0.3, relheight=0.1)
        #produtos
        self.bt_prod = Button(self.frame_1, text="Produtos", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: products.start(self.startRoot()))
        self.bt_prod.place(relx=0.35, rely=0.51, relwidth=0.3, relheight=0.1)
        #contas a receber
        self.bt_to_recieve = Button(self.frame_1, text="Contas a Receber", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: mtR.start(self.startRoot()))
        self.bt_to_recieve.place(relx=0.35, rely=0.62, relwidth=0.3, relheight=0.1)
        #contas a pagar
        self.bt_to_pay = Button(self.frame_1, text="Contas a Pagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_to_pay.place(relx=0.35, rely=0.73, relwidth=0.3, relheight=0.1) 
        #sair
        self.bt_quit = Button(self.frame_1, text="Sair", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.root.destroy())
        self.bt_quit.place(relx=0.35, rely=0.84, relwidth=0.3, relheight=0.1)      


Application()