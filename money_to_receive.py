from import_aux import *

#Iniciando db
jmanagerP = json.JsonManagerProd()
jmanagerC = json.JsonManagerClient()
jmanagerPurch = json.JsonManagerPurchases()
dictProducts = []
dictClients = []
dictPurchases = []
dictProducts = jmanagerP.read_json('data/products.json')
dictClients = jmanagerC.read_json('data/clients.json')
dictPurchases = jmanagerPurch.read_json('data/purchases.json')


class Application():
    def start(self, root2):
        self.root2 = root2
        self.mtr_screen()
        self.mtr_widgets_frame_1()
        self.mtr_list_frame_2()
        root2.mainloop()
    
    def mtr_screen(self):
            self.root2.title("Contas a Receber")
            self.root2.configure(background= '#582f0e')
            self.root2.geometry('1200x700')
            self.root2.resizable(True, True)
            self.root2.minsize(width=600, height=500)
            self.frame_1 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
            self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.16)
            self.frame_2 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
            self.frame_2.place(relx=0.02 , rely=0.2, relwidth=0.96, relheight=0.76)
    
    def mtr_widgets_frame_1(self):
        #Criação da label e entrada do Código
        self.codigo_prod = Label(self.frame_1, text="Código do Produto", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.codigo_prod.place(relx=0.15, rely=0.2)
        self.codigo_prod_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.codigo_prod_entry.place(relx=0.15, rely=0.5, relwidth=0.2)

        #search
        self.bt_search = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_prod())
        self.bt_search.place(relx=0.38, rely=0.3, relwidth=0.1, relheight=0.4)
        #limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.clean_screen_prod())
        self.bt_limpar.place(relx=0.49, rely=0.3, relwidth=0.1, relheight=0.4)
        #edit
        self.bt_edit = Button(self.frame_1, text="Editar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.edit_prod(2))
        self.bt_edit.place(relx=0.63, rely=0.3, relwidth=0.1, relheight=0.4)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.cad_prod(1, ""))
        self.bt_novo.place(relx=0.74, rely=0.3, relwidth=0.1, relheight=0.4)

    def mtr_list_frame_2(self):
        self.listProd = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listProd.heading("#0", text="")
        self.listProd.heading("#1", text="Código")
        self.listProd.heading("#2", text="Produto")
        self.listProd.heading("#3", text="Quantidade")
        self.listProd.heading("#4", text="Valor SEM Desconto")
        self.listProd.heading("#5", text="Valor COM Desconto")
        
        #tamanho -> 500=100%
        self.listProd.column('#0', width=0, stretch=NO)
        self.listProd.column("#1", width=50)
        self.listProd.column("#2", width=150)
        self.listProd.column("#3", width=100)
        self.listProd.column("#4", width=100)
        self.listProd.column("#5", width=100)

        self.listProd.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.listProd.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.052, relwidth=0.03, relheight=0.896)
        self.listProd.bind("<Double-1>",self.on_duble_click) #Função DoubleClick