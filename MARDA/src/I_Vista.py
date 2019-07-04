import abc
from abc import ABC


class I_Vista(ABC):

    @abc.abstractmethod
    def dibujar_tablero(self, tablero, restantes_j1, restantes_j2, nombre1, nombre2, jugador_en_turno):
        """"""
        pass

    @abc.abstractmethod
    def mostrar_reglas_juego(self):
        """"""
        pass

    @abc.abstractmethod
    def colocar_boton(self):
        """"""
        pass
    
    @abc.abstractmethod
    def mostrar_ventana_autores(self):
        """"""
        pass
    
    @abc.abstractmethod
    def mostrar_menu_nombres(self):
        pass