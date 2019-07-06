class Pieza():
    """Clase general encargada de representar una pieza"""

    def __init__(self,pieza_T):
        """Constructor de clase.
        
        Parametros: pieza_T: implementacion concreta de pieza."""
        self.pieza_concreta_t = pieza_T

    def obt_fila(self):
        """Retoro : fila donde se encuentra la pieza"""
        return self.pieza_concreta_t.obt_fila()
        
    def obt_columna(self):
        """Retorno :  columna donde se encuentra la pieza"""
        return self.pieza_concreta_t.obt_columna()
    
    def obt_id(self):
        """Retorno : entero con el identificador de la pieza"""
        return self.pieza_concreta_t.obt_id()
    
    def obt_pieza_concreta(self):
        """Retorno : instancia de la pieza concreta para hacer uso de sus metodos propios"""
        return self.pieza_concreta_t

    
    
 
     
