from Tablero import Tablero
from Jugador import Jugador
from Vista import Vista
from Arbitro import Arbitro
from TableroGo import TableroGo
from JugadorGo import JugadorGo
from VistaGo import VistaGo
from ArbitroGo import ArbitroGo

from tkinter import *
from tkinter import messagebox
from pygame.locals import *
import queue
import pygame

WIDTH = 44
HEIGHT = 44 
MARGIN = 2


class Controlador():
    """Clase encargada de toda la interaccion entre la vista y el modelo."""

    def __init__(self):
        """Contructor de la clase."""
        # Se crea la vista en el controlador para poder interactuar , ademas de instancias del modelo para poder actualizar datos por detras (Composition)
        self.vista = Vista ( VistaGo(self) ) ################
        self.tablero = None
        self.jugador1 = None
        self.jugador2 = None
        self.arbitro = None
        #Variables necesarias para el control
        self.tablero_logico = []
        self.eventos = queue.Queue()
        self.nombre1 = ""
        self.nombre2 = ""
        self.piedras_jugador1 = 0
        self.piedras_jugador2 = 0
        self.color_jugador1 = 0
        self.color_jugador2 = 0
        self.color = 1
        self.cambiar_turno = 0
        self.m_tablero = False
    
    ################################################## REACCIONES A EVENTOS DE LA VISTA ##########################################################################
    def iniciar_framework(self):
        """Inicia la interaccion entre el modelo y la vista para mostrar el framework."""
        self.vista.obt_vista_concreta().mostrar_ventana_inicial()
        
    def boton_autores_presionado(self):
        """Responde al evento de presionar el boton de autores para indicarle a la vista que debe mostrar una nueva ventana."""
        self.vista.mostrar_ventana_autores()
    
    def boton_reglas_presionado(self):
        """Responde al evento de presionar el boton de reglas para indicarle a la vista que debe mostrar una nueva ventana."""
        self.vista.obt_vista_concreta().mostrar_info()
        
    def boton_entrar_presionado(self,op):
        """Responde al evento de presionar el boton de entrar para indicarle a la vista que debe mostrar una nueva ventana."""
        self.vista.obt_vista_concreta().mostrar_menu_inicial(op)

    def boton_volver_presionado(self,ventana, metodo, opcion):
        """Responde al evento de presionar el boton de volver para indicarle a la vista que debe devolverse a una nueva anterior."""
        self.vista.obt_vista_concreta().volver(ventana, metodo, opcion)
        
    def boton_jugar_presionado(self):
        """Responde al evento de presionar el boton de jugar para indicarle a la vista que debe mostrar una nueva ventana."""
        self.vista.mostrar_menu_nombres()
        
    def boton_continuar_presionado(self):
        """Responde al evento de presionar el boton de continuar para indicarle a la vista que debe mostrar una nueva ventana."""
        self.vista.obt_vista_concreta().avisar_inicio_nigiri(self.nombre1,self.nombre2)
        self.vista.obt_vista_concreta().mostrar_ventana_nigiri() 
        
    def cerrar_menu(self):
        """Responde al evento de presionar el boton de continuar en el nigiri para indicarle a la vista que cierre el menu para poder desplegar el tablero."""
        self.vista.obt_vista_concreta().ventana_nigiri.destroy()
        self.m_tablero = True
        
    def validar_nombre(self,len_nombre,nom_j,num_j):
        """Verifica que se ingrese algun nombre en los inputs de texto.
        
        Parametros:     len_nombre: longitud del nombre ingresado.
                        nom_j: input en el que se validara.
                        nun_j : numero del jugador al que se le esta validando el nombre.
                        
        Retorno:    True si los nombres son validos,False en caso contrario.
        """            
        n_valido = False
        if((len_nombre < 1 or ("Nombre del jugador") in nom_j ) and (n_valido == False) ):
            self.vista.obt_vista_concreta().mostrar_error_nombres(num_j)
        else: 
            n_valido = True
            self.vista.obt_vista_concreta().deshabilitar_input_nombre(num_j)
            
        return n_valido
        

    def obtener_nombres(self):
        """Obtiene los nombres de los jugadores de las entradas de texto en la ventana correspondiente."""
        nom_j1 = str(self.vista.obt_vista_concreta().nombre1.get())
        nom_j2 = str(self.vista.obt_vista_concreta().nombre2.get())
        len_nombre1 = len(nom_j1)
        len_nombre2 = len(nom_j2)
        nombre1_valido = False
        nombre2_valido = False
        
        nombre1_valido = self.validar_nombre(len_nombre1, nom_j1 ,1)
        nombre2_valido = self.validar_nombre(len_nombre2, nom_j2 ,2)
        
        if( nombre1_valido and nombre2_valido ):
            self.vista.obt_vista_concreta().deshabilitar_boton_listo("nombres")
            self.vista.obt_vista_concreta().habilitar_boton_continuar(1)
            self.vista.obt_vista_concreta().hover_button(self.vista.obt_vista_concreta().boton_continuar,self.vista.obt_vista_concreta().color_boton_go,self.vista.obt_vista_concreta().color_fuente_boton)
            self.nombre1 = nom_j1
            self.nombre2 = nom_j2
     
    def validar_cantidad_piedras(self,piedras_jugador,num_jugador):
        """Valida que se ingrese una cantidad de piedras correcta en las entradas de texto de la ventana correspondiente.
        
            Parametros: piedras_jugador: cantidad de piedras ingresada en la entrada de texto.
                        num_jugador: numero de jugador que ingreso la cantidad de piedras.
                    
            Retorno:    True si la cantidad de piedras ingresada es valida,False en caso contrario.
            """    
        piedras_validas = False
        try:
            #Se intenta provocar el error
            piedras = int(piedras_jugador)
            if (num_jugador == 1):
                piedras_validas = True
                self.vista.obt_vista_concreta().deshabilitar_input_piedras(num_jugador)
                
            elif (num_jugador == 2 ):
                if (piedras > 0 and piedras <= 2):
                    piedras_validas = True
                    self.vista.obt_vista_concreta().deshabilitar_input_piedras(2)
                else:
                    raise Exception 
                
        except Exception:
            if(num_jugador == 1):
                    self.vista.obt_vista_concreta().mostrar_error_piedras(self.nombre1,1)
            elif (num_jugador == 2):
                    self.vista.obt_vista_concreta().mostrar_error_piedras(self.nombre2,2)
                    
        return piedras_validas
                    
    def obtener_cantidad_piedras(self):
        """Obtiene la cantidad de piedras que ingresaron los jugadores en las entradas de texto de la ventana correspondiente.
            
            Retorno: la cantidad de piedras para cada jugador si ingresaron una cantidad valida, (0 , 0) en caso contrario."""
        piedras_j1_validas = False
        piedras_j2_validas = False
        
        piedras_j1 = self.vista.obt_vista_concreta().piedras_j1.get()
        piedras_j1_validas = self.validar_cantidad_piedras(piedras_j1,1)
        
        piedras_j2 = self.vista.obt_vista_concreta().piedras_j2.get()
        piedras_j2_validas = self.validar_cantidad_piedras(piedras_j2,2)
                
        if(piedras_j1_validas and piedras_j2_validas):
            self.vista.obt_vista_concreta().deshabilitar_boton_listo("nigiri")
            self.vista.obt_vista_concreta().habilitar_boton_continuar(2)
            self.vista.obt_vista_concreta().hover_button(self.vista.obt_vista_concreta().boton_nigiri_continuar,self.vista.obt_vista_concreta().color_boton_go,self.vista.obt_vista_concreta().color_fuente_boton)
            return int(piedras_j1) , int (piedras_j2) , True
        return 0 , 0 , False
            
    def elegir_color(self):
        """Se elije el color para cada jugador de acuerdo al resultado del nigiri."""
        # Si j2 eligio una piedra y la suma es impar entonces inicia
        if(self.piedras_jugador2 == 1 and ((self.piedras_jugador1 + self.piedras_jugador2) % 2 != 0)):
            self.color = 2
        # Si j2 eligio dos piedras y la suma es par entonces inica
        elif (self.piedras_jugador2 == 2 and ((self.piedras_jugador1 + self.piedras_jugador2) % 2 == 0)):
            self.color = 2
              
    def nigiri(self):
        """Manera en la que se decide que jugador va primero,el jugador 1 elige una cantidad de piedras sin ensenarlas y\n\
        el jugador 2 elige una para decir impar o dos para decir par, si acierta entonces empieza con las negras sino con blancas."""
        self.piedras_jugador1,self.piedras_jugador2 , respuesta_valida =  self.obtener_cantidad_piedras()
        if(respuesta_valida):
            self.elegir_color()
            self.vista.obt_vista_concreta().mostrar_resultado_nigiri(self.color, self.piedras_jugador1, self.piedras_jugador2,self.nombre1,self.nombre2)
 
    def retornar_nombre_jugador1(self):
        """Retorno: el nombre del jugador 1"""
        return self.nombre1 
    
    def retornar_nombre_jugador2(self):
        """Retorno: el nombre del jugador 2"""
        return self.nombre2 
    
    ##################################################### METODOS PARA EL TABLERO EN PYGAME #######################################################################
    def responder_a_dibujar_tablero(self,pantalla):
        """Se responde al evento para dibujar el tablero.
        
            Retorno: True si hay algun evento en el tablero,False en caso de que se cierre el tablero en la X de la ventana."""
        return self.vista.dibujar_tablero(pantalla)
    
    def asignar_tablero (self):
        """Refresca el tablero de la vista con el que resulta de algun evento en el controlador."""
        self.vista.obt_vista_concreta().tablero = self.tablero_logico
        
    def iniciar_eventos (self):
        """Refresca la cola de eventos con la resultante de algun evento en el controlador."""
        self.vista.obt_vista_concreta().eventos = self.eventos
        
    def asignar_color_jugador(self,negro,blanco):
        """Se le asigna color a cada jugador de acuerdo al resultado del nigiri.
            
            Parametros: negro: color de fichas para el jugador que inicia.
                        blanco: color de fichas para el jugador que va de segundo.
                        
            Retorno:    Un entero que identifica que jugador inicia."""
        proximo_en_jugar = 0
        if(self.color == 1):
            self.jugador1 = Jugador( JugadorGo(1, negro, self.nombre1) ) #############
            self.jugador2 = Jugador( JugadorGo(2, blanco, self.nombre2) ) ##############

        else:
            self.jugador1 = Jugador (JugadorGo(1, blanco, self.nombre1) ) #########
            self.jugador2 = Jugador (JugadorGo(2, negro, self.nombre2) )##########
            proximo_en_jugar = 1
            
        return proximo_en_jugar
    
    def asignar_nombre_ganador(self,ganador):
        """Asigna el nombre del jugador ganador.
        
        Parametros: ganador: numero que identifica al jugador ganador.
        
        Retorno: nombre del ganador (string)."""
        if (ganador == 1):
            return self.nombre1
        elif (ganador ==2 ):
            return self.nombre2
        else:
            return "Empate"
        
    def iniciar_jugadas(self):
        """Logica principal del tablero que captura eventos y refresca la vista de acuerdo al evento que surge por un jugador."""
        negro = 1
        blanco = 2
        turnos_saltados = 0
        jugador_en_turno = ""
        
        self.tablero = Tablero ( TableroGo() )
        self.tablero.crear_tablero()
        self.arbitro = Arbitro( ArbitroGo ( self.tablero.obt_tablero_concreto() ) )
        self.vista.obt_vista_concreta().iniciar_tablero()
        
        #Inicia el que tenga color negro en las fichas
        proximo_en_jugar = self.asignar_color_jugador(negro,blanco)
        
        cantidad_piezas_j1 = self.jugador1.obt_jugador_concreto().obt_total_piezas()
        cantidad_piezas_j2 = self.jugador2.obt_jugador_concreto().obt_total_piezas()
        if(proximo_en_jugar == 0):
            jugador_en_turno = self.nombre1
        else:
            jugador_en_turno = self.nombre2
            
        self.vista.dibujar_tablero(self.tablero_logico,cantidad_piezas_j1,cantidad_piezas_j2,self.nombre1,self.nombre2,jugador_en_turno)
        
        while True:
            
            salir = self.caputurar_eventos()
            if salir:
                pygame.quit()
                break

            if not self.eventos.empty(): 
                
                coordenadas = self.eventos.get()
                fila = coordenadas[0]
                columna = coordenadas[1]
                
                if(self.arbitro.validar_posicion(fila,columna)): ######ARBITRO
                    if(proximo_en_jugar == 0):
                        jugador_en_turno = self.nombre2
                        proximo_en_jugar = self.movimiento_jugador(self.jugador1,fila,columna,self.tablero,self.vista)        
                        cantidad_piezas_j1 -= 1
                    else:
                        jugador_en_turno = self.nombre1
                        proximo_en_jugar = self.movimiento_jugador(self.jugador2,fila,columna,self.tablero,self.vista)  
                        cantidad_piezas_j2 -= 1

                    self.convertir_tablero(self.tablero)
            else:
                if(self.cambiar_turno == 1):
                    if(proximo_en_jugar == 0):
                        jugador_en_turno = self.nombre2
                        self.vista.obt_vista_concreta().mostrar_salto_turno(self.jugador1.obt_nombre())
                        
                    elif (proximo_en_jugar == 1):
                        jugador_en_turno = self.nombre1
                        self.vista.obt_vista_concreta().mostrar_salto_turno(self.jugador2.obt_nombre())
                    
                    proximo_en_jugar = self.arbitro.saltar_turno(proximo_en_jugar) ###ARBITRO
                    turnos_saltados += 1
                    self.cambiar_turno = 0
                    
                if(self.arbitro.terminar_juego(turnos_saltados)): ####ARBITRO
                    puntos_jugador_1,puntos_jugador_2 =  self.arbitro.obt_arbitro_concreto().contar_puntos() #####ARBITRO
                    ganador = self.arbitro.obt_arbitro_concreto().determinar_ganador(puntos_jugador_1,puntos_jugador_2) ##ARBITRO
                    self.vista.obt_vista_concreta().mostrar_fin_juego(self.nombre1,puntos_jugador_1,self.nombre2,puntos_jugador_2,self.asignar_nombre_ganador(ganador))
                    break
                
            self.vista.dibujar_tablero(self.tablero_logico,cantidad_piezas_j1,cantidad_piezas_j2,self.nombre1,self.nombre2,jugador_en_turno)
    
    def movimiento_jugador(self,jugador,fila,columna,tablero,vista):
        """Coloca la ficha en el tablero en la posicion que elige el jugador.
            
            Parametros: jugador: instancia que representa al jugador en turno.
                        fila: fila donde se desea colocar una ficha.
                        columna : columna donde se desea colocar una ficha.
                        tablero: instancia de tablero donde se colocara la ficha.
                        vista:  instancia de la vista para refrescar el tablero mostrado.
                        
            Retorno:    Un entero que representa el proximo jugado en turno.
            """

        jugador_en_turno = ( jugador.obt_id() - 1 )  
        if(tablero.colocar_ficha(fila, columna, jugador.obt_jugador_concreto()) == False):
            vista.obt_vista_concreta().mostrar_error_posicion()
        else:
            tablero.obt_tablero_concreto().revisar_eliminar_agrupamientos()
            if (self.arbitro.obt_arbitro_concreto().jugada_suicida(fila,columna) == True): ###ARBITRO
                vista.obt_vista_concreta().mostrar_error_jugada_suicida()
                
            else:
                if(jugador_en_turno == 0):
                    jugador_en_turno =  1
                elif (jugador_en_turno == 1):
                    jugador_en_turno =  0   
                    
        return jugador_en_turno
        
    def iniciar_tablero(self):
        """Inicia la interaccion con el tablero grafico."""
        self.iniciar_eventos ()
        self.asignar_tablero()
        self.vista.mostrar_tablero()

    def convertir_tablero(self,tablero):
        """Castea el tablero grafico con el tablero del modelo para poder representarlo por medio de la vista"""      
        for i in range(9):
            for j in range(9):
                pieza = tablero.obt_tablero_concreto().tablero_juego[i][j]
                self.tablero_logico[i][j] = pieza.obt_tipo() 

    def mostrar_tablero(self):
        """Muestra el tablero grafico en pantalla por primera vez"""
        for fila in range(9):
            self.tablero_logico.append([])
            for columna in range(9):
                self.tablero_logico[fila].append("-")
        
        self.iniciar_jugadas()
        
    def caputurar_eventos(self):
        """Captura los eventos producidos por cada jugador para interactuar con la vista"""
        for event in pygame.event.get():  # Obtiene el evento que produce el jugador
            if event.type == pygame.QUIT:  # En caso de que el jugador cierre la ventana
                done = True  # Bandera para indicar que se quiere salir del juego
                return done
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Se optiene la cordenada de la posicion donde el jugador hizo click
                pos = pygame.mouse.get_pos()
                # Convierte las coordenada de la pantalla a coordenadas para el tablero del modelo
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                self.eventos.put((row,column))
    
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.cambiar_turno = 1
            elif event.type == KEYDOWN and event.key == K_0:
                self.vista.mostrar_reglas_juego()
        return False
        
    

    
        