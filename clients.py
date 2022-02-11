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
dictProducts = []
dictProducts = jmanagerP.read_json('data/products.json')

root = Tk()


class Relatorios():
    def printClient(self):
        webbrowser.open("client.pdf")

    def geraRelatClient(self, key):
        self.c = canvas.Canvas("client.pdf")

        self.nomeRel = key
        self.cpfRel = dictClients[key][0]
        self.telefoneRel = dictClients[key][1]
        self.emailRel = dictClients[key][2]
        self.dataNasRel = dictClients[key][3]
        self.nomeMaeRel = dictClients[key][4]
        self.enderecoRel = dictClients[key][5]
        self.obsRel = dictClients[key][6]

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Client")
        #________________width, height 

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50,700, "Nome: ")# pode ser self.c.drawString(50,700, "Nome: "+self.nomeRel), mas ficaria com a mesma fonte e tamanho
        self.c.drawString(50,670, "CPF: ")

        self.c.setFont("Helvetica", 16)
        self.c.drawString(150, 700, self.nomeRel)
        self.c.drawString(150, 670, self.cpfRel)

        #Criar molduras na screen
        self.c.rect(20, 550, 550, 20, fill=False, stroke=True)
        #__________início esquerda, início cima, width, height, preencher, borda



        self.c.showPage()
        self.c.save()
        self.printClient()


class Funcs():
    def clean_screen_clients(self):
        self.nome_clients_entry.delete(0, END)
        self.cpf_clients_entry.delete(0, END)
        self.telefone_clients_entry.delete(0, END)
 
    def clean_screen_cadClients(self):
        self.nome_cadClients_entry.delete(0, END)
        self.cpf_cadClients_entry.delete(0, END)
        self.telefone_cadClients_entry.delete(0, END)
        self.email_cadClients_entry.delete(0, END)
        self.dataNas_cadClients_entry.delete(0, END)
        self.nomeMae_cadClients_entry.delete(0, END)
        self.endereco_cadClients_entry.delete(0, END)
        self.obs_cadClients_entry.delete(0, END)
 
    def variables_client(self):
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
 
    def add_client(self):
        cAux = []
        cAux, name = self.variables_client()
        dictClients[name] = cAux

        jmanagerC.create_json('data/clients.json', dictClients)
        self.select_list_clients()
        self.clean_screen_cadClients()       

    def select_list_clients(self):
        self.listCli.delete(*self.listCli.get_children())
        
        list = []
        for i in dictClients:
            list.append(i)
            list.append(dictClients[i][0])
            list.append(dictClients[i][1])
            self.listCli.insert("", END, values=list)
            list=[] 

    def on_duble_click(self, event):
        self.clean_screen_clients()
        self.listCli.selection()
        col1=""
        for i in self.listCli.selection():
            col1, col2, col3 = self.listCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do client
        self.show_client(col1) 

    def edit_client(self, flag):
        self.clean_screen_clients()
        self.listCli.selection()
        col1=""
        for i in self.listCli.selection():
            col1, col2, col3 = self.listCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do client
        if col1 != "":
            aux=col1
            self.cad_clients(flag, aux)
            self.nome_cadClients_entry.insert(END, col1)
            self.cpf_cadClients_entry.insert(END, dictClients[col1][0])
            self.telefone_cadClients_entry.insert(END, dictClients[col1][1])
            self.email_cadClients_entry.insert(END, dictClients[col1][2])
            self.dataNas_cadClients_entry.insert(END, dictClients[col1][3])
            self.nomeMae_cadClients_entry.insert(END, dictClients[col1][4])
            self.endereco_cadClients_entry.insert(END, dictClients[col1][5])
            self.obs_cadClients_entry.insert(END, dictClients[col1][6])  

    def delete_client(self):
        cAux = []
        cAux, name = self.variables_client()
        del dictClients[name]

        jmanagerC.create_json('data/clients.json', dictClients)
        self.clean_screen_cadClients()
        self.select_list_clients()

    def change_client(self, name):
        if self.nome_cadClients_entry.get() in dictClients:
            self.add_client()
        else:
            del dictClients[name]
            self.add_client()
        
    def search_client(self):
        nome = self.nome_clients_entry.get()
        cpf = self.cpf_clients_entry.get()
        telefone = self.telefone_clients_entry.get()
        list=[]
        if nome!="":
            self.listCli.delete(*self.listCli.get_children())
            for i in dictClients:
                if re.match(nome, i, re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    self.listCli.insert("", END, values=list)
                    list=[] 

        elif cpf!="":
            self.listCli.delete(*self.listCli.get_children())
            for i in dictClients:
                if re.search(cpf, dictClients[i][0], re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    self.listCli.insert("", END, values=list)
                    list=[]  

        elif telefone!="":
            self.listCli.delete(*self.listCli.get_children())
            for i in dictClients:
                if re.search(telefone, dictClients[i][1], re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    self.listCli.insert("", END, values=list)
                    list=[] 
        else:
            self.select_list_clients()

        self.clean_screen_clients


    

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.clients_screen()
        self.clients_widgets_frame_1()
        self.clients_list_frame_2()
        self.select_list_clients()
        root.mainloop()
  
    def clients_screen(self):
        self.root.title("Clients")
        self.root.configure(background= '#582f0e')
        self.root.geometry('1200x700') #tamanho da screen
        self.root.resizable(True, True) #Horizontal, Vertical
        self.root.minsize(width=600, height=500) #tamanho das screens
        #Frames da screen de clients
        self.frame_1 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem
        self.frame_2 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem   
  
    def clients_widgets_frame_1(self):
        #Criação da label e entrada do nome
        self.nome_clients = Label(self.frame_1, text="Nome do Client", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.nome_clients.place(relx=0.1, rely=0.1)
        self.nome_clients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_clients_entry.place(relx=0.1, rely=0.21, relwidth=0.8)
        #Criação da label e entrada do CPF
        self.cpf_clients = Label(self.frame_1, text="CPF", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.cpf_clients.place(relx=0.1, rely=0.33)
        self.cpf_clients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.cpf_clients_entry.place(relx=0.1, rely=0.44, relwidth=0.375)
        #Criação da label e entrada do telefone
        self.telefone_clients = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.telefone_clients.place(relx=0.525, rely=0.33)
        self.telefone_clients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.telefone_clients_entry.place(relx=0.525, rely=0.44, relwidth=0.375)

        #limpar
        self.bt_limpar_clients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clean_screen_clients)
        self.bt_limpar_clients.place(relx=0.15, rely=0.7, relwidth=0.1, relheight=0.15)
        #searchr
        self.bt_searchr = Button(self.frame_1, text="searchr", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_client())
        self.bt_searchr.place(relx=0.275, rely=0.7, relwidth=0.1, relheight=0.15)
        #edit
        self.bt_edit = Button(self.frame_1, text="edit", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.edit_client(2))
        self.bt_edit.place(relx=0.625, rely=0.7, relwidth=0.1, relheight=0.15)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.cad_clients(1, ""))
        self.bt_novo.place(relx=0.75, rely=0.7, relwidth=0.1, relheight=0.15)
        
    def clients_list_frame_2(self):
        self.listCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3"))
        self.listCli.heading("#0", text="")
        self.listCli.heading("#1", text="NomeClient")
        self.listCli.heading("#2", text="CPF")
        self.listCli.heading("#3", text="Telefone")
        
        #tamanho -> 500=100%
        self.listCli.column('#0', width=0, stretch=NO)
        self.listCli.column("#1", width=300)
        self.listCli.column("#2", width=100)
        self.listCli.column("#3", width=100)

        self.listCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroollist = Scrollbar(self.frame_2, orient='vertical')
        self.listCli.configure(yscroll=self.scroollist.set)
        self.scroollist.place(relx=0.96, rely=0.102, relwidth=0.03, relheight=0.846)
        self.listCli.bind("<Double-1>",self.on_duble_click) #Função DoubleClick  
   
    def cad_clients(self, flag, aux):
        self.root2 = Toplevel()
        self.root2.title("Cadastro Client")
        self.root2.configure(background= '#582f0e')
        self.root2.geometry('900x600') #tamanho da screen
        self.root2.resizable(False, False) #Horizontal, Vertical
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

        self.frame_1 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)#Trabalha com porcentagem

        self.cad_clients_widgets(flag, aux)
   
    def cad_clients_widgets(self, flag, aux):
        #Criação da label e entrada do nome
        self.nome_cadClients = Label(self.frame_1, text="Nome do Client", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.nome_cadClients.place(relx=0.1, rely=0.05)
        self.nome_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_cadClients_entry.place(relx=0.1, rely=0.1, relwidth=0.8)
        #Criação da label e entrada do CPF
        self.cpf_cadClients = Label(self.frame_1, text="CPF", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.cpf_cadClients.place(relx=0.1, rely=0.15)
        self.cpf_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.cpf_cadClients_entry.place(relx=0.1, rely=0.2, relwidth=0.375)
        #Criação da label e entrada do telefone
        self.telefone_cadClients = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.telefone_cadClients.place(relx=0.525, rely=0.15)
        self.telefone_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.telefone_cadClients_entry.place(relx=0.525, rely=0.2, relwidth=0.375)
        #Criação da label e entrada do email
        self.email_cadClients = Label(self.frame_1, text="Email", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.email_cadClients.place(relx=0.1, rely=0.25)
        self.email_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.email_cadClients_entry.place(relx=0.1, rely=0.3, relwidth=0.375)
        #Criação da label e entrada da data de nascimento
        self.dataNas_cadClients = Label(self.frame_1, text="Data de Nascimento(00/00/0000)", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.dataNas_cadClients.place(relx=0.525, rely=0.25)
        self.dataNas_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.dataNas_cadClients_entry.place(relx=0.525, rely=0.3, relwidth=0.375)
        #Criação da label e entrada do nome da mãe
        self.nomeMae_cadClients = Label(self.frame_1, text="Nome da Mãe", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.nomeMae_cadClients.place(relx=0.1, rely=0.35)
        self.nomeMae_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nomeMae_cadClients_entry.place(relx=0.1, rely=0.4, relwidth=0.8)
        #Criação da label e entrada do endereco
        self.endereco_cadClients = Label(self.frame_1, text="Endereço", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.endereco_cadClients.place(relx=0.1, rely=0.45)
        self.endereco_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.endereco_cadClients_entry.place(relx=0.1, rely=0.5, relwidth=0.8)
        #Criação da label e entrada do observação
        self.obs_cadClients = Label(self.frame_1, text="Observação", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.obs_cadClients.place(relx=0.1, rely=0.55)
        self.obs_cadClients_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.obs_cadClients_entry.place(relx=0.1, rely=0.6, relwidth=0.8)

        if flag==1:
            #limpar
            self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clean_screen_cadClients)
            self.bt_limpar_cadClients.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
            #enviar
            self.bt_cadClients_enviar = Button(self.frame_1, text="Enviar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.add_client(), self.root2.destroy()])
            self.bt_cadClients_enviar.place(relx=0.7, rely=0.7, relwidth=0.15, relheight=0.1)
        elif flag==2:
            #limpar
            self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clean_screen_cadClients)
            self.bt_limpar_cadClients.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
            #change
            self.bt_change = Button(self.frame_1, text="change", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.change_client(aux), self.root2.destroy()])
            self.bt_change.place(relx=0.425, rely=0.7, relwidth=0.15, relheight=0.1)
            #apagar
            self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.delete_client(), self.root2.destroy()])
            self.bt_apagar.place(relx=0.7, rely=0.7, relwidth=0.15, relheight=0.1)
   
    def show_client(self, key):
        self.root3 = Toplevel()
        self.root3.title("Informações do Client")
        self.root3.configure(background= '#582f0e')
        self.root3.geometry('900x600') #tamanho da screen
        self.root3.resizable(False, False) #Horizontal, Vertical
        self.root3.transient(self.root)
        self.root3.focus_force()
        self.root3.grab_set()
        

        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)#Trabalha com porcentagem

        self.show_client_widgets(key)     

    def show_client_widgets(self, key):
        #Nome
        self.show_nome = Label(self.frame_1, text="Nome: "+key, bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_nome.place(relx=0.1, rely=0.1)
        #cpf
        self.show_cpf = Label(self.frame_1, text="CPF: "+dictClients[key][0], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_cpf.place(relx=0.1, rely=0.2)
        #Telefone
        self.show_telefone = Label(self.frame_1, text="Telefone: "+dictClients[key][1], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_telefone.place(relx=0.5, rely=0.2)
        #email
        self.show_email = Label(self.frame_1, text="Email: "+dictClients[key][2], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_email.place(relx=0.1, rely=0.3)
        #Data de nascimento
        self.show_dataNas = Label(self.frame_1, text="Data de Nascimento: "+dictClients[key][3], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_dataNas.place(relx=0.5, rely=0.3)
        #Nome da mãe
        self.show_nomeMae = Label(self.frame_1, text="Nome da Mãe: "+dictClients[key][4], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_nomeMae.place(relx=0.1, rely=0.4)
        #Endereço
        self.show_endereco = Label(self.frame_1, text="Endereço: "+dictClients[key][5], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_endereco.place(relx=0.1, rely=0.5)
        #Observações
        self.show_obs = Label(self.frame_1, text="Observações: "+dictClients[key][6], bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD), wraplength=691.2, justify=LEFT)
        self.show_obs.place(relx=0.1, rely=0.6)

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

        filemenu.add_command(label="Limpa search", command=self.clean_screen_clients)
        filemenu.add_command(label="Sair", command=Quit)

        filemenu2.add_command(label="Ficha do Client", command=lambda: self.geraRelatClient(key))


Application()