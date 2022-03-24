
from pymongo import MongoClient
from datetime import datetime
from time import sleep

client = MongoClient("mongodb://localhost:27017")
db = client["padaria"]

produtos_collection = db["produtos"]
padeiros_collection = db["padeiros"]

def cadastrarpadeiro():
    padeiro = {}
    padeiro["nome"] = input("\nDigite o nome do padeiro: ")
    while True:
        ranking = int(input("Insira a avaliação do padeiro, de 1 a 10: "))
        if ranking in range (1,11):
            padeiro["ranking"] = ranking
            break
        else:
            print("\nValor inválido. Insira um valor de 1 a 10.\n")
            sleep(1)
    padeiros_collection.insert_one(padeiro)

def cadastrarproduto():
    produto = {}
    produto["nome"] = input("\nDigite o nome do produto: ")
    produto["descricao"] = input("Digite a descrição do produto: ")
    while True:
        data = input("Digite a data de validade do produto no formato dd/mm/aaaa: ")
        data = data.split("/")
        try:
            produto["data_validade"] = datetime(int(data[2]), int(data[1]), int(data[0]))
            break
        except:
            print("\nData inválida!\n")
            sleep(1)
    while True:
        ranking = int(input("Insira a avaliação do produto, de 1 a 10: "))
        if ranking in range (1,11):
            produto["ranking"] = ranking
            break
        else:
            print("\nValor inválido!\n")
            sleep(1)
    while True:
        padeiro = input("Digite o nome do padeiro que o produziu: ")
        try:
            padeiro_doc = padeiros_collection.find_one({"nome": padeiro}) 
            produto["padeiro_id"] = padeiro_doc["_id"]
            break
        except:
            print("\nNome de padeiro inválido!\n")
            sleep(1)  
    produtos_collection.insert_one(produto)


def listarpadeiros():
    if padeiros_collection.find_one() == None:
        print("\nNão há padeiros cadastrados!\n")
        sleep(1)
    else:
        print("\nRanking dos padeiros:\n")
        for doc in padeiros_collection.find().sort('ranking', -1):
            print(f"Nome: {doc['nome']}")
            print(f"Ranking: {doc['ranking']}")
            print("-----------------")


def listarprodutos():
    if produtos_collection.find_one() == None:
        print("\nNão há produtos cadastrados!\n")
        sleep(1)
    else:
        print("\nRanking dos produtos:\n")
        for doc in produtos_collection.find().sort('ranking', -1):
            padeiro_doc = padeiros_collection.find_one(doc['padeiro_id'])
            print(f"Nome: {doc['nome']}")
            print(f"Descrição: {doc['descricao']}")            
            print(f"Data de Validade: {doc['data_validade'].strftime('%d/%m/%y')}")
            print(f"Ranking: {doc['ranking']}")
            print(f"Padeiro: {padeiro_doc['nome']}")
            print("-----------------")    

while True:
    print("\nO que você deseja fazer?")
    print("1 - Cadastrar produto")
    print("2 - Cadastrar padeiro")
    print("3 - Listar ranking dos padeiros")
    print("4 - Listar ranking dos produtos")
    print("5 - Sair\n")

    opcao = int(input())
    if opcao == 5:
        break
    elif opcao == 1:
        cadastrarproduto()
    elif opcao == 2:
        cadastrarpadeiro()
    elif opcao == 3:
        listarpadeiros()
    elif opcao == 4:
        listarprodutos()
    else:
        print("\nEscolha uma opção válida!")
        sleep(1)
