
CREATE TABLE autores (
    id_autor PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
 );

DROP TABLE autores;
 INSERT INTO autores (id_autor, nome, nacionalidade) VALUES (1,'Messi', 'Argentino');

  INSERT INTO autores (id_autor, nome, nacionalidade) VALUES (2,'Cristiano', 'Portugues');

  CREATE TABLE livros ( id_livro PRIMARY KEY,
   titulo TEXT NOT NULL,
    ano_publicacao INTEGER,
     id_autor INTEGER, FOREIGN KEY(id_autor) REFERENCES autores (id_autor) );


INSERT INTO livros ( id_livro, titulo, ano_publicacao, id_autor) VALUES ( )