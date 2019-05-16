from Jugador import Jugador

class JugadorGo(Jugador):
    """Representa un jugador de Go"""

    def __init__(self, id, color_pieza, nombre):
        """Se construye un jugador con identificador y un objeto de tipo piezas"""
        self.id_jugador = str(id)  # Identificador del jugador
        self.piezas_perdidas = 0
        self.piezas_colocadas = []
        self.color_pieza = color_pieza
        self.cantidad_piezas = 41
        if(color_pieza == 2):
            self.cantidad_piezas = 40
        self.nombre = nombre

    def obt_id(self):
        """Retorna una string que representa el identificador del jugador"""
        return self.id_jugador

    def obt_nombre(self):
        """Retorna una string que representa el identificador del jugador"""
        return self.nombre

    def obt_piezas_restantes(self):
        """Retorna la cantidad de piezas que le quedan al jugador"""
        return self.cantidad_piezas

    def eliminar_pieza(self, cantidad_a_eliminar):
        """Disminuye en una las piezas del jugador"""
        self.cantidad_piezas -= cantidad_a_eliminar

    def obt_piezas_perdidas(self):
        """Despliega piezas perdidas"""
        return self.piezas_perdidas
    
    def obt_color_pieza(self):
        """Despliega piezas perdidas"""
        return self.color_pieza

