class Pieza():
    """Representa la piezas que posee cada jugador\nHereda de una pieza abstracta,pero tambien realiza la herencia multiple\n
    para que herede de una pieza concreta y pueda utilizar sus metodos"""

    def __init__(self,pieza_T):
    #Atributo de clase que podran usar las clases hijas
        self.pieza_contreta_t = pieza_T

    def obt_fila(self):
        """Retorna la fila donde se encuentra la pieza"""
        return self.pieza_contreta_t.obt_fila()
        
    def obt_columna(self):
        """Retorna la columna donde se encuentra la pieza"""
        return self.pieza_contreta_t.obt_columna()
    
    def obt_id(self):
        """Retorna un entero con el identificador de la pieza"""
        return self.pieza_contreta_t.obt_id()
    
    def obt_pieza_concreta(self):
        """Retorna la instancia de la pieza concreta para hacer uso de sus metodos propios"""
        return self.pieza_contreta_t
    
if __name__ == "__main__":
    
    from PiezaGo import PiezaGo
    
    pieza_T = PiezaGo(0,5,3,1)
    
    pieza_concreta = Pieza(pieza_T)
    
    print( pieza_concreta.obt_fila() )
    print( pieza_concreta.obt_columna() )
    print( pieza_concreta.obt_id() )
    
    print( pieza_concreta.obt_pieza_concreta().obt_agrupacion())

    
    
 
     
