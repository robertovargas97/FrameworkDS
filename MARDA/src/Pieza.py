class Pieza():
   

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

    
    
 
     
