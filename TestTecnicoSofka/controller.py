import model
from tkinter import messagebox


def iniciarSistema():
    if model.crearBase() == 1:
        messagebox.showinfo('¡Éxito!', 'La base de datos ha sido creada con éxito.')
    else:
        pass


def obtenerPreguntas():
    query = 'SELECT id, pregunta FROM preguntas;'
    cur = model.consultaPreguntas(query)
    return cur


def insertarPregunta(question, trueansw, fakeansw1, fakeansw2, fakeansw3, category):
    if len(question) != 0 and len(trueansw) != 0 and len(fakeansw1) != 0 and len(fakeansw2) != 0 and len(fakeansw3) != 0 and len(category) != 0:
        queryObtenerIdCat = "SELECT id FROM categorias WHERE categoria = '{}'".format(category)
        curIdCat = model.obtenerIdCat(queryObtenerIdCat)
        id = curIdCat.fetchall()
        if id:
            queryInsertarPregunta = "INSERT INTO preguntas (pregunta, idCategoria) VALUES ('{}', {})".format(question, id[0][0])
            curPregunta = model.insertarPregunta(queryInsertarPregunta)
            idPregunta = curPregunta
            if idPregunta != 0:
                queryInsertarRespuestas = """INSERT INTO 
                respuestas (respuestaVerdadera, respuestaFalsa1, respuestaFalsa2, RespuestaFalsa3, idPregunta) 
                VALUES ('{}', '{}', '{}', '{}', {});""".format(trueansw, fakeansw1, fakeansw2, fakeansw3, idPregunta)
                curRespuestas = model.insertarRespuestas(queryInsertarRespuestas)
                if curRespuestas == 1:
                    messagebox.showinfo('¡Éxito!', 'La pregunta fue ingresada con éxito.')
                else:
                    messagebox.showerror('¡Atención!', 'No se pudieron ingresar las respuestas.')
            else:
                messagebox.showerror('¡Atención!', 'No se pudo ingresar la pregunta.')
        else:
            messagebox.showerror('¡Atención!', 'La categoría ingresada no es válida.')
    else:
        messagebox.showerror('¡Atención!', 'Debe ingresar todos los campos correctamente.')


def eliminarPregunta(idPregunta):
    if idPregunta:
        queryEliminarRespuestas = 'DELETE FROM respuestas WHERE idPregunta = {};'.format(idPregunta)
        curEliminarRespuestas = model.eliminarRespuestas(queryEliminarRespuestas)
        if curEliminarRespuestas == 1:
            queryEliminarPregunta = 'DELETE FROM preguntas WHERE id = {};'.format(idPregunta)
            curEliminarPregunta = model.eliminarPregunta(queryEliminarPregunta)
            if curEliminarPregunta == 1:
                messagebox.showinfo('¡Éxito!', 'Ha eliminado la pregunta con éxito.')
            else:
                messagebox.showerror('¡Atención!', 'No se pudo eliminar la pregunta.')
        else:
            messagebox.showerror('¡Atención!', 'No se pudieron eliminar las respuestas de la pregunta.')
    else:
        pass


def obtenerCategorias():
    query = 'SELECT id, categoria FROM categorias;'
    cur = model.consultaCategorias(query)
    return cur


def insertarCategoria(cat, dif):
    if len(cat) != 0 and len(dif) != 0:
        queryInsertarCat = "INSERT INTO categorias (categoria, dificultad) VALUES ('{}', {})".format(cat, dif)
        curCat = model.insertarCategoria(queryInsertarCat)
        if curCat == 1:
            messagebox.showinfo('¡Éxito!', 'La categoría fue ingresada con éxito.')
        else:
            messagebox.showerror('¡Atención!', 'No se pudo ingresar la categoría.')
    else:
        messagebox.showerror('¡Atención!', 'Debe ingresar todos los campos correctamente.')


def eliminarCategoria(idCat):
    if idCat:
        queryEliminarRespuestasPreguntasCat = """DELETE FROM respuestas WHERE idPregunta IN (SELECT id FROM preguntas WHERE idCategoria = {});""".format(idCat)
        curEliminarRespuestasPreguntasCat = model.eliminarRespuestasPreguntasCat(queryEliminarRespuestasPreguntasCat)
        if curEliminarRespuestasPreguntasCat == 1:
            queryEliminarPreguntasCat = "DELETE FROM preguntas WHERE idCategoria = {};".format(idCat)
            curEliminarPreguntasCat = model.eliminarPreguntasCat(queryEliminarPreguntasCat)
            if curEliminarPreguntasCat == 1:
                queryEliminarCat = "DELETE FROM categorias WHERE id = {};".format(idCat)
                curEliminarCat = model.eliminarCategoria(queryEliminarCat)
                if curEliminarCat == 1:
                    messagebox.showinfo('¡Éxito!', 'La categoría fue eliminada con éxito.')
                else:
                    messagebox.showerror('¡Atención!', 'No se pudo eliminar la categoría.')
            else:
                messagebox.showerror('¡Atención!', 'No se pudieron eliminar las preguntas de esta categoría.')
        else:
            messagebox.showerror('¡Atención!', 'No se pudieron eliminar las respuestas de una pregunta de esta categoría.')
    else:
        pass


def obtenerRegistros():
    query = 'SELECT id, nombreUsuario, puntuacion FROM registros ORDER BY puntuacion DESC;'
    cur = model.consultaRegistros(query)
    return cur


def eliminarRegistro(idRegistro):
    if idRegistro:
        queryEliminarReg = 'DELETE FROM registros WHERE id = {};'.format(idRegistro)
        curEliminarReg = model.eliminarRegistro(queryEliminarReg)
        if curEliminarReg == 1:
            messagebox.showinfo('¡Éxito!', 'Ha eliminado el registro con éxito.')
        else:
            messagebox.showerror('¡Atención!', 'No se pudo eliminar el registro.')
    else:
        pass


def obtenerCategoriasNivel(nivel):
    if(nivel):
        queryObtenerCatNivel = '''SELECT id, categoria
                                FROM categorias AS C
                                WHERE dificultad = {} AND
                                (SELECT COUNT(*)
                                FROM preguntas
                                WHERE idCategoria = C.id) >= 5'''.format(nivel)
        curObtenerCatNivel = model.consultaCatNivel(queryObtenerCatNivel)
        if curObtenerCatNivel:
            return curObtenerCatNivel
        else:
            messagebox.showerror('¡Atención!', 'No hay categorías de ese nivel.')
    else:
        messagebox.showerror('¡Atención!', 'El nivel no es correcto.')


def validarJuego():
    i = 1
    while i <= 5:
        queryObtenerCatNivel = '''SELECT COUNT(*)
                                FROM categorias AS C
                                WHERE dificultad = {} AND
                                (SELECT COUNT(*)
                                FROM preguntas
                                WHERE idCategoria = C.id) >= 5'''.format(i)
        cur = model.consultaCatNivel(queryObtenerCatNivel)
        cant = cur.fetchall()
        if cant[0][0] < 1:
            messagebox.showerror('¡Atención!', 'El juego no contiene suficientes preguntas y/o categorías.')
            return 0
        i = i+1
    return 1


def terminarJuego(usuario, puntuacion):
    query = "INSERT INTO registros (nombreUsuario, puntuacion) VALUES('{}', {});".format(usuario, puntuacion)
    curTerminarJuego = model.terminarJuego(query)
    if curTerminarJuego == 1:
        messagebox.showinfo('¡Juego terminado!', '{}, has terminado el juego.\nTu puntuación ha sido de {}/150.'.format(usuario, puntuacion))
    else:
        messagebox.showerror('¡Atención!', 'Hubo un error al terminar el juego.')


def obtenerPreguntaCat(nombreCat):
    query = '''SELECT id, pregunta 
            FROM preguntas AS P 
            WHERE P.idCategoria = (
                SELECT id
                FROM categorias
                WHERE categoria = "{}");'''.format(nombreCat)
    cur = model.obtenerPreguntaCat(query)
    return cur


def obtenerRespuestasPregunta(nombreCat, pregunta):
    query = '''SELECT respuestaVerdadera, respuestaFalsa1, respuestaFalsa2, respuestaFalsa3 
                FROM respuestas AS R 
                WHERE R.idPregunta = (
                    SELECT id
                    FROM preguntas AS P
                    WHERE P.pregunta = "{}"
                    AND idCategoria = (
                        SELECT id
                        FROM categorias AS C
                        WHERE C.categoria = "{}"));'''.format(pregunta, nombreCat)
    cur = model.consultaRespuestasPregunta(query)
    return cur


def verificarRespuesta(respuesta, categoria, pregunta):
    query = '''SELECT respuestaVerdadera
            FROM respuestas as R
            WHERE R.idPregunta = (
                SELECT id
                FROM preguntas AS P
                WHERE P.idCategoria = (
                    SELECT id
                    FROM categorias AS C
                    WHERE C.categoria = "{}")
                AND P.pregunta = "{}");'''.format(categoria, pregunta)
    cur = model.obtenerRespuestaVerdadera(query)
    respuestaVerdadera = cur.fetchall()
    if respuestaVerdadera[0][0] == respuesta:
        return 1
    return 0