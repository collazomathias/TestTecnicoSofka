import controller
import tkinter.font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from random import randint


class Main:
    def __init__(self, sis):
        self.sis = sis
        self.sis.title('Preguntas y respuestas')
        self.sis.resizable(False, False)
        self.sis.geometry('550x290')
        style = ttk.Style(sis)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="blanchedalmond", foreground="black")
        style.configure("Treeview", rowheight="30")
        controller.iniciarSistema()

        # Menú
        self.nb = ttk.Notebook(self.sis)
        self.nb.pack(fill='both', expand='yes')

        # Pestañas
        pesGame = ttk.Frame(self.nb)
        pesConfig = ttk.Frame(self.nb)
        pesReg = ttk.Frame(self.nb)

        # Agregamos las pestañas al menú
        self.nb.add(pesGame, text='Jugar', padding=5)
        self.nb.add(pesConfig, text='Configuración')
        self.nb.add(pesReg, text='Ver registros', padding=5)

        # Interfaz gráfica para administrar preguntas
        # Menú config
        nb2 = ttk.Notebook(pesConfig)
        nb2.pack(fill='both', expand='yes')

        # Pestañas menú config
        pesAddQuest = ttk.Frame(nb2)
        pesDelQuest = ttk.Frame(nb2)
        pesAdminCat = ttk.Frame(nb2)

        # Agregamos las pestañas al menú config
        nb2.add(pesAdminCat, text='Administrar categorías', padding=5)
        nb2.add(pesAddQuest, text='Agregar pregunta', padding=5)
        nb2.add(pesDelQuest, text='Eliminar pregunta', padding=5)

        # Interfaz gráfica para agregar preguntas
        labQuestion = Label(pesAddQuest, text='Pregunta:')
        labQuestion.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.textQuestion = Entry(pesAddQuest, width=63)
        self.textQuestion.grid(row=0, column=1, pady=5)
        labTrueAnsw = Label(pesAddQuest, text='Respuesta verdadera:')
        labTrueAnsw.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.textTrueAnsw = Entry(pesAddQuest, width=63)
        self.textTrueAnsw.grid(row=1, column=1, pady=5)
        labFakeAnsw1 = Label(pesAddQuest, text='Respuesta falsa 1:')
        labFakeAnsw1.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.textFakeAnsw1 = Entry(pesAddQuest, width=63)
        self.textFakeAnsw1.grid(row=2, column=1, pady=5)
        labFakeAnsw2 = Label(pesAddQuest, text='Respuesta falsa 2:')
        labFakeAnsw2.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.textFakeAnsw2 = Entry(pesAddQuest, width=63)
        self.textFakeAnsw2.grid(row=3, column=1, pady=5)
        labFakeAnsw3 = Label(pesAddQuest, text='Respuesta falsa 3:')
        labFakeAnsw3.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        self.textFakeAnsw3 = Entry(pesAddQuest, width=63)
        self.textFakeAnsw3.grid(row=4, column=1, pady=5)
        labCategory = Label(pesAddQuest, text='Categoría:')
        labCategory.grid(row=5, column=0, sticky='w', padx=10, pady=5)
        self.cbCategory = ttk.Combobox(pesAddQuest, width=30)
        self.cbCategory.grid(row=5, column=1, pady=5, sticky='w')
        self.bAddQuest = Button(pesAddQuest, text='Agregar pregunta', fg='white', bg='green',
                                activebackground="darkgreen", activeforeground="white",
                                command=lambda: [controller.insertarPregunta(self.textQuestion.get(),
                                                                             self.textTrueAnsw.get(),
                                                                             self.textFakeAnsw1.get(),
                                                                             self.textFakeAnsw2.get(),
                                                                             self.textFakeAnsw3.get(),
                                                                             self.cbCategory.get()),
                                                 self.mostrarPreguntas(),
                                                 self.limpiarTextosQuest()])
        self.bAddQuest.grid(row=6, columnspan=2, sticky=W + E, padx=(13, 0), pady=5)

        # Interfaz gráfica para eliminar preguntas
        self.tvQuest = ttk.Treeview(pesDelQuest, columns=1, height=5)
        self.tvQuest.place(x=12, y=5)
        self.tvQuest.heading('#1', text='Preguntas', anchor=W)
        self.tvQuest.column('#0', width=0, minwidth=0)
        self.tvQuest.column('#1', width=504)
        self.bDelQuest = Button(pesDelQuest, text='Eliminar pregunta', fg='white', bg='red', activebackground="darkred",
                                activeforeground="white", width=71,
                                command=lambda: [
                                    controller.eliminarPregunta(
                                        str(self.tvQuest.item(self.tvQuest.selection())['text'])),
                                    self.mostrarPreguntas()])
        self.bDelQuest.place(x=12, y=191)

        # Interfaz gráfica para administrar categorías
        labCat = Label(pesAdminCat, text='Categoría:')
        labCat.grid(row=0, column=0, sticky='w', padx=(10, 13), pady=5)
        self.textCat = Entry(pesAdminCat, width=43)
        self.textCat.grid(row=0, column=1, pady=5)
        labDif = Label(pesAdminCat, text='Dificultad:')
        labDif.grid(row=0, column=3, sticky='w', padx=10, pady=5)
        self.textDif = Entry(pesAdminCat, width=15)
        self.textDif.grid(row=0, column=4, pady=5)
        self.bAddCat = Button(pesAdminCat, text='Agregar categoría', fg='white', bg='green',
                              activebackground="darkgreen", activeforeground="white", width=15,
                              command=lambda: [controller.insertarCategoria(self.textCat.get(),
                                                                            self.textDif.get()),
                                               self.mostrarCategorias(),
                                               self.limpiarTextosCat()])
        self.bAddCat.grid(row=1, column=0, columnspan=5, sticky=W + E, pady=(3, 0), padx=(13, 0))
        self.tvCat = ttk.Treeview(pesAdminCat, columns=1, height=3)
        self.tvCat.place(x=12, y=65)
        self.tvCat.heading('#1', text='Categorías', anchor=W)
        self.tvCat.column('#0', width=0, minwidth=0)
        self.tvCat.column('#1', width=504)
        self.bDelCat = Button(pesAdminCat, text='Eliminar categoría', fg='white', bg='red', activebackground='darkred',
                              activeforeground='white', width=71, command=lambda: [
                                  controller.eliminarCategoria(str(self.tvCat.item(self.tvCat.selection())['text'])),
                                  self.mostrarCategorias(), self.mostrarPreguntas()])
        self.bDelCat.place(x=12, y=191)

        # Interfaz gráfica para registros
        self.tvReg = ttk.Treeview(pesReg, columns=('Usuario', 'Puntuacion'), height=6)
        self.tvReg.place(x=12, y=5)
        self.tvReg.heading('#1', text='Usuario', anchor=W)
        self.tvReg.heading('#2', text='Puntuación', anchor=W)
        self.tvReg.column('#0', width=0, minwidth=0)
        self.tvReg.column('#1', width=354)
        self.tvReg.column('#2', width=150)
        self.bDelReg = Button(pesReg, text='Eliminar registro', fg='white', bg='red', activebackground='darkred',
                              activeforeground='white', width=71, command=lambda: [
                                                      controller.eliminarRegistro(
                                                          str(self.tvReg.item(self.tvReg.selection())['text'])),
                                                      self.mostrarRegistros()])
        self.bDelReg.place(x=12, y=221)

        # Interfaz gráfica para jugar
        self.frGame = Frame(pesGame, width=550, height=290)
        self.frGame.place_forget()
        fontTitle = tkinter.font.Font(family="Meiryo", size=10, weight="bold")
        fontTitleMin = tkinter.font.Font(family="Meiryo", size=8, weight="bold")
        fontLeveLPrice = tkinter.font.Font(family="Sans-serif", size=10, weight="bold")

        self.labCatSelect = Label(self.frGame, text='Selecciona una categoría:', height=2, width=25)
        self.labCatSelect.configure(font=fontTitleMin)
        self.cbCatGame = ttk.Combobox(self.frGame, width=39)

        self.labQuest = Label(self.frGame, bg='blanchedalmond', height=2, wraplength=350)
        self.labQuest.configure(font=fontTitle)
        self.labQuestSelect = Label(self.frGame, text='Selecciona una respuesta:', height=2, width=25)
        self.labQuestSelect.configure(font=fontTitleMin)

        self.cbQuestGame = ttk.Combobox(self.frGame, width=39)



        self.bSelectCat = Button(self.frGame, text='Elegir categoría', width=16, height=2, bg='green', fg='white',
                                 activebackground='darkgreen', activeforeground='white',
                                 command=lambda: self.elegirPregunta())
        self.bSelectQuest = Button(self.frGame, text='Elegir pregunta', width=16, height=2, bg='green', fg='white',
                                activebackground='darkgreen', activeforeground='white',
                                command=lambda: self.elegirCategoria())

        self.bCloseGame = Button(self.frGame, text='Finalizar juego', width=16, height=2, bg='red', fg='white',
                                 activebackground='darkred', activeforeground='white',
                                 command=lambda: self.terminarJuego())
        self.bCloseGame.place(x=392, y=75)

        self.labLevel = Label(self.frGame, text='Nivel: 1', height=2, bg="blanchedalmond", width=15)
        self.labLevel.configure(font=fontLeveLPrice)
        self.labLevel.place(x=390, y=135)

        self.labPrice = Label(self.frGame, text='Premio: 0', height=2, bg="blanchedalmond", width=15)
        self.labPrice.configure(font=fontLeveLPrice)
        self.labPrice.place(x=390, y=195)

        fontButtonGame = tkinter.font.Font(family="Meiryo", size=12)
        self.labUsuario = Label(pesGame, text='Usuario:')
        self.labUsuario.place(relx=0.5, rely=0.30, anchor=CENTER)
        self.labUsuario.configure(font=fontButtonGame)
        self.textUsuario = Entry(pesGame, width=31)
        self.textUsuario.place(relx=0.5, rely=0.40, anchor=CENTER)

        self.bGame = Button(pesGame, text='Comenzar el juego', fg='black', bg='blanchedalmond', activebackground='navajowhite',
                            activeforeground='black', height=2, width=20, command=lambda: self.iniciarJuego(self.textUsuario.get()))
        self.bGame.place(relx=0.5, rely=0.60, anchor=CENTER)
        self.bGame.configure(font=fontButtonGame)

    # -------------------------- FUNCIONES -------------------------- #
    # Relleno la tabla (treeview) con las preguntas que contiene la base de datos
    def mostrarPreguntas(self):
        reg = self.tvQuest.get_children()
        for i in reg:
            self.tvQuest.delete(i)
        cur = controller.obtenerPreguntas()
        for (id, pregunta) in cur:
            self.tvQuest.insert('', 'end', id, text=id, values=pregunta.replace(" ", "\ "))

    # Relleno la tabla (treeview) con las categorías que contiene la base de datos
    def mostrarCategorias(self):
        reg = self.tvCat.get_children()
        for i in reg:
            self.tvCat.delete(i)
        cur = controller.obtenerCategorias()
        self.cbCategory['values'] = ()
        for (id, categoria) in cur:
            if categoria not in self.cbCategory['values']:
                self.cbCategory['values'] = (*self.cbCategory['values'], categoria)
            self.tvCat.insert('', 'end', id, text=id, values=categoria.replace(" ", "\ "))
        if self.cbCategory['values']:
            self.cbCategory.current(0)
        else:
            self.cbCategory.delete(0, END)

    # Relleno la tabla (treeview) con las preguntas que contiene la base de datos
    def mostrarRegistros(self):
        reg = self.tvReg.get_children()
        for i in reg:
            self.tvReg.delete(i)
        cur = controller.obtenerRegistros()
        for (id, nombreUsuario, puntuacion) in cur:
            self.tvReg.insert('', 'end', id, text=id, values=(nombreUsuario, puntuacion))

    # Limpio todas las casillas de texto de agregar pregunta
    def limpiarTextosQuest(self):
        self.textQuestion.delete(0, END)
        self.textTrueAnsw.delete(0, END)
        self.textFakeAnsw1.delete(0, END)
        self.textFakeAnsw2.delete(0, END)
        self.textFakeAnsw3.delete(0, END)
        self.textQuestion.focus()
        if self.cbCategory['values']:
            self.cbCategory.current(0)
        else:
            self.cbCategory.delete(0, END)

    # Limpio todas las casillas de texto de agregar categoría
    def limpiarTextosCat(self):
        self.textCat.delete(0, END)
        self.textDif.delete(0, END)
        self.textCat.focus()

    def iniciarJuego(self, usuario):
        self.gameStarted = 0
        if len(usuario) > 0:
            self.nivel = 1
            self.premio = 0
            self.usuario = '{}'.format(usuario)
            if controller.validarJuego() == 1:
                self.elegirCategoria()
        else:
            messagebox.showerror('¡Atención!', 'Debe ingresar un nombre de usuario para jugar.')

    def terminarJuego(self):
        controller.terminarJuego(self.usuario, self.premio)
        app.mostrarRegistros()
        self.gameStarted = 0
        self.nb.tab(1, state='normal')
        self.nb.tab(2, state='normal')
        self.labUsuario.place(relx=0.5, rely=0.30, anchor=CENTER)
        self.textUsuario.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.bGame.place(relx=0.5, rely=0.60, anchor=CENTER)
        self.frGame.place_forget()
        self.mostrarCategorias()

    def elegirCategoria(self):
        if self.gameStarted == 1:
            cur = controller.verificarRespuesta(self.cbQuestGame.get(), self.cbCatGame.get(), self.labQuest['text'])
            if cur == 1:
                self.premio = self.premio + (self.nivel*10)
                if self.nivel == 5:
                    messagebox.showinfo('¡Increíble!', 'Has pasado el último nivel del juego con éxito, ¡felicidades!')
                    self.terminarJuego()
                    return
                else:
                    messagebox.showinfo('¡Excelente!', 'La respuesta es correcta, avanzas a la siguiente fase.')
                    self.nivel = self.nivel+1
            else:
                messagebox.showinfo('¡Juego terminado!', 'Lo sentimos {}, tu respuesta fue errónea y el juego ha terminado.\nTu puntuación ha sido de {}/150.'.format(self.usuario, 0))
                self.premio = 0
                self.terminarJuego()
                return
        self.cbCatGame['values'] = ()
        self.labLevel['text'] = 'Nivel: {}/5'.format(self.nivel)
        self.labPrice['text'] = 'Premio: {}/150'.format(self.premio)
        cur = controller.obtenerCategoriasNivel(self.nivel)
        for (id, categoria) in cur:
            if categoria not in self.cbCatGame['values']:
                self.cbCatGame['values'] = (*self.cbCatGame['values'], categoria)
        if self.cbCatGame['values']:
            self.cbCatGame.current(0)
        self.nb.tab(1, state='disabled')
        self.nb.tab(2, state='disabled')
        self.labUsuario.place_forget()
        self.textUsuario.place_forget()
        self.bGame.place_forget()
        self.labQuest.place_forget()
        self.labQuestSelect.place_forget()
        self.cbQuestGame.place_forget()
        self.frGame.place(x=0, y=0)
        self.labCatSelect.place(relx=0.35, y=40, anchor=CENTER)
        self.cbCatGame.place(relx=0.35, y=65, anchor=CENTER)
        self.bSelectCat.place(x=392, y=15)
        self.bSelectQuest.place_forget()
        if self.gameStarted != 1:
            self.gameStarted = 1

    def elegirPregunta(self):
        self.labCatSelect.place_forget()
        self.cbCatGame.place_forget()
        curQuest = controller.obtenerPreguntaCat(self.cbCatGame.get())
        rQuest = randint(0, 4)
        quest = curQuest.fetchall()
        self.labQuest['text'] = quest[rQuest][1]
        curAnswers = controller.obtenerRespuestasPregunta(self.cbCatGame.get(), self.labQuest['text'])
        answers = curAnswers.fetchall()
        answers_random = list(answers[0])
        random.shuffle(answers_random)
        self.cbQuestGame['values'] = ()
        for index in answers_random:
            if index not in self.cbQuestGame['values']:
                self.cbQuestGame['values'] = (*self.cbQuestGame['values'], index)
        if self.cbQuestGame['values']:
            self.cbQuestGame.current(0)
        self.labQuest.place(relx=0.35, y=50, anchor=CENTER)
        self.labQuestSelect.place(relx=0.35, y=120, anchor=CENTER)
        self.cbQuestGame.place(relx=0.35, y=145, anchor=CENTER)
        self.bSelectQuest.place(x=392, y=15)
        self.bSelectCat.place_forget()



    # -------------------------- FIN FUNCIONES -------------------------- #


if __name__ == '__main__':
    sis = Tk()
    app = Main(sis)
    app.mostrarPreguntas()
    app.mostrarCategorias()
    app.mostrarRegistros()
    sis.mainloop()
