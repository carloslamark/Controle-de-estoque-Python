import json_manager as json


def startClients():
    jmanager = json.JsonManagerClient()
    return jmanager.read_json('data/clients.json')


def startProducts():
    jmanager = json.JsonManagerProd()
    return jmanager.read_json('data/product.json')


def registerProd():
    # produto, quantidade, valorSemDesconto, valorComDesconto
    pAux = ["", 0, 0.0, 0.0]
    code = input("Código: ")
    pAux[0] = input("Produto: ")
    pAux[1] = int(input("Quantidade: "))
    pAux[2] = float(input("Valor SEM desconto: "))
    pAux[3] = float(input("Valor COM desconto: "))
    dictProd[code] =  pAux
    
    jmanager = json.JsonManagerProd()
    jmanager.create_json('data/product.json', dictProd)
    

def showProd(prod):
    print(prod)


def registerClient(prod):
    x = 1  
    # telefone, endereço, cpf, nomeDaMãe, email, listaDeCodigoProdutos, valorTotalPagar
    cAux = ["", "", "", "", "", [], 0]
    name = input("Nome do Cliente: ")
    cAux[0] = input("Telefone: ")
    cAux[1] = input("Endereço: ")
    cAux[2] = input("CPF: ")
    cAux[3] = input("Nome da Mãe: ")
    cAux[4] = input("Email: ")
    while x != 2:
        x = int(input("\n\n[1]Adicionar um produto\n[2]Sair\n"))  
        if x == 1:
            cod = int(input("Código do produto: "))
            while prod.get(cod) == None:
                cod = int(input("Código inválido! Digite outro ou 0 para sair: "))
            
            qProd = prod[cod][1]
            print("Quantidade Disponível: " + str(qProd))
            q = int(input("Quantidade do Produto: "))
            
            while q > qProd:
                print("Quantidade Excedeu!")
                q = int(input("Digite outra quantidade: "))

            flag = int(input("[1]Sem Desconto\n[2]Com Desconto\n"))
            if flag == 1:
                cAux[6] += prod[cod][2]*q
            elif flag == 2:
                cAux[6] += prod[cod][3]*q
            prod[cod][1] -= q
            cAux[5].append(cod)
    dictClients[name] = cAux

    jmanager = json.JsonManagerClient()
    jmanager.create_json('data/clients.json', dictClients)
    jmanager = json.JsonManagerProd()
    jmanager.create_json('data/product.json', dictProd)
    

def showClients(clients):
    print(clients)  

def addProdClient(clients, prod):
    x = 1
    while x != 2:
        x = int(input("\n\n[1]Adicionar um produto\n[2]Sair\n"))  
        if x == 1:
            showClients(clients)
            nameClient = input("\nNome do Cliente: ")
            cod = input("Código do produto: ")
            while prod.get(cod) == None:
                cod = int(input("Código inválido! Digite outro ou 0 para sair: "))
            
            qProd = prod[cod][1]
            print("Quantidade Disponível: " + str(qProd))
            q = int(input("Quantidade do Produto: "))
            
            while q > qProd:
                print("Quantidade Excedeu!")
                q = int(input("Digite outra quantidade: "))

            flag = int(input("[1]Sem Desconto\n[2]Com Desconto\n"))
            if flag == 1:
                clients[nameClient][6] += prod[cod][2]*q
            elif flag == 2:
                clients[nameClient][6] += prod[cod][3]*q
            prod[cod][1] -= q
            clients[nameClient][5].append(cod)
    jmanager = json.JsonManagerClient()
    jmanager.create_json('data/clients.json', dictClients)
    jmanager = json.JsonManagerProd()
    jmanager.create_json('data/product.json', dictProd)





aux = 0
dictProd = {}
dictClients = {}
dictProd = startProducts()
dictClients = startClients()


while aux != 6:
    print("[1] para cadastrar produto\n")
    print("[2] para mostrar produto\n")
    print("[3] para cadastrar cliente\n")
    print("[4] para mostrar cliente\n")
    print("[5] para adicionar produto ao cliente\n")
    print("[6] sair")
    aux = int(input())


    if aux == 1:
        registerProd()
    elif aux == 2:
        showProd(dictProd)
    elif aux == 3:
        registerClient(dictProd) 
    elif  aux == 4:
        showClients(dictClients)
    elif aux == 5:
        addProdClient(dictClients, dictProd)

# removerProduto
# editarProduto
# removerCliente
# editarCliente
        

