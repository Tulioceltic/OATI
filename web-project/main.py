from flask import Flask,render_template,redirect,request
from crud import *



app = Flask(__name__)

@app.route("/actualizarComent", methods=["GET","POST"])
def actualizarComent():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    actualizarCo(id,descripcion)
    return redirect("/videos")

@app.route("/formEditComent/<int:id>")
def editarComent(id):
    return render_template("editarcoment.html", coment=comentario(id))

@app.route("/eliminarComent", methods=["POST"])
def eliminarComent():
    a=request.form["id"]
    eliminarco(request.form["id"])
    return redirect("/videos")

@app.route("/guardarComentario/<id>", methods=["GET","POST"])
def guardarComentario(id):
    idtu = id
    descripcion = request.form["descripcion"]
    insertComen(idtu, descripcion)
    return redirect("/videos")

@app.route("/agreCo/<id>", methods=["GET","POST"])
def formAgreCo(id):
    return render_template("agregarComentario.html",idv=id)

@app.route("/agreVi", methods=["GET"])
def formAgreVi():
    return render_template("agregarVideo.html")

@app.route("/guardarVideo", methods=["POST"])
def guardarVideo():
    nombre = request.form["nombre"]
    fecha = request.form["fecha"]
    descripcion = request.form["descripcion"]
    direccion = request.form["direccion"]
    insertVideo(nombre, fecha, descripcion, direccion)
    return redirect("/videos")

@app.route("/agregarVid")
def agregarVideo():
    return render_template("agregarVideo.html")

@app.route('/mas/<id>', methods = ['POST','GET'])
def mostrarmas(id):
    return render_template('comentarios.html',video=video(id),comentarios=comentarios(id))

@app.route("/")
@app.route("/videos")
def inicio():
    return render_template('index.html',videos=videos())

if __name__=="__main__":
    app.run() 