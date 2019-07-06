import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase

class I_Arbitro(ABC):
    """Interfaz abstracta de arbitro."""

    @abc.abstractmethod
    def validar_posicion(self,tablero,fila,columna):
        """Valida si la posicion ingresada existe.
        
        Parametros:     fila: fila en el tablero.
                        columna: columna en el tablero.
                        
        Retorno : True si la posicion es valida, False en caso contrario."""
        pass