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

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 44
HEIGHT = 44 
# This sets the margin between each cell
MARGIN = 2


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

    def __init__(self,controlador):
        
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
        self.color_boton = "#0B6121" 
        self.color_boton_pres = "white" #848484
        self.color_boton_go = "#8D6E63"
        self.boton_des = "#5e3631"
        self.color_fuente_boton = "white"
        self.color_fuente_boton_press = "#0B6121"
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
        ventana.title(titulo)
        ventana.geometry(dimensiones)  # Ancho por alto
        ventana.configure(background=color_fondo)
        if(op != "no"):
            reajuste = Reajustar_tamano(ventana,ruta_imagen)
            reajuste.pack(fill=tk.BOTH, expand=tk.YES)
        ventana.resizable(False, False)

    def mostrar_info(self):
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
        self.ventana_autores = tk.Toplevel()
        self.generar_ventana(self.ventana_autores,"Autores",'540x379+430+70','black',self.ruta_autores,"")
        self.colocar_boton_volver(self.ventana_autores, "Cerrar",450,340,80,30,self.color_boton,"","",self.color_boton)#Modularizar este boton
        self.ventana_autores.mainloop()

    def mostrar_ventana_inicial(self):
        self.ventana_principal = tk.Tk()
        self.generar_ventana(self.ventana_principal,"FRAMEWORK",'600x500+400+20','black',self.ruta_img_principal,"")
        self.colocar_boton(self.ventana_principal,self.boton_autores, "Autores", 490, 430, 90, 40, self.color_boton,self.color_boton_pres, self.color_fuente_boton,self.color_fuente_boton_press,self.controlador.boton_autores_presionado)
        self.colocar_boton_entrar(self.ventana_principal)
        self.ventana_principal.mainloop()

    def mostrar_menu_inicial(self, destruir):
        if(destruir == 1):
            self.ventana_principal.destroy()
            
        self.menu = tk.Tk()
        self.generar_ventana(self.menu ,"Juego del Go",'520x420+440+70','black',self.ruta_menu,"")
        self.colocar_boton(self.menu,self.boton_reglas , "Reglas del juego", 205, 370, 120, 40, self.color_boton_go ,self.color_fuente_boton_go_press, self.color_fuente_boton ,self.color_boton_go ,self.controlador.boton_reglas_presionado)
        self.colocar_boton(self.menu,self.boton_jugar , "Jugar", 100, 370, 90, 40, self.color_boton_go ,self.color_fuente_boton_go_press, self.color_fuente_boton ,self.color_boton_go ,self.controlador.boton_jugar_presionado)
        self.colocar_boton_volver(self.menu, "Volver", 340, 370, 90,40, self.color_boton_go, "r1", self.controlador.iniciar_framework,self.color_fuente_boton_go_press) 

        self.menu.mainloop()
        
    def mostrar_menu_nombres(self):
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
        boton = tk.Button(ventana, text=texto, font=self.fuente_boton, fg=color_fuente_boton,activeforeground=color_fuente_press, background=fondo_boton, activebackground=color_boton_press, command = metodo)
        boton.place(x=x, y=y, width=ancho, height=alto)
        self.hover_button (boton,fondo_boton,color_fuente_boton)
    
    ########################################################### BOTONES CON FUNCIONES ESPECIFICAS ###############################################################

    def colocar_boton_entrar(self,ventana):
        self.boton_entrar = tk.Button(ventana, text="Ingresar", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_press,background=self.color_boton, activebackground=self.color_boton_pres,command=lambda: self.controlador.boton_entrar_presionado(1))
        self.boton_entrar.place(x=380, y=self.y_boton, width=90, height=40)
        self.hover_button(self.boton_entrar,self.color_boton,self.color_fuente_boton)

    def colocar_boton_volver(self, ventana, texto, x, y, w, h, color, opcion, metodo,color_fuente_press):
        self.boton_volver = tk.Button(ventana, text=texto, font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=color_fuente_press,background=color, activebackground=self.color_boton_pres,command=lambda: self.controlador.boton_volver_presionado(ventana,metodo,opcion))
        self.boton_volver.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.boton_volver,color,self.color_fuente_boton)
        
    def colocar_boton_listo(self, ventana, x, y, w, h):
        self.boton_listo = tk.Button(ventana, text="Listo", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.color_boton_go, activebackground=self.color_boton_pres , command = self.controlador.obtener_nombres)
        self.boton_listo.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.boton_listo,self.color_boton_go,self.color_fuente_boton)
    
    def colocar_boton_nigiri_listo(self, ventana, x, y, w, h):
        self.boton_nigiri_listo = tk.Button(ventana, text="Listo", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.color_boton_go, activebackground=self.color_boton_pres , command = self.controlador.nigiri)
        self.boton_nigiri_listo.place(x=x, y=y, width=w, height=h)
        self.hover_button(self.boton_nigiri_listo,self.color_boton_go,self.color_fuente_boton)
        
    def colocar_boton_continuar(self, ventana, x, y, w, h):
        self.boton_continuar = tk.Button(ventana, text="Continuar", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.boton_des, activebackground=self.color_boton_pres , command = self.controlador.boton_continuar_presionado)
        self.boton_continuar.config(state='disabled')
        self.boton_continuar.place(x=x, y=y, width=w, height=h)
        
    def colocar_boton_nigiri_continuar(self, ventana, x, y, w, h):
        self.boton_nigiri_continuar = tk.Button(ventana, text="Continuar", font=self.fuente_boton, fg=self.color_fuente_boton, activeforeground=self.color_fuente_boton_go_press, background=self.boton_des, activebackground=self.color_boton_pres , command = self.controlador.cerrar_menu)
        self.boton_nigiri_continuar.config(state='disabled')
        self.boton_nigiri_continuar.place(x=x, y=y, width=w, height=h)

################################################################# INPUT DE LA VISTA #######################################################################

    def colocar_input(self, nombre,pady,texto,tipo):
        if(tipo == "piedras"):
            nombre.bind("<Key>" , lambda args: nombre.config(show="*"))
            
        placeholder = texto
        nombre.insert(0, placeholder)
        nombre.bind("<FocusIn>", lambda args: nombre.delete('0', 'end'))
        nombre.pack(padx=5, pady=pady, ipadx=5, ipady=5)
    
################################################################# ACCIONES SECUNDARIAS ###################################################################
    def deshabilitar_input_nombre(self,n_input):
        if(n_input == 1):
            self.nombre1.config(state='disabled')
        elif (n_input ==2 ):
            self.nombre2.config(state='disabled')
            
    def deshabilitar_input_piedras(self,n_input):
        if(n_input == 1):
            self.piedras_j1.config(state='disabled')
        elif (n_input == 2 ):
            self.piedras_j2.config(state='disabled')
            
    def deshabilitar_boton_listo(self,op):
        if(op == "nombres"):
            self.boton_listo['state'] = 'disabled',
            self.boton_listo['bg'] = self.boton_des
        elif (op == "nigiri"):
            self.boton_nigiri_listo.config(state='disabled',bg=self.boton_des)
    
    def habilitar_boton_continuar(self,opcion):
        if opcion == 1:
            self.boton_continuar.config(state='normal',bg= self.color_boton_go)
        elif opcion == 2:
            self.boton_nigiri_continuar.config(state='normal',bg= self.color_boton_go)

    def volver(self, ventana_matar, metodo, opcion):
        ventana_matar.destroy()
        if(opcion == "r1"):
            metodo()
        elif (opcion == "r2"):
            metodo(0)
            
    ############################################################## MENSAJES DE LA VISTA ##################################################################
    def mostrar_error_nombres(self,num_jugador):
        msj = "Debe ingresar un nombre para el jugador " + str(num_jugador)
        messagebox.showwarning("ERROR", msj)
        
    def mostrar_error_piedras(self,nombre,num_j):
        msj = ""
        if(num_j == 1):
            msj = str(nombre) + " ingrese una cantidad de piedras válida"
        elif(num_j == 2):
            msj = str(nombre) + " debe ingresar 1 o 2 piedras"
            
        messagebox.showwarning("ERROR", msj)
        
    def mostrar_fin_juego(self):
        tk.Tk().wm_withdraw()
        messagebox.showinfo('Juego terminado', 'Fin del juego')
        
    def mostrar_error_posicion(self):
        tk.Tk().wm_withdraw()
        messagebox.showwarning('Jugada invalida', 'Escoja otra posicion')
        
    def mostrar_error_jugada_suicida(self):
        tk.Tk().wm_withdraw()
        messagebox.showwarning('Jugada suicida!', 'Escoja otra posicion')
        
    def mostrar_error_fuera_tablero(self):
        tk.Tk().wm_withdraw()
        messagebox.showwarning('Jugada invalida', 'Debe seleccionar una posicion dentro del tablero')
        
    def avisar_inicio_nigiri(self,nom1,nom2):
        msj = "Bien " + nom1 +" y " + nom2 + " ahora inicia el nigiri.\nMucha suerte."
        messagebox.showinfo("Nigiri", msj)
        
    def mostrar_resultado_nigiri(self,color, piedras_j1, piedras_j2,nombre1,nombre2):
        msj = nombre1 + " eligio " + str(piedras_j1) + " piedra(s)\n"+ nombre2 + " eligio " + str(piedras_j2) + " piedra(s).\n\n"
        msj2 = ""
        
        if(color == 1):
            msj2 = nombre1 + " juega con las piedras negras.\n" + nombre2 + " juega con las piedras blancas.\n"
        else:
            msj2 = nombre1 + " juega con las piedras blancas.\n" + nombre2 + " juega con las piedras negras.\n"
            
        messagebox.showinfo("Nigiri", msj + msj2)
        
    def mostrar_reglas_juego(self):
        tk.Tk().wm_withdraw()
        msj = "• Se puede capturar una piedra o un conjunto de piedras y eliminarlas del tablero si están completamente rodeadas por piedras de otro color.\n\n• Se deben sacar las piedras rodeadas del tablero y guardarlas separadamente hasta el final de la partida.\n\n• Suicidio: No se permite hacer una jugada ocupando una posición libre en el interior de una formación enemiga (suicidio), a no ser que esta jugada capture piedras enemigas.\n\n• Cuando los dos jugadores pasan consecutivamente de turno o cuando ya no hay espacios en el tablero, se acaba la partida.\n\n• Los jugadores cuentan los puntos de cada territorio,teniendo en cuenta las piedras prisioneras y gana el jugador que controla la mayor cantidad de territorio al finalizar la partida.\n\n"
        messagebox.showinfo("Reglas", msj)
        
    ############################################################## EFECTOS VISUALES #####################################################################
    def cambiar_color(self,event,color_fuente,color_boton,op,boton):
        if op == "dentro":
            boton.configure(bg=color_boton,fg=color_fuente)
        elif op == "fuera":
            boton.configure(bg=color_boton,fg=color_fuente)

    def hover_button (self,boton,color_boton,color_fuente):
        estado_boton = str(boton['state'])
        if estado_boton == 'normal':
            boton.bind( "<Enter>",lambda event: self.cambiar_color(event,color_boton,color_fuente,"dentro",boton) )
            boton.bind( "<Leave>", lambda event: self.cambiar_color(event,color_fuente,color_boton,"fuera",boton) )
    
################################################################### CODIGO DE PYGAME ####################################################################

    def iniciar_tablero(self):
        # Initialize pygame
        pygame.init()
        
        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [600, 450]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        # Set title of screen
        pygame.display.set_caption("Go Board Game")
               
    def dibujar_tablero(self, tablero):
        # Set the screen background
        self.screen.fill(BROWN)
 
        # Draw the grid
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
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 13)
                elif tablero[row][column] == 'B':
                    pygame.draw.circle(self.screen,WHITE,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 13)

                else:
                    pygame.draw.circle(self.screen,RED,((MARGIN + WIDTH) * column + MARGIN + 20,
                                (MARGIN + HEIGHT) * row + MARGIN + 20), 5)
        pygame.display.flip()