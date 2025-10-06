-- Active: 1759769973598@@127.0.0.1@3306
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

INSERT INTO alunos (nome, idade) VALUES ('João', 20);
INSERT INTO alunos (nome, idade) VALUES ('Maria', 22);

SELECT * FROM alunos;

SELECT nome, idade FROM alunos;

SELECT * FROM alunos WHERE idade = 20;

SELECT * FROM alunos WHERE nome = 'Maria' AND idade = 22;

UPDATE alunos SET idade = 21 WHERE nome = 'João';

-- Comentario = para comentar use o -- Traço Traço 

/* Comentario = /*  Tem que ficar entre barras */

DELETE FROM alunos WHERE nome = 'Maria';
-- Sempre usar Where para não apagar todos os dados e escolher os dados especificos 

