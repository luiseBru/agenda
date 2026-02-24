from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.tarefa import Tarefa
from models.database import init_db

app = Flask(__name__)

#inicia o banco de dados
init_db()


@app.route('/')
def home():
    #abre a pagina inicial
    return render_template('home.html', titulo='Home')


@app.route('/agenda', methods=['GET', 'POST'])
def agenda():

    #se o formulario for enviado
    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data = request.form['data-conclusao']
        
        #cria e salva nova tarefa
        nova_tarefa = Tarefa(titulo, data)
        nova_tarefa.salvar_tarefa()
        
        return redirect(url_for('agenda'))

    #busca todas as tarefas
    lista = Tarefa.obter_tarefas()

    return render_template('agenda.html', titulo='Agenda', tarefas=lista, tarefa_selecionada=None)


@app.route('/status/<int:idTarefa>', methods=['POST'])
def status(idTarefa):
    #alterna o status da tarefa, concluida/aberta
    tarefa = Tarefa.id(idTarefa)
    tarefa.alternar_status()
    return jsonify(sucesso=True)


@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)

    #nao permite excluir se estiver concluida
    if tarefa.concluida == 1:
        return "<script>alert('Reabra a tarefa antes de excluir!'); window.location.href='/agenda';</script>"
    
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))


@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):

    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data = request.form['data-conclusao']

        #atualiza a tarefa no banco
        tarefa = Tarefa(titulo, data, id_tarefa=idTarefa)
        tarefa.atualizar_tarefas()
        return redirect(url_for('agenda'))
    
    #carrega dados para edição
    tarefa_edit = Tarefa.id(idTarefa)
    lista = Tarefa.obter_tarefas()

    return render_template('agenda.html', titulo='Editar', tarefa_selecionada=tarefa_edit, tarefas=lista)


if __name__ == '__main__':
    #executa a aplicação
    app.run(debug=True)