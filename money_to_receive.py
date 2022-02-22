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


class Funcs():
    def clean_screen(self):
        self.nome_mtr_entry.delete(0, END)
        self.nomeMae_mtr_entry.delete(0, END)
        self.cpf_mtr_entry.delete(0, END)
        self.telefone_mtr_entry.delete(0, END)

    def select_list_mtr(self):
        self.listMtr.delete(*self.listMtr.get_children())
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        list = []
        for i in dictClients:
            list.append(i)
            list.append(dictClients[i][4])
            list.append(dictClients[i][0])
            list.append(dictClients[i][1])
            list.append(0)
            list.append(0)
            list.append(dictClients[i][7])
            for j in dictPurchases[i]:
                if dictPurchases[i][j][4] == "n":
                    list[4] = dictPurchases[i][j][1]
                    list[5] = dictPurchases[i][j][5]
                    self.listMtr.insert("", END, values=list)
            list=[]
            



class Application(Funcs):
    def start(self, root2):
        self.root2 = root2
        self.mtr_screen()
        self.mtr_widgets_frame_1()
        self.mtr_list_frame_2()
        self.select_list_mtr()
        root2.mainloop()
    
    def mtr_screen(self):
        self.root2.title("Contas a Receber")
        self.root2.configure(background= '#582f0e')
        self.root2.geometry('1200x700')
        self.root2.resizable(True, True)
        self.root2.minsize(width=600, height=500)
        self.frame_1 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.36)
        self.frame_2 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.4, relwidth=0.96, relheight=0.56)
    
    def mtr_widgets_frame_1(self):
        #Criação da label e entrada do nome do cliente
        self.nome_mtr = Label(self.frame_1, text="Nome", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.nome_mtr.place(relx=0.15, rely=0.15)
        self.nome_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nome_mtr_entry.place(relx=0.15, rely=0.3, relwidth=0.3)
        #Criação da label e entrada do cpf
        self.cpf_mtr = Label(self.frame_1, text="CPF", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.cpf_mtr.place(relx=0.55, rely=0.15)
        self.cpf_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.cpf_mtr_entry.place(relx=0.55, rely=0.3, relwidth=0.3)
        #Criação da label e entrada do nome do cliente
        self.nomeMae_mtr = Label(self.frame_1, text="Nome da Mãe", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.nomeMae_mtr.place(relx=0.15, rely=0.4)
        self.nomeMae_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nomeMae_mtr_entry.place(relx=0.15, rely=0.55, relwidth=0.3)
        #Criação da label e entrada do telefone
        self.telefone_mtr = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.telefone_mtr.place(relx=0.55, rely=0.4)
        self.telefone_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.telefone_mtr_entry.place(relx=0.55, rely=0.55, relwidth=0.3)
        

        #search
        self.bt_search = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_prod())
        self.bt_search.place(relx=0.2, rely=0.75, relwidth=0.1, relheight=0.2)
        #limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.clean_screen())
        self.bt_limpar.place(relx=0.45, rely=0.75, relwidth=0.1, relheight=0.2)
        #edit
        self.bt_edit = Button(self.frame_1, text="Alterar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.edit_prod(2))
        self.bt_edit.place(relx=0.7, rely=0.75, relwidth=0.1, relheight=0.2)
        

    def mtr_list_frame_2(self):
        self.listMtr = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listMtr.heading("#0", text="")
        self.listMtr.heading("#1", text="Nome")
        self.listMtr.heading("#2", text="Nome da Mãe")
        self.listMtr.heading("#3", text="CPF")
        self.listMtr.heading("#4", text="Telefone")
        self.listMtr.heading("#5", text="Data da Compra")
        self.listMtr.heading("#6", text="Parcelas")
        self.listMtr.heading("#7", text="Total")
        
        #tamanho -> 500=100%
        self.listMtr.column('#0', width=0, stretch=NO)
        self.listMtr.column("#1", width=125)
        self.listMtr.column("#2", width=125)
        self.listMtr.column("#3", width=75)
        self.listMtr.column("#4", width=75)
        self.listMtr.column("#5", width=35)
        self.listMtr.column("#6", width=30)
        self.listMtr.column("#7", width=35)

        self.listMtr.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.listMtr.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.052, relwidth=0.03, relheight=0.896)
        # self.listMtr.bind("<Double-1>",self.on_duble_click) #Função DoubleClick