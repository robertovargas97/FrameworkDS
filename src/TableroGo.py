from Tablero import Tablero


class TableroGo(Tablero):
    """Implementacion especifica de un tablero de Go"""

    # Las filas y columnas se toman como valores por defecto
    def __init__(self, filas=9, columnas=9):
        self.filas = filas
        self.columnas = columnas

    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        self.tablero_juego = ['-'] * self.filas  # Crea las filas del tablero
        for fila in range(self.filas):
            self.tablero_juego[fila] = ['-'] * \
                self.columnas  # Crea las columnas del tablero
        # return self.tablero_juego

    def mostrar_tablero(self):
        """Muestra en pantalla el tablero"""
        #Este for coloca el numero de columnas para mayor facilidad a la hora de colocar una posicion
        for i in range(self.filas):
            if(i == 0):
                 print("   ", i , " ", end="")
            else:
                print(i, " ", end="")
        print()
        
        #Aca se empieza a imprimir la matriz como tal
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if(columna == 0):
                    print(fila," ",self.tablero_juego[fila][columna], " ", end="")
                else:
                    print(self.tablero_juego[fila][columna], " ", end="")
            print()
        print()

    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.tablero_juego[fila][columna] = '-'
