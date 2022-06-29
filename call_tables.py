from bd_connection import admin_connection

c = admin_connection()
def calltables():
    try:
        with c.cursor() as cursor:
            users = cursor.execute("SELECT * FROM Usuario").fetchall()
            list = []
            for i in users:
                list.append(i)
            
            #for f in list:
            #    print(f[1:5])
    except Exception as e:
        print("Ocurrió un error al consultar: ", e) 