from bd_connection import student_connection

c = student_connection()
def validar_login():
    try:
        e = c.cursor()
        e.callproc('Validar_Acceso')
    except Exception as e:
        print("adasd")