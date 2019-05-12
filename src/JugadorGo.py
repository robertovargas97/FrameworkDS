from Jugador import Jugador
from PiezasGo import PiezasGo


class JugadorGo(Jugador):
    """Representa un jugador de Go"""

    def __init__(self, id):
        """Se construye un jugador con identificador y un objeto de tipo piezas"""
        self.id_jugador = str(id)  # Identificador del jugador
        self.piezas = PiezasGo()  # Objeto de tipo piezas que contiene la cantidad de piezas que posee el jugador
        self.tipo_piezas = []
        self.tipo_piezas.append(self.piezas.get_tipo()) #Arreglo con el tipo de piezas que hay en Go
        self.piezas_perdidas=0

    def obt_id(self):
        """Retorna una string que representa el identificador del jugador"""
        return self.id_jugador

    def validar_posicion(self, fila, columna, tablero):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorno : True en caso de que la posicion para colocar la ficha exista y este libre,False en caso contrario"""
        posicion_valida = True
        # Posicion no existe en el tablero
        if (((fila < 0) or (fila >= tablero.filas)) or ((columna < 0) or (columna >= tablero.columnas))):
            posicion_valida = False
        # La posicion existe entonces se verifica si esta marcada
        elif (tablero.tablero_juego[fila][columna] != '-'):
            posicion_valida = False
        return posicion_valida

    def colocar_ficha(self, fila, columna, tablero):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorn0 : True en caso de que se haya colocado una ficha en el tablero, False en caso contrario"""
        jugada_valida = False
        # Si la posicion es valida
        if (self.validar_posicion(fila, columna, tablero)):
            # Coloca la ficha en el tablero
            tablero.tablero_juego[fila][columna] = self.id_jugador
            jugada_valida = True
        return jugada_valida

    def obt_piezas_restantes(self):
        """Retorna la cantidad de piezas que le quedan al jugador"""
        return self.piezas.get_piezas()

    def eliminar_pieza(self):
        """Disminuye en una las piezas del jugador"""
        self.piezas.set_cantidad_piezas(self.piezas.cantidad_piezas - 1)
 
    def desplegar_piezas_perdidas(self):
        print("Jugador ",self.id_jugador, " ha perdido: ",self.piezas_perdidas,end=" piezas \n\n\n\n")


    def analizar_jugada(self,Contrincante):
        Contrincante.piezas_perdidas+=1
        Contrincante.desplegar_piezas_perdidas()
