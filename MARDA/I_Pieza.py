import abc
from abc import ABC

class I_Pieza(ABC):
    """Interfaz abstracta de pieza."""

    @abc.abstractmethod
    def obt_fila(self):
        """Retorno : fila donde se encuentra la pieza"""
        pass

    @abc.abstractmethod    
    def obt_columna(self):
        """Retorno : columna donde se encuentra la pieza"""
        pass
    
    @abc.abstractmethod    
    def obt_id(self):
        """Retorno : entero con el identificador de la pieza"""
        pass   
 