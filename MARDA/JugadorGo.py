from I_Jugador import I_Jugador


class JugadorGo(I_Jugador):
    """Representa un jugador de Go"""

    def __init__(self, id, color_pieza, nombre):
        """Constructor de la clase.
        
        Parametros: id : identificador del jugador.
                    color_pieza = color de pieza del jugador.
                    nombre : nombre del jugador. """
                    
        self.id_jugador = id
        self.piezas_perdidas = 0
        self.piezas_colocadas = []
        self.color_pieza = color_pieza
        self.cantidad_piezas = 41
        if(color_pieza == 2):
            self.cantidad_piezas = 40
        self.nombre = nombre

    def obt_id(self):
        """Retorno : entero que representa el identificador del jugador"""
        return self.id_jugador

    def obt_nombre(self):
        """Retorno : string que representa el nombre del jugador"""
        return self.nombre

    def obt_piezas_restantes(self):
        """Retorno : cantidad de piezas que le quedan al jugador"""
        return (self.cantidad_piezas - self.piezas_perdidas)

    def eliminar_pieza(self, cantidad_a_eliminar):
        """Disminuye las piezas del jugador
        
        Paramteros : cantidad_eliminar : numero de piedras que se le deben quitar al jugador"""
        self.cantidad_piezas -= cantidad_a_eliminar

    def obt_piezas_perdidas(self):
        """Retorno : cantidad de piezas perdidas"""
        return self.piezas_perdidas

    def obt_color_pieza(self):
        """Retorno : color de pieza del jugador"""
        return self.color_pieza

    def asignar_piezas_perdidas(self, piezas_perdidas):
        """Asigna la cantidad de piezas perdidas por turno al jugador
        
        Parametros : piezas_perdidas : cantidad de piezas que pierde un jugador or turno
        """
        self.piezas_perdidas += piezas_perdidas

    def asignar_cant_piezas(self, valor):
        """Asigna la cantidad de piezas al jugador
        
        Parametros : valor: cantidad de piezas que posee un jugador"""
        self.cantidad_piezas += valor
        
    def obt_total_piezas(self):
        """Retorno : cantidad total de piezas que posee un jugador"""
        return self.cantidad_piezas
