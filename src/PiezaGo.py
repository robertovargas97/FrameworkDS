from Pieza import Pieza


class PiezaGo(Pieza):
    """Representa las piezas de Go que posee cada jugador"""


    def __init__(self,id,fila,columna):
        # Atributo de clase que podran usar las clases hijas
        if(id == 1):
            self.tipo_pieza = "N"   # String con el tipo de pieza que tiene un jugador
        elif(id == 2 ):
            self.tipo_pieza = "B" 
        self.fila = fila
        self.columna = columna
        self.id = id
        

    def get_fila(self):
        """ """
        return self.fila

    def get_columna(self):
        """ """
        return self.columna

    def get_id(self):
        """Retorna un entero con el identificador de la pieza"""
        return self.id
    
    def get_tipo(self):
        """Retorna un string con el tipo de pieza a la que corresponde"""
        return self.tipo_pieza