import sqlite3
from datetime import datetime
from database import DatabaseConnection


class BlogModel:

    def __init__(self):
        self.db_conn =  DatabaseConnection()
        self._create_table()

    def __create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
             """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL UNIQUE,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );
        """
        )
        self.db_conn.close()

    def create_post(self, titulo, conteudo):
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO usuarios (titulo, conteudo)
                    VALUES (?, ?);
                """,
                (titulo, conteudo)
        )
            print("Post criado com sucesso!") 
        except sqlite3.IntegrityError:
            print(f"Erro: O Conteudo 'conteudo'já está em uso.")
        finally:
            self.db_conn.close()
    def find_user_by_id(self, id_user):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;"(id_user))
        post = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return
        
    def find_usr_by_id(self, ser_id, titulo=None,email=None):
        pass
        

