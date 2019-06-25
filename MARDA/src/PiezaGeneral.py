from I_Pieza import I_Pieza
from PiezaGo import PiezaGo

#Si se quieren usar metodos de la clase concreta simplemente deben heredar de esa clase
class Pieza_General(PiezaGo,I_Pieza):
    """Representa la piezas que posee cada jugador"""
    
    def __init__(self,pieza_concreta):
    #Atributo de clase que podran usar las clases hijas
        self.pieza_concr = pieza_concreta

    def obt_fila(self):
        """Retorna la fila donde se encuentra la pieza"""
        return self.pieza_concr.obt_fila()
        
    def obt_columna(self):
        """Retorna la columna donde se encuentra la pieza"""
        return self.pieza_concr.obt_columna()
    
    def obt_id(self):
        """Retorna un entero con el identificador de la pieza"""
        return self.pieza_concr.obt_id()
    
    def obt_pieza_general(self):
        return self.pieza_concr
    
if __name__ == "__main__":
    pieza = PiezaGo(0,5,3,1)
    pieza_gene = Pieza_General(pieza)
    
    print( pieza_gene.obt_fila() )
    print( pieza_gene.obt_columna() )
    print( pieza_gene.obt_id() )
    
    
    print( pieza_gene.obt_pieza_general().obt_agrupacion())

    
    
 
     
