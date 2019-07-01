import abc
from abc import ABC

class I_Pieza(ABC):
    """Representa una interfaz de piezas que posee cada jugador"""
    
    def __init__(self,color,fila,columna):
    #Atributo de clase que podran usar las clases hijas
        self.fila = fila
        self.columna = columna
        self.color = color

    @abc.abstractmethod
    def obt_fila(self):
        """Retorna la fila donde se encuentra la pieza"""
        pass

    @abc.abstractmethod    
    def obt_columna(self):
        """Retorna la columna donde se encuentra la pieza"""
        pass
    
    @abc.abstractmethod    
    def obt_id(self):
        """Retorna un entero con el identificador de la pieza"""
        pass   
 