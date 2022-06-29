import pyodbc 
def admin_connection():
    try:
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=ANN-01;'
                            'CHARSET=UTF8;'
                            'Database=BecasEstudioUE;'
                            'Trusted_Connection=yes;'
                            'UID=AdminBecas;'
                            'PWD=Becas2021*;')
        conn.setdecoding(pyodbc.SQL_CHAR,encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WCHAR,encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-16le') 
    except Exception as e:
        print("Ocurrió un error al conectar como Administrador a SQL Server: ", e)
    return conn

def student_connection():
    try:
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=ANN-01;'
                            'CHARSET=UTF8;'
                            'Database=BecasEstudioUE;'
                            'Trusted_Connection=yes;'
                            'UID=Estudiante;'
                            'PWD=EstudiantesBecas*;')
        conn.setdecoding(pyodbc.SQL_CHAR,encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WCHAR,encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-16le') 
    except Exception as e:
        print("Ocurrió un error al conectar como Estudiantes a SQL Server: ", e)
    return conn
        
