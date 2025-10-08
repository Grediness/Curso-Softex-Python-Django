-- CREATE Table aluno(
--     id INTEGER PRIMARY KEY,
--     nome TEXT not NULL
-- );
-- CREATE Table cursos(
--     id INTEGER PRIMARY KEY,
--     titulo TEXT not NULL
-- );

-- CREATE TABLE aluno_cursos(
--     id_aluno INTEGER NOT NULL,
--     id_curso INTEGER NOT NULL,
--     Foreign Key (id_aluno) REFERENCES aluno(id)
--     Foreign Key (id_curso) REFERENCES cursos(id)
-- );


-- INSERT INTO aluno(nome) VALUES ('Pedro'),('Michele'),('Rafael'),('Carol');
-- INSERT INTO cursos(titulo) VALUES ('back-end'),('front-end');
-- INSERT INTO aluno_cursos(id_aluno,id_curso) VALUES (1,1),(1,2),(2,1),(3,1);

-- SELECT A.nome,C.titulo from aluno A
-- INNER JOIN aluno_cursos as AC on AC.id_aluno=A.id
-- INNER JOIN cursos as C on AC.id_curso=C.id;       
-- SELECT count(A.nome),C.titulo from aluno A
-- INNER JOIN aluno_cursos as AC on AC.id_aluno=A.id
-- INNER JOIN cursos as C on AC.id_curso=C.id  
-- GROUP BY C.titulo;
-- SELECT count(A.nome),C.titulo from aluno A
-- INNER JOIN aluno_cursos as AC on AC.id_aluno=A.id
-- INNER JOIN cursos as C on AC.id_curso=C.id  
-- GROUP BY C.titulo
-- HAVING count(A.nome)>2;

-- EXERCICIOS
--1)

CREATE TABLE autores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);
CREATE TABLE livros(
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    id_autor INTEGER,
    Foreign Key (id_autor) REFERENCES autores(id)
);

DROP Table livros;

INSERT INTO autores(nome,nacionalidade) VALUES('João Roberto','Europeu'),('Adriana','Indiana');
INSERT INTO livros(titulo,ano_publicacao,id_autor) VALUES('Turma de Mônica',1900,1),('Marvel',2000,1),('DC',2015,1),
                                                         ('Star Wars',1000,2),('Indiana Jones',2020,2),('Alakazam',1950,2);

SELECT * from livros;

--2)
SELECT livros.titulo,
       autores.nome
FROM autores
INNER JOIN livros on id_autor=autores.id;

--3)
SELECT livros.titulo,
       autores.nome
FROM autores
INNER JOIN livros on id_autor=autores.id
WHERE nacionalidade='Britânica';

--4)
SELECT count(livros.titulo),
       autores.nome
FROM autores
INNER JOIN livros on id_autor=autores.id
GROUP BY autores.nome;