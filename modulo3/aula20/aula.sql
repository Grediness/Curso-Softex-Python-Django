CREATE Table professores(
    id INTEGER PRIMARY KEY,
    nome text NOT NULL
);
CREATE Table alunos(
    id INTEGER PRIMARY KEY,
    nome text NOT NULL,
    id_professor INTEGER,
    Foreign Key (id_professor) REFERENCES professores(id)
);

INSERT INTO professores(nome)VALUES('Pedro');
INSERT INTO professores(nome)VALUES('bruna');
INSERT INTO alunos(nome,id_professor)VALUES('carla',2);
INSERT INTO alunos(nome,id_professor)VALUES('bianca',2);

SELECT * from alunos;

SELECT alunos.nome as nome_aluno,
        professores.nome as nome_professor
FROM alunos
INNER JOIN professores ON alunos.id_professor=professores.id;





