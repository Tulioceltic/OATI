# OATI
Prueba técnica de ingreso como desarrollador  Perfil tecnólogo  Oficina Asesora de Tecnologías e Información - OATI Universidad Distrital Francisco José de Caldas

Autor: Julio Cesar Bernal Pineda

Desarrollo realizado utilizando Flask y MySQL

Librerias necesarias: Flask, pymysql

main.py: Contiene la aplicacion flask haciendo referencia a los templates a utilizar

crud.py: Contiene las funciones CRUD a utilizar en la base de datos

bd.py: Archivo necesario para realizar la conexion a la base de datos

base.sql: En este archivo encontraras la cracion de la base de datos a utilizar, incluyendo el schema

Recomendaciones:

1) cuando se cree un nuevo tutorial la direccion hace referencia a un link de youtube este sera el valor del atributo src que se encuentra al dar compartir opcion insertar, anexo video explicativo de como obtener este codigo https://www.youtube.com/watch?v=lJIrF4YjHfQ de lo contrario saldra un error en donde el navegador no mostrara la miniatura del video

2) al realizar la edicion, eliminacion o creacion de comentarios sera reenviado a la pagina principal

3) los videos usados en este ejemplo no son de mi autoria

4) es vulnerable

Desarrollo:

Enunciado: en un contexto de aprendizaje virtual, un tutorial de un tema en
específico puede contar con muchos comentarios por parte de los estudiantes.
Se quiere registrar la descripción, título y fecha de publicación del tutorial; así
como el contenido del comentario hecho al tutorial. Se debe permitir listar los
tutoriales, los comentarios para un tutorial en particular, así como permitirse la
modificación y eliminación de un comentario.

se crearan dos instancias entidades y comentario, teniendo (id, titulo, fecha, descripcion, direccion) y (id, idtuto, comentario) como atributos de cada entidad respectivamente. siendo idtuto la llave foranea que usaremos para conectar ambas entidades. Para efectos practicos ambos id de las de las entidades se manejaran como auto incrementos, con el fin de facilitar el ingreso de nuevos registros; el resto de atributos seran de tipo VARCHAR a exepcion de fecha quien es de tipo DATE.

Se menciona que el desarrollo es vulnerble ante SQL inyeccion debido a que no tiene forma de validar tipos de ingresos maliciosos. (Esta validacion se puede añadir posteriormente usando archivos js en los templates de ingreso de tal manera que se haga la validacion y verificacion en el front antes de ser enviados al back)

Se creo un pequeño archivo de tipo css con el fin de visualizar mejor los comentarios hechos a cada video

Funcionamiento:

Lo primero que encontrara son los videos previamente cargados en la base de datos (base.sql), debajo de cada video encontrara "Ver mas" y al finalizar la lista encontrara un boton para añadir mas videos tutoriales (tener en cuenta recomendacion 1 y recomendacion 4)

Siguiendo en el boton "Ver mas" que se encuentra al final de cada video se dirigira a un template con el titulo del video, el video, su fecha, su descripcion y bajo esto la lista de los comentarios del video. Esta lista se encuentra estructurada de la siguiente manera:

añadir mas
comentario 1 eliminar editar
comentario 1 eliminar editar

siguiendo añadir mas iran a un templete para añadir un nuevo comentario al video
siguiendo eliminar se elimina el comentario al cual hace referencia el boton
siguiendo editar se dirigira a un nuevo template en donde se pyuede editar el contenido del comentario

tener en cuenta recomendacion 2
