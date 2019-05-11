from Piezas import Piezas


class PiezasGo(Piezas):
    """Representa las piezas de Go que posee cada jugador"""

    # Se inicia con 81 piezas ya que el tablero es de 9 x 9 y en Go se puede tener tantas piezas como se quiera
    def __init__(self, cantidad_piezas=81):
        self.cantidad_piezas = cantidad_piezas
        self.tipo_pieza = "Piedra"

    def set_cantidad_piezas(self, cantidad_actual):
        """cantidad actual : cantidad de piezas que posee el jugador despues de alguna perdida o ganancia\n
        Coloca en la cantidad de piezas la cantidad de piezas actual"""
        self.cantidad_piezas = cantidad_actual

    def get_piezas(self):
        """Retorna un entero con la cantidad de piezas que posee el jugador"""
        return self.cantidad_piezas

    def get_tipo(self):
        """Retorna un string con el tipo de pieza a la que corresponde"""
        return self.tipo_pieza
