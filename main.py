from tkinter import *
from tkinter.font import BOLD
from ctypes.wintypes import RGB
from tkinter import ttk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#582f0e')
        self.root.geometry('900x600') #tamanho da tela
        self.root.resizable(True, True) #Horizontal, Vertical
        # self.root.maxsize(width=800, height=700)
        self.root.minsize(width=600, height=500) #tamanho das telas
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem

        self.frame_2 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem
    
    def widgets_frame_1(self):

        #Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome do Cliente", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_nome.place(relx=0.1, rely=0.1)

        self.nome_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_entry.place(relx=0.1, rely=0.21, relwidth=0.8)

        #Criação da label e entrada do CPF
        self.lb_codigo = Label(self.frame_1, text="CPF", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_codigo.place(relx=0.1, rely=0.33)

        self.codigo_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.codigo_entry.place(relx=0.1, rely=0.44, relwidth=0.375)

        #Criação da label e entrada do telefone
        self.lb_nome = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_nome.place(relx=0.525, rely=0.33)

        self.nome_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_entry.place(relx=0.525, rely=0.44, relwidth=0.375)


        #limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_limpar.place(relx=0.15, rely=0.7, relwidth=0.1, relheight=0.15)
        #buscar
        self.bt_limpar = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_limpar.place(relx=0.275, rely=0.7, relwidth=0.1, relheight=0.15)
        #novo
        self.bt_limpar = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_limpar.place(relx=0.55, rely=0.7, relwidth=0.1, relheight=0.15)
        #alterar
        self.bt_limpar = Button(self.frame_1, text="Alterar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_limpar.place(relx=0.675, rely=0.7, relwidth=0.1, relheight=0.15)
        #apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_limpar.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.15)

    def lista_frame_2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="NomeCliente")
        self.listaCli.heading("#2", text="CPF")
        self.listaCli.heading("#3", text="Telefone")

        #tamanho -> 500=100%
        self.listaCli.column('#0', width=0, stretch=NO)
        self.listaCli.column("#1", width=300)
        self.listaCli.column("#2", width=100)
        self.listaCli.column("#3", width=100)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.102, relwidth=0.03, relheight=0.846)






Application()