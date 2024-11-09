from flask import Flask, jsonify, json
from requests import *
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('todo.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE Tasks (
            taskid INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            status TEXT NOT NULL)""")
conn.commit()
conn.close()


@app.route("/add",methods=["POST"])
def add_task():
    if request.method == "POST":
        conn = sqlite3.connect('todo.db')
        cur = conn.cursor()
        task = request.form["task"]
        status = request.form["status"]
        data = (task,status)
        cur.execute("INSERT INTO Tasks VALUES(?, ?)",data)
        conn.commit()
        taskid= cur.lastrowid
        conn.close()
    return jsonify({"taskid" : taskid , "task": task, "status": status})


@app.route("/delete",methods=["DELETE"])
def delete_task():
    if request.method == "DELETE":
        conn = sqlite3.connect('todo.db')
        cur = conn.cursor()
        taskid = request.form["taskid"]
        cur.execute(f"DELETE FROM Tasks WHERE taksid= ?",(taskid,))
        conn.commit()
        conn.close()
        return 

@app.route("/update",methods=["PUT"])
def update_task():
    if request.method == "PUT":
        conn = sqlite3.connect('todo.db')
        cur = conn.cursor()
        taskid = request.form["taskid"]
        task = request.form["task"]
        status = request.form["status"]
        cur.execute(f"UPDATE Tasks SET task= ? status= ? WHERE taskid= ?",(task,status,taskid))
        conn.commit()
        conn.close()
        return 
