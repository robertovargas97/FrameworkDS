from I_Jugador import I_Jugador
from JugadorGo import JugadorGo

class Jugador_General(I_Jugador):
    """Representa un jugador"""

    def __init__(self,jugador_concreto):
        #Atributo de clase que podran usar las clases hijas
        self.jug_concreto = jugador_concreto

    def obt_id(self):
        """Retorna un entero que representa el identificador del jugador"""
        return self.jug_concreto.obt_id()
    
    def obt_nombre(self):
        """Retorna una string que representa el nombre del jugador"""
        return self.jug_concreto.obt_nombre()
        

if __name__ == "__main__":
    jugador = JugadorGo(0,"N","Roberto")
    jugGene = Jugador_General(jugador)
    
    print( jugGene.obt_nombre() )
    
    
