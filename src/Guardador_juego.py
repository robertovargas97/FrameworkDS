import abc
from abc import ABC


class Guardar_juego(ABC):
    """Representacion abstracta de como se va a guardar un juego"""
    #No contiene atributos en comun ya que cada tablero especifico contendra los suyos

    @abc.abstractmethod
    def guardar_estado(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        pass


