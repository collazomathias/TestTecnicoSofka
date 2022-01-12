import sqlite3


def crearBase():
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute('''CREATE TABLE categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        categoria VARCHAR(30) NOT NULL, 
        dificultad INTEGER NOT NULL);
        ''')
        cur.execute('''CREATE TABLE preguntas (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        pregunta VARCHAR(100) NOT NULL, 
        idCategoria INTEGER NOT NULL);
        ''')
        cur.execute('''CREATE TABLE respuestas (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        respuestaVerdadera VARCHAR(50) NOT NULL,
        respuestaFalsa1 VARCHAR(50) NOT NULL, 
        respuestaFalsa2 VARCHAR(50) NOT NULL,
        respuestaFalsa3 VARCHAR(50) NOT NULL,
        idPregunta INTEGER NOT NULL);
        ''')
        cur.execute('''CREATE TABLE registros (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombreUsuario VARCHAR(30) NOT NULL, 
        puntuacion INTEGER NOT NULL);
        ''')
        return 1
    except:
        return 0


def consultaPreguntas(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur


def insertarPregunta(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return cur.lastrowid
    except:
        return 0


def insertarRespuestas(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def eliminarRespuestas(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def eliminarPregunta(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def consultaCategorias(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur


def insertarCategoria(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def eliminarCategoria(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def obtenerIdCat(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        return cur
    except:
        return 0


def eliminarRespuestasPreguntasCat(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def eliminarPreguntasCat(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def consultaRegistros(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur


def eliminarRegistro(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def consultaCatNivel(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur


def terminarJuego(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    try:
        cur.execute(query)
        con.commit()
        return 1
    except:
        return 0


def obtenerPreguntaCat(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur


def consultaRespuestasPregunta(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur


def obtenerRespuestaVerdadera(query):
    con = sqlite3.connect('basePreguntas')
    cur = con.cursor()
    cur.execute(query)
    return cur