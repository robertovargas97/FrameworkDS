from Jugador import Jugador
from PiezaGo import PiezaGo


class JugadorGo(Jugador):
    """Representa un jugador de Go"""

    def __init__(self, id, color_pieza,nombre):
        """Se construye un jugador con identificador y un objeto de tipo piezas"""
        self.id_jugador = str(id)  # Identificador del jugador
        self.piezas_perdidas = 0
        self.piezas = []
        self.color_pieza = color_pieza
        self.cantidad_piezas = 41
        if( color_pieza == 2):
            self.cantidad_piezas = 40
        self.nombre = nombre
        
       
    def get_id(self):
        """Retorna una string que representa el identificador del jugador"""
        return self.id_jugador
    
    def get_nombre(self):
        """Retorna una string que representa el identificador del jugador"""
        return self.nombre

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
            pieza_nueva = PiezaGo(self.color_pieza,fila,columna)
            self.piezas.append(pieza_nueva)
            # Coloca la ficha en el tablero
            tablero.tablero_juego[fila][columna] = pieza_nueva.get_tipo()
            jugada_valida = True
        return jugada_valida

    def get_piezas_restantes(self):
        """Retorna la cantidad de piezas que le quedan al jugador"""
        return self.cantidad_piezas

    def eliminar_pieza(self):
        """Disminuye en una las piezas del jugador"""
        self.cantidad_piezas -= 1
 
    def retornar_piezas_perdidas(self):
        return self.piezas_perdidas

    def analizar_jugada(self,contrincante):
        
        contrincante.piezas_perdidas += 1

        print("Jugador: ",contrincante.id_jugador,"ha perdido ",contrincante.piezas_perdidas,"piezas\n")

    def esta_conectada(self, pieza):
        x = pieza.get_fila()
        y = pieza.get_columna()
        color = pieza.get_id()
        for i in range (0, len(self.piezas)):
            if(self.piezas[i].get_id() == color):
                if(self.piezas[i].get_fila() == x-1 and self.piezas[i].get_columna() == y): # se pueden meter todos en una condicion, pero se ve muy feo
                    return True
                elif(self.piezas[i].get_fila() == x+1 and self.piezas[i].get_columna() == y):
                    return True
                elif(self.piezas[i].get_fila() == x and self.piezas[i].get_columna() == y-1):
                    return True
                elif(self.piezas[i].get_fila() == x and self.piezas[i].get_columna() == y+1):
                    return True
                else:
                    return False
        
