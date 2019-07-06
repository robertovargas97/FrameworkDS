class Jugador():
    """Clase general encargada de representar un jugador."""

    def __init__(self,jugador_T):
        """Constructor de clase.
        
        Parametros: jugador_T: implementacion concreta de jugador."""
        self.jugador_concreto_t = jugador_T

    def obt_id(self):
        """Retorno: un entero que representa el identificador del jugador"""
        return self.jugador_concreto_t.obt_id()
    
    def obt_nombre(self):
        """Retorno: string que representa el nombre del jugador"""
        return self.jugador_concreto_t.obt_nombre()
    
    def obt_jugador_concreto(self):
        """Retorno: instancia del jugador concreto para hacer uso de sus metodos propios"""
        return self.jugador_concreto_t