from bd_connection import connection
from call_tables import calltables
from flask import Flask, session, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

if __name__ == '__main__':
    connection()
    calltables()
    app.run(port=3300)