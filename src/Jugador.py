import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase


class Jugador(ABC):
    """Representa un jugador"""

    def __init__(self):
        # Atributo de clase que podran usar las clases hijas
        self.id_jugador = '0'  # identificara al numero de jugador
        # representa una instancia que tendra la cantidad de piezas que posee un jugador
        self.piezas_perdidas = 0
        self.piezas_colocadas = []  # Representara la piezas que un jugador tiene en el tablero
        self.cantidad_piezas = 0  # Esto se podria representar con len(piezas)
        self.nombre = ""  # Nombre del jugador

    # Se deben definir los siguientes metodos en el tipo de jugador especifico para el juego
    @abc.abstractmethod
    def obt_id(self):
        """Retorna una string que representa el identificador del jugador"""
        pass

    @abc.abstractmethod
    def obt_nombre(self):
        """Retorna una string que representa el nombre del jugador"""
        pass

    @abc.abstractmethod
    def obt_piezas_restantes(self):
        """Retorna la cantidad de piezas que le quedan al jugador"""
        pass

    @abc.abstractmethod
    def eliminar_pieza(self, cantidad_a_eliminar):
        """Disminuye en cantidad_a_eliminar las piezas del jugador"""
        pass

    @abc.abstractmethod
    def obt_piezas_perdidas(self):
        """Retorna la cantidad de piezas perdidas del jugador"""
        pass

    @abc.abstractmethod
    def obt_color_pieza(self):
        """Retorna el color de pieza del jugador"""
        pass
    @abc.abstractmethod    
    def set_piezas_perdidas(self,piezas_perdidas):
        pass    
