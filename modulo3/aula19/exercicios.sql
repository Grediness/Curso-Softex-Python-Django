CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    primeiro_nome  TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);
CREATE TABLE postagens(
    id INTEGER PRIMARY KEY,
    titulo  TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER NOT NULL
);

INSERT INTO usuarios(primeiro_nome,sobrenome,email,senha) VALUES('Pedro','Defanti','pedrodefanti8@gmail.com','123456789');
INSERT INTO usuarios(primeiro_nome,sobrenome,email,senha) VALUES('Lucas','Cravo','abc@gmail.com','987654321');
INSERT INTO usuarios(primeiro_nome,sobrenome,email,senha) VALUES('Bianca','Cruz','bianquinga@gmail.com','qwertyuiop');
INSERT INTO usuarios(primeiro_nome,sobrenome,email,senha) VALUES('Ana','Pardo','anaclaropardo@gmail.com','QqAaZzXxSsWw');
INSERT INTO usuarios(primeiro_nome,sobrenome,email,senha) VALUES('julia','mattos','mattosjulia@gmail.com','ZxCVbnM');
INSERT INTO postagens(titulo,postagem,id_autor) VALUES('A criação do crud','CRUDIZADA','ADOLETA');
INSERT INTO postagens(titulo,postagem,id_autor) VALUES('A morte do crud','AAAAAAAAHHHHH','borboletinha ta na cozinha');
INSERT INTO postagens(titulo,postagem,id_autor) VALUES('fazendo chocolate','para a madrinha','peti-éti');
INSERT INTO postagens(titulo,postagem,id_autor) VALUES('olho','de','vivro');
INSERT INTO postagens(titulo,postagem,id_autor) VALUES('E nariz','de coisas','AAAAAAAAA');

SELECT * FROM postagens;
SELECT * FROM usuarios;
SELECT * FROM usuarios WHERE id=2;

DROP Table usuarios;
