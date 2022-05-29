import pyodbc 
def connection():
    try:
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=ANN-01;'
                            'CHARSET=UTF8;'
                            'Database=BecasEstudioUE;'
                            'Trusted_Connection=yes;')
        conn.setdecoding(pyodbc.SQL_CHAR,encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WCHAR,encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='unicode_escape')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-16le') 
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
    return conn
