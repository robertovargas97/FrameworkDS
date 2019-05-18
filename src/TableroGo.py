from Tablero import Tablero
from PiezaGo import PiezaGo
import random


class TableroGo(Tablero):
    """Implementacion especifica de un tablero de Go"""

    # Las filas y columnas se toman como valores por defecto
    def __init__(self, filas=9, columnas=9):
        self.filas = filas
        self.columnas = columnas
        self.tablero_juego = []

    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        self.tablero_juego = ['-'] * self.filas  # Crea las filas del tablero
        for fila in range(self.filas):
            self.tablero_juego[fila] = ['-'] * \
                self.columnas  # Crea las columnas del tablero
        # return self.tablero_juego

    def mostrar_tablero(self):
        """Muestra en pantalla el tablero"""
        # Este for coloca el numero de columnas para mayor facilidad a la hora de colocar una posicion
        print()
        for i in range(self.filas):
            if(i == 0):
                print("   ", i, " ", end="")
            else:
                print(i, " ", end="")
        print()

        # Aca se empieza a imprimir la matriz como tal
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if(columna == 0):
                    print(
                        fila, " ", self.tablero_juego[fila][columna], " ", end="")
                else:
                    print(self.tablero_juego[fila][columna], " ", end="")
            print()
        print()

    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.tablero_juego[fila][columna] = '-'
                
    def validar_posicion(self, fila, columna):
        """fila , columna : posicion en el tablero\n
        Retorno : True en caso de que la posicion para colocar la ficha este libre,False en caso contrario"""
        posicion_valida = True
        if (self.tablero_juego[fila][columna] != '-'):
            posicion_valida = False
        return posicion_valida
                
    def colocar_ficha(self, fila, columna, jugador):
        """fila , columna : posicion en el tablero\n
        jugador: instancia del jugador que coloca la pieza\n
        Retorno: True si se puede colocar la pieza, False en caso contrario"""
        posicion_valida = False
        if(self.validar_posicion(fila,columna) == True):
            pieza_nueva = PiezaGo(jugador.obt_color_pieza(), fila, columna)
            jugador.piezas_colocadas.append(pieza_nueva)
            # Coloca la ficha en el tablero
            self.tablero_juego[fila][columna] = pieza_nueva.get_tipo()
            posicion_valida = True 
        
        return posicion_valida
                    
    def validar_fila(self,fila):
        """fila: fila en el tablero\n
        retorno : True si la fila es valida, False en caso contrario"""
        posicion_valida = True
        # Posicion no existe en el tablero
        if ((fila < 0) or (fila >= self.filas)):
            posicion_valida = False
        return posicion_valida
        
    def validar_columna(self,columna):
        """columna: columna en el tablero\n
        retorno : True si la columna es valida, False en caso contrario"""
        posicion_valida = True
        # Posicion no existe en el tablero
        if ((columna < 0) or (columna >= self.columnas)):
            posicion_valida = False
        return posicion_valida    
       
    def pedir_fila(self):
        """Pide la fila donde se quiere colocar la pieza\n
        retorno: el numero de fila que se ingreso"""
        salir = False
        fila = 0
        while(salir == False):
            try:
                fila = int(input("Ingrese la fila en la que desea colocar la ficha: "))
                if (self.validar_fila(fila) == True):
                    salir = True
                else:
                    print("Fila invalida.")
            except ValueError:
                print("Fila invalida.")
                
        return fila
    
    def pedir_columna(self):
        """Pide la columna donde se quiere colocar la pieza\n
        retorno: el numero de columna que se ingreso"""
        salir = False
        columna = 0
        while(salir == False):
            try:
                columna = int(input("Ingrese la columna en la que desea colocar la ficha: "))
                if (self.validar_columna(columna) == True):
                    salir = True
                else:
                    print("Columna invalida.")
            except ValueError:
                print("Columna invalida.")
                
        return columna
        
    def pedir_posicion(self):
        """Se pide la posicion donde se colocara la pieza en el tablero"""
        fila = self.pedir_fila()
        columna = self.pedir_columna()
        return fila,columna

    def nigiri(self, piezasj1, piezasj2):
        """Manera en la que se decide que jugador va primero,el jugador 1 elige una cantidad de piedras sin ensenarlas y\n\
        el jugador 2 elige una para decir impar o dos para decir par si acierta entonces empieza con negras sino con blancas"""
        resultado = 1
        # Si j2 eligio una piedra y la suma es impar entonces inicia
        if(piezasj2 == 1 and ((piezasj1 + piezasj2) % 2 != 0)):
            resultado = 2
        # Si j2 eligio dos piedras y la suma es par entonces inica
        elif (piezasj2 == 2 and ((piezasj1 + piezasj2) % 2 == 0)):
            resultado = 2
        return resultado

    def mostrar_resultado_nigiri(self, color, piedras_j1, piedras_j2):
        print("El jugador 1 eligio ", piedras_j1,
              " piedra(s), mientras que el jugador 2 eligio ", piedras_j2, "piedra(s).\n")
        if(color == 1):
            print("\nEl jugador 1 juega con las piedras negras.")
            print("El jugador 2 juega con las piedras blancas.\n")

        else:
            print("El jugador 1 juega con las piedras blancas.")
            print("El jugador 2 juega con las piedras negras.")

