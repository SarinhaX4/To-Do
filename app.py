from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# lista vazia para armazenar as *tarefas*
tasks = []

# a rota principal da aplicação é:
@app.route('/')
def home():
    # renderizamos o template ('index.html') passando a lista de tarefas
    return render_template('index.html', tasks=tasks)

# Definimos a rota para adicionar uma nova tarefa. Ela só aceita o método POST.
@app.route('/add', methods=['POST'])
def add_task():
    # obtemos a tarefa do formulário enviado
    task = request.form.get('task')
    # verificamos se a tarefa não é vazia e adicionamos
    if task:
        tasks.append(task)  # o método correto é "append" em vez de "oppend"
        # caso seja vazio, redicionar a tela principal
        return redirect(url_for('home'))

# Definimos a rota para deletar uma tarefa. Ela aceita o método POST.
# O '<int:task_id>' na URL captura o índice da tarefa a ser deletada.
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # verificação se o índice é válido
    if 0 <= task_id < len(tasks):
        # Removemos a tarefa da lista com base no índice.
        del tasks[task_id]
    # redirecionamos para a tela principal
    return redirect(url_for('home'))

# Executamos a aplicação Flask em modo de depuração.
if __name__ == '__main__':  # corrigido para '__main__'
    app.run(debug=True)
