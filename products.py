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
jmanagerP = json.JsonManagerProd()
dictProducts = []
dictProducts = jmanagerP.read_json('data/products.json')

root = Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.prod_tela()
        self.prod_widgets_frame_1()
        self.prod_lista_frame_2()
        root.mainloop()

    def prod_tela(self):
            self.root.title("Estoque")
            self.root.configure(background= '#582f0e')
            self.root.geometry('1200x700')
            self.root.resizable(True, True)
            self.root.minsize(width=600, height=500)
            self.frame_1 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
            self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.16)
            self.frame_2 = Frame(self.root, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
            self.frame_2.place(relx=0.02 , rely=0.2, relwidth=0.96, relheight=0.76)
    
    def prod_widgets_frame_1(self):
        #Criação da label e entrada do Código
        self.code_prod = Label(self.frame_1, text="Código do Produto", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.code_prod.place(relx=0.15, rely=0.2)
        self.code_prod_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.code_prod_entry.place(relx=0.15, rely=0.5, relwidth=0.2)

        #buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_buscar.place(relx=0.38, rely=0.3, relwidth=0.1, relheight=0.4)
        #limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_limpar.place(relx=0.49, rely=0.3, relwidth=0.1, relheight=0.4)
        #editar
        self.bt_novo = Button(self.frame_1, text="Editar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_novo.place(relx=0.63, rely=0.3, relwidth=0.1, relheight=0.4)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11))
        self.bt_novo.place(relx=0.74, rely=0.3, relwidth=0.1, relheight=0.4)

    def prod_lista_frame_2(self):
        self.listaProd = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listaProd.heading("#0", text="")
        self.listaProd.heading("#1", text="Código")
        self.listaProd.heading("#2", text="Produto")
        self.listaProd.heading("#3", text="Quantidade")
        self.listaProd.heading("#4", text="Valor SEM Desconto")
        self.listaProd.heading("#5", text="Valor SEM Desconto")
        
        #tamanho -> 500=100%
        self.listaProd.column('#0', width=0, stretch=NO)
        self.listaProd.column("#1", width=50)
        self.listaProd.column("#2", width=150)
        self.listaProd.column("#3", width=100)
        self.listaProd.column("#3", width=100)
        self.listaProd.column("#3", width=100)

        self.listaProd.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaProd.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.052, relwidth=0.03, relheight=0.896)
        # self.listaProd.bind("<Double-1>",self.onDubleClick) #Função DoubleClick  

    





Aplication()