import abc
from abc import ABC

class Piezas(ABC):
    
    def __init__(self):
    #Atributo de clase que podran usar las clases hijas
        self.cantidad_piezas = 0
        
    @abc.abstractmethod    
    def set_cantidad_piezas():
        pass
    
    @abc.abstractmethod    
    def get_piezas(self):
        pass
    
    @abc.abstractmethod    
    def get_tipo(self):
        pass
