from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from plyer import notification
from threading import Thread
from datetime import datetime
import time

app = Flask(__name__)

# Clase para manejar la base de datos
class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def fetch_all(self, query, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result

    def fetch_one(self, query, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        conn.close()
        return result

db = Database('tasks.db')

# Crear la base de datos
def init_db():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        due_time TEXT
    )
    '''
    db.execute_query(create_table_query)

# Notificaciones automáticas
def notify_due_tasks():
    while True:
        tasks = db.fetch_all("SELECT title, due_date, due_time FROM tasks")
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        for task in tasks:
            due_datetime = f"{task[1]} {task[2]}"
            if due_datetime == now:
                notification.notify(
                    title="Tarea Pendiente",
                    message=f"Tarea: {task[0]} está programada para ahora.",
                    timeout=10
                )
        time.sleep(60)

# Rutas
@app.route('/')
def index():
    tasks = db.fetch_all("SELECT * FROM tasks")
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        due_time = request.form['due_time']
        db.execute_query("INSERT INTO tasks (title, description, due_date, due_time) VALUES (?, ?, ?, ?)",
                         (title, description, due_date, due_time))
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        due_time = request.form['due_time']
        db.execute_query("UPDATE tasks SET title = ?, description = ?, due_date = ?, due_time = ? WHERE id = ?",
                         (title, description, due_date, due_time, task_id))
        return redirect(url_for('index'))
    task = db.fetch_one("SELECT * FROM tasks WHERE id = ?", (task_id,))
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    db.execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    Thread(target=notify_due_tasks, daemon=True).start()
    app.run(debug=True)
