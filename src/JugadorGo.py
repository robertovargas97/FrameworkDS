from Jugador import Jugador
from PiezasGo import PiezasGo


class JugadorGo(Jugador):

    def __init__(self, id):
        self.id_jugador = str(id)
        # Se colocan fichas igual a la cantidad de piezas del juego Go
        self.piezas = PiezasGo()

    def obt_id(self):
        return self.id_jugador

    def validar_posicion(self, fila, columna, tablero):
        posicion_valida = True
        # Posicion no existe en el tablero
        if (((fila < 0) or (fila >= tablero.filas)) or ((columna < 0) or (columna >= tablero.columnas))):
            posicion_valida = False
        # La posicion existe entonces se verifica si esta marcada
        elif (tablero.tablero_juego[fila][columna] != '-'):
            posicion_valida = False
        return posicion_valida

    def colocar_ficha(self, fila, columna, tablero):
        jugada_valida = False
        if (self.validar_posicion(fila, columna, tablero)):
            tablero.tablero_juego[fila][columna] = self.id_jugador
            jugada_valida = True
        return jugada_valida

    def obt_piezas_restantes(self):
        return self.piezas.get_piezas()

    def eliminar_pieza(self):
        self.piezas.set_cantidad_piezas(self.piezas.cantidad_piezas - 1)
