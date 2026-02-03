from flask import Flask, render_template, request
from models.tarefa import Tarefa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo='home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='agenda', tarefa=tarefas)

@app.route('/delite/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa,id(idTarefa)
    tarefa.excluir_tarefa()

@app.route('/ola')
def ola_mundo():
    return "Ola, mundo"