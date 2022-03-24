
from datetime import datetime
from time import sleep
from cassandra.cluster import Cluster
import uuid

cluster = Cluster(['0.0.0.0'],port=9042)
db = cluster.connect('padaria', wait_for_all_pools=True)

def cadastrarpadeiro():
    padeiro = {}
    padeiro["nome"] = input("\nDigite o nome do padeiro: ")
    while True:
        rating = int(input("Insira a avaliação do padeiro, de 1 a 10: "))
        if rating in range (1,11):
            padeiro["rating"] = rating
            break
        else:
            print("\nValor inválido. Insira um valor de 1 a 10.\n")
            sleep(1)
    
    db.execute(f"insert into padeiros(id, nome, rating)values({uuid.uuid4()}, '{padeiro['nome']}', {padeiro['rating']});")

def cadastrarproduto():
    produto = {}
    produto["nome"] = input("\nDigite o nome do produto: ")
    produto["descricao"] = input("Digite a descrição do produto: ")
    while True:
        data = input("Digite a data de validade do produto no formato dd/mm/aaaa: ")
        data = data.split("/")
        try:
            produto["data_validade"] = f"{data[2]}-{data[1]}-{data[0]}"
            break
        except:
            print("\nData inválida!\n")
            sleep(1)
    while True:
        rating = int(input("Insira a avaliação do produto, de 1 a 10: "))
        if rating in range (1,11):
            produto["rating"] = rating
            break
        else:
            print("\nValor inválido!\n")
            sleep(1)
    while True:
        padeiro = input("Digite o nome do padeiro que o produziu: ")
        try:
            print(f"select * from padeiros where nome = '{padeiro}'")
            padeiro_doc = db.execute(f"select * from padeiros where nome = '{padeiro}'").one()
            produto["padeiro_id"] = padeiro_doc.id
            break
        except:
            print("\nNome de padeiro inválido!\n")
            sleep(1)  
            
    db.execute(f"insert into produtos(id, nome, rating, padeiro_id, data_validade, descricao)values({uuid.uuid4()}, '{produto['nome']}', {produto['rating']}, {produto['padeiro_id']}, '{produto['data_validade']}', '{produto['descricao']}');")


def listarpadeiros():
    qtd_padeiros = db.execute(f"select count(1) as qtd from padeiros").one()

    if qtd_padeiros.qtd == 0:
        print("\nNão há padeiros cadastrados!\n")
        sleep(1)
    else:
        print("\nrating dos padeiros:\n")
        for doc in db.execute(f"select * from padeiros"):
            print(f"Nome: {doc.nome}")
            print(f"Rating: {doc.rating}")
            print("-----------------")


def listarprodutos():
    qtd_produtos = db.execute(f"select count(1) as qtd from produtos").one()
    if qtd_produtos.qtd == 0:
        print("\nNão há produtos cadastrados!\n")
        sleep(1)
    else:
        print("\nrating dos produtos:\n")
        for doc in db.execute(f"select * from produtos"):
            padeiro_doc = db.execute(f"select * from padeiros where id = {doc.padeiro_id}").one()
            print(f"Nome: {doc.nome}")
            print(f"Descrição: {doc.descricao}")            
            print(f"Data de Validade: {doc.data_validade}")
            print(f"Rating: {doc.rating}")
            print(f"Padeiro: {padeiro_doc.nome}")
            print("-----------------")    

while True:
    print("\nO que você deseja fazer?")
    print("1 - Cadastrar produto")
    print("2 - Cadastrar padeiro")
    print("3 - Listar rating dos padeiros")
    print("4 - Listar rating dos produtos")
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
