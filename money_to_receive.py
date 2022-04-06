from ast import Break
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
    def clear_screen(self):
        self.nome_mtr_entry.delete(0, END)
        self.nomeMae_mtr_entry.delete(0, END)
        self.cpf_mtr_entry.delete(0, END)
        self.telefone_mtr_entry.delete(0, END)

    def select_list_mtr(self):
        self.listMtr.delete(*self.listMtr.get_children())
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        list = []
        for i in dictClients:
            if dictClients[i][7] != 0:
                list.append(i)
                list.append(dictClients[i][4])
                list.append(dictClients[i][0])
                list.append(dictClients[i][1])
                list.append(round(dictClients[i][7], 3))
                self.listMtr.insert("", END, values=list)
                list=[]
    
    def select_list_mtr2(self, name, purchCode):
        self.listMtr2.delete(*self.listMtr2.get_children())
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        list = []
        aux = []
        aux = dictPurchases[name][purchCode][0]
        for i in range(len(dictPurchases[name][purchCode][0])):
            list.append(dictProducts[aux[i]][0])
            list.append(dictPurchases[name][purchCode][2][i])
            list.append(dictProducts[aux[i]][2] - dictProducts[aux[i]][2]*dictPurchases[name][purchCode][1][i])
            self.listMtr2.insert("", END, values=list)
            list = []
        
    
    def search_mtr(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        nome = self.nome_mtr_entry.get()
        cpf = self.cpf_mtr_entry.get()
        nomeMae = self.nomeMae_mtr_entry.get()
        telefone = self.telefone_mtr_entry.get()
        list=[]
        if nome!="":
            self.listMtr.delete(*self.listMtr.get_children())
            for i in dictClients:
                if re.match(nome, i, re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][4])
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    list.append(dictClients[i][7])
                    list.append(0)
                    self.listMtr.insert("", END, values=list)
                    list=[]
        elif cpf!="":
            self.listMtr.delete(*self.listMtr.get_children())
            for i in dictClients:
                if re.search(cpf, dictClients[i][0], re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][4])
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    list.append(dictClients[i][7])
                    list.append(0)
                    self.listMtr.insert("", END, values=list)
                    list=[]
        elif nomeMae!="":
            self.listMtr.delete(*self.listMtr.get_children())
            for i in dictClients:
                if re.search(nomeMae, dictClients[i][4], re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][4])
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    list.append(dictClients[i][7])
                    list.append(0)
                    self.listMtr.insert("", END, values=list)
                    list=[]
        elif telefone!="":
            self.listMtr.delete(*self.listMtr.get_children())
            for i in dictClients:
                if re.search(telefone, dictClients[i][1], re.IGNORECASE):
                    list.append(i)
                    list.append(dictClients[i][4])
                    list.append(dictClients[i][0])
                    list.append(dictClients[i][1])
                    list.append(dictClients[i][7])
                    list.append(0)
                    self.listMtr.insert("", END, values=list)
                    list=[]
        else:
            self.select_list_mtr()
        self.clear_screen()

    def open_finish_mtr(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.clear_screen()
        self.listMtr.selection()
        col1=""
        for i in self.listMtr.selection():
            col1, col2, col3, col4, col5 = self.listMtr.item(i, 'values')
            #col1 possui a chave para pegar a informações da lista
        if col1 != "":
            for i in dictPurchases[col1]:
                if dictPurchases[col1][i][3] == "n": 
                    self.mtr_finish(col1, i)
                    break
        

    def finish_payment(self, key, purchCode, parcNow):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        topay = self.pagando_mtr_entry.get()
        dictClients[key][7] = float(dictClients[key][7]) - float(topay)
        if dictClients[key][7]< 0.1:
            dictClients[key][7] = 0
        dictPurchases[key][purchCode][4] = self.parcelas_mtr_entry.get()
        if float(dictClients[key][7]) < 0:
            print("Enviar valor que sobrou para o money_to_pay")
        if float(dictClients[key][7]) <= 0:
            dictPurchases[key][purchCode][3] = "s"
        
        jmanagerC.create_json('data/clients.json', dictClients)
        jmanagerP.create_json('data/products.json', dictProducts)
        jmanagerPurch.create_json('data/purchases.json', dictPurchases)
        self.select_list_mtr()


class Application(Funcs):
    def start(self, root2):
        self.root2 = root2
        self.mtr_screen()
        self.mtr_widgets_frame_1()
        self.mtr_list_frame_2()
        self.select_list_mtr()
        root2.mainloop()
    
    def mtr_screen(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.root2.title("Contas a Receber")
        self.root2.configure(background= '#582f0e')
        width= self.root2.winfo_screenwidth() 
        height= self.root2.winfo_screenheight()
        self.root2.wm_state('zoomed')
        self.root2.geometry("%dx%d+0+0" % (width, height))
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
        #Criação da label e entrada do nome da mae do cliente
        self.nomeMae_mtr = Label(self.frame_1, text="Nome da Mãe", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.nomeMae_mtr.place(relx=0.15, rely=0.4)
        self.nomeMae_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nomeMae_mtr_entry.place(relx=0.15, rely=0.55, relwidth=0.3)
        #Criação da label e entrada do telefone
        self.telefone_mtr = Label(self.frame_1, text="Telefone", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.telefone_mtr.place(relx=0.55, rely=0.4)
        self.telefone_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.telefone_mtr_entry.place(relx=0.55, rely=0.55, relwidth=0.3)
        

        #buscar
        self.bt_search = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_mtr())
        self.bt_search.place(relx=0.2, rely=0.75, relwidth=0.1, relheight=0.2)
        #limpar
        self.bt_clear = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.clear_screen())
        self.bt_clear.place(relx=0.45, rely=0.75, relwidth=0.1, relheight=0.2)
        #abrir
        self.bt_open = Button(self.frame_1, text="Abrir", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.open_finish_mtr())
        self.bt_open.place(relx=0.7, rely=0.75, relwidth=0.1, relheight=0.2)
        

    def mtr_list_frame_2(self):
        self.listMtr = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listMtr.heading("#0", text="")
        self.listMtr.heading("#1", text="Nome")
        self.listMtr.heading("#2", text="Nome da Mãe")
        self.listMtr.heading("#3", text="CPF")
        self.listMtr.heading("#4", text="Telefone")
        self.listMtr.heading("#5", text="Total")
        
        #tamanho -> 500=100%
        self.listMtr.column('#0', width=0, stretch=NO)
        self.listMtr.column("#1", width=140)
        self.listMtr.column("#2", width=140)
        self.listMtr.column("#3", width=90)
        self.listMtr.column("#4", width=90)
        self.listMtr.column("#5", width=50)

        self.listMtr.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.listMtr.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.052, relwidth=0.03, relheight=0.896)
        # self.listMtr.bind("<Double-1>",self.on_duble_click) #Função DoubleClick

    def mtr_finish(self, key, purchCode):
        self.select_list_mtr()
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.root3 = Toplevel()
        self.root3.title("Finalizar Compra")
        self.root3.configure(background= '#582f0e')
        width= self.root3.winfo_screenwidth() 
        height= self.root3.winfo_screenheight()
        self.root3.wm_state('zoomed')
        self.root3.geometry("%dx%d+0+0" % (width, height))
        self.root3.resizable(True, True)
        self.root3.minsize(width=600, height=500)
        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.18)
        self.frame_2 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.22, relwidth=0.475, relheight=0.76)
        self.frame_3 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_3.place(relx=0.505 , rely=0.22, relwidth=0.475, relheight=0.76)
        # insertValue = self.valorPago_mtr_entry.get()
        self.mtr_finish_widgets(key)
        self.mtr_finish_widgets2(key)
        self.mtr_finish_widgets3(key, purchCode)
        self.select_list_mtr2(key, purchCode)
    
    def mtr_finish_widgets(self, key):
        #Criação da label do nome do cliente
        self.nome_mtr = Label(self.frame_1, text="Nome: "+key, bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.nome_mtr.place(relx=0.25, rely=0.4)
        #Criação da label do cpf
        self.cpf_mtr = Label(self.frame_1, text="CPF: "+dictClients[key][0], bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.cpf_mtr.place(relx=0.25, rely=0.6)
        #Criação da label do telefone
        self.telefone_mtr = Label(self.frame_1, text="Telefone: "+dictClients[key][1], bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.telefone_mtr.place(relx=0.6, rely=0.6)
    
    def mtr_finish_widgets2(self, key):
        self.listMtr2 = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3"))
        self.listMtr2.heading("#0", text="")
        self.listMtr2.heading("#1", text="Nome do Produto")
        self.listMtr2.heading("#2", text="Quantidade")
        self.listMtr2.heading("#3", text="Valor")
    
        self.listMtr2.column('#0', width=0, stretch=NO)
        self.listMtr2.column("#1", width=300)
        self.listMtr2.column("#2", width=100)
        self.listMtr2.column("#3", width=100)

        self.listMtr2.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)
        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.listMtr2.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.052, relwidth=0.03, relheight=0.896)
        
    def mtr_finish_widgets3(self, key, purchCode):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        # Criação da label da data da compra
        self.data_mtr = Label(self.frame_3, text="Data da Compra: "+str(dictPurchases[key][purchCode][5]) , bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.data_mtr.place(relx=0.1, rely=0.1)
        # Criação da label da compra total(Abaixo é o cálculo da soma)
        somPurch = 0
        code = dictPurchases[key][purchCode][0]
        flag = dictPurchases[key][purchCode][1]
        quant = dictPurchases[key][purchCode][2]
        for i in range(len(code)):
            somPurch += dictProducts[code[i]][2]*quant[i] - dictProducts[code[i]][2]*quant[i]*flag[i]
            
        self.compraTotal_mtr = Label(self.frame_3, text="Compra Total: "+str(somPurch) , bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.compraTotal_mtr.place(relx=0.1, rely=0.2)

        #Criação da label e entrada das parcelas
        self.parcelas_mtr = Label(self.frame_3, text="Dividido em", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.parcelas_mtr.place(relx=0.1, rely=0.3)
        self.parcelas_mtr_entry = Entry(self.frame_3, bg='#c2c5aa')
        self.parcelas_mtr_entry.place(relx=0.3, rely=0.31, relwidth=0.1)
        self.parcelas_mtr_entry.insert(0, dictPurchases[key][purchCode][4])
            #Cálculo das parcelas totais
        parcTot = dictPurchases[key][purchCode][4]
        parcValue = round(float(somPurch/int(parcTot)), 3)
        self.parcelas2_mtr = Label(self.frame_3, text="vezes de R$"+str(parcValue)+"(Sugestão)", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.parcelas2_mtr.place(relx=0.42, rely=0.3)

        #Criação da label das parcelas que faltam
        parcNow = int(parcTot)
        owe = dictClients[key][7]
        j = int(parcTot)
        for i in range(int(parcTot)):
            j -= 1
            if parcValue*(i+1) >= owe:
                parcNow = int(parcTot)-j
                break
        self.parcelas3_mtr = Label(self.frame_3, text="Faltam "+str(parcNow)+" parcelas", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.parcelas3_mtr.place(relx=0.1, rely=0.4)

        #Criação da label do quanto deve
        self.devendo_mtr = Label(self.frame_3, text="Ainda deve R$"+str(parcNow*parcValue), bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.devendo_mtr.place(relx=0.1, rely=0.5)

        #Criação da label e da entrada de quanto está pagando
        self.pagando_mtr = Label(self.frame_3, text="Pagando", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.pagando_mtr.place(relx=0.1, rely=0.6)
        self.pagando_mtr_entry = Entry(self.frame_3, bg='#c2c5aa')
        self.pagando_mtr_entry.place(relx=0.3, rely=0.6, relwidth=0.1)
        self.pagando_mtr_entry.insert(0, parcValue)

        #fechar
        self.bt_close = Button(self.frame_3, text="Fechar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.root3.destroy())
        self.bt_close.place(relx=0.1, rely=0.75, relwidth=0.3, relheight=0.1)
        #confirmar pagamento
        self.bt_finish = Button(self.frame_3, text="Confirmar pagamento", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: [self.finish_payment(key, purchCode, parcNow), self.root3.destroy()])
        self.bt_finish.place(relx=0.6, rely=0.75, relwidth=0.3, relheight=0.1)

