import sqlite3
import tkinter as tk
from tkinter import messagebox
import csv



def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn, conn.cursor()

conn, cursor = connect_db()

import sqlite3

def view_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    
    for task in tasks:
        print(task)
    
    conn.close()

view_tasks()


#########################################################################################################################




cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        due_date TEXT,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
    )
''')
conn.commit()

def add_task(title, description, due_date, category_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO tasks (title, description, due_date, category_id, completed)
    VALUES (?, ?, ?, ?, 0)
    ''', (title, description, due_date, category_id))

    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    for task in tasks:
        print(task)

    conn.close()


def mark_task_complete(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE tasks
    SET completed = 1
    WHERE id = ?
    ''', (task_id,))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))

    conn.commit()
    conn.close()

def filter_tasks(category_id=None, due_date=None):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM tasks WHERE 1=1'
    params = []

    if category_id:
        query += ' AND category_id = ?'
        params.append(category_id)
    
    if due_date:
        query += ' AND due_date = ?'
        params.append(due_date)

    cursor.execute(query, params)
    tasks = cursor.fetchall()

    for task in tasks:
        print(task)

    conn.close()

import tkinter as tk
from tkinter import messagebox

def add_task_ui():
    title = title_entry.get()
    description = description_entry.get()
    due_date = due_date_entry.get()
    category_id = category_entry.get()  # Simplified, you might want to use a dropdown with existing categories

    add_task(title, description, due_date, category_id)
    messagebox.showinfo("Success", "Task added successfully!")

root = tk.Tk()
root.title("Task Manager")

tk.Label(root, text="Title:").grid(row=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Description:").grid(row=1)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

tk.Label(root, text="Due Date (YYYY-MM-DD):").grid(row=2)
due_date_entry = tk.Entry(root)
due_date_entry.grid(row=2, column=1)

tk.Label(root, text="Category:").grid(row=3)
category_entry = tk.Entry(root)
category_entry.grid(row=3, column=1)

tk.Button(root, text="Add Task", command=add_task_ui).grid(row=4, column=1)

root.mainloop()


def export_tasks(filename='tasks.csv'):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Title', 'Description', 'Due Date', 'Category ID', 'Completed'])
        writer.writerows(tasks)

    conn.close()
