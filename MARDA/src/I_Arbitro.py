import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase

class I_Arbitro(ABC):
    """ """

    @abc.abstractmethod
    def validar_posicion(self,tablero,fila,columna):
        pass