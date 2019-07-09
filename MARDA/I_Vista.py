import abc
from abc import ABC


class I_Vista(ABC):

    @abc.abstractmethod
    def dibujar_tablero(self, tablero, restantes_j1, restantes_j2, nombre1, nombre2, jugador_en_turno):
        """Dibuja las celdas del tablero en la ventana de pygame.
        
        Parametros: tablero: representacion logica de lo que se debe dibujar.
                    restantes_j1 : piezas restantes jugador 1.
                    restantes_j2 : piezas restantes jugador 2.
                    nombre1 : nombre jugador 1.
                    nombre2 : nombre jugador 1.
                    jugador_en_turno : jugador que esta jugando en ese momento."""
        pass

    @abc.abstractmethod
    def mostrar_reglas_juego(self):
        """Muestra un msj que indica las reglas mas importates a la hora de jugar"""
        pass

    @abc.abstractmethod
    def mostrar_ventana_autores(self):
        """Muestra la ventana de los autores del framework"""
        pass
    
    @abc.abstractmethod
    def mostrar_menu_nombres(self):
        """Muestra la ventana para ingresar los nombres de cada jugador"""
        pass
    