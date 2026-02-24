from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database
from datetime import datetime


#classe que representa uma tarefa do sistema
class Tarefa:
    """
    Representa uma tarefa e possui métodos para salvar,
    buscar, atualizar e excluir no banco de dados.
    """

    #construtor: define os dados da tarefa
    def __init__(self: Self, 
                 titulo_tarefa: Optional[str], 
                 data_conclusao: Optional[str] = None, 
                 id_tarefa: Optional[int] = None, 
                 concluida: int = 0, 
                 data_hora_conclusao: Optional[str] = None) -> None:
        
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao
        self.id_tarefa = id_tarefa
        self.concluida = concluida
        self.data_hora_conclusao = data_hora_conclusao
    

    #busca uma tarefa pelo ID no banco
    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query = '''
                SELECT titulo_tarefa, data_conclusao, concluida, data_hora_conclusao 
                FROM tarefas WHERE id = ?;
            '''
            resultado = db.buscar_tudo(query, (id,))

            #pega os dados do banco
            [[titulo, data, concluida, data_h]] = resultado

        return cls(id_tarefa=id, 
                   titulo_tarefa=titulo, 
                   data_conclusao=data, 
                   concluida=concluida, 
                   data_hora_conclusao=data_h)


    #salva uma nova tarefa no banco
    def salvar_tarefa(self) -> None:
        with Database() as db:
            query = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            db.executar(query, (self.titulo_tarefa, self.data_conclusao))


    #retorna todas as tarefas cadastradas
    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query = '''
                SELECT titulo_tarefa, data_conclusao, id, concluida, data_hora_conclusao 
                FROM tarefas;
            '''
            resultados = db.buscar_tudo(query)

            #cria uma lista de objetos Tarefa
            tarefas = [cls(r[0], r[1], r[2], r[3], r[4]) for r in resultados]
            return tarefas


#alterna o status
    def alternar_status(self) -> None:
        novo_status = 1 if self.concluida == 0 else 0




        #se der certo ele salva data e hora atual
        agora = datetime.now().strftime("%d/%m/%Y %H:%M") if novo_status == 1 else None

        with Database() as db:
            query = '''
                UPDATE tarefas 
                SET concluida = ?, data_hora_conclusao = ? 
                WHERE id = ?;
            '''
            db.executar(query, (novo_status, agora, self.id_tarefa))


    #exclui a tarefa do banco
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query = 'DELETE FROM tarefas WHERE id = ?;'
            return db.executar(query, (self.id_tarefa,))


    #atualiza título e data da tarefa
    def atualizar_tarefas(self) -> Cursor:
        with Database() as db:
            query = '''
                UPDATE tarefas 
                SET titulo_tarefa = ?, data_conclusao = ? 
                WHERE id = ?;
            '''
            return db.executar(query, 
                               (self.titulo_tarefa, 
                                self.data_conclusao, 
                                self.id_tarefa))
            
