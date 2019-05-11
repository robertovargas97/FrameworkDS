import abc
from abc import ABC

class Tablero(ABC):
    """Representa el tablero en el que se jugara"""
    
    def __init__(self):
        #Atributo de clase que podran usar las clases hijas
        self.tablero_juego = [] #Arreglo de arreglo que representa la matriz tablero
        self.filas = 0
        self.columnas = 0 
        
    @abc.abstractmethod
    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        pass
   
    @abc.abstractmethod
    def mostrar_tablero(self):
        """Muestra en pantalla el tablero""" 
        pass
   
    @abc.abstractmethod
    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        pass
    