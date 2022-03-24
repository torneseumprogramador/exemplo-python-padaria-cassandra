from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'],port=9042)
session = cluster.connect('alunas_accenture', wait_for_all_pools=True)
session.execute("insert into usuarios(id, nome, email, nascimento, nacionalidade, idade)values(e4b0cdae-aaff-11ec-b909-0242ac120001, 'Danilo1', 'danilo1@bmail.com', '1997-05-21', 'Brasileira', 25);")
rows = session.execute('SELECT * FROM usuarios')
for row in rows:
    print(row.id,row.nome,row.nacionalidade)