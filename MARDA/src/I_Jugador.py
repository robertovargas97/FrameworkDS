import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase

class I_Jugador(ABC):
    """Representa una interfaz de un jugador"""

    def __init__(self):
        #Atributo de clase que podran usar las clases hijas
        
        self.id_jugador = '0'
        self.cantidad_piezas = 0 
        self.nombre = "" 

    # Se deben definir los siguientes metodos en el tipo de jugador especifico para el juego
    @abc.abstractmethod
    def obt_id(self):
        """Retorna una string que representa el identificador del jugador"""
        pass

    @abc.abstractmethod
    def obt_nombre(self):
        """Retorna una string que representa el nombre del jugador"""
        pass