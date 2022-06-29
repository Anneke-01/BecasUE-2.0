from bd_connection import admin_connection, student_connection
from call_tables import calltables
from flask_session import Session
from flask import Flask, redirect, session, render_template, request, flash



c_admin = admin_connection()
engine_admin = c_admin.cursor()
c_student = student_connection()
engine_student = c_student.cursor()

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        rol = request.form.get("rol")
        if rol == 'Administrador':
            sql = 'exec [BecasEstudioUE].[dbo].[Validar_Acceso] @Usuario =?, @Contrasena =?, @Rol =?;'
            values = (username, password, rol)
            engine_admin.execute(sql,values)
            r = engine_admin.fetchval()
            print(r, "AAHHHH")
            if r == "Acceso Exitoso":
                id_admin = engine_admin.execute('exec [BecasEstudioUE].[dbo].[Obtener_ID] @Usuario = ?', username).fetchval()
                print(id_admin)
                session["user_id"] = id_admin
                flash(r,'exitoso')
                return redirect("/")
            else:
                flash(r, 'error')
                return render_template("login.html", message=r)
        elif rol == 'Estudiante':
            sql = 'exec [BecasEstudioUE].[dbo].[Validar_Acceso] @Usuario =?, @Contrasena =?, @Rol =?;'
            values = (username, password, rol)
            engine_student.execute(sql,values)
            r = engine_student.fetchval()
            print(r)
            if r == "Acceso Exitoso":
                id_std = engine_student.execute('exec [BecasEstudioUE].[dbo].[Obtener_ID] @Usuario = ?', username).fetchval()
                print(id_std)
                session["user_id"] = id_std
                flash(r,'exitoso')
                return redirect("/")
            else:
                flash(r, 'error')
                return render_template("login.html")
            
        return redirect("/")
    if request.method == "GET":
        session.clear()
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("login")
    
if __name__ == '__main__':
    admin_connection()
    calltables()
    app.run(port=3300, debug=True)