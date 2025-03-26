from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas (en una aplicación real, usarías una base de datos)
tareas = []

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    tarea = request.form.get('tarea')
    if tarea and tarea.strip():
        tareas.append(tarea)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:indice>')
def eliminar(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)