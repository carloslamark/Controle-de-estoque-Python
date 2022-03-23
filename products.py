from import_aux import *

#Iniciando db
jmanagerP = json.JsonManagerProd()
dictProducts = []
dictProducts = jmanagerP.read_json('data/products.json')



class Funcs():
    def update_dict(self):
        dictProducts = jmanagerP.read_json('data/products.json')

    def clear_screen_prod(self):
        self.codigo_prod_entry.delete(0, END)

    def clear_screen_cadProd(self):
        self.codigo_cadProd_entry.delete(0, END)
        self.produto_cadProd_entry.delete(0, END)
        self.quantidade_cadProd_entry.delete(0, END)
        self.semD_cadProd_entry.delete(0, END)
        self.comD_cadProd_entry.delete(0, END)
         
    def variables_prod(self):
        pAux = ["", 0, 0, 0]
        codigo = self.codigo_cadProd_entry.get()
        pAux[0] = self.produto_cadProd_entry.get()
        pAux[1] = int(self.quantidade_cadProd_entry.get())
        pAux[2] = float(self.semD_cadProd_entry.get())
        pAux[3] = float(self.comD_cadProd_entry.get())
        
        return pAux, codigo
    
    def add_prod(self):
        pAux = []
        pAux, codigo = self.variables_prod()
        dictProducts[codigo] = pAux

        jmanagerP.create_json('data/products.json', dictProducts)
        self.select_list_prod()
        self.clear_screen_cadProd()

    def select_list_prod(self):
        self.listProd.delete(*self.listProd.get_children())
        
        list = []
        for i in dictProducts:
            list.append(i)
            list.append(dictProducts[i][0])
            list.append(dictProducts[i][1])
            list.append(dictProducts[i][2])
            list.append(dictProducts[i][3])
            self.listProd.insert("", END, values=list)
            list=[]

    def on_duble_click(self, event):
        self.clear_screen_prod()
        self.listProd.selection()
        col1=""
        for i in self.listProd.selection():
            col1, col2, col3, col4, col5 = self.listProd.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do produto
        self.edit_prod(2)

    def edit_prod(self, flag):
        self.clear_screen_prod()
        self.listProd.selection()
        col1=""
        for i in self.listProd.selection():
            col1, col2, col3, col4, col5 = self.listProd.item(i, 'values')
            #col1 possui a chave para pegar a informações na ficha do produto
        if col1 != "":
            aux=col1
            self.cad_prod(flag, aux)
            self.codigo_cadProd_entry.insert(END, col1)
            self.produto_cadProd_entry.insert(END, dictProducts[col1][0])
            self.quantidade_cadProd_entry.insert(END, dictProducts[col1][1])
            self.semD_cadProd_entry.insert(END, dictProducts[col1][2])
            self.comD_cadProd_entry.insert(END, dictProducts[col1][3])
             
    def delete_prod(self):
        pAux = []
        pAux, codigo = self.variables_prod()
        del dictProducts[codigo]

        jmanagerP.create_json('data/products.json', dictProducts)
        self.clear_screen_cadProd()
        self.select_list_prod()

    def change_prod(self, codigo):
        if self.codigo_cadProd_entry.get() in dictProducts:
            self.add_prod()
        else:
            del dictProducts[codigo]
            self.add_prod()

    def search_prod(self):
        codigo = self.codigo_prod_entry.get()
        list=[]
        if codigo!="":
            self.listProd.delete(*self.listProd.get_children())
            for i in dictProducts:
                if re.match(codigo, i, re.IGNORECASE):
                    list.append(i)
                    list.append(dictProducts[i][0])
                    list.append(dictProducts[i][1])
                    list.append(dictProducts[i][2])
                    list.append(dictProducts[i][3])
                    self.listProd.insert("", END, values=list)
                    list=[] 
        else:
            self.select_list_prod()

        self.clear_screen_prod




class Application(Funcs):
    def start(self, root2):
        self.root2 = root2
        self.prod_screen()
        self.prod_widgets_frame_1()
        self.prod_list_frame_2()
        self.select_list_prod()
        root2.mainloop()

    def prod_screen(self):
        self.root2.title("Estoque")
        self.root2.configure(background= '#582f0e')
        width= self.root2.winfo_screenwidth() 
        height= self.root2.winfo_screenheight()
        self.root2.wm_state('zoomed')
        self.root2.geometry("%dx%d+0+0" % (width, height))
        self.root2.resizable(True, True)
        self.root2.minsize(width=600, height=500)
        self.frame_1 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.16)
        self.frame_2 = Frame(self.root2, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.2, relwidth=0.96, relheight=0.76)
    
    def prod_widgets_frame_1(self):
        #Criação da label e entrada do Código
        self.codigo_prod = Label(self.frame_1, text="Código do Produto", bg='#a68a64', fg='#582f0e', font=('Arial', 15, BOLD))
        self.codigo_prod.place(relx=0.15, rely=0.2)
        self.codigo_prod_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.codigo_prod_entry.place(relx=0.15, rely=0.5, relwidth=0.2)

        #search
        self.bt_search = Button(self.frame_1, text="Buscar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.search_prod())
        self.bt_search.place(relx=0.38, rely=0.3, relwidth=0.1, relheight=0.4)
        #limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.clear_screen_prod())
        self.bt_limpar.place(relx=0.49, rely=0.3, relwidth=0.1, relheight=0.4)
        #edit
        self.bt_edit = Button(self.frame_1, text="Editar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.edit_prod(2))
        self.bt_edit.place(relx=0.63, rely=0.3, relwidth=0.1, relheight=0.4)
        #novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda: self.cad_prod(1, ""))
        self.bt_novo.place(relx=0.74, rely=0.3, relwidth=0.1, relheight=0.4)

    def prod_list_frame_2(self):
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

    def cad_prod(self, flag, aux):
        self.root3 = Toplevel()
        self.root3.title("Cadastro Produto")
        self.root3.configure(background= '#582f0e')
        width= self.root3.winfo_screenwidth() 
        height= self.root3.winfo_screenheight()
        self.root3.wm_state('zoomed')
        self.root3.geometry("%dx%d+0+0" % (width, height))
        self.root3.resizable(True, True)
        self.root3.transient(self.root2)
        self.root3.focus_force()
        self.root3.grab_set()

        self.frame_1 = Frame(self.root3, border=4, bg='#a68a64', highlightbackground='#936639', highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)#Trabalha com porcentagem

        self.cad_prod_widgets(flag, aux)   
    
    def cad_prod_widgets(self, flag, aux):
        #Criação da label e entrada do Código do Produto
        self.codigo_cadProd = Label(self.frame_1, text="Código do Produto", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.codigo_cadProd.place(relx=0.1, rely=0.05)
        self.codigo_cadProd_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.codigo_cadProd_entry.place(relx=0.1, rely=0.1, relwidth=0.8)
        #Criação da label e entrada do Nome do Produto
        self.produto_cadProd = Label(self.frame_1, text="Nome do Produto", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.produto_cadProd.place(relx=0.1, rely=0.15)
        self.produto_cadProd_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.produto_cadProd_entry.place(relx=0.1, rely=0.2, relwidth=0.375)
        #Criação da label e entrada da Quantidade no Estoque
        self.quantidade_cadProd = Label(self.frame_1, text="Quantidade no Estoque", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.quantidade_cadProd.place(relx=0.525, rely=0.15)
        self.quantidade_cadProd_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.quantidade_cadProd_entry.place(relx=0.525, rely=0.2, relwidth=0.375)
        #Criação da label e entrada do Valor SEM desconto
        self.semD_cadProd = Label(self.frame_1, text="Valor SEM desconto", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.semD_cadProd.place(relx=0.1, rely=0.25)
        self.semD_cadProd_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.semD_cadProd_entry.place(relx=0.1, rely=0.3, relwidth=0.375)
        #Criação da label e entrada do Valor COM desconto
        self.comD_cadProd = Label(self.frame_1, text="Valor COM desconto", bg='#a68a64', fg='#582f0e', font=('Arial', 12, BOLD))
        self.comD_cadProd.place(relx=0.525, rely=0.25)
        self.comD_cadProd_entry = Entry(self.frame_1, bg='#c2c5aa')
        self.comD_cadProd_entry.place(relx=0.525, rely=0.3, relwidth=0.375)
        

        if flag==1:
            #limpar
            self.bt_limpar_cadProd = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clear_screen_cadProd)
            self.bt_limpar_cadProd.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
            #enviar
            self.bt_enviar_cadProd = Button(self.frame_1, text="Enviar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.add_prod(), self.root3.destroy()])
            self.bt_enviar_cadProd.place(relx=0.7, rely=0.7, relwidth=0.15, relheight=0.1)
        elif flag==2:
            #limpar
            self.bt_limpar_cadProd = Button(self.frame_1, text="Limpar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=self.clear_screen_cadProd)
            self.bt_limpar_cadProd.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.1)
            #change
            self.bt_change_cadProd = Button(self.frame_1, text="Alterar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.change_prod(aux), self.root3.destroy()])
            self.bt_change_cadProd.place(relx=0.425, rely=0.7, relwidth=0.15, relheight=0.1)
            #apagar
            self.bt_apagar_cadProd = Button(self.frame_1, text="Apagar", bd=2, bg='#a4ac86', fg='black', font=('Verdana', 11), command=lambda:[self.delete_prod(), self.root3.destroy()])
            self.bt_apagar_cadProd.place(relx=0.7, rely=0.7, relwidth=0.15, relheight=0.1)
    

