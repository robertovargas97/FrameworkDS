import abc
from abc import ABC

class Pieza(ABC):
    """Representa las piezas que posee cada jugador"""
    
    def __init__(self,id,fila,columna):
    #Atributo de clase que podran usar las clases hijas
        self.tipo_pieza = "" #String con el tipo de pieza que tiene un jugador
        self.fila = fila
        self.columna = columna
        self.id = id

    @abc.abstractmethod
    def get_fila(self):
        """ """
        pass

    @abc.abstractmethod    
    def get_columna(self):
        """ """
        pass
    
    @abc.abstractmethod    
    def get_id(self):
        """Retorna un entero con el identificador de la pieza"""
        pass
    
    @abc.abstractmethod    
    def get_tipo(self):
        """Retorna un string con el tipo de pieza a la que corresponde"""
        pass
