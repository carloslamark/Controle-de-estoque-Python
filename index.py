import functions as func


aux = 0
dictProd = {}
dictClients = {}
dictProd = func.startProducts()
dictClients = func.startClients()



    


while aux != 10:
    print("[1] para cadastrar produto\n")
    print("[2] para mostrar produto\n")
    print("[3] para cadastrar cliente\n")
    print("[4] para mostrar cliente\n")
    print("[5] para adicionar produto ao cliente\n")
    print("[6] para remover produto\n")
    print("[7] para editar produto\n")
    print("[8] para remover cliente\n")
    print("[8] para editar cliente\n")
    print("[10] sair")
    aux = int(input("--> "))


    if aux == 1:
        func.registerProd(dictProd)
    elif aux == 2:
        func.showProd(dictProd)
    elif aux == 3:
        func.registerClient(dictClients, dictProd) 
    elif  aux == 4:
        func.showClients(dictClients)
    elif aux == 5:
        func.addProdClient(dictClients, dictProd, 2, None)
    elif aux == 6:
        func.removeProd(dictProd)
    elif aux == 7:
        func.editProd(dictProd)
    elif aux == 8:
        func.removeClient(dictClients)
    elif aux == 9:
        func.editClient(dictClients, dictProd)





        

