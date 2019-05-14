import abc
from abc import ABC  # esta es la clase que permite la abstraccion para otras clase


class Jugador(ABC):
    """Representa un jugador"""

    def __init__(self):
        # Atributo de clase que podran usar las clases hijas
        self.id_jugador = '0'  # identificara al numero de jugador
        self.piezas_perdidas  = 0 # representa una instancia que tendra la cantidad de piezas que posee un jugador
        self.piezas = [] #Representara la piezas que tiene un jugador
        self.cantidad_piezas = 0
        
    # Se deben definir los siguientes metodos en el tipo de jugador especifico para el juego
    @abc.abstractmethod
    def get_id(self):
        """Retorna una string que representa el identificador del jugador"""
        pass

    @abc.abstractmethod
    def validar_posicion(self, fila, columna, tablero_jugador):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retornp : True en caso de que la posicion para colocar la ficha exista y este libre,False en caso contrario"""
        pass

    @abc.abstractmethod
    def colocar_ficha(self,fila,columna,tablero):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorn0 : True en caso de que se haya colocado una ficha en el tablero, False en caso contrario"""
        pass

    @abc.abstractmethod
    def get_piezas_restantes(self):
        """Retorna la cantidad de piezas que le quedan al jugador"""
        pass

    @abc.abstractmethod
    def eliminar_pieza(self):
        """Disminuye en una las piezas del jugador"""
        pass
    @abc.abstractmethod
    def retornar_piezas_perdidas(self):
        """Despliega piezas perdidas"""
        pass
    @abc.abstractmethod
    def analizar_jugada(self,contrincante):
        """Despliega piezas perdidas"""
        pass          
