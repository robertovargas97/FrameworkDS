import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import font
import PIL.Image
import PIL.ImageTk
from PIL import Image, ImageTk


class Reajustar_tamano(Frame):
    def __init__(self, master,ruta, *pargs):
        Frame.__init__(self, master, *pargs)
        self.ruta_fondo = ruta
        self.imagen_para_fondo = Image.open(self.ruta_fondo)
        self.img_copy = self.imagen_para_fondo.copy()
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_para_fondo)
        self.fondo = tk.Label(self, image=self.imagen_fondo)
        self.fondo.pack(fill=tk.BOTH, expand=tk.YES)
        self.fondo.bind('<Configure>', self._reajustar_imagen)

    def _reajustar_imagen(self, event):
        nuevo_ancho = event.width
        nueva_altura = event.height

        self.imagen_para_fondo = self.img_copy.resize((nuevo_ancho, nueva_altura))
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_para_fondo)
        self.fondo.configure(image=self.imagen_fondo)


class Vista(Frame):

    def __init__(self,):
        # Colores para los botones de la vista
        self.fnt_btn = ('Comic Sans', 10, 'italic bold')
        self.clr_btn = "#848484"
        self.clr_fnt_btn = "white"
        self.clr_btn_pres = "#0B6121"
        self.clr_btn_menu = "#8D6E63"
        self.y_boton = 430
        self.ventana_principal = None
        self.ventana_autores = None
        self.menu = None
        self.ruta_img_principal = 'img/fondo2.png'
        self.ruta_autores = 'img/autores2.png'
        self.ruta_menu = 'img/go2.jpg'

    def mostrar_reglas(self):
        win = tk.Toplevel()
        win.title("Reglas del juego")
        win.geometry("+%d+%d" % (150, 30))
        win.resizable(False, False)
        frame = tk.Frame(win)
        ruta_imagen = 'img/go.jpg'

        imagen_reglas = tk.Text(frame, height=39, width=50)
        im = PIL.Image.open(ruta_imagen)
        im = im.resize((480, 624))
        foto = PIL.ImageTk.PhotoImage(im)
        foto.image = foto
        imagen_reglas.image_create(tk.END, image=foto)
        imagen_reglas.pack(side=tk.LEFT)

        texto_reglas = tk.Text(frame, height=39, width=65, bg='dark grey')
        scroll = tk.Scrollbar(frame, command=texto_reglas.yview)
        texto_reglas.configure(yscrollcommand=scroll.set)
        texto_reglas.tag_configure('bold_italics', font=('Arial', 10, 'italic'))
        texto_reglas.tag_configure('big', foreground='#795548',font=('Arial', 15, 'bold'))
        texto_reglas.tag_configure('color', foreground='#000000',font=('Arial', 10, 'bold'))
        
        # Texto de jugando la partida
        texto_reglas.insert(tk.END, ' \n ¿En que consiste el juego de GO?', 'big')
        quote2 = """
        \t• Consiste en colocar las piedras en las intersecciones del tablero.\n
        \t• Antes de comenzar se asigna un color a cada jugador. \n
        \t• Las negras inician la partida y una vez colocada una piedra, no se
        \tpuede volver a mover. \n
        \t• Se puede capturar una piedra o un conjunto de piedras y eliminarlas 
        \tdel tablero si están completamente rodeadas por piedras de otro color.  
        """
        texto_reglas.insert(tk.END, quote2, 'color')
        
        # Texto de las reglas basicas del juego
        texto_reglas.insert(tk.END, '\n Objetivo', 'big')
        quote = """
        \t• El objetivo del juego, cuya traducción aproximada es juego de 
        \trodear, es controlar una cantidad de territorio mayor a la del 
        \toponente.\n 
        \t• Para controlar un área, debe rodearse con las piedras.\n
        \t• Gana el jugador que controla la mayor cantidad de territorio 
        \tal finalizar la partida.
        """ 
        texto_reglas.insert(tk.END, quote, 'color')

        # Texto de las reglas basicas del juego
        texto_reglas.insert(tk.END, '\n Tablero', 'big')
        quote = """
        \t• El tablero 9x9 es el más pequeño y se utiliza o para principiantes 
        \to para partidas muy rápidas. Luego el tablero 13x13 es el tablero 
        \tpara jugadas intermedias.\n
        \t• El tablero 19x19 es el tablero estándar de go, y es en este donde 
        \tse juegan casi todas las partidas.
        """ 
        texto_reglas.insert(tk.END, quote, 'color')

        # Texto del proposito del juego
        texto_reglas.insert(tk.END, ' \n Piedras', 'big')
        quote1 = """
        \t• Las fichas del go se llaman piedras (Goishi) y son negras y 
        \tblancas.\n
        \t• Cada jugador puede llevar las que quiera pero debido a que 
        \tlas negras empiezan primero (esto se compensa como veremos 
        \tluego) se puede preferir unas u otras.   
        """
        texto_reglas.insert(tk.END, quote1, 'color')

        # Texto del inicio del juego
        texto_reglas.insert(tk.END, ' \n ¿Quién inicia primero?', 'big')
        quote1 = """
        \t• Normalmente se decide quien va a llevar cada color mediante el 
        \t"nigiri". Esto consiste en que un jugador coge un número de piedras 
        \tsin enseñarlas y el otro coge una o dos piedras para indicar par o 
        \timpar.\n 
        \t• Al abrir sus puños y soltarlas si el que elegía par o impar 
        \tacierta llevará negras, si falla llevará blancas.  
        """
        texto_reglas.insert(tk.END, quote1, 'color')

        # Texto de jaque
        texto_reglas.insert(tk.END, ' \n Captura de piedras', 'big')
        quote2 = """
        \t• Cuando un jugador hace una jugada que priva de su última libertad 
        \ta una piedra o formación del oponente, debe sacar las piedras 
        \trodeadas del tablero ty guardarlas separadamente hasta el final de 
        \tla partida.
        """
        texto_reglas.insert(tk.END, quote2, 'color')

        # Texto de Jaque Mate
        texto_reglas.insert(tk.END, ' \n Jugadas no permitidas', 'big')
        quote3 = """
        \t• Suicidio: No se permite hacer una jugada ocupando una posición 
        \tlibre en el interior de una formación enemiga (suicidio), a no ser 
        \tque esta jugada capture piedras enemigas.  
        """
        texto_reglas.insert(tk.END, quote3, 'color')

        # Texto de Tablas por ahogado
        texto_reglas.insert(tk.END, '\n Pasar el turno', 'big')
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
        texto_reglas.insert(tk.END, quote4, 'color')
        
        # Texto de Tablas por ahogado
        texto_reglas.insert(tk.END, '\n Fin de la partida', 'big')
        quote4 = """
        \t•Una vez finalizada la partida, se retiran las piedras muertas 
        \tde cada bando añadiéndolas a las capturadas.\n
        \t•Se conocen como piedras muertas a aquellas que se encuentran 
        \trodeada,por lo que no podrían resistir una eventual captura.\n 
        \t•Entonces, los jugadores cuentan los puntos de cada territorio, 
        \tteniendo en cuenta las piedras prisioneras y las muertas, y 
        \tse decide quién ganó la partida.
        """
        texto_reglas.insert(tk.END, quote4, 'color')
        
        texto_reglas.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.colocar_boton(win,"Volver",10,590,80,30,self.clr_btn_menu)
        frame.pack()

    def mostrar_autores(self):
        self.ventana_autores = tk.Toplevel()
        self.ventana_autores.title("Autores")
        self.ventana_autores.geometry('540x379+430+70')  # Ancho por alto
        self.ventana_autores.configure(background='black')
        reajuste = Reajustar_tamano(self.ventana_autores,self.ruta_autores)
        reajuste.pack(fill=tk.BOTH, expand=tk.YES)
        self.ventana_autores.resizable(False, False)
        self.colocar_boton(self.ventana_autores,"Cerrar",450,340,80,30,self.clr_btn)
        self.ventana_autores.mainloop()
        
    def mostrar_pantalla_inicial(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("FRAMEWORK")
        self.ventana_principal.geometry('600x500+400+20')  # Ancho por alto
        self.ventana_principal.configure(background='black')
        reajuste = Reajustar_tamano(self.ventana_principal,self.ruta_img_principal)
        reajuste.pack(fill=tk.BOTH, expand=tk.YES)
        self.ventana_principal.resizable(False, False)
        self.colocar_boton_entrar(self.ventana_principal)
        self.colocar_boton_autores(self.ventana_principal)
        self.ventana_principal.mainloop()
        
    def mostrar_menu_inicial(self,ventana_principal):
        self.menu = tk.Toplevel()
        self.menu.title("Juego del Go")
        self.menu.geometry('520x420+440+70')  # Ancho por alto
        self.menu.configure(background='black')
        reajuste = Reajustar_tamano(self.menu,self.ruta_menu)
        reajuste.pack(fill=tk.BOTH, expand=tk.YES)
        self.menu.resizable(False, False)
        self.colocar_boton(self.menu,"Volver",340,370,90,40,self.clr_btn_menu)
        self.colocar_boton_reglas(self.menu)
        self.colocar_boton_jugar(self.menu)
        self.menu.mainloop()

    def colocar_boton(self,ventana,texto,x,y,w,h,color):
        boton = tk.Button(ventana, text=texto, font=self.fnt_btn, fg="white",
                                  activeforeground="white", background=color  , activebackground=self.clr_btn_pres, command=lambda: ventana.destroy())
        boton.place(x=x, y=y, width=w, height=h)
        
    def colocar_boton_entrar(self,ventana):
        boton_entrar = tk.Button(ventana, text="Ingresar", font=self.fnt_btn, fg=self.clr_fnt_btn, activeforeground=self.clr_fnt_btn,
                                background=self.clr_btn, activebackground=self.clr_btn_pres, command=lambda: self.mostrar_menu_inicial(self.ventana_principal))
        boton_entrar.place(x=380, y=self.y_boton, width=90, height=40)

    def colocar_boton_autores(self,ventana):
        boton_autores = tk.Button(ventana, text="Autores", font=self.fnt_btn, fg=self.clr_fnt_btn,
                                  activeforeground=self.clr_fnt_btn, background=self.clr_btn, activebackground=self.clr_btn_pres, command=self.mostrar_autores)
        boton_autores.place(x=490, y=self.y_boton, width=90, height=40)
        
    def colocar_boton_reglas(self,ventana):
        boton_reglas = tk.Button(ventana, text="Reglas del juego", font=self.fnt_btn, fg=self.clr_fnt_btn,
                                 activeforeground=self.clr_fnt_btn, background="#8D6E63", activebackground=self.clr_btn_pres, command=self.mostrar_reglas)
        boton_reglas.place(x=205, y=370, width=120, height=40)
        
    def colocar_boton_jugar(self,ventana):
        boton_jugar = tk.Button(ventana, text="Jugar", font=self.fnt_btn, fg=self.clr_fnt_btn, activeforeground=self.clr_fnt_btn,
                                background=self.clr_btn_menu, activebackground=self.clr_btn_pres, command=lambda: self.validar())
        boton_jugar.place(x=100, y=370, width=90, height=40)
        
    def validar(self):
        messagebox.showwarning("Arial", "Password incorrecto")


#########################################################################################################################################################

vista = Vista()
vista.mostrar_pantalla_inicial()


