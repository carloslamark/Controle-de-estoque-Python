from tkinter import *
from tkinter.font import BOLD
from ctypes.wintypes import RGB
from tkinter import ttk
import functions as func

root = Tk()
dictProd = {}
dictClients = {}

class Funcs():
    def limpa_tela_clients(self):
        self.nome_clients_entry.delete(0, END)
        self.cpf_clients_entry.delete(0, END)
        self.telefone_clients_entry.delete(0, END)

    def limpa_tela_cadClients(self):
        self.nome_cadClients_entry.delete(0, END)
        self.cpf_cadClients_entry.delete(0, END)
        self.telefone_cadClients_entry.delete(0, END)
        self.email_cadClients_entry.delete(0, END)
        self.nomeMae_cadClients_entry.delete(0, END)
        self.obs_cadClients_entry.delete(0, END)
        

    def inicia_bd():
        dictProd = func.startProducts()
        dictClients = func.startClients()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.clients_tela()
        self.clients_widgets_frame_1()
        self.clients_lista_frame_2()
        root.mainloop()

    def clients_tela(self):
        self.root.title("Clientes")
        self.root.configure(background= '#582f0e')
        self.root.geometry('900x600') #tamanho da tela
        self.root.resizable(True, True) #Horizontal, Vertical
        self.root.minsize(width=600, height=500) #tamanho das telas
        #Frames da tela de clientes
        self.frame_1 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem
        self.frame_2 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem
    
    def clients_widgets_frame_1(self):

        #Criação da label e entrada do nome
        self.lb_nome_clients = Label(self.frame_1, text="Nome do Cliente", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_nome_clients.place(relx=0.1, rely=0.1)

        self.nome_clients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_clients_entry.place(relx=0.1, rely=0.21, relwidth=0.8)

        #Criação da label e entrada do CPF
        self.lb_cpf_clients = Label(self.frame_1, text="CPF", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_cpf_clients.place(relx=0.1, rely=0.33)

        self.cpf_clients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.cpf_clients_entry.place(relx=0.1, rely=0.44, relwidth=0.375)

        #Criação da label e entrada do telefone
        self.lb_telefone_clients = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_telefone_clients.place(relx=0.525, rely=0.33)

        self.telefone_clients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.telefone_clients_entry.place(relx=0.525, rely=0.44, relwidth=0.375)


        #limpar
        self.bt_limpar_clients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.limpa_tela_clients)
        self.bt_limpar_clients.place(relx=0.15, rely=0.7, relwidth=0.1, relheight=0.15)
        #buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_buscar.place(relx=0.275, rely=0.7, relwidth=0.1, relheight=0.15)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.cad_clientes)
        self.bt_novo.place(relx=0.55, rely=0.7, relwidth=0.1, relheight=0.15)
        #alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_alterar.place(relx=0.675, rely=0.7, relwidth=0.1, relheight=0.15)
        #apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_apagar.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.15)

    def clients_lista_frame_2(self):
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

    def cad_clientes(self):
        self.root2 = Toplevel()
        self.root2.title("Cadastro Cliente")
        self.root2.configure(background= '#582f0e')
        self.root2.geometry('900x600') #tamanho da tela
        self.root2.resizable(False, False) #Horizontal, Vertical
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

        self.frame_1 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)#Trabalha com porcentagem

        self.cad_clientes_widgets()

    def cad_clientes_widgets(self):
        #Criação da label e entrada do nome
        self.lb_nome_cadClients = Label(self.frame_1, text="Nome do Cliente", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_nome_cadClients.place(relx=0.1, rely=0.05)

        self.nome_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_cadClients_entry.place(relx=0.1, rely=0.1, relwidth=0.8)

        #Criação da label e entrada do CPF
        self.lb_cpf_cadClients = Label(self.frame_1, text="CPF", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_cpf_cadClients.place(relx=0.1, rely=0.15)

        self.cpf_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.cpf_cadClients_entry.place(relx=0.1, rely=0.2, relwidth=0.375)

        #Criação da label e entrada do telefone
        self.lb_telefone_cadClients = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_telefone_cadClients.place(relx=0.525, rely=0.15)

        self.telefone_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.telefone_cadClients_entry.place(relx=0.525, rely=0.2, relwidth=0.375)

        #Criação da label e entrada do email
        self.lb_email_cadClients = Label(self.frame_1, text="Email", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_email_cadClients.place(relx=0.1, rely=0.25)

        self.email_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.email_cadClients_entry.place(relx=0.1, rely=0.3, relwidth=0.8)

        #Criação da label e entrada do nome da mãe
        self.lb_nomeMae_cadClients = Label(self.frame_1, text="Nome da Mãe", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_nomeMae_cadClients.place(relx=0.1, rely=0.35)

        self.nomeMae_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nomeMae_cadClients_entry.place(relx=0.1, rely=0.4, relwidth=0.8)

        #Criação da label e entrada do observação
        self.lb_obs_cadClients = Label(self.frame_1, text="Observação", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_obs_cadClients.place(relx=0.1, rely=0.45)

        self.obs_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.obs_cadClients_entry.place(relx=0.1, rely=0.5, relwidth=0.8)


        #limpar
        self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.limpa_tela_cadClients)
        self.bt_limpar_cadClients.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
        #enviar
        self.bt_cadClients_enviar = Button(self.frame_1, text="Enviar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_cadClients_enviar.place(relx=0.65, rely=0.7, relwidth=0.15, relheight=0.1)


Application()