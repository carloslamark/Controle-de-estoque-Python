import json_manager as json


def startClients():
    return jmanagerC.read_json('data/clients.json')


def startProducts():
    return jmanagerP.read_json('data/product.json')


def registerProd(prod):
    # produto, quantidade, valorSemDesconto, valorComDesconto
    pAux = ["", 0, 0.0, 0.0]
    code = input("Código: ")
    pAux[0] = input("Produto: ")
    pAux[1] = int(input("Quantidade: "))
    pAux[2] = float(input("Valor SEM desconto: "))
    pAux[3] = float(input("Valor COM desconto: "))
    prod[code] =  pAux
    
    jmanagerP.create_json('data/product.json', prod)
    

def showProd(prod):
    print(prod)


def registerClient(clients, prod):
    x = 1  
    # telefone, endereço, cpf, nomeDaMãe, email, listaDeCodigoProdutos, valorTotalPagar
    cAux = ["", "", "", "", "", [], 0]
    name = input("Nome do Cliente: ")
    cAux[0] = input("Telefone: ")
    cAux[1] = input("Endereço: ")
    cAux[2] = input("CPF: ")
    cAux[3] = input("Nome da Mãe: ")
    cAux[4] = input("Email: ")
    #data de nascimento
    clients[name] = cAux
    addProdClient(clients, prod, 1, name)

    jmanagerC.create_json('data/clients.json', clients)
    jmanagerP.create_json('data/product.json', prod)
    

def showClients(clients):
    print(clients)  


def addProdClient(clients, prod, num, name):
    x = 1
    if num == 1:
        while x != 2:
            x = int(input("\n\n[1]Adicionar um produto\n[2]Sair\n"))  
            if x == 1:            
                showProd(prod) 
                cod = checkProd(prod) 
                
                qProd = prod[cod][1]
                print("Quantidade Disponível: " + str(qProd))
                q = int(input("Quantidade do Produto: "))
                
                while q > qProd:
                    print("Quantidade Excedeu!")
                    q = int(input("Digite outra quantidade: "))

                flag = int(input("[1]Sem Desconto\n[2]Com Desconto\n"))
                if flag == 1:
                    clients[name][6] += prod[cod][2]*q
                elif flag == 2:
                    clients[name][6] += prod[cod][3]*q
                prod[cod][1] -= q
                clients[name][5].append(cod)
    else:
        while x != 2:
            x = int(input("\n\n[1]Adicionar um produto\n[2]Sair\n"))  
            if x == 1:
                showClients(clients)
                name = checkClient(clients)
                print("\n\n")

                showProd(prod)
                cod = checkProd(prod)
                
                qProd = prod[cod][1]
                print("Quantidade Disponível: " + str(qProd))
                q = int(input("Quantidade do Produto: "))
                
                while q > qProd:
                    print("Quantidade Excedeu!")
                    q = int(input("Digite outra quantidade: "))

                flag = int(input("[1]Sem Desconto\n[2]Com Desconto\n"))
                if flag == 1:
                    clients[name][6] += prod[cod][2]*q
                elif flag == 2:
                    clients[name][6] += prod[cod][3]*q
                prod[cod][1] -= q
                clients[name][5].append(cod)


def removeProd(prod):
    cod = checkProd(prod)
    del prod[cod]
    jmanagerP.create_json('data/product.json', prod)


def editProd(prod):
    cod = checkProd(prod)
    prod[cod][0] = input("Produto: ")
    prod[cod][1] = int(input("Quantidade: "))
    prod[cod][2] = float(input("Valor SEM desconto: "))
    prod[cod][3] = float(input("Valor COM desconto: "))
    jmanagerP.create_json('data/product.json', prod)


def removeClient(clients):
    name = checkClient(clients)
    del clients[name]
    jmanagerC.create_json('data/clients.json', clients)


def editClient(clients, prod):
    showClients(clients)
    name = checkClient(clients)
    clients[0] = input("Telefone: ")
    clients[1] = input("Endereço: ")
    clients[2] = input("CPF: ")
    clients[3] = input("Nome da Mãe: ")
    clients[4] = input("Email: ")
    flag = int(input("\n[1] Mudar Produtos Comprados\n[2] Não mudar nada\n"))
    if flag == 1:
        addProdClient(clients, prod, 1, name)

    jmanagerC.create_json('data/clients.json', clients)
    jmanagerP.create_json('data/product.json', prod)

def checkProd(prod):
    cod = input("Código do produto: ")
    while prod.get(cod) == None:
        cod = input("Código inválido! Digite outro ou 0 para sair: ")
    return cod


def checkClient(clients):
    name = input("Nome do cliente: ")
    while clients.get(name) == None:
        name = input("Nome inválido! Digite outro ou 0 para sair: ")
    return name


jmanagerC = json.JsonManagerClient()
jmanagerP = json.JsonManagerProd()