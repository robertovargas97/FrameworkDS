from Tablero import Tablero
from PiezaGo import PiezaGo


class TableroGo(Tablero):
    """Implementacion especifica de un tablero de Go"""

    # Las filas y columnas se toman como valores por defecto
    def __init__(self, filas=9, columnas=9):
        self.filas = filas
        self.columnas = columnas
        self.tablero_juego = []

    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        self.tablero_juego = ['-'] * self.filas  # Crea las filas del tablero
        for fila in range(self.filas):
            self.tablero_juego[fila] = ['-'] * self.columnas  # Crea las columnas del tablero
        # return self.tablero_juego

    def mostrar_tablero(self):
        """Muestra en pantalla el tablero"""
        # Este for coloca el numero de columnas para mayor facilidad a la hora de colocar una posicion
        for i in range(self.filas):
            if(i == 0):
                print("   ", i, " ", end="")
            else:
                print(i, " ", end="")
        print()

        # Aca se empieza a imprimir la matriz como tal
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if(columna == 0):
                    print(fila, " ", self.tablero_juego[fila][columna], " ", end="")
                else:
                    print(self.tablero_juego[fila][columna], " ", end="")
            print()
        print()

    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.tablero_juego[fila][columna] = '-'

    def validar_posicion(self, fila, columna):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorno : True en caso de que la posicion para colocar la ficha exista y este libre,False en caso contrario"""
        posicion_valida = True
        # Posicion no existe en el tablero
        if (((fila < 0) or (fila >= self.filas)) or ((columna < 0) or (columna >= self.columnas))):
            posicion_valida = False
        # La posicion existe entonces se verifica si esta marcada
        elif (self.tablero_juego[fila][columna] != '-'):
            posicion_valida = False
        return posicion_valida

    def colocar_ficha(self, fila, columna, jugador, color_pieza):
        """fila , columna : posicion en el tablero\n
            tablero : objeto de tipo tablero donde se colocara la ficha\n
            Retorn0 : True en caso de que se haya colocado una ficha en el tablero, False en caso contrario"""
        jugada_valida = False
        # Si la posicion es valida
        if (self.validar_posicion(fila, columna)):
            pieza_nueva = PiezaGo(color_pieza, fila, columna)
            jugador.piezas_colocadas.append(pieza_nueva)
            # Coloca la ficha en el tablero
            self.tablero_juego[fila][columna] = pieza_nueva.get_tipo()
            jugada_valida = True
        return jugada_valida


    # def analizar_jugada(self,contrincante):

        #     contrincante.piezas_perdidas += 1

        #     print("Jugador: ",contrincante.id_jugador,"ha perdido ",contrincante.piezas_perdidas,"piezas\n")
