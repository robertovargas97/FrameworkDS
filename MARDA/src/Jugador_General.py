from I_Jugador import I_Jugador
from JugadorGo import JugadorGo


class Jugador_General(JugadorGo,I_Jugador):
    """Representa un jugador.\nHereda de un jugador abstracto,pero tambien se realiza la herencia multiple\n
    para que herede de un jugador concreto y pueda utilizar sus metodos"""

    def __init__(self,jugador_concreto):
        #Instancia de jugador concreto para realizar puente
        self.jug_concreto = jugador_concreto

    def obt_id(self):
        """Retorna un entero que representa el identificador del jugador"""
        return self.jug_concreto.obt_id()
    
    def obt_nombre(self):
        """Retorna una string que representa el nombre del jugador"""
        return self.jug_concreto.obt_nombre()
    
    def obt_jugador_general(self):
        """Retorna la instancia del jugador concreto para hacer uso de sus metodos propios"""
        return self.jug_concreto
        

if __name__ == "__main__":
    jugador = JugadorGo(0,"N","Roberto")
    jugGene = Jugador_General(jugador)
    
    print(jugGene.obt_jugador_general().obt_color_pieza())
    
    print( jugGene.obt_nombre() )
    
    
