from _thread import *
import threading
from TableroGo import TableroGo  # Se importa la clase como tal y no como modulo
from JugadorGo import JugadorGo
from PiezaGo import PiezaGo
from view import View
from tkinter import *
from tkinter import messagebox
import queue


class Controlador:

    def __init__(self):
        self.tablero = []
        self.eventos = queue.Queue()
        
    
    def iniciar_modelo(self):
        tableroGo = TableroGo()
        tableroGo.crear_tablero()

        turno = 0
        jugador1 = JugadorGo(1, 1, "Aaron")
        jugador2 = JugadorGo(2, 2, "Denisse")

        while True:

            if not self.eventos.empty(): #si hay al
                coordenadas = self.eventos.get()
                fila = coordenadas[0]
                columna = coordenadas[1]
                if(turno == 0):
                    if(tableroGo.colocar_ficha(fila, columna, jugador1) == False):
                        Tk().wm_withdraw()
                        messagebox.showwarning('Jugada invalida', 'Escoja otra posicion')
                    else:
                       # tablero.colocar_ficha(fila, columna, jugador1)
                        piezas_perdidas = tableroGo.revisar_eliminar_agrupamientos()
                        if (tableroGo.jugada_suicida(fila,columna) == True):
                            Tk().wm_withdraw()
                            messagebox.showwarning('Jugada suicida!', 'Escoja otra posicion')
                        else:
                            turno += 1                   
                else:
                    if(tableroGo.colocar_ficha(fila, columna, jugador2) == False):
                        Tk().wm_withdraw()
                        messagebox.showwarning('Jugada invalida', 'Escoja otra posicion')
                    else:
                        piezas_perdidas = tableroGo.revisar_eliminar_agrupamientos()
                        if (tableroGo.jugada_suicida(fila,columna) == True):
                            Tk().wm_withdraw()
                            messagebox.showwarning('Jugada suicida!', 'Escoja otra posicion')
                        else:
                            turno -= 1 
                self.tablero_enteros(tableroGo)
    
    def iniciar_vista(self):
        vista = View(self.eventos,self.tablero)
        vista.iniciar()
    
        

    def main(self):
        for fila in range(9):
            self.tablero.append([])
            for columna in range(9):
                self.tablero[fila].append("-")  # Append a cell

        start_new_thread(self.iniciar_vista,())
        self.iniciar_modelo()
    
    def tablero_enteros(self,tablero_go):      
        for i in range(9):
            for j in range(9):
                pieza = tablero_go.tablero_juego[i][j]
                self.tablero[i][j] =  pieza.obt_tipo() 

        
        

if __name__ == "__main__":
    controlador = Controlador()
    controlador.main()
