from Piezas import Piezas


class PiezasGo(Piezas):

    #Se inicia con 81 piezas ya que el tablero es de 9 x 9 y en Go se puede tener tantas piezas como se quiera
    def __init__(self, cantidad_piezas = 81):
        self.cantidad_piezas = cantidad_piezas
        self.tipo = "PiezaGo"

    def set_cantidad_piezas(self, cantidad_actual):
        self.cantidad_piezas = cantidad_actual

    def get_piezas(self):
        return self.cantidad_piezas
    
    def get_tipo(self):
        return self.cantidad_piezas

