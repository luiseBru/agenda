# Agenda em python usando Flask

este projeto foi elaborado para permitir o aprendizado de conceito como o padrão de objeto MVC (Model-View-Controller), framework Flask e seus componentes, váriaveis de ambiente, paradigma de programação orientado a objetois e reforço de fundamentos da linguagem de programação Python.

Para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork deste repositório, clicando no botão `fork`

2. Clone este repositótio localmente:

~~~bash
git clone <url_seu_repositorioo>
~~~

3. Abra o projeto utilizando seu IDE preferido

4. Crie, preferencialmente, um ambiente virtual utilizando uma versão do Python >3.12.10

~~~bash
python -m venv .venv
~~~

5. Ativew seu ambiente virtual.

    No bsah:

    ~~~bash
    source .venv/Scripts/activate
    ~~~

    No PowerShell:
    ~~~powershell
    .\.venv\Scripts\Activate.ps1
    ~~~


6. Intale todas as dependencias constantes no `requirements.txt`:

    ~~~python
    pip install -r requeriments.txt
    ~~~

7. Copie o arquivo `.env.example`, cole na raiz do projeto e renomeie a cópia para `.env`,

8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Exemplo:

~~~env
DATABASE='./data/meubanco.db'
~~~

9. Rode a aplicação no Python utilizando o comando:

~~~bash
flas run
~~~

10. Acesse a aplicação no endereço e prota indicados no terminal. Exemplo:
`http://127.0.0.1:5000`