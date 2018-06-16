from Client import Client
from Utils import Utils

def showMenu(lstOptions):
    if not(lstOptions):
        print("\nNenhum opção encontrada para este programa!")
        return

    print("\nOpções:")
    index = 0
    for option in lstOptions:
        print(" [{}] - {}" .format(index, option))
        index += 1

def getClientByEmail(database, email):
    for client in database:
        if(client.getEmail() == email):
            return client
    return False

def newClient(database, client):
    while not(client.setFirstName(input("\nInsira o seu primeiro nome: "))):
        print("\nNome inválido!")

    if(client.getEmail() == ""):
        while not(client.setEmail(input("\nInsira o seu e-mail: "))):
            print("\nFormato de e-mail inválido!")

    client.setEvaluation(input("\nEscreva uma breve avaliação do serviço: "))

    while not(client.setStars(int(input("\nQuantas estrelas o serviço merece? [0-5]: ")))):
        print("\nQuantidade inválida!")

    database.append(client)

def listEvaluations(database):
    if not(database):
        print("\nNenhuma avaliação cadastrada no banco de dados!")
        return

    print("\nClassificações:")
    index = 5
    while(index > -1):
        for client in database:
            if(client.getStars() == index):
                print("\n  {} estrelas:" .format(index))
                print("    Cliente: {}" .format(client.getFirstName()))
                print("    E-mail: {}" .format(client.getEmail()))
                print("    Avaliação: {}" .format(client.getEvaluation()))
                print("    Classificação automatica: {}" .format(client.getClassification()))
        index -= 1

def updateEvaluation(database):
    client = Client()

    while not(client.setEmail(input("\nDigite o seu e-mail: "))):
        print("\nFormato de e-mail inválido!")

    clientBackup = client
    client = getClientByEmail(database, client.getEmail())
    if not(client):
        question = input("\nNão existe um cliente com esse e-mail em nosso banco de dados! Gostaria de adicionar um agora? [s/n]: ")
        if(question == "s"):
            return newClient(database, clientBackup)
        else:
            return
    else:
        client.setEvaluation(input("\nEscreva uma breve avaliação do serviço: "))
        print("\nAvaliação editada com sucesso!")
        return

def showAvarage(database):
    if not(database):
        print("\nNenhuma avaliação cadastrada no banco de dados!")
        return

    lstAvarages = []
    for client in database:
        lstAvarages.append(client.getStars())
    print("\nA media do restaurante é {:.2f} estrela(s)" .format(sum(lstAvarages)/len(lstAvarages)))
    return

lstOptions = ["Novo cliente", "Mostrar avaliações", "Editar avaliação", "Avaliação media", "Sair"]
database = []

def menu(database):
    showMenu(lstOptions)
    option = Utils.getUserOption(0, len(lstOptions) - 1)

    if(option == -1):
        print("\nOpção inválida!")
        return menu()

    if(option == 0):
        client = Client()
        newClient(database, client)
    elif(option == 1):
        listEvaluations(database)
    elif(option == 2):
        updateEvaluation(database)
    elif(option == 3):
        showAvarage(database)
    elif(option == 4):
        return

    menu(database)

menu(database)

print("\nFim do programa!")