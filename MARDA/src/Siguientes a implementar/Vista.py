import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import font
import PIL.Image
import PIL.ImageTk
from PIL import Image,ImageTk
import pygame
import queue

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WOOD = (255,211,155)
BROWN = (94, 9, 9)
GREY = (130,130,130)

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 44
HEIGHT = 44 
# This sets the margin between each cell
MARGIN = 2


class Reajustar_tamano(Frame):
    """Clase que permite ajustar una imagen al tamano de ventana cada vez que esta crezca o se haga pequena"""
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
    """Representacion grafica del framework"""

    def __init__(self,controlador):
        """Inicializador de la clase"""
        
        self.tablero = None
        self.eventos = None
        
        #Referencia al controldor
        self.controlador = controlador
        #Rutas para imagenes de fondo
        self.ruta_img_principal = 'img/fondo2.png'
        self.ruta_autores = 'img/autores2.png'
        self.ruta_menu = 'img/go2.jpg'
        # Colores y fuentes para los botones de la vista
        self.fuente_boton = ('Comic Sans', 10, 'italic bold')
        self.color_boton = "#008287"#"#0B6121" 
        self.color_boton_pres = "white" 
        self.color_boton_go = "#8D6E63"
        self.boton_des = "#5e3631"
        self.color_fuente_boton = "white"
        self.color_fuente_boton_press = "#008287"#"#0B6121"
        self.color_fuente_boton_go_press = "#8D6E63"
        self.y_boton = 430
        #Ventanas que se crearan en la vista
        self.ventana_principal = None
        self.ventana_autores = None
        self.menu = None
        self.menu_nombres = None
        self.ventana_nigiri = None
        #Botones de la vista
        self.boton_listo = None
        self.boton_volver = None
        self.boton_entrar = None
        self.boton_autores = None
        self.boton_reglas = None
        self.boton_jugar = None
        self.boton_continuar = None
        self.boton_nigiri_listo = None
        self.boton_nigiri_continuar = None
        #Entradas de texto
        self.nombre1 = None
        self.nombre2 = None
        self.piedras_j1 = None
        self.piedras_j2 = None
        self.screen = 0
    
    #################################################################### VENTANAS DE LA VISTA ###################################################################   
    def generar_ventana(self,ventana,titulo,dimensiones,color_fondo,ruta_imagen,op):
        """Permite generar una ventana grafica.
        
            Parametros: ventana: ventana que se dibujara.
                        titulo: titulo que tendra la ventana.
                        dimensiones: dimensiones de la ventana.
                        color_fondo: color de fondo de la ventana en caso de que no cargue la imagen.
                        ruta_imagen: ruta de la imagen para el fondo.
                        op : indica si se desea reajustar la imagen de fondo o no."""
        ventana.title(titulo)
        ventana.geometry(dimensiones)  # Ancho por alto
        ventana.configure(background=color_fondo)
        if(op != "no"):
            reajuste = Reajustar_tamano(ventana,ruta_imagen)
            reajuste.pack(fill=tk.BOTH, expand=tk.YES)
        ventana.resizable(False, False)

    def mostrar_info(self):
        """Genera la ventana con toda la informacion del juego"""
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
        self.colocar_boton_volver(win, "Volver",10,590,80,30,self.color_boton_go,"","",self.color_boton_go)
        frame.pack()

    def mostrar_ventana_autores(self):
        """Muestra la ventana de los autores del framework"""
        self.ventana_autores = tk.Toplevel()
        self.generar_ventana(self.ventana_autores,"Autores",'540x379+430+70','black',self.ruta_autores,"")
        self.colocar_boton_volver(self.ventana_autores, "Cerrar",450,340,80,30,self.color_boton,"","",self.color_boton)#Modularizar este boton
        self.ventana_autores.mainloop()

    def mostrar_ventana_inicial(self):
        """Muestra la ventana inicial del framework"""
        self.ventana_principal = tk.Tk()
        self.generar_ventana(self.ventana_principal,"FRAMEWORK",'600x500+400+20','black',self.ruta_img_principal,"")
        self.colocar_boton(self.ventana_principal,self.boton_autores, "Autores", 490, 430, 90, 40, self.color_boton,self.color_boton_pres, self.color_fuente_boton,self.color_fuente_boton_press,self.controlador.boton_autores_presionado)
        self.colocar_boton_entrar(self.ventana_principal)
        self.ventana_principal.mainloop()

    def mostrar_menu_inicial(self, destruir):
        """Muestra la ventana de menu inicial del juego"""

        if(destruir == 1):
            self.ventana_principal.destroy()
            
        self.menu = tk.Tk()
        self.generar_ventana(self.menu ,"Juego del Go",'520x420+440+70','black',self.ruta_menu,"")
        self.colocar_boton(self.menu,self.boton_reglas , "Reglas del juego", 260, 370, 120, 40, self.color_boton_go ,self.color_fuente_boton_go_press, self.color_fuente_boton ,self.color_boton_go ,self.controlador.boton_reglas_presionado)
        self.colocar_boton(self.menu,self.boton_jugar , "Jugar", 30, 370, 90, 40, self.color_boton_go ,self.color_fuente_boton_go_press, self.color_fuente_boton ,self.color_boton_go ,self.controlador.boton_jugar_presionado)
        self.colocar_boton_volver(self.menu, "Volver", 390, 370, 90,40, self.color_boton_go, "r1", self.controlador.iniciar_framework,self.color_fuente_boton_go_press) 
        self.colocar_boton_cargar(self.menu, 130, 370, 120, 40)
          
        self.menu.mainloop()
        
    def mostrar_menu_nombres(self):
        """Muestra la ventana para ingresar los nombres de cada jugador"""
        self.menu.destroy()
        self.menu_nombres = tk.Tk()
        self.generar_ventana(self.menu_nombres,"Go",'440x340+440+70','black',self.ruta_menu,"no")
        #Se realiza de esta forma ya que los inputs no salen si se coloca el fondo como los demas
        imagen_para_fondo = Image.open(self.ruta_menu)
        imagen_fondo = ImageTk.PhotoImage(imagen_para_fondo)
        label1 = tk.Label(self.menu_nombres, image=imagen_fondo)
        label1.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.nombre1 = tk.Entry(self.menu_nombres, justify=tk.CENTER, width=50)
        self.colocar_input(self.nombre1,25,"Nombre del jugador 1","")

        self.nombre2 = tk.Entry(self.menu_nombres, justify=tk.CENTER, width=50)
        self.colocar_input(self.nombre2,0,"Nombre del jugador 2","")
            
        self.colocar_boton(self.menu_nombres,self.boton_reglas , "Reglas del juego", 160, 300, 120, 30, self.color_boton_go ,self.color_fuente_boton_go_press, self.color_fuente_boton ,self.color_boton_go ,self.controlador.boton_reglas_presionado)
        self.colocar_boton_listo(self.menu_nombres, 180, 120, 80, 30)  
        self.colocar_boton_continuar(self.menu_nombres, 60, 300, 80, 30)
        self.colocar_boton_volver(self.menu_nombres, "Volver", 300, 300,80, 30, self.color_boton_go, "r2", self.controlador.boton_entrar_presionado,self.color_fuente_boton_go_press)

        self.menu_nombres.mainloop()

    def mostrar_ventana_nigiri(self):
        """Muestra la ventana para ingresar la cantidad de piedras de cada jugador"""
        self.menu_nombres.destroy()
        self.ventana_nigiri = tk.Tk()
        self.generar_ventana(self.ventana_nigiri,"Go",'440x340+440+70','black',self.ruta_menu,"no")
        imagen_para_fondo = Image.open(self.ruta_menu)
        imagen_fondo = ImageTk.PhotoImage(imagen_para_fondo)
        label1 = tk.Label(self.ventana_nigiri, image=imagen_fondo)
        label1.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        
        placeholder = " Cantidad de piedras de " + self.controlador.retornar_nombre_jugador1()
        placeholder2 =" Cantidad de piedras de " + self.controlador.retornar_nombre_jugador2()
        
        self.piedras_j1 = tk.Entry(self.ventana_nigiri, justify=tk.CENTER, width=50)
        self.colocar_input(self.piedras_j1,25,placeholder,"piedras")
        
        self.piedras_j2 = tk.Entry(self.ventana_nigiri, justify=tk.CENTER, width=50)
        self.colocar_input(self.piedras_j2,0, placeholder2,"piedras")

        self.colocar_boton(self.ventana_nigiri,self.boton_reglas , "Reglas del juego",220, 300, 120, 30, self.color_boton_go ,self.color_fuente_boton_go_press, self.color_fuente_boton ,self.color_boton_go ,self.controlador.boton_reglas_presionado)
        self.colocar_boton_nigiri_listo(self.ventana_nigiri, 180, 120, 80, 30)
        self.colocar_boton_nigiri_continuar(self.ventana_nigiri, 120, 300, 80, 30)

        self.ventana_nigiri.mainloop()
    
    ############################################################ BOTONES SIN ALGUNA FUNCION ESPECIFICA ##########################################################
    
    def colocar_boton(self, ventana,boton, texto, x, y, ancho, alto, fondo_boton,color_boton_press, color_fuente_boton,color_fuente_press,metodo):
        """Permite colocar un boton que no tenga alguna funcion en especifica
            
            Parametros: ventana:    ventana donde sera colocado el boton
                        boton:  nombre del boton que se va a generar
                        texto:  titulo que tendra el boton.
                        x:  posicion horizontal en la ventana.
                        y:  posiciopn vertical en la ventana.
                        ancho:  ancho del boton
                        alto:   alto del boton
                        fondo_boton:    color de fondo del boton
                        color_boton_press:  color del boton al ser presionado
                        color_fuente_boton: color de las letras del boton
                        color_fuente_press: color de las letras cuando se presiona el boton
                        metodo: funcion que ejecutara el boton al ser presionado
        """
        boton = tk.Button(ventana, text=texto, font=self.fuente_boton, fg=color_fuente_boton,activeforeground=color_fuente_press, background=fondo_boton, activebackground=color_boton_press, command = metodo)
        boton.place(x=x, y=y, width=ancho, height=alto)
        self.hover_button (boton,fondo_boton,color_fuente_boton)
    
    ########################################################### BOTONES CON FUNCIONES ESPECIFICAS ###############################################################


    def colocar_boton_cargar(self,ventana,x,y,w,h):
        """Permite colocar el boton para cargar el jurgo.
            
            Parametros: ventana:    ventana donde sera colocado el boton.            
        """
        
        self.colocar_boton_cargar = tk.Button(ventana, text="Cargar juego", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_press,background=self.color_boton, activebackground=self.color_boton_pres,command=lambda: print("Cargar juego"))
        self.colocar_boton_cargar.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.colocar_boton_cargar,self.color_boton,self.color_fuente_boton)

    def colocar_boton_entrar(self,ventana):
        """Permite colocar el boton para entrar al framnework.
            
            Parametros: ventana:    ventana donde sera colocado el boton.            
        """
        self.boton_entrar = tk.Button(ventana, text="Ingresar", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_press,background=self.color_boton, activebackground=self.color_boton_pres,command=lambda: self.controlador.boton_entrar_presionado(1))
        self.boton_entrar.place(x=380, y=self.y_boton, width=90, height=40)
        self.hover_button(self.boton_entrar,self.color_boton,self.color_fuente_boton)

    def colocar_boton_volver(self, ventana, texto, x, y, w, h, color, opcion, metodo,color_fuente_press):
        """Permite colocar un boton para devolverse de ventana.
            
            Parametros: ventana:    ventana donde sera colocado el boton.
                        texto:  titulo que tendra el boton.
                        x:  posicion horizontal en la ventana.
                        y:  posiciopn vertical en la ventana.
                        w:  ancho del boton.
                        h:   alto del boton.
                        opcion: entero que representa una opcion para que el boton cierre o no una ventana principal.
                        color_fuente_press: color de las letras cuando se presiona el boton.
                        metodo: funcion que ejecutara el boton al ser presionado.
        """
        self.boton_volver = tk.Button(ventana, text=texto, font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=color_fuente_press,background=color, activebackground=self.color_boton_pres,command=lambda: self.controlador.boton_volver_presionado(ventana,metodo,opcion))
        self.boton_volver.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.boton_volver,color,self.color_fuente_boton)
        
    def colocar_boton_listo(self, ventana, x, y, w, h):
        """Permite colocar un boton que acepta los nombres ingresados en la ventana de nombres.
            
            Parametros: ventana:    ventana donde sera colocado el boton
                        x:  posicion horizontal en la ventana.
                        y:  posiciopn vertical en la ventana.
                        w:  ancho del boton
                        h:   alto del boton
        """
        self.boton_listo = tk.Button(ventana, text="Listo", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.color_boton_go, activebackground=self.color_boton_pres , command = self.controlador.obtener_nombres)
        self.boton_listo.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.boton_listo,self.color_boton_go,self.color_fuente_boton)
    
    def colocar_boton_nigiri_listo(self, ventana, x, y, w, h):
        """Permite colocar un boton que acepta la cantidad de piedra ingresada en la ventana de nigiri.
            
            Parametros: ventana:    ventana donde sera colocado el boton
                        x:  posicion horizontal en la ventana.
                        y:  posiciopn vertical en la ventana.
                        w:  ancho del boton
                        h:   alto del boton
        """
        self.boton_nigiri_listo = tk.Button(ventana, text="Listo", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.color_boton_go, activebackground=self.color_boton_pres , command = self.controlador.nigiri)
        self.boton_nigiri_listo.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.boton_nigiri_listo,self.color_boton_go,self.color_fuente_boton)
        
    def colocar_boton_continuar(self, ventana, x, y, w, h):
        """Permite colocar un boton que permite continuar una vez que se ingresaron los nombres correctamente en la ventana de nombres.
            
            Parametros: ventana:    ventana donde sera colocado el boton
                        x:  posicion horizontal en la ventana.
                        y:  posiciopn vertical en la ventana.
                        w:  ancho del boton
                        h:   alto del boton
        """
        self.boton_continuar = tk.Button(ventana, text="Continuar", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.boton_des, activebackground=self.color_boton_pres , command = self.controlador.boton_continuar_presionado)
        self.boton_continuar.config(state='disabled')
        self.boton_continuar.place(x=x, y=y, width=w, height=h)
        
    def colocar_boton_nigiri_continuar(self, ventana, x, y, w, h):
        """Permite colocar un boton que permite continuar una vez que se ingreso la cantidad de piedras correctamente en la ventana de nigiri.
            
            Parametros: ventana:    ventana donde sera colocado el boton
                        x:  posicion horizontal en la ventana.
                        y:  posiciopn vertical en la ventana.
                        w:  ancho del boton
                        h:   alto del boton
        """
        self.boton_nigiri_continuar = tk.Button(ventana, text="Continuar", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.boton_des, activebackground=self.color_boton_pres , command = self.controlador.cerrar_menu)
        self.boton_nigiri_continuar.config(state='disabled')
        self.boton_nigiri_continuar.place(x=x, y=y, width=w, height=h)

################################################################# INPUT DE LA VISTA #######################################################################

    def colocar_input(self, nombre,pady,texto,tipo):
        """Permite colocar una entrada de texto en la ventana correspondiente.
        
            Parametros: nombre: nombre del input que se desea colocar.
                        pady:   distancia en el eje vertical con otro widget.
                        texto: placeholder del input.
                        tipo:   representa el tipo de input que se quiere colocar.
        """
        if(tipo == "piedras"):
            nombre.bind("<Key>" , lambda args: nombre.config(show="*"))
            
        placeholder = texto
        nombre.insert(0, placeholder)
        nombre.bind("<FocusIn>", lambda args: nombre.delete('0', 'end'))
        nombre.pack(padx=5, pady=pady, ipadx=5, ipady=5)
    
################################################################# ACCIONES SECUNDARIAS ###################################################################
    def deshabilitar_input_nombre(self,n_input):
        """Permite deshabilitar el input de nombre una vez que se ingreso un nombre valido.
        
            Parametros: n_input:    numero del input que se quiere deshabilitar
        """
        if(n_input == 1):
            self.nombre1.config(state='disabled')
        elif (n_input ==2 ):
            self.nombre2.config(state='disabled')
            
    def deshabilitar_input_piedras(self,n_input):
        """Permite deshabilitar el input de piedras una vez que se ingreso una cantidad valida.
        
            Parametros: n_input:    numero del input que se quiere deshabilitar
        """
        if(n_input == 1):
            self.piedras_j1.config(state='disabled')
        elif (n_input == 2 ):
            self.piedras_j2.config(state='disabled')
            
    def deshabilitar_boton_listo(self,op):
        """Permite deshabilitar el boton de listo una vez que se ingreso un valor valido en los inputs de la ventana correspondiente.
        
            Parametros: op: identifica el boton que se quiere deshabiliar.
        """
        if(op == "nombres"):
            self.boton_listo['state'] = 'disabled',
            self.boton_listo['bg'] = self.boton_des
        elif (op == "nigiri"):
            self.boton_nigiri_listo.config(state='disabled',bg=self.boton_des)
    
    def habilitar_boton_continuar(self,opcion):
        """Permite habilitar el boton de continuar una vez que se ingreso un valor valido en los inputs de la ventana correspondiente.
        
            Parametros: opcion: identifica el boton que se quiere habiliar.
        """
        if opcion == 1:
            self.boton_continuar.config(state='normal',bg= self.color_boton_go)
        elif opcion == 2:
            self.boton_nigiri_continuar.config(state='normal',bg= self.color_boton_go)

    def volver(self, ventana_matar, metodo, opcion):
        """Permite devolverse a la ventana anterior
            
            Parametros: ventana_matar:  ventana que se quiere cerrar para devolverse
                        metodo: funcion que se ejecuta al cerrar una ventana
                        opcion: indica la ventana a la que se quiere devolver cuando se esta en las reglas."""
        ventana_matar.destroy()
        if(opcion == "r1"):
            metodo()
        elif (opcion == "r2"):
            metodo(0)
            
    ############################################################## MENSAJES DE LA VISTA ##################################################################
    def mostrar_error_nombres(self,num_jugador):
        """Muestra un msj de error en caso de que se ingrese un nombre invalido
            
            Parametros: num_jugador:    indica el numero de jugador que ingreso un nombre invalido
        """
        msj = "Debe ingresar un nombre para el jugador " + str(num_jugador)
        messagebox.showwarning("ERROR", msj)
        
    def mostrar_error_piedras(self,nombre,num_j):
        """Muestra un msj de error en caso de que se ingrese una cantidad de piedras invalida.
            
            Parametros: nombre:    indica el nombre del jugador que ingreso una cantidad de piedras invalida.
                        num_jugador:    indica el numero de jugador que ingreso un nombre invalido.
        """
        msj = ""
        if(num_j == 1):
            msj = str(nombre) + " ingrese una cantidad de piedras válida"
        elif(num_j == 2):
            msj = str(nombre) + " debe ingresar 1 o 2 piedras"
            
        messagebox.showwarning("ERROR", msj)
        
    def mostrar_fin_juego(self,nombre1,puntos_jugador_1,nombre2,puntos_jugador_2,ganador):
        """Muestra un msj para indicar el fin del juego"""
        tk.Tk().wm_withdraw()
        if(ganador != "Empate"):
            msj = nombre1 + " obtuvo " + str(puntos_jugador_1) + " puntos\n" + nombre2 + " obtuvo " + str(puntos_jugador_2) + " puntos.\n\nEl ganador es " + ganador + ".\n"
        else:
            msj = nombre1 + " obtuvo " + str(puntos_jugador_1) + " puntos\n" + nombre2 + " obtuvo " + str(puntos_jugador_2) + "puntos.\n\nEl juego termina empatado."
        
        messagebox.showinfo('Juego terminado', msj)
        
    def mostrar_salto_turno(self,jugador):
        """Muestra un msj para indicar que un jugador paso el turno"""
        tk.Tk().wm_withdraw()
        msj = jugador + " paso el turno.\n"
        messagebox.showinfo('Salto de turno', msj)
        
    def mostrar_error_posicion(self):
        """Muestra un msj para indicar un error al colocar una pieza."""
        tk.Tk().wm_withdraw()
        messagebox.showwarning('Jugada invalida', 'Escoja otra posicion')
        
    def mostrar_error_jugada_suicida(self):
        """Muestra un msj para indicar una jugada invalida"""
        tk.Tk().wm_withdraw()
        messagebox.showwarning('Jugada suicida!', 'Escoja otra posicion')
        
    def avisar_inicio_nigiri(self,nom1,nom2):
        """Muestra un msj para indicar el inicio del nigiri"""
        msj = "Bien " + nom1 +" y " + nom2 + " ahora inicia el nigiri.\nMucha suerte."
        messagebox.showinfo("Nigiri", msj)
        
    def mostrar_resultado_nigiri(self,color, piedras_j1, piedras_j2,nombre1,nombre2):
        """ Muestra el resultado del nigiri.
            
            Parametros: color:  indica el color que tendra el jugador.
                        piedras_j1 :    indica la canridad de piedras que eligio el jugador 1.
                        piedras_j2 :    indica la canridad de piedras que eligio el jugador 2.
                        nombre1:    nombre del jugador 1.
                        nombre2:    nombre del jugador 2.
        """          
        msj = nombre1 + " eligio " + str(piedras_j1) + " piedra(s)\n"+ nombre2 + " eligio " + str(piedras_j2) + " piedra(s).\n\n"
        msj2 = ""
        
        if(color == 1):
            msj2 = nombre1 + " juega con las piedras negras.\n" + nombre2 + " juega con las piedras blancas.\n"
        else:
            msj2 = nombre1 + " juega con las piedras blancas.\n" + nombre2 + " juega con las piedras negras.\n"
            
        messagebox.showinfo("Nigiri", msj + msj2)
        
    def mostrar_reglas_juego(self):
        """Muestra un msj que indica las reglas mas importates a la hora de jugar"""
        tk.Tk().wm_withdraw()
        msj = "• Se puede capturar una piedra o un conjunto de piedras y eliminarlas del tablero si están completamente rodeadas por piedras de otro color.\n\n• Se deben sacar las piedras rodeadas del tablero y guardarlas separadamente hasta el final de la partida.\n\n• Suicidio: No se permite hacer una jugada ocupando una posición libre en el interior de una formación enemiga (suicidio), a no ser que esta jugada capture piedras enemigas.\n\n• Cuando los dos jugadores pasan consecutivamente de turno o cuando ya no hay espacios en el tablero, se acaba la partida.\n\n• Los jugadores cuentan los puntos de cada territorio,teniendo en cuenta las piedras prisioneras y gana el jugador que controla la mayor cantidad de territorio al finalizar la partida.\n\n"
        messagebox.showinfo("Reglas", msj)
        
    ############################################################## EFECTOS VISUALES #####################################################################
    def cambiar_color(self,event,color_fuente,color_boton,op,boton):
        """Produce un efecto de color al colocar el mouse dentro de un boton y al retirarlo
            
            Parametros: event:  reaccion al widget.
                        color_fuente:   color de la letra al aplicar el efecto.
                        color_boton:    color del boton al aplicar el efecto.
                        op: representa si se esta dentro o fuera del boton.
                        boton:  boton al que se le aplica el efecto visual.
        """ 
        if op == "dentro":
            boton.configure(bg=color_boton,fg=color_fuente)
        elif op == "fuera":
            boton.configure(bg=color_boton,fg=color_fuente)

    def hover_button (self,boton,color_boton,color_fuente):
        """Produce un efecto hover a un boton al producirse un evento
            
            Parametros: boton:  boton al que se le aplica el efecto visual.
                        color_boton:    color del boton al aplicar el efecto.
                        color_fuente:   color de la letra al aplicar el efecto.                
        """ 
        estado_boton = str(boton['state'])
        if estado_boton == 'normal':
            boton.bind( "<Enter>",lambda event: self.cambiar_color(event,color_boton,color_fuente,"dentro",boton) )
            boton.bind( "<Leave>", lambda event: self.cambiar_color(event,color_fuente,color_boton,"fuera",boton) )
    
################################################################### CODIGO DE PYGAME ####################################################################

    def iniciar_tablero(self):
        """Se construye la ventana donde estara el tablero"""
        # Se inicia pygame
        pygame.init()
        # Se coloca el ancho y alto de la pantalla
        WINDOW_SIZE = [750, 450]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Go Board Game")
             
    def colocar_label_pygame(self,color,msj,x,y):
        myfont = pygame.font.SysFont('Times New Roman', 16, 'bold')           
        label = myfont.render(msj, 1,color)
        self.screen.blit(label, (x,y))
        
    def dibujar_tablero(self, tablero,restantes_j1,restantes_j2,nombre1,nombre2,jugador_en_turno):
        """Dibuja las celdas del tablero en la ventana de pygame """
        # Fondo de la pantalla
        self.screen.fill(BROWN)
        #Se dibuja el tablero
        for row in range(8):
            for column in range(8):
                color = WOOD
                pygame.draw.rect(self.screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20,
                                WIDTH,
                                HEIGHT])
        for row in range(9):
            for column in range(9):
                if  tablero[row][column] == 'N':
                    pygame.draw.circle(self.screen,BLACK,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 12)
                elif tablero[row][column] == 'B':
                    pygame.draw.circle(self.screen,WHITE,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 12)
                elif tablero[row][column] == 'x':
                    pygame.draw.circle(self.screen,GREY,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 5)

                else:
                    pygame.draw.circle(self.screen,RED,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 5)
                    
                    
        ayuda = "Para ayuda presione 0."
        self.colocar_label_pygame((255,255,255),ayuda,410,20)
        
        ayuda = "Para saltar turno presione <esc>."
        self.colocar_label_pygame((255,255,255),ayuda,410,50) 
        
        div = "************************************"
        self.colocar_label_pygame((255, 255, 255),div,410,80)
            
        msj_1 = "Piedras restantes de " + nombre1 + ": " + str(restantes_j1)
        self.colocar_label_pygame((255, 255, 255),msj_1,410,130)
        
        msj_2 = "Piedras restantes de " + nombre2 + ": " + str(restantes_j2)
        self.colocar_label_pygame((255, 255, 255),msj_2,410,180)
   
        j_turno = "Jugador en turno: " + jugador_en_turno + "."
        self.colocar_label_pygame((73,169,69),j_turno,410,230)
        
        div2 = "************************************"
        self.colocar_label_pygame((255, 255, 255),div2,410,280)
        
        
    
    
        pygame.display.flip()