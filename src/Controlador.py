from TableroGo import TableroGo
from JugadorGo import JugadorGo
from Vista import Vista
from tkinter import *
from tkinter import messagebox
from _thread import *
import queue
import threading


class Controlador:

    def __init__(self):
        """Class initializer."""
        # Se crea la vista en el controlador para poder interactuar , ademas de instancias del modelo para poder actualizar datos por detras (Composition)
        self.vista = Vista(self)
        self.tableroGo = None
        self.jugador1 = None
        self.jugador2 = None
        #Variables necesarias para el control
        self.tablero = []
        self.eventos = queue.Queue()
        self.nombre1 = ""
        self.nombre2 = ""
        self.piedras_jugador1 = 0
        self.piedras_jugador2 = 0
        self.color_jugador1 = 0
        self.color_jugador2 = 0
        self.color = 1
    
    ################################################## REACCIONES A EVENTOS DE LA VISTA ##########################################################################
    def iniciar_framework(self):
        self.vista.mostrar_ventana_inicial()
        
    def boton_autores_presionado(self):
        self.vista.mostrar_ventana_autores()
    
    def boton_reglas_presionado(self):
        self.vista.mostrar_reglas()
        
    def boton_entrar_presionado(self,op):
        self.vista.mostrar_menu_inicial(op)

    def boton_volver_presionado(self,ventana, metodo, opcion):
        self.vista.volver(ventana, metodo, opcion)
        
    def boton_jugar_presionado(self):
        self.vista.mostrar_menu_nombres()
        
    def boton_continuar_presionado(self):
        self.vista.avisar_inicio_nigiri(self.nombre1,self.nombre2)
        self.vista.mostrar_ventana_nigiri() 
        
    def cerrar_menu(self):
        self.vista.ventana_nigiri.destroy()
        
    def validar_nombre(self,len_nombre,nom_j,n_valido,num_j):
        n_valido = False
        if((len_nombre < 1 or ("Nombre del jugador") in nom_j ) and (n_valido == False) ):
            self.vista.mostrar_error_nombres(num_j)
        else: 
            n_valido = True
            self.vista.deshabilitar_input_nombre(num_j)
            
        return n_valido
        
    def obtener_nombres(self):
        nom_j1 = str(self.vista.nombre1.get())
        nom_j2 = str(self.vista.nombre2.get())
        len_nombre1 = len(nom_j1)
        len_nombre2 = len(nom_j2)
        nombre1_valido = False
        nombre2_valido = False
        
        nombre1_valido = self.validar_nombre(len_nombre1, nom_j1 ,nombre1_valido,1)
        nombre2_valido = self.validar_nombre(len_nombre2, nom_j2 ,nombre2_valido,2)
        
        if( nombre1_valido and nombre2_valido ):
            self.vista.deshabilitar_boton_listo("nombres")
            self.vista.habilitar_boton_continuar(1)
            self.vista.hover_button(self.vista.boton_continuar,self.vista.color_boton_go,self.vista.color_fuente_boton)
            self.nombre1 = nom_j1
            self.nombre2 = nom_j2
     
    def validar_cantidad_piedras(self,piedras_jugador,num_jugador):
        piedras_validas = False
        try:
            #Se intenta provocar el error
            piedras = int(piedras_jugador)
            if (num_jugador == 1):
                piedras_validas = True
                self.vista.deshabilitar_input_piedras(num_jugador)
                
            elif (num_jugador == 2 ):
                if (piedras > 0 and piedras <= 2):
                    piedras_validas = True
                    self.vista.deshabilitar_input_piedras(2)
                else:
                    raise Exception 
                
        except Exception:
            if(num_jugador == 1):
                    self.vista.mostrar_error_piedras(self.nombre1,1)
            elif (num_jugador == 2):
                    self.vista.mostrar_error_piedras(self.nombre2,2)
                    
        return piedras_validas
                    
    def obtener_cantidad_piedras(self):
        piedras_j1_validas = False
        piedras_j2_validas = False
        
        piedras_j1 = self.vista.piedras_j1.get()
        piedras_j1_validas = self.validar_cantidad_piedras(piedras_j1,1)
        
        piedras_j2 = self.vista.piedras_j2.get()
        piedras_j2_validas = self.validar_cantidad_piedras(piedras_j2,2)
                
        if(piedras_j1_validas and piedras_j2_validas):
            self.vista.deshabilitar_boton_listo("nigiri")
            self.vista.habilitar_boton_continuar(2)
            self.vista.hover_button(self.vista.boton_nigiri_continuar,self.vista.color_boton_go,self.vista.color_fuente_boton)
            return int(piedras_j1) , int (piedras_j2) , True
        return 0 , 0 , False
            
    def elegir_color(self):
        # Si j2 eligio una piedra y la suma es impar entonces inicia
        if(self.piedras_jugador2 == 1 and ((self.piedras_jugador1 + self.piedras_jugador2) % 2 != 0)):
            self.color = 2
        # Si j2 eligio dos piedras y la suma es par entonces inica
        elif (self.piedras_jugador2 == 2 and ((self.piedras_jugador1 + self.piedras_jugador2) % 2 == 0)):
            self.color = 2
              
    def nigiri(self):
        """Manera en la que se decide que jugador va primero,el jugador 1 elige una cantidad de piedras sin ensenarlas y\n\
        el jugador 2 elige una para decir impar o dos para decir par, si acierta entonces empieza con las negras sino con blancas"""
        self.piedras_jugador1,self.piedras_jugador2 , respuesta_valida =  self.obtener_cantidad_piedras()
        if(respuesta_valida):
            self.elegir_color()
            self.vista.mostrar_resultado_nigiri(self.color, self.piedras_jugador1, self.piedras_jugador2,self.nombre1,self.nombre2)
 
    def retornar_nombre_jugador1(self):
        return self.nombre1 
    
    def retornar_nombre_jugador2(self):
        return self.nombre2 
    
    ##################################################### METODOS PARA EL TABLERO EN PYGAME #######################################################################
    def responder_a_dibujar_tablero(self,pantalla):
        return self.vista.dibujar_tablero(pantalla)
    
    def refrescar_tablero (self):
        self.vista.tablero = self.tablero
        
    def refrescar_eventos (self):
        self.vista.eventos = self.eventos
        
    def asignar_color_jugador(self,negro,blanco):
        proximo_en_jugar = 0
        if(self.color == 1):
            self.jugador1 = JugadorGo(1, negro, self.nombre1)
            self.jugador2 = JugadorGo(2, blanco, self.nombre2)

        else:
            self.jugador1 = JugadorGo(1, blanco, self.nombre1)
            self.jugador2 = JugadorGo(2, negro, self.nombre2)
            proximo_en_jugar = 1
            
        return proximo_en_jugar
        
    
    def iniciar_jugadas(self):
        negro = 1
        blanco = 2
        
        self.tableroGo = TableroGo()
        self.tableroGo.crear_tablero()
        
        #Inicia el que tenga color negro en las fichas
        proximo_en_jugar = self.asignar_color_jugador(negro,blanco)
      
        while True:

            if not self.eventos.empty(): #ESTA LINEA ES LA QUE HACE QUE NO SALGA DEL WHILE UNA VEZ QUE SE CIERRA CON LA X
                coordenadas = self.eventos.get()
                fila = coordenadas[0]
                columna = coordenadas[1]
                if(self.tableroGo.validar_posicion(fila,columna)):
                    if(proximo_en_jugar == 0):
                        if(self.tableroGo.colocar_ficha(fila, columna, self.jugador1) == False):
                            self.vista.mostrar_error_posicion()
                        else:
                            piezas_perdidas = self.tableroGo.revisar_eliminar_agrupamientos()
                            if (self.tableroGo.jugada_suicida(fila,columna) == True):
                                self.vista.mostrar_error_jugada_suicida()
                            else:
                                proximo_en_jugar += 1                   
                    else:
                        if(self.tableroGo.colocar_ficha(fila, columna, self.jugador2) == False):
                            self.vista.mostrar_error_posicion()
                        else:
                            piezas_perdidas = self.tableroGo.revisar_eliminar_agrupamientos()
                            if (self.tableroGo.jugada_suicida(fila,columna) == True):
                                self.vista.mostrar_error_jugada_suicida()
                            else:
                                proximo_en_jugar -= 1 
                    self.convertir_tablero(self.tableroGo)
                else:
                    self.vista.mostrar_error_fuera_tablero()
    
    def iniciar_tablero(self):
        self.refrescar_eventos ()
        self.refrescar_tablero()
        self.vista.mostrar_tablero()

    def convertir_tablero(self,tablero_go):      
        for i in range(9):
            for j in range(9):
                pieza = tablero_go.tablero_juego[i][j]
                self.tablero[i][j] = pieza.obt_tipo() 

    def mostrar_tablero(self):
        for fila in range(9):
            self.tablero.append([])
            for columna in range(9):
                self.tablero[fila].append("-")  # Append a cell
        
        start_new_thread(self.iniciar_tablero,())
        self.iniciar_jugadas()
        
        
if __name__ == "__main__":
    controlador = Controlador()
    controlador.iniciar_framework()
    #HAY QUE ARREGLAR QUE SI SE CIERRA LA VENTANA DE TKINTER CON LA "X" NO SE EJECUTE LA LINEA DE MOSTRAR TABLERO
    controlador.mostrar_tablero()
