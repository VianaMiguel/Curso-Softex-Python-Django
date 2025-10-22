
# user_service.py
import sqlite3
from user_model import UserModel
from hasher import hash_senha, verificar_senha
from datetime import datetime
from database import DatabaseConnection


class UserService:

    def __init__(self):
       self.user_model = UserModel

    def _safe_user_data(self, user) -> dict | None:

        if user:
            return{
                'id': user['id'],
                'email': user['email'],
                'nome_completo': user['nome_completo'],
                'perfil_acesso': user['perfil_acesso'],
                'data_criacao': user['data_criacao'],
                'data_atualizacao': user['data_atualizacao']
            }
        else:
            return None

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        if current_user_id == 'Diretoria':
            return True
        if not targe_user_id:
            return False
        
    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        
        senha_hash =
        """
        Método para criar um usuários.
        o campo senha deve ter no mínimo 8 caracteres, caso contrário retorne False a mensagem de erro.
        O campo email deve ter pelo menos 10 caracteres, uma @ e terminar com .com, retorne False se não tiver e a mensagem de erro.
        O campo Nome deve ter apenas letras e não deve estar vazio, retorne False se não tiver e a mensagem de erro.
        Caso os campos atendas as requisições, faça o hash da senha e salve use o método create_user da User Model
        """

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Este método é o login do usuários, deve receber um email e senha não vazios
        Use o método do find_user_by_email para buscar o usuario
        Se houver usuarios faça a comparação da senha passada com a senha hash do DB
        Use a função verificar_senha, se tiver ok, retorn o usuarios pelo método privado _safe_user_data
        e a mensagem Login bem-sucedido!.
        Caso contrario retorne None e a mensagem de erro
        """

        def update_user_profile(
            self,
            current_user_id: int | None,
            current_user_profile: str,
            target_user_id: int,
            new_data: dict,
        ) -> tuple[bool, str]:
            
            if not self._is_autorized(current_user_id, current_user_profile, target_user_id)
                return False, "acesso Negado!"
            update_data ={}

            self.db_conn.connect()
            updates = []
            params = []

            if updates_data.get("senha_hash"):
                updates.append("senha_hash = ?")
                params.append(updates_data["senha_hash"])
            if updates_data.get("email"):
                updates.append("email = ?")
                params.append(updates_data["email"])
            if updates_data.get("nome_completo"):
                updates.append("nome_completo = ?")
                params.append(updates_data["nome_completo"])

            if not updates:
                self.db_conn.close()
                return False, "Nenhum dado válido para atualizar."

            updates.append("data_atualizacao = ?")
            params.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            params.append(user_id)

            query_updates_str = ", ".join(updates)
            query = f"UPDATE usuarios SET {query_updates_str} WHERE id = ?;"

            try:
                self.db_conn.cursor.execute(query, params)
                rows_affected = self.db_conn.cursor.rowcount
                self.db_conn.close()
                if rows_affected > 0:
                    return True, "Usuário atualizado com sucesso!"
                return False, "Usuário não encontrado."
            except sqlite3.IntegrityError:
                self.db_conn.close()
                return False, f"Erro: O e-mail já está em uso por outro usuário."
            except Exception as e:
                self.db_conn.close()
                return False, f"Erro desconhecido: {e}"

        def delete_user(
            self,
            current_user_profile: str,
            user_id: int,
        ) -> tuple[bool, str]:
            self.db_conn.connect()
            self.db_conn.cursor.execute("DELETE FROM usuarios WHERE id = ?;", (user_id,))
            rows_affected = self.db_conn.cursor.rowcount
            self.db_conn.close()
            if rows_affected > 0:
                return True, "Usuário deletado com sucesso!"
            return False, "Usuário não encontrado."

        def get_user_by_id(self, user_id: int) -> dict | None:
            self.db_conn.connect()
            self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (user_id,))
            course = self.db_conn.cursor.fetchone()
            self.db_conn.close()
            return course
        def get_all_users(self) -> list[dict | None]:
            self.db_conn.connect()
            self.db_conn.cursor.execute("SELECT * FROM usuarios;")
            courses = self.db_conn.cursor.fetchall()
            self.db_conn.close()
            return usuarios