import abc
from abc import ABC


class I_Tablero(ABC):
    """Representacion abstracta del tablero en el que se jugara"""
    #No contiene atributos en comun ya que cada tablero especifico contendra los suyos

    @abc.abstractmethod
    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        pass

    @abc.abstractmethod
    def colocar_ficha(self, fila, columna, jugador):
        """fila , columna : posicion en el tablero\n
        jugador: instancia del jugador que coloca la pieza\n
        Retorno: True si se puede colocar la pieza, False en caso contrario"""
        pass
    
    @abc.abstractmethod
    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe\n
        fila: fila en el tablero\n
        columna: columna en el tablero\n"""
        pass
