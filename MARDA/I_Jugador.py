import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase

class I_Jugador(ABC):
    """Interfaz abstracta de un jugador."""

    @abc.abstractmethod
    def obt_id(self):
        """Retorno : string que representa el identificador del jugador"""
        pass

    @abc.abstractmethod
    def obt_nombre(self):
        """Retorno : string que representa el nombre del jugador"""
        pass