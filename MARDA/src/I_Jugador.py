import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase


class I_Jugador(ABC):
    """Representa un jugador"""

    def __init__(self):
        #Atributo de clase que podran usar las clases hijas
        
        #Identificara al numero de jugador
        self.id_jugador = '0'
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