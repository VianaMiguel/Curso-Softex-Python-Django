CREATE TABLE professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE  alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    FOREIGN KEY (id_professor)REFERENCES professor(id));


DROP TABLE alunos; -- apaga a tabela e todo seu conteudo

INSERT INTO professores(nome) VALUES ('Anderson'),('Paulo');

SELECT * FROM professores; -- Select para mostrar a coluna dos alunos

INSERT INTO alunos (nome, id_professor) VALUES ('Pedro', 1), ('Maria',2), ('José', 1);

SELECT * FROM alunos;

-- DELETE FROM alunos WHERE id BETWEEN 1 AND 9; apaga por intervalos 

SELECT id AS Identificador, nome, id_professor AS Registro_Professor FROM alunos;

SELECT alunos.nome AS Nome_aluno, professores.nome AS Nome_Professor From alunos INNER JOIN professores on alunos.id =  professores.id;  -- O INNER JOIN é o comando que junta as informações de duas ou mais tabelas.
