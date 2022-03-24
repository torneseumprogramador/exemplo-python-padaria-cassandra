from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["alunas_accenture"]

alunos_collection = db["alunos"]
alunos = alunos_collection.find()

for aluno in alunos:
  print("---------------")
  print(f"Nome: {aluno['nome']}")
  print(f"Matricula: {str(aluno['matricula'])}")

#https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

'''
db.pedidos.insert(
  {
    valorTotal: 275000,
    data: new Date(2011, 04, 01, 00, 00, 00)
    itens: [
      {
        nome: "Jeta",
        valorUnidade: 25000,
        quantidade: 1
      },
      {
        nome: "Evoc",
        valorUnidade: 250000,
        quantidade: 1
      }
    ],
    cliente: {
      nome: "Danilo",
      email: "danilo@torneseumprogramador.com.br",
      telefone: "(11)11111-1111"
    }
  }
)
'''


"""
fazer um programa de padaria, utilizando o banco de dados mongodb
teremos as seguintes coleções
produtos{
  _id,
  nome,
  descricao
  data_validade
  ranking: int
  padeiro_id
}
padeiros{
  _id,
  nome,
  ranking: int
}

relatório dos melhores padeiros
relatório dos melhores produtos

menu de cadastro, exemplo:
O que vc deseja fazer?
1 - cadastrar produto
2 - cadastrar padeiro
3 - listar ranking dos padeiros
4 - lista ranking dos produdos (mostrando o nome do padeiro que fez o produto)

"""