from Tablero import Tablero

class TableroGo(Tablero):
    """Implementacion especifica de un tablero de Go"""
    
    #Las filas y columnas se toman como valores por defecto
    def __init__(self,filas = 9, columnas = 9):
        self.filas = filas
        self.columnas = columnas
    
    def crear_tablero(self):
        self.tablero_juego = ['-'] * self.filas
        for fila in range (self.filas):
            self.tablero_juego[fila] = ['-'] * self.columnas
        # return self.tablero_juego
    
    def mostrar_tablero(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                print(self.tablero_juego[fila][columna], " " , end="")
            print()
            
    def limpiar_tablero(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.tablero_juego[fila][columna] = '-'
            
            
            
    
    
        
        


