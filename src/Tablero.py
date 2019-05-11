import abc
from abc import ABC

class Tablero(ABC):
    
    def __init__(self):
        #Atributo de clase que podran usar las clases hijas
        self.tablero_juego = [] 
        self.filas = 0
        self.columnas = 0 
        
    #Se debe crear el tablero en la clase concreta
    @abc.abstractmethod
    def crear_tablero(self):
       pass
   
    #Se debe limpiar el tablero en la clase concreta
    @abc.abstractmethod
    def mostrar_tablero(self):
        pass
   
    #Se debe limpiar el tablero en la clase concreta
    @abc.abstractmethod
    def limpiar_tablero(self):
        pass
    