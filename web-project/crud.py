from bd import conectar

def videos():
    base = conectar()
    videos=[]
    with base.cursor() as cursor:
        cursor.execute("SELECT titulo, direccion, idtutorial FROM tutorial")
        videos=cursor.fetchall()
    base.close()
    return videos

def video(id):
    base = conectar()
    video=[]
    with base.cursor() as cursor:
        cursor.execute("SELECT * FROM tutorial WHERE idtutorial=%s",(id))
        video=cursor.fetchall()
    base.close()
    return video

def comentarios(id):
    base = conectar()
    comentarios=[]
    with base.cursor() as cursor:
        cursor.execute("SELECT * FROM comentario WHERE idtuto=%s",(id))
        comentarios=cursor.fetchall()
    base.close()
    return comentarios

def comentario(id):
    base = conectar()
    comentario=[]
    with base.cursor() as cursor:
        cursor.execute("SELECT * FROM comentario WHERE idcomentario=%s",(id))
        comentario=cursor.fetchall()
    base.close()
    return comentario

def eliminarco(id):
    base = conectar()
    with base.cursor() as cursor:
        cursor.execute("DELETE FROM comentario WHERE idcomentario= %s", (id))
    base.commit()
    base.close()

def editarco(id, comentario):
    base = conectar()
    with base.cursor() as cursor:
        cursor.execute("UPDATE comentario SET comentarioD = %s WHERE idcomentario = %s",
                       (comentario, id))
    base.commit()
    base.close()

def insertVideo(nombre, fecha, descripcion, direccion):
    base = conectar()
    with base.cursor() as cursor:
        cursor.execute("INSERT INTO tutorial(titulo, fecha, descripcion, direccion) VALUES (%s, %s, %s, %s)",
                       (nombre, fecha, descripcion, direccion))
    base.commit()
    base.close()

def insertComen(idv,comentario):
    base = conectar()
    with base.cursor() as cursor:
        cursor.execute("INSERT INTO comentario (idTuto, comentarioD) VALUES (%s, %s)",
                       (idv,comentario))
    base.commit()
    base.close()

def actualizarCo(id,descripcion):
    base = conectar()
    with base.cursor() as cursor:
        cursor.execute("UPDATE comentario SET comentarioD=%s WHERE idcomentario = %s",
                       (descripcion,id))
    base.commit()
    base.close()