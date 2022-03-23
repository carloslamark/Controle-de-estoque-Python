from tarfile import ENCODING
from import_aux import *


#Iniciando db
jmanagerC = json.JsonManagerClient()
jmanagerP = json.JsonManagerProd()
jmanagerPurch = json.JsonManagerPurchases()
dictClients = []
dictProducts = []
dictPurchases = []
dictClients = jmanagerC.read_json('data/clients.json')
dictProducts = jmanagerP.read_json('data/products.json') 
dictPurchases = jmanagerPurch.read_json('data/purchases.json')

dt = str(date.today())
dateToday = dt[8]+dt[9]+"/"+dt[5]+dt[6]+"/"+dt[0]+dt[1]+dt[2]+dt[3]

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
    def clear_screen_clients(self):
        self.nome_clients_entry.delete(0, END)
        self.cpf_clients_entry.delete(0, END)
        self.telefone_clients_entry.delete(0, END)
 
    def clear_screen_cadClients(self):
        self.nome_cadClients_entry.delete(0, END)
        self.cpf_cadClients_entry.delete(0, END)
        self.telefone_cadClients_entry.delete(0, END)
        self.email_cadClients_entry.delete(0, END)
        self.dataNas_cadClients_entry.delete(0, END)
        self.nomeMae_cadClients_entry.delete(0, END)
        self.endereco_cadClients_entry.delete(0, END)
        self.obs_cadClients_entry.delete(0, END)

    def clear_screen_buy_list(self):
        self.codigo_insert_entry.delete(0, END)
        self.nomeProd_insert_entry.delete(0, END)
        self.quantity_insert_entry.delete(0, END)
        self.quantity_insert_entry.insert(0, 1)
        self.discount_insert_entry.delete(0, END)

    def variables_client(self):
        cAux = ["", "", "", "", "", "", "", 0]
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
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        cAux = []
        cAux, name = self.variables_client()
        dictClients[name] = cAux
        dictPurchases[name] = {}
        jmanagerC.create_json('data/clients.json', dictClients)
        jmanagerP.create_json('data/products.json', dictProducts)
        jmanagerPurch.create_json('data/purchases.json', dictPurchases)
        self.select_list_clients()
        self.clear_screen_cadClients()       

    def select_list_clients(self):
        self.listCli.delete(*self.listCli.get_children())
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        list = []
        for i in dictClients:
            list.append(i)
            list.append(dictClients[i][0])
            list.append(dictClients[i][1])
            self.listCli.insert("", END, values=list)
            list=[] 

    def on_duble_click(self, event):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.clear_screen_clients()
        self.listCli.selection()
        col1=""
        for i in self.listCli.selection():
            col1, col2, col3 = self.listCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do client
        self.show_client(col1) 

    def on_duble_click_prod(self, event):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.listProd.selection()
        self.codigo_insert_entry.delete(0, END)
        self.nomeProd_insert_entry.delete(0, END)
        col1=""
        for i in self.listProd.selection():
            col1, col2, col3, col4 = self.listProd.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do client
        self.codigo_insert_entry.insert(0, col1)
        self.nomeProd_insert_entry.insert(0, dictProducts[col1][0])

    def edit_client(self, flag):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.clear_screen_clients()
        self.listCli.selection()
        col1=""
        for i in self.listCli.selection():
            col1, col2, col3 = self.listCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do client
        if col1 != "":
            self.cad_clients(flag, col1)
            self.nome_cadClients_entry.insert(END, col1)
            self.cpf_cadClients_entry.insert(END, dictClients[col1][0])
            self.telefone_cadClients_entry.insert(END, dictClients[col1][1])
            self.email_cadClients_entry.insert(END, dictClients[col1][2])
            self.dataNas_cadClients_entry.insert(END, dictClients[col1][3])
            self.nomeMae_cadClients_entry.insert(END, dictClients[col1][4])
            self.endereco_cadClients_entry.insert(END, dictClients[col1][5])
            self.obs_cadClients_entry.insert(END, dictClients[col1][6])  

    def delete_client(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        cAux = []
        cAux, name = self.variables_client()
        del dictClients[name]

        jmanagerC.create_json('data/clients.json', dictClients)
        jmanagerP.create_json('data/products.json', dictProducts)
        jmanagerPurch.create_json('data/purchases.json', dictPurchases)
        self.clear_screen_cadClients()
        self.select_list_clients()

    def change_client(self, name):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        if self.nome_cadClients_entry.get() in dictClients:
            self.add_client()
        else:
            del dictClients[name]
            self.add_client()
        jmanagerC.create_json('data/clients.json', dictClients)
        jmanagerP.create_json('data/products.json', dictProducts)
        jmanagerPurch.create_json('data/purchases.json', dictPurchases)
        
    def search_client(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
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

        self.clear_screen_clients

    def insert_prod(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.clear_screen_clients()
        self.listCli.selection()
        col1=""
        for i in self.listCli.selection():
            col1, col2, col3 = self.listCli.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do cliente
        if col1 != "":
            self.insert_prod_to_cli(col1)

    def search_prod(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        codigo = self.codigo_insert_entry.get()
        nomeProd = self.nomeProd_insert_entry.get()
        list=[]
        if codigo!="":
            self.listProd.delete(*self.listProd.get_children())
            for i in dictProducts:
                if re.match(codigo, i, re.IGNORECASE):
                    list.append(i)
                    list.append(dictProducts[i][0])
                    list.append(dictProducts[i][1])
                    list.append(dictProducts[i][2])
                    self.listProd.insert("", END, values=list)
                    list=[] 
        elif nomeProd!="":
            self.listProd.delete(*self.listProd.get_children())
            for i in dictProducts:
                if re.match(nomeProd, dictProducts[i][0], re.IGNORECASE):
                    list.append(i)
                    list.append(dictProducts[i][0])
                    list.append(dictProducts[i][1])
                    list.append(dictProducts[i][2])
                    self.listProd.insert("", END, values=list)
                    list=[] 
        else:
            self.select_list_prod()
        self.codigo_insert_entry.delete(0, END)
    
    def select_list_prod(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.listProd.delete(*self.listProd.get_children())
        list = []
        for i in dictProducts:
            list.append(i)
            list.append(dictProducts[i][0])
            list.append(dictProducts[i][1])
            list.append(dictProducts[i][2])
            self.listProd.insert("", END, values=list)
            list=[]

    def select_list_shop(self, key):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.listShop.delete(*self.listShop.get_children())
        list = []
        aux = 0
        if key in dictPurchases:
            for i in dictPurchases[key]:
                if dictPurchases[key][i][3] == "n":
                    for j in range(len(dictPurchases[key][i][0])):
                        list.append(dictProducts[dictPurchases[key][i][0][j]][0])
                        list.append(dictPurchases[key][i][2][j])
                        aux = str((dictPurchases[key][i][1][j])*100) +"%"
                        list.append(aux)
                        list.append(dictProducts[dictPurchases[key][i][0][j]][2] - (dictProducts[dictPurchases[key][i][0][j]][2]*dictPurchases[key][i][1][j]))
                        
                        self.listShop.insert("", END, values=list)
                        list=[]
                    break
        
    
    def update_buy_list(self, key, code, quant, disc, dCom, parc):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        if code!="" and disc!="":
            j=1
            if quant == "":
                quant = 1
            if parc == "":
                parc =  1
            if dCom == "":
                dCom = str(dateToday)
            disc = round((disc/100),3)
            if key not in dictPurchases:
                dictPurchases[key] = {}
                dictPurchases[key]["1"] = [[], [], [], "n", "", ""]

            for i in dictPurchases[key].keys():
                j=i
           
            if dictPurchases[key][j][3] == "s":
                j = int(j)+1
                dictPurchases[key][j] = [[], [], [], "n", "", ""]
                dictPurchases[key][j][0].append(code)
                dictPurchases[key][j][1].append(disc)
                dictPurchases[key][j][2].append(int(quant))
                dictPurchases[key][j][3] ="n"
                dictPurchases[key][j][4] = parc
                dictPurchases[key][j][5] = dCom
                if disc == 0:
                    disc = 1
                dictClients[key][7] += dictProducts[code][2] - (dictProducts[code][2]*int(quant)*disc)

                if dictProducts[code][1]-int(quant) >= 0:
                    dictProducts[code][1] -= int(quant)
                else:
                    dictProducts[code][1] = 0 
            else:
                dictPurchases[key][j][0].append(code)
                dictPurchases[key][j][1].append(disc)
                dictPurchases[key][j][2].append(int(quant))
                dictPurchases[key][j][4] = parc
                dictPurchases[key][j][5] = dCom
                if disc == 0:
                    disc = 1
                dictClients[key][7] += dictProducts[code][2] - (dictProducts[code][2]*int(quant)*disc)

                if dictProducts[code][1]-int(quant) >= 0:
                    dictProducts[code][1] -= int(quant)
                else:
                    dictProducts[code][1] = 0
                
            self.clear_screen_buy_list()
            jmanagerC.create_json('data/clients.json', dictClients)
            jmanagerP.create_json('data/products.json', dictProducts)
            jmanagerPurch.create_json('data/purchases.json', dictPurchases)
            self.select_list_shop(key)
            


class Application(Funcs, Relatorios):
    def start(self, root2):
        self.root2 = root2
        self.clients_screen()
        self.clients_widgets_frame_1()
        self.clients_list_frame_2()
        self.select_list_clients()
        root2.mainloop()
  
    def clients_screen(self):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.root2.title("Clients")
        self.root2.configure(background= '#582f0e')
        width= self.root2.winfo_screenwidth() 
        height= self.root2.winfo_screenheight()
        self.root2.wm_state('zoomed')
        self.root2.geometry("%dx%d+0+0" % (width, height))#tamanho da screen
        self.root2.resizable(True, True) #Horizontal, Vertical
        self.root2.minsize(width=600, height=500) #tamanho das screens
        #Frames da screen de clients
        self.frame_1 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem
        self.frame_2 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)#Trabalha com porcentagem  

    def clients_widgets_frame_1(self):
        #Criação da label e entrada do nome
        self.nome_clients = Label(self.frame_1, text="Nome do Cliente", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
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
        self.bt_limpar_clients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clear_screen_clients)
        self.bt_limpar_clients.place(relx=0.15, rely=0.7, relwidth=0.1, relheight=0.15)
        #search
        self.bt_search = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_client())
        self.bt_search.place(relx=0.275, rely=0.7, relwidth=0.1, relheight=0.15)
        #Botão inserir produto na conta do cliente
        self.bt_insertProd = Button(self.frame_1, text="Adicionar Compra", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.insert_prod()])
        self.bt_insertProd.place(relx=0.4125, rely=0.7, relwidth=0.175, relheight=0.15)
        #edit
        self.bt_edit = Button(self.frame_1, text="Editar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.edit_client(2))
        self.bt_edit.place(relx=0.625, rely=0.7, relwidth=0.1, relheight=0.15)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.cad_clients(1, ""))
        self.bt_novo.place(relx=0.75, rely=0.7, relwidth=0.1, relheight=0.15)
        
    def clients_list_frame_2(self):
        self.listCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3"))
        self.listCli.heading("#0", text="")
        self.listCli.heading("#1", text="Nome")
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
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.root3 = Toplevel()
        self.root3.title("Cadastro Client")
        self.root3.configure(background= '#582f0e')
        width= self.root3.winfo_screenwidth() 
        height= self.root3.winfo_screenheight()
        self.root3.wm_state('zoomed')
        self.root3.geometry("%dx%d+0+0" % (width, height))
        self.root3.resizable(False, False) #Horizontal, Vertical
        self.root3.transient(self.root2)
        self.root3.focus_force()
        self.root3.grab_set()

        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)#Trabalha com porcentagem

        self.cad_clients_widgets(flag, aux)
   
    def cad_clients_widgets(self, flag, aux):
        #Criação da label e entrada do nome
        self.nome_cadClients = Label(self.frame_1, text="Nome do Cliente", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
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
            self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clear_screen_cadClients)
            self.bt_limpar_cadClients.place(relx=0.15, rely=0.85, relwidth=0.15, relheight=0.1)
            #enviar
            self.bt_cadClients_enviar = Button(self.frame_1, text="Enviar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.add_client(), self.root3.destroy()])
            self.bt_cadClients_enviar.place(relx=0.7, rely=0.85, relwidth=0.15, relheight=0.1)
        elif flag==2:
            #limpar
            self.bt_limpar_cadClients = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clear_screen_cadClients)
            self.bt_limpar_cadClients.place(relx=0.15, rely=0.85, relwidth=0.15, relheight=0.1)
            #change
            self.bt_change = Button(self.frame_1, text="Alterar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.change_client(aux), self.root3.destroy()])
            self.bt_change.place(relx=0.425, rely=0.85, relwidth=0.15, relheight=0.1)
            #apagar
            self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.delete_client(), self.root3.destroy()])
            self.bt_apagar.place(relx=0.7, rely=0.85, relwidth=0.15, relheight=0.1)
   
    def show_client(self, key):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.root3 = Toplevel()
        self.root3.title("Informações do Cliente")
        self.root3.configure(background= '#582f0e')
        width= self.root3.winfo_screenwidth() 
        height= self.root3.winfo_screenheight()
        self.root3.wm_state('zoomed')
        self.root3.geometry("%dx%d+0+0" % (width, height))
        self.root3.resizable(False, False) #Horizontal, Vertical
        self.root3.transient(self.root2)
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
            self.root2.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatórios", menu=filemenu2)

        filemenu.add_command(label="Limpa busca", command=self.clear_screen_clients)
        filemenu.add_command(label="Sair", command=Quit)

        filemenu2.add_command(label="Ficha do Cliente", command=lambda: self.geraRelatClient(key))

    def insert_prod_to_cli(self, key):
        dictProducts = jmanagerP.read_json('data/products.json')
        dictClients = jmanagerC.read_json('data/clients.json')
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        self.root3 = Toplevel()
        self.root3.title("Adicionar Compra")
        self.root3.configure(background= '#582f0e')
        width= self.root3.winfo_screenwidth() 
        height= self.root3.winfo_screenheight()
        self.root3.wm_state('zoomed')
        self.root3.geometry("%dx%d+0+0" % (width, height))
        self.root3.resizable(False, False) #Horizontal, Vertical
        self.root3.transient(self.root2)
        self.root3.focus_force()
        self.root3.grab_set()
        
        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.16)#Trabalha com porcentagem
        self.frame_2 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.2, relwidth=0.475, relheight=0.76)#Trabalha com porcentagem
        self.frame_3 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_3.place(relx=0.505 , rely=0.2, relwidth=0.475, relheight=0.76)#Trabalha com porcentagem
       
        self.insert_prod_to_cli_widgetsF1(key)  
        self.insert_prod_to_cli_widgetsF2(key)
        self.insert_prod_to_cli_widgetsF3(key)   
        self.select_list_prod()
        self.select_list_shop(key)
        

    def insert_prod_to_cli_widgetsF1(self, key):
        #Nome
        self.show_nome = Label(self.frame_1, text="Nome: "+key, bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.show_nome.place(relx=0.2, rely=0.01)
        #Criação da label e entrada do codigo do produto
        self.codigo_insert = Label(self.frame_1, text="Código", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.codigo_insert.place(relx=0.2, rely=0.4)
        self.codigo_insert_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.codigo_insert_entry.place(relx=0.2, rely=0.6, relwidth=0.15)
        #Criação da label e entrada do nome do produto
        self.nomeProd_insert = Label(self.frame_1, text="Produto", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.nomeProd_insert.place(relx=0.5, rely=0.4)
        self.nomeProd_insert_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.nomeProd_insert_entry.place(relx=0.5, rely=0.6, relwidth=0.15)
    
        #search
        self.bt_search = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_prod())
        self.bt_search.place(relx=0.7, rely=0.4, relwidth=0.15, relheight=0.4)
        
        
        
    def insert_prod_to_cli_widgetsF2(self, key):
        self.listProd = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listProd.heading("#0", text="")
        self.listProd.heading("#1", text="Código")
        self.listProd.heading("#2", text="Produto")
        self.listProd.heading("#3", text="Quantidade")
        self.listProd.heading("#4", text="Valor")
        
        #tamanho -> 500=100%
        self.listProd.column('#0', width=0, stretch=NO)
        self.listProd.column("#1", width=75)
        self.listProd.column("#2", width=175)
        self.listProd.column("#3", width=125)
        self.listProd.column("#4", width=125)


        self.listProd.place(relx=0.01, rely=0.02, relwidth=0.95, relheight=0.5)

        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.listProd.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.496)
        self.listProd.bind("<Double-1>", self.on_duble_click_prod) #Função DoubleClick 

        #Criação da label e entrada do quantidade
        self.quantity_insert = Label(self.frame_2, text="Quantidade", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.quantity_insert.place(relx=0.2, rely=0.6)
        self.quantity_insert_entry = Entry(self.frame_2, bg='#c2c5aa')
        self.quantity_insert_entry.place(relx=0.2, rely=0.7, relwidth=0.2)
        self.quantity_insert_entry.insert(0, 1)

        #Criação da label e entrada do desconto
        self.discount_insert = Label(self.frame_2, text="Desconto(Digite o Número)", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.discount_insert.place(relx=0.6, rely=0.6)
        self.discount_insert_entry = Entry(self.frame_2, bg='#c2c5aa')
        self.discount_insert_entry.place(relx=0.6, rely=0.7, relwidth=0.2)

        #insert
        self.bt_insert = Button(self.frame_2, text="Inserir na Compra", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: [self.update_buy_list(key, self.codigo_insert_entry.get(), self.quantity_insert_entry.get(), float(self.discount_insert_entry.get()), self.dataCom_insert_entry.get(), self.parcelas_insert_entry.get())])
        self.bt_insert.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

    
    def insert_prod_to_cli_widgetsF3(self, key):
        dictClients = jmanagerC.read_json('data/clients.json')
        dictProducts = jmanagerP.read_json('data/products.json') 
        dictPurchases = jmanagerPurch.read_json('data/purchases.json')
        #Criação da label e entrada da data da compra
        self.dataCom_insert = Label(self.frame_3, text="Data da Compra", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.dataCom_insert.place(relx=0.02, rely=0.02)
        self.dataCom_insert_entry = Entry(self.frame_3, bg='#c2c5aa')
        self.dataCom_insert_entry.place(relx=0.02, rely=0.1, relwidth=0.15)

        self.listShop = ttk.Treeview(self.frame_3, height=3, column=("col1", "col2", "col3", "col4"))
        self.listShop.heading("#0", text="")
        self.listShop.heading("#1", text="Produto")
        self.listShop.heading("#2", text="Quantidade")
        self.listShop.heading("#3", text="Desconto")
        self.listShop.heading("#4", text="Valor")
        
        #tamanho -> 500=100%
        self.listShop.column('#0', width=0, stretch=NO)
        self.listShop.column("#1", width=200)
        self.listShop.column("#2", width=100)
        self.listShop.column("#3", width=100)
        self.listShop.column("#3", width=100)
        
        self.listShop.place(relx=0.01, rely=0.2, relwidth=0.95, relheight=0.4)

        self.scroolList = Scrollbar(self.frame_3, orient='vertical')
        self.listShop.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.2, relwidth=0.03, relheight=0.396)

        #Criação da label do total
        self.total = Label(self.frame_3, text="Total: R$" + str(dictClients[key][7]), bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.total.place(relx=0.1, rely=0.65)

        #Criação da label e entrada das parcelas
        self.parcelas_insert = Label(self.frame_3, text="Parcelas", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.parcelas_insert.place(relx=0.6, rely=0.65)
        self.parcelas_insert_entry = Entry(self.frame_3, bg='#c2c5aa')
        self.parcelas_insert_entry.place(relx=0.6, rely=0.7, relwidth=0.15)
        if key in dictPurchases:
            j=0
            for i in dictPurchases[key]:
                j=i
            if dictPurchases[key][j][3] == "n":
                self.parcelas_insert_entry.insert(0, dictPurchases[key][j][4])
                self.dataCom_insert_entry.insert(0, dictPurchases[key][j][5])
            else:
                self.parcelas_insert_entry.insert(0, 1)
                self.dataCom_insert_entry.insert(0, dateToday)
        else:
            self.parcelas_insert_entry.insert(0, 1)
            self.dataCom_insert_entry.insert(0, dateToday)

        #finish
        self.bt_finish = Button(self.frame_3, text="Finalizar Compra", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: [self.clear_screen_buy_list(), self.root3.destroy()])
        self.bt_finish.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

        