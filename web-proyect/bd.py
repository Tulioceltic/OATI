import pymysql

def conectar():
    return pymysql.connect(host='localhost',
                           user='root',#Cambiar dependiendo de la configuracion
                           password='***',#Cambiar dependiendo de la configuracion
                           db='videos')
2