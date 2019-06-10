from Jugador import Jugador


class JugadorGo(Jugador):
    """Representa un jugador de Go"""

    def __init__(self, id, color_pieza, nombre):
        """Se construye un jugador"""
        self.id_jugador = id
        self.piezas_perdidas = 0
        self.piezas_colocadas = []
        self.color_pieza = color_pieza
        self.cantidad_piezas = 41
        if(color_pieza == 2):
            self.cantidad_piezas = 40
        self.nombre = nombre

    def obt_id(self):
        """Retorna un entero que representa el identificador del jugador"""
        return self.id_jugador

    def obt_nombre(self):
        """Retorna una string que representa el nombre del jugador"""

        return self.nombre

    def obt_piezas_restantes(self):
        """Retorna la cantidad de piezas que le quedan al jugador"""
        return (self.cantidad_piezas - self.piezas_perdidas)

    def eliminar_pieza(self, cantidad_a_eliminar):
        """Disminuye en cantidad_a_eliminar las piezas del jugador"""
        self.cantidad_piezas -= cantidad_a_eliminar

    def obt_piezas_perdidas(self):
        """Retorna la cantidad de piezas perdidas"""
        return self.piezas_perdidas

    def obt_color_pieza(self):
        """Retorna el color de pieza del jugador"""
        return self.color_pieza

    def asignar_piezas_perdidas(self, piezas_perdidas):
        """Asigna la cantidad de piezas perdidas por turno al jugador"""
        self.piezas_perdidas += piezas_perdidas

    def asignar_cant_piezas(self, valor):
        """Asigna la cantidad de piezas al jugador"""
        self.cantidad_piezas += valor
        
    def obt_total_piezas(self):
        return self.cantidad_piezas
