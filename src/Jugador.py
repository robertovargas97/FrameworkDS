import abc
from abc import ABC


class Jugador(ABC):

    def __init__(self):
    # Atributo de clase que podran usar las clases hijas
        self.id_jugador = 0
        self.cantidad_piezas = 0
        self.turno = 0

    # Se debe definir en el tipo se jugador especifico para el juego
    @abc.abstractmethod
    def obt_id(self):
        pass
    
    # Se debe definir en el tipo se jugador especifico para el juego
    @abc.abstractmethod
    def validar_posicion(self, fila, columna,tablero_jugador):
        pass

    # Se debe definir en el tipo se jugador especifico para el juego
    @abc.abstractmethod
    def colocar_ficha(self):
        pass
    
    # Se debe definir en el tipo se jugador especifico para el juego
    @abc.abstractmethod
    def obt_piezas_restantes(self):
        pass
    
    # Se debe definir en el tipo se jugador especifico para el juego
    @abc.abstractmethod
    def eliminar_pieza(self):
        pass
