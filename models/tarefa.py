from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database
from datetime import datetime

class Tarefa:
    """
        Classe para representar uma tarefa, com métodos para salvar, obter, excluir e atualizar 
        tarefas em um banco de dados usando a classe 'Database'.
    """
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None, id_tarefa:Optional[int] = None, concluida: int = 0, data_hora_conclusao: Optional[str] = None)-> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str]  = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa
        self.concluida: int = concluida
        self.data_hora_conclusao: Optional[str] = data_hora_conclusao
 
    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, concluida, data_hora_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
 
            #desenpacotamento de coleção
            [[titulo, data, concluida, data_h]] = resultado
 
        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, concluida=concluida, data_hora_conclusao=data_h)

    def salvar_tarefa(self: Self)-> None:
        with Database() as db:
            query: str = " INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)
 
    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, id, concluida, data_hora_conclusao FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Any] = [cls(r[0], r[1], r[2], r[3], r[4]) for r in resultados]
            return tarefas

    def alternar_status(self) -> None:
        # RF03 e RF04: Inverte o status e registra data/hora
        novo_status = 1 if self.concluida == 0 else 0
        agora = datetime.now().strftime("%d/%m/%Y %H:%M") if novo_status == 1 else None
        with Database() as db:
            query: str = 'UPDATE tarefas SET concluida = ?, data_hora_conclusao = ? WHERE id = ?;'
            db.executar(query, (novo_status, agora, self.id_tarefa))

    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado

    def atualizar_tarefas(self) -> Cursor:
           with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ? WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado

            
