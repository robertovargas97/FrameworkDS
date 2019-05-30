import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import font
import PIL.Image
import PIL.ImageTk
from PIL import Image, ImageTk


class Reajustar_tamano(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.ruta_fondo = 'img/fondo.png'
        self.imagen_para_fondo = Image.open(self.ruta_fondo)

        # self.image = Image.open("img/poto.gif")
        self.img_copy = self.imagen_para_fondo.copy()
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_para_fondo)
        self.fondo = tk.Label(self, image=self.imagen_fondo)
        self.fondo.pack(fill=tk.BOTH, expand=tk.YES)
        self.fondo.bind('<Configure>', self._reajustar_imagen)

    def _reajustar_imagen(self, event):

        new_width = event.width
        new_height = event.height

        self.imagen_para_fondo = self.img_copy.resize((new_width, new_height))
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_para_fondo)
        self.fondo.configure(image=self.imagen_fondo)


class Vista(Frame):

    def __init__(self,):
        # Colores para los botones de la vista
        self.fnt_btn = ('Comic Sans', 10, 'italic bold')
        self.clr_btn = "#FF4000"
        self.clr_fnt_btn = "white"
        self.clr_btn_pres = "#B43104"
        self.y_boton_menu = 430

    def mostrar_reglas(self):
        win = tk.Toplevel()
        win.geometry("+%d+%d" % (150, 30))
        win.resizable(False, False)
        frame = tk.Frame(win)
        iconPath1 = 'img/go.jpg'

        text1 = tk.Text(frame, height=39, width=50)
        im = PIL.Image.open(iconPath1)
        im = im.resize((480, 624))
        photo = PIL.ImageTk.PhotoImage(im)
        photo.image = photo
        text1.image_create(tk.END, image=photo)
        text1.pack(side=tk.LEFT)

        text2 = tk.Text(frame, height=39, width=65, bg='dark grey')
        scroll = tk.Scrollbar(frame, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 10, 'italic'))
        text2.tag_configure('big', foreground='#DF3A01',font=('Arial', 15, 'bold'))
        text2.tag_configure('color', foreground='#000000',font=('Arial', 10, 'bold'))
        
        
        # Texto de jugando la partida
        text2.insert(tk.END, ' \n ¿En que consiste el juego de GO?', 'big')
        quote2 = """
        \t• Consiste en colocar las piedras en las intersecciones del tablero.\n
        \t• Antes de comenzar se asigna un color a cada jugador. \n
        \t• Las negras inician la partida y una vez colocada una piedra, no se
        \tpuede volver a mover. \n
        \t• Se puede capturar una piedra o un conjunto de piedras y eliminarlas 
        \tdel tablero si están completamente rodeadas por piedras de otro color.  
        """
        text2.insert(tk.END, quote2, 'color')
        
        # Texto de las reglas basicas del juego
        text2.insert(tk.END, '\n Objetivo', 'big')
        quote = """
        \t• El objetivo del juego, cuya traducción aproximada es juego de 
        \trodear, es controlar una cantidad de territorio mayor a la del 
        \toponente.\n 
        \t• Para controlar un área, debe rodearse con las piedras.\n
        \t• Gana el jugador que controla la mayor cantidad de territorio 
        \tal finalizar la partida.
        """ 
        text2.insert(tk.END, quote, 'color')

        # Texto de las reglas basicas del juego
        text2.insert(tk.END, '\n Tablero', 'big')
        quote = """
        \t• El tablero 9x9 es el más pequeño y se utiliza o para principiantes 
        \to para partidas muy rápidas. Luego el tablero 13x13 es el tablero 
        \tpara jugadas intermedias.\n
        \t• El tablero 19x19 es el tablero estándar de go, y es en este donde 
        \tse juegan casi todas las partidas.
        """ 
        text2.insert(tk.END, quote, 'color')

        # Texto del proposito del juego
        text2.insert(tk.END, ' \n Piedras', 'big')
        quote1 = """
        \t• Las fichas del go se llaman piedras (Goishi) y son negras y 
        \tblancas.\n
        \t• Cada jugador puede llevar las que quiera pero debido a que 
        \tlas negras empiezan primero (esto se compensa como veremos 
        \tluego) se puede preferir unas u otras.   
        """
        text2.insert(tk.END, quote1, 'color')

        # Texto del inicio del juego
        text2.insert(tk.END, ' \n ¿Quién inicia primero?', 'big')
        quote1 = """
        \t• Normalmente se decide quien va a llevar cada color mediante el 
        \t"nigiri". Esto consiste en que un jugador coge un número de piedras 
        \tsin enseñarlas y el otro coge una o dos piedras para indicar par o 
        \timpar.\n 
        \t• Al abrir sus puños y soltarlas si el que elegía par o impar 
        \tacierta llevará negras, si falla llevará blancas.  
        """
        text2.insert(tk.END, quote1, 'color')

        # Texto de jaque
        text2.insert(tk.END, ' \n Captura de piedras', 'big')
        quote2 = """
        \t• Cuando un jugador hace una jugada que priva de su última libertad 
        \ta una piedra o formación del oponente, debe sacar las piedras 
        \trodeadas del tablero ty guardarlas separadamente hasta el final de 
        \tla partida.
        """
        text2.insert(tk.END, quote2, 'color')

        # Texto de Jaque Mate
        text2.insert(tk.END, ' \n Jugadas no permitidas', 'big')
        quote3 = """
        \t• Suicidio: No se permite hacer una jugada ocupando una posición 
        \tlibre en el interior de una formación enemiga (suicidio), a no ser 
        \tque esta jugada capture piedras enemigas.  
        """
        text2.insert(tk.END, quote3, 'color')

        # Texto de Tablas por ahogado
        text2.insert(tk.END, '\n Pasar el turno', 'big')
        quote4 = """
        \t• En lugar de poner una piedra, un jugador puede pasar 
        \t(perder un turno).\n
        \t• Pasar un turno casi nunca es buena idea, puesto que 
        \tda al oponente una jugada libre.\n

        \t• Solo es bueno pasar de turno al final de la partida, 
        \tcuando los territorios ya están definidos y no hay jugadas 
        \tpor hacer.\n
        \t• Cuando los dos jugadores pasan consecutivamente, se acaba la 
        \tpartida.
        """
        text2.insert(tk.END, quote4, 'color')
        
        # Texto de Tablas por ahogado
        text2.insert(tk.END, '\n Fin de la partida', 'big')
        quote4 = """
        \t•Una vez finalizada la partida, se retiran las piedras muertas 
        \tde cada bando añadiéndolas a las capturadas.\n
        \t•Se conocen como piedras muertas a aquellas que se encuentran 
        \trodeada,por lo que no podrían resistir una eventual captura.\n 
        \t•Entonces, los jugadores cuentan los puntos de cada territorio, 
        \tteniendo en cuenta las piedras prisioneras y las muertas, y 
        \tse decide quién ganó la partida.
        """
        text2.insert(tk.END, quote4, 'color')
        
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        frame.pack()

    def crear_menu_principal(self, ventana_principal):
        ventana_principal.title("FRAMEWORK")
        ventana_principal.geometry('600x500+400+20')  # Ancho por alto
        ventana_principal.configure(background='black')
        reajuste = Reajustar_tamano(ventana_principal)
        reajuste.pack(fill=tk.BOTH, expand=tk.YES)
        ventana_principal.resizable(False, False)

    def colocar_boton_jugar(self):
        boton_jugar = tk.Button(ventana_principal, text="Jugar", font=self.fnt_btn, fg=self.clr_fnt_btn, activeforeground=self.clr_fnt_btn,
                                background=self.clr_btn, activebackground=self.clr_btn_pres, command=self.mostrar_reglas)
        boton_jugar.place(x=240, y=self.y_boton_menu, width=90, height=40)

    def colocar_boton_reglas(self):
        boton_reglas = tk.Button(ventana_principal, text="Reglas del juego", font=self.fnt_btn, fg=self.clr_fnt_btn,
                                 activeforeground=self.clr_fnt_btn, background=self.clr_btn, activebackground=self.clr_btn_pres, command=self.mostrar_reglas)
        boton_reglas.place(x=345, y=self.y_boton_menu, width=120, height=40)

    def colocar_boton_autores(self):
        boton_autores = tk.Button(ventana_principal, text="Autores", font=self.fnt_btn, fg=self.clr_fnt_btn,
                                  activeforeground=self.clr_fnt_btn, background=self.clr_btn, activebackground=self.clr_btn_pres, command=self.validar)
        boton_autores.place(x=480, y=self.y_boton_menu, width=90, height=40)

    def validar(self):
        messagebox.showwarning("Arial", "Password incorrecto")


#########################################################################################################################################################

vista = Vista()

ventana_principal = tk.Tk()

vista.crear_menu_principal(ventana_principal)
vista.colocar_boton_jugar()
vista.colocar_boton_reglas()
vista.colocar_boton_autores()

ventana_principal.mainloop()
