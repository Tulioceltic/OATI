import pymysql

def conectar():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='Juliopor5000',
                           db='videos')
2