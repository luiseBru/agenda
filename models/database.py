from sqlite3 import Connection, connect, Cursor
from typing import Any, Optional, Self, Type
from types import TracebackType
from dotenv import load_dotenv
import traceback
import os

#procura arquivo .env com variaveis
load_dotenv()

#funcao para iniciar o banco de dados e criar a tabela de tarefa
DB_PATH = os.getenv('DATABASE', './data/tarefas.sqlite3')


#se nao existir tabela no banco ele cria
def init_db(db_name: str = DB_PATH) -> None:
    with connect(db_name) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo_tarefa TEXT NOT NULL,
                data_conclusao TEXT,
                concluida INTEGER DEFAULT 0,
                data_hora_conclusao TEXT
            );
        """)


class Database:
    """
    Classe que cuida da conexão com o banco SQLite
    e executa comandos SQL.
    """

    #conexão com o banco
    def __init__(self, db_name: str = DB_PATH) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()
        

    #executa insert, update e delete
    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    

    #executa select e retorna todos os resultados
    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    

    
#conexao do banco fecha
    def close(self) -> None:
        self.connection.close()
    

    #usa with Database() as db:
    def __enter__(self) -> Self:
        return self
    

    #ele fecha automaticamente a conexao mesmo se der erro
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        if exc_type is not None:
            print("Exceção capturada no contexto:")
            print(f"Tipo: {exc_type.__name__}")
            print(f"Mensagem: {exc_value}")

        self.close()