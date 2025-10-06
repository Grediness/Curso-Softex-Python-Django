CREATE Table alunos(
    id INTEGER PRIMARY KEY,
    nome TEXT not NULL,
    idade INTEGER
);

INSERT INTO alunos(nome,idade) VALUES('João',20);
INSERT INTO alunos(nome,idade) VALUES('Maria',22);
INSERT INTO alunos(nome,idade) VALUES('Pedro',19);
SELECT * from alunos;
SELECT * from alunos WHERE id=2;
UPDATE alunos SET idade = 21 WHERE nome='João';
DELETE FROM alunos WHERE nome='Maria';