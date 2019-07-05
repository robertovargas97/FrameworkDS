class Jugador():


    def __init__(self,jugador_T):
        #Instancia de jugador concreto para realizar puente
        self.jugador_concreto_t = jugador_T

    def obt_id(self):
        """Retorna un entero que representa el identificador del jugador"""
        return self.jugador_concreto_t.obt_id()
    
    def obt_nombre(self):
        """Retorna una string que- representa el nombre del jugador"""
        return self.jugador_concreto_t.obt_nombre()
    
    def obt_jugador_concreto(self):
        """Retorna la instancia del jugador concreto para hacer uso de sus metodos propios"""
        return self.jugador_concreto_t