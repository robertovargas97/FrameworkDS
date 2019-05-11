import abc
from abc import ABC

class Piezas(ABC):
    """Representa las piezas que posee cada jugador"""
    
    def __init__(self):
    #Atributo de clase que podran usar las clases hijas
        self.cantidad_piezas = 0 #Cantidad de piezas que posee cada jugador
        self.tipo_pieza = "" #String con el tipo de pieza que tiene un jugador
        
    @abc.abstractmethod    
    def set_cantidad_piezas(self,cantidad_actual):
        """cantidad actual : cantidad de piezas que posee el jugador despues de alguna perdida o ganancia\n
        Coloca en la cantidad de piezas la cantidad de piezas actual"""
        pass
    
    @abc.abstractmethod    
    def get_piezas(self):
        """Retorna un entero con la cantidad de piezas que posee el jugador"""
        pass
    
    @abc.abstractmethod    
    def get_tipo(self):
        """Retorna un string con el tipo de pieza a la que corresponde"""
        pass
