from distutils import command
from tkinter import *
from tkinter.filedialog import Directory
from tkinter.font import BOLD
from ctypes.wintypes import RGB
from tkinter import ttk

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

import json_manager as json
import re




#Iniciando db
jmanagerC = json.JsonManagerClient()
jmanagerP = json.JsonManagerProd()
dictClients = []
dictClients = jmanagerC.read_json('data/clients.json')


root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")

    def geraRelatCliente(self, key):
        self.c = canvas.Canvas("cliente.pdf")

        self.nomeRel = key
        self.cpfRel = dictClients[key][0]
        self.telefoneRel = dictClients[key][1]
        self.emailRel = dictClients[key][2]
        self.dataNasRel = dictClients[key][3]
        self.nomeMaeRel = dictClients[key][4]
        self.enderecoRel = dictClients[key][5]
        self.obsRel = dictClients[key][6]

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")
        #________________width, height 

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50,700, "Nome: ")# pode ser self.c.drawString(50,700, "Nome: "+self.nomeRel), mas ficaria com a mesma fonte e tamanho
        self.c.drawString(50,670, "CPF: ")

        self.c.setFont("Helvetica", 16)
        self.c.drawString(150, 700, self.nomeRel)
        self.c.drawString(150, 670, self.cpfRel)

        #Criar molduras na tela
        self.c.rect(20, 550, 550, 20, fill=False, stroke=True)
        #__________início esquerda, início cima, width, height, preencher, borda



        self.c.showPage()
        self.c.save()
        self.printCliente()



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
        self.dataNas_cadClients_entry.delete(0, END)
        self.nomeMae_cadClients_entry.delete(0, END)
        self.endereco_cadClients_entry.delete(0, END)
        self.obs_cadClients_entry.delete(0, END)
 
    def variaveisCliente(self):
        cAux = ["", "", "", "", "", "", ""]
        name = self.nome_cadClients_entry.get()
        cAux[0] = self.cpf_cadClients_entry.get()
        cAux[1] = self.telefone_cadClients_entry.get()
        cAux[2] = self.email_cadClients_entry.get()
        cAux[3] = self.dataNas_cadClients_entry.get()
        cAux[4] = self.nomeMae_cadClients_entry.get()
        cAux[5] = self.endereco_cadClients_entry.get()
        cAux[6] = self.obs_cadClients_entry.get()
        return cAux, name
 
    def addClient(self):
        # cpf, telefone, email, dataNascimento, nomeDaMãe,  endereço,  obs
        cAux = []
        cAux, name = self.variaveisCliente()
        dictClients[name] = cAux

        jmanagerC.create_json('data/clients.json', dictClients)
        self.select_lista_clients()
        self.limpa_tela_cadClients()       

    def select_lista_clients(self):
        self.listaCli.delete(*self.listaCli.get_children())
        
        lista = []
        for i in dictClients:
            lista.append(i)
            lista.append(dictClients[i][0])
            lista.append(dictClients[i][1])
            self.listaCli.insert("", END, values=lista)
            lista=[] 

    def onDubleClick(self, event):
        self.limpa_tela_clients()
        self.listaCli.selection()
        col1=""
        for i in self.listaCli.selection():
            col1, col2, col3 = self.listaCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do cliente
        self.exibir_cliente(col1) 

    def editarCliente(self, flag):
        self.limpa_tela_clients()
        self.listaCli.selection()
        col1=""
        for i in self.listaCli.selection():
            col1, col2, col3 = self.listaCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do cliente
        if col1 != "":
            aux=col1
            self.cad_clientes(flag, aux)
            self.nome_cadClients_entry.insert(END, col1)
            self.cpf_cadClients_entry.insert(END, dictClients[col1][0])
            self.telefone_cadClients_entry.insert(END, dictClients[col1][1])
            self.email_cadClients_entry.insert(END, dictClients[col1][2])
            self.dataNas_cadClients_entry.insert(END, dictClients[col1][3])
            self.nomeMae_cadClients_entry.insert(END, dictClients[col1][4])
            self.endereco_cadClients_entry.insert(END, dictClients[col1][5])
            self.obs_cadClients_entry.insert(END, dictClients[col1][6])  

    def deleta_cliente(self):
        cAux = []
        cAux, name = self.variaveisCliente()
        del dictClients[name]

        jmanagerC.create_json('data/clients.json', dictClients)
        self.limpa_tela_cadClients()
        self.select_lista_clients()

    def alterar_cliente(self, name):
        if self.nome_cadClients_entry.get() in dictClients:
            self.addClient()
        else:
            del dictClients[name]
            self.addClient()
        
    def busca_cliente(self):
        nome = self.nome_clients_entry.get()
        cpf = self.cpf_clients_entry.get()
        telefone = self.telefone_clients_entry.get()
        lista=[]
        if nome!="":
            self.listaCli.delete(*self.listaCli.get_children())
            for i in dictClients:
                if re.match(nome, i, re.IGNORECASE):
                    lista.append(i)
                    lista.append(dictClients[i][0])
                    lista.append(dictClients[i][1])
                    self.listaCli.insert("", END, values=lista)
                    lista=[] 

        elif cpf!="":
            self.listaCli.delete(*self.listaCli.get_children())
            for i in dictClients:
                if re.search(cpf, dictClients[i][0], re.IGNORECASE):
                    lista.append(i)
                    lista.append(dictClients[i][0])
                    lista.append(dictClients[i][1])
                    self.listaCli.insert("", END, values=lista)
                    lista=[]  

        elif telefone!="":
            self.listaCli.delete(*self.listaCli.get_children())
            for i in dictClients:
                if re.search(telefone, dictClients[i][1], re.IGNORECASE):
                    lista.append(i)
                    lista.append(dictClients[i][0])
                    lista.append(dictClients[i][1])
                    self.listaCli.insert("", END, values=lista)
                    lista=[] 
        else:
            self.select_lista_clients()

        self.limpa_tela_clients


    

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.clients_tela()
        self.clients_widgets_frame_1()
        self.clients_lista_frame_2()
        self.select_lista_clients()
        root.mainloop()
  
    def clients_tela(self):
        self.root.title("Clientes")
        self.root.configure(background= '#582f0e')
        self.root.geometry('1200x700') #tamanho da tela
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
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.busca_cliente())
        self.bt_buscar.place(relx=0.275, rely=0.7, relwidth=0.1, relheight=0.15)
        #editar
        self.bt_novo = Button(self.frame_1, text="Editar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.editarCliente(2))
        self.bt_novo.place(relx=0.625, rely=0.7, relwidth=0.1, relheight=0.15)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.cad_clientes(1, ""))
        self.bt_novo.place(relx=0.75, rely=0.7, relwidth=0.1, relheight=0.15)
        
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
        self.listaCli.bind("<Double-1>",self.onDubleClick) #Função DoubleClick  
   
    def cad_clientes(self, flag, aux):
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

        self.cad_clientes_widgets(flag, aux)
   
    def cad_clientes_widgets(self, flag, aux):
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
        self.email_cadClients_entry.place(relx=0.1, rely=0.3, relwidth=0.375)

        #Criação da label e entrada da data de nascimento
        self.lb_dataNas_cadClients = Label(self.frame_1, text="Data de Nascimento(00/00/0000)", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_dataNas_cadClients.place(relx=0.525, rely=0.25)

        self.dataNas_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.dataNas_cadClients_entry.place(relx=0.525, rely=0.3, relwidth=0.375)

        #Criação da label e entrada do nome da mãe
        self.lb_nomeMae_cadClients = Label(self.frame_1, text="Nome da Mãe", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_nomeMae_cadClients.place(relx=0.1, rely=0.35)

        self.nomeMae_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nomeMae_cadClients_entry.place(relx=0.1, rely=0.4, relwidth=0.8)

        #Criação da label e entrada do endereco
        self.lb_endereco_cadClients = Label(self.frame_1, text="Endereço", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_endereco_cadClients.place(relx=0.1, rely=0.45)

        self.endereco_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.endereco_cadClients_entry.place(relx=0.1, rely=0.5, relwidth=0.8)

        #Criação da label e entrada do observação
        self.lb_obs_cadClients = Label(self.frame_1, text="Observação", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.lb_obs_cadClients.place(relx=0.1, rely=0.55)

        self.obs_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.obs_cadClients_entry.place(relx=0.1, rely=0.6, relwidth=0.8)

        if flag==1:
            #limpar
            self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.limpa_tela_cadClients)
            self.bt_limpar_cadClients.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
            #enviar
            self.bt_cadClients_enviar = Button(self.frame_1, text="Enviar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.addClient(), self.root2.destroy()])
            self.bt_cadClients_enviar.place(relx=0.7, rely=0.7, relwidth=0.15, relheight=0.1)
        elif flag==2:
            #limpar
            self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.limpa_tela_cadClients)
            self.bt_limpar_cadClients.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
            #alterar
            self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.alterar_cliente(aux), self.root2.destroy()])
            self.bt_alterar.place(relx=0.425, rely=0.7, relwidth=0.15, relheight=0.1)
            #apagar
            self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.deleta_cliente(), self.root2.destroy()])
            self.bt_apagar.place(relx=0.7, rely=0.7, relwidth=0.15, relheight=0.1)
   
    def exibir_cliente(self, key):
        self.root3 = Toplevel()
        self.root3.title("Informações do Cliente")
        self.root3.configure(background= '#582f0e')
        self.root3.geometry('900x600') #tamanho da tela
        self.root3.resizable(False, False) #Horizontal, Vertical
        self.root3.transient(self.root)
        self.root3.focus_force()
        self.root3.grab_set()
        

        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)#Trabalha com porcentagem

        self.exibir_cliente_widgets(key)     

    def exibir_cliente_widgets(self, key):
        #Nome
        self.exibir_nome = Label(self.frame_1, text="Nome: "+key, bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_nome.place(relx=0.1, rely=0.1)
        #cpf
        self.exibir_cpf = Label(self.frame_1, text="CPF: "+dictClients[key][0], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_cpf.place(relx=0.1, rely=0.2)
        #Telefone
        self.exibir_telefone = Label(self.frame_1, text="Telefone: "+dictClients[key][1], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_telefone.place(relx=0.5, rely=0.2)
        #email
        self.exibir_email = Label(self.frame_1, text="Email: "+dictClients[key][2], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_email.place(relx=0.1, rely=0.3)
        #Data de nascimento
        self.exibir_dataNas = Label(self.frame_1, text="Data de Nascimento: "+dictClients[key][3], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_dataNas.place(relx=0.5, rely=0.3)
        #Nome da mãe
        self.exibir_nomeMae = Label(self.frame_1, text="Nome da Mãe: "+dictClients[key][4], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_nomeMae.place(relx=0.1, rely=0.4)
        #Endereço
        self.exibir_endereco = Label(self.frame_1, text="Endereço: "+dictClients[key][5], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.exibir_endereco.place(relx=0.1, rely=0.5)
        #Observações
        self.exibir_obs = Label(self.frame_1, text="Observações: "+dictClients[key][6], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD), wraplength=691.2, justify=LEFT)
        self.exibir_obs.place(relx=0.1, rely=0.6)

        self.Menus(key)

    def Menus(self, key):
        menubar = Menu(self.root3)
        self.root3.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): 
            self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatórios", menu=filemenu2)

        filemenu.add_command(label="Limpa Busca", command=self.limpa_tela_clients)
        filemenu.add_command(label="Sair", command=Quit)

        filemenu2.add_command(label="Ficha do Cliente", command=lambda: self.geraRelatCliente(key))









Application()