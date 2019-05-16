import abc
from abc import ABC


class Tablero(ABC):
    """Representacion abstracta del tablero en el que se jugara"""
    #No contiene atributos en comun ya que cada tablero especifico contendra los suyos

    @abc.abstractmethod
    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        pass

    @abc.abstractmethod
    def mostrar_tablero(self):
        """Muestra en pantalla el tablero"""
        pass

    @abc.abstractmethod
    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        pass

    @abc.abstractmethod
    def validar_posicion(self, fila, columna, tablero_jugador):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorno : True en caso de que la posicion para colocar la ficha exista y este libre,False en caso contrario"""
        pass

    @abc.abstractmethod
    def colocar_ficha(self, fila, columna, jugador,color_pieza):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorno : True en caso de que se haya colocado una ficha en el tablero, False en caso contrario"""
        pass
     
    # @abc.abstractmethod
    # def analizar_jugada(self,contrincante):
    #     """Despliega piezas perdidas"""
    #     pass     
    
    
def n():
    return "b","a",1

print(n())