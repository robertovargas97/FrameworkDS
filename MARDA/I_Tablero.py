import abc
from abc import ABC


class I_Tablero(ABC):
    """Interfaz abstracta del tablero en el que se jugara."""

    @abc.abstractmethod
    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones."""
        pass

    @abc.abstractmethod
    def colocar_ficha(self, fila, columna, jugador):
        """Coloca una ficha en el tablero.
        
        Parametros:  fila , columna : posicion en el tablero.
                        jugador: instancia del jugador que coloca la pieza.
                        
        Retorno:        True si se puede colocar la pieza, False en caso contrario."""
        pass
