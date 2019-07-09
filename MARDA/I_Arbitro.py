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
    
    @abc.abstractmethod
    def saltar_turno(self, jugador):
        """Permite al jugador saltar su turno.
        
        Parametros: jugador : el jugador que ha decidido saltar el turno.
        
        Retorno: el siguiente jugadir en turno (int)."""
        pass
    
    @abc.abstractmethod
    def terminar_juego(self, turnos_saltados):
        """Verifica si el juego ya acabo.Si ambos jugadores saltan turno en la misma ronda, el juego acaba.
        
        Parametros: turnos_saltados : la cantidad de turnos saltados en una ronda."""
        pass