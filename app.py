from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

lista = ['T1', 'T2', 'T3']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tarefas=lista)

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    lista.append(request.form['tarefa'])
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
