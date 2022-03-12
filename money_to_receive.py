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
        dictClients = jmanagerC.read_json('data/clients.json')
        list = []
        for i in dictClients:
            list.append(i)
            list.append(dictClients[i][4])
            list.append(dictClients[i][0])
            list.append(dictClients[i][1])
            list.append(dictClients[i][7])
            self.listMtr.insert("", END, values=list)
            list=[]
    
    def select_list_mtr2(self, name):
        self.listMtr2.delete(*self.listMtr2.get_children())
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        list = []
        for i in dictPurchases[name]:
            if dictPurchases[name][i][4] == "n":
                list.append(dictPurchases[name][i][0])
                list.append(dictProducts[dictPurchases[name][i][0]][0])
                list.append(dictPurchases[name][i][2])
                if dictPurchases[name][i][3] == "s":
                    list.append(dictProducts[dictPurchases[name][i][0]][3])
                else:
                    list.append(dictProducts[dictPurchases[name][i][0]][2])
                list.append(dictPurchases[name][i][5])
                self.listMtr.insert("", END, values=list)
                list=[]
    
    def search_mtr(self):
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
                    list.append(0)
                    list.append(0)
                    list.append(dictClients[i][7])
                    list.append(0)
                    for j in dictPurchases[i]:
                        if dictPurchases[i][j][4] == "n":
                            list[4] = dictPurchases[i][j][1]
                            list[5] = dictPurchases[i][j][5]
                            list[7] = dictPurchases[i][j]
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
                    list.append(0)
                    list.append(0)
                    list.append(dictClients[i][7])
                    list.append(0)
                    for j in dictPurchases[i]:
                        if dictPurchases[i][j][4] == "n":
                            list[4] = dictPurchases[i][j][1]
                            list[5] = dictPurchases[i][j][5]
                            list[7] = dictPurchases[i][j]
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
                    list.append(0)
                    list.append(0)
                    list.append(dictClients[i][7])
                    list.append(0)
                    for j in dictPurchases[i]:
                        if dictPurchases[i][j][4] == "n":
                            list[4] = dictPurchases[i][j][1]
                            list[5] = dictPurchases[i][j][5]
                            list[7] = dictPurchases[i][j]
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
                    list.append(0)
                    list.append(0)
                    list.append(dictClients[i][7])
                    list.append(0)
                    for j in dictPurchases[i]:
                        if dictPurchases[i][j][4] == "n":
                            list[4] = dictPurchases[i][j][1]
                            list[5] = dictPurchases[i][j][5]
                            list[7] = dictPurchases[i][j]
                            self.listMtr.insert("", END, values=list) 
                    list=[]
        else:
            self.select_list_mtr()
        self.clear_screen()

    def open_finish_mtr(self):
        self.clear_screen()
        self.listMtr.selection()
        col1=""
        for i in self.listMtr.selection():
            col1, col2, col3, col4, col5 = self.listMtr.item(i, 'values')
            #col1 possui a chave para pegar a informações da lista
        if col1 != "":
            self.mtr_finish(col1)
            aux=0
            for i in dictPurchases[col1]:
                if dictPurchases[col1][i][4] == "n": 
                    self.valorPago_mtr_entry.insert(END, dictPurchases[col1][i][5])
                    break
        #Repensar como utilizar as parcelas!!!!
        #Talvez uma parcela total das compras e deixar o usuario mudar a quantidade de parcelas...
        self.select_list_mtr2(self, col1)

    def finish_payment(self, key, insertValue):
        topay = self.valorPago_mtr_entry.get()
        dictClients[key][7] = float(dictClients[key][7]) - float(topay)
        if float(dictClients[key][7]) < 0:
            print("Enviar valor que sobrou para o money_to_pay")
        if float(topay)<insertValue:
            dictPurchases[key][purchCode][4]
        dictPurchases[key][purchCode][4] = "s"
        jmanagerC.create_json('data/clients.json', dictClients)
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

    def mtr_finish(self, key):
        self.root3 = Toplevel()
        self.root3.title("Finalizar Compra")
        self.root3.configure(background= '#582f0e')
        self.root3.geometry('1200x700')
        self.root3.resizable(True, True)
        self.root3.minsize(width=600, height=500)
        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)
        insertValue = self.valorPago_mtr_entry.get()
        self.mtr_finish_widgets(key, insertValue)
    
    def mtr_finish_widgets(self, key, insertValue):
        #Criação da label do nome do cliente
        self.nome_mtr = Label(self.frame_1, text="Nome: "+key, bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.nome_mtr.place(relx=0.01, rely=0.01)
        #Criação da label do cpf
        self.cpf_mtr = Label(self.frame_1, text="CPF: "+dictClients[key][0], bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.cpf_mtr.place(relx=0.01, rely=0.08)
        #Criação da label do telefone
        self.telefone_mtr = Label(self.frame_1, text="Telefone: "+dictClients[key][1], bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.telefone_mtr.place(relx=0.45, rely=0.08)
        
        #Criação da label do (total devendo - valor da compra)
        # self.dividas_mtr = Label(self.frame_1, text="Dívidas totais: "+str(dictClients[key][7])+" - "+str(float(prodValue)*float(dictPurchases[key][purchCode][2]))+ " = "+str(float(dictClients[key][7])-(float(prodValue)*float(dictPurchases[key][purchCode][2]))) , bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        # self.dividas_mtr.place(relx=0.5, rely=0.32)


        #Criação da label e entrada do valor pago
        self.valorPago_mtr = Label(self.frame_1, text="O cliente vai pagar ", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.valorPago_mtr.place(relx=0.32, rely=0.4)
        self.valorPago_mtr_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.valorPago_mtr_entry.place(relx=0.5, rely=0.41, relwidth=0.1)

        #fechar
        self.bt_close = Button(self.frame_1, text="Fechar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.root3.destroy())
        self.bt_close.place(relx=0.2, rely=0.75, relwidth=0.2, relheight=0.1)
        #confirmar pagamento
        self.bt_finish = Button(self.frame_1, text="Confirmar pagamento", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: [self.finish_payment(key, purchCode, float(insertValue)), self.root3.destroy()])
        self.bt_finish.place(relx=0.55, rely=0.75, relwidth=0.2, relheight=0.1)

        #Lista -> tenho que posicionar
        self.listMtr2 = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listMtr2.heading("#0", text="")
        self.listMtr2.heading("#1", text="Código")
        self.listMtr2.heading("#2", text="Nome do Produto")
        self.listMtr2.heading("#3", text="Quantidade")
        self.listMtr2.heading("#4", text="Valor")
        self.listMtr2.heading("#5", text="Parcelas")
    
        self.listMtr2.column('#0', width=0, stretch=NO)
        self.listMtr2.column("#1", width=100)
        self.listMtr2.column("#2", width=100)
        self.listMtr2.column("#3", width=100)
        self.listMtr2.column("#4", width=100)
        self.listMtr2.column("#5", width=100)
        self.listMtr2.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)
        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.listMtr2.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.052, relwidth=0.03, relheight=0.896)
        

    

# self.listMtr.delete(*self.listMtr.get_children())
#         dictClients = jmanagerC.read_json('data/clients.json')
#         dictPurchases = jmanagerPurch.read_json('data/purchases.json')
#         list = []
#         for i in dictClients:
#             list.append(i)
#             list.append(dictClients[i][4])
#             list.append(dictClients[i][0])
#             list.append(dictClients[i][1])
#             list.append(0)
#             list.append(0)
#             list.append(dictClients[i][7])
#             list.append(0)
#             for j in dictPurchases[i]:
#                 if dictPurchases[i][j][4] == "n":
#                     list[4] = dictPurchases[i][j][1]
#                     list[5] = dictPurchases[i][j][5]
#                     list[7] = j
#                     self.listMtr.insert("", END, values=list)
#             list=[]

#Lista das compras