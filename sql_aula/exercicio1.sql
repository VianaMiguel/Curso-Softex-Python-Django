CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha INTEGER
);

INSERT INTO usuarios (primeiro_nome, email, senha)
 VALUES 
('Arthur', '@Arthur.com','Arthur123'),
('Caio', '@Caio.com','Caio123'),
('Ana', '@Ana.com','Ana123'),
('Mariana', '@Mariana.com','Mariana123'),
('Karen', '@Karen.com','Karen123');

CREATE TABLE postagem (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER
);

INSERT INTO postagem (titulo, postagem, id_autor)
VALUES
('Arthur no Futebol', 'foto', 1),
('Caio nadando', 'foto', 2),
('Ana dançando', 'foto', 3),
('Mariana lutando', 'foto', 4),
('Karen jogando', 'foto', 5)
;

SELECT * FROM usuarios;

SELECT * FROM postagem;

UPDATE usuarios SET  email = '@Caindo.com'  WHERE primeiro_nome = 'Caio';

UPDATE postagem SET titulo = 'Karen Ganhando' WHERE id_autor = 5;

DELETE FROM "postagem" WHERE "id" IN (6,7,8,9,10)

DELETE FROM "usuarios" WHERE "id" IN (6,7,8,9,10)