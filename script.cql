CREATE KEYSPACE IF NOT EXISTS padaria WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };

CREATE TABLE padeiros ( 
  id UUID, rating int, nome text,
  primary key((id), rating, nome)
) WITH CLUSTERING ORDER BY (rating desc, nome asc);

CREATE TABLE produtos ( 
  id UUID, rating int, nome text,
  descricao text, padeiro_id uuid,
  data_validade date,
  primary key((id), rating, nome, padeiro_id)
) WITH CLUSTERING ORDER BY (rating desc, nome asc, padeiro_id asc);


CREATE INDEX busca_nome_padeiro ON padeiros (nome);
