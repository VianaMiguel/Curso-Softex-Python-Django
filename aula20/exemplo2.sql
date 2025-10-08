CREATE TABLE  alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL);

 CREATE TABLE curso ( id INTEGER PRIMARY KEY, titulo TEXT NOT NULL);

 CREATE TABLE alunos_cursos (
        id_aluno INTEGER,
        id_curso INTEGER,
        FOREIGN KEY (id_aluno) REFERENCES alunos(id),
        FOREIGN KEY (id_curso) REFERENCES cursos(id)
    );

INSERT INTO alunos(nome) VALUES ('Paulo'), ('Mara'), ('Andre'), ('Carla');

SELECT * FROM cursos;

INSERT INTO alunos_cursos (id_aluno, id_curso) VALUES (1,1),(1,2),(2,1),(3,1),(4,1),(4,2);

SELECT * FROM  alunos_cursos;

SELECT alunos.nome, cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id;

SELECT count(*) FROM alunos_cursos where id_aluno = 1;








SELECT 
A.nome AS nome_aluno,
C.titulo AS titulo_curso
FROM
alunos AS A
INNER JOIN alunos_cursos AS AC ON A.id = AC.id_aluno 
INNER JOIN cursos AS AC ON AC A.id_curso = C.id;