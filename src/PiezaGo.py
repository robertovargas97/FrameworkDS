from Pieza import Pieza


class PiezaGo(Pieza):
    """Representa las piezas de Go que posee cada jugador"""


    def __init__(self,id,fila,columna,agrupacion):
        if(id == 1):
            self.tipo_pieza = "N"   # String con el tipo de pieza que tiene un jugador N para pieza Negra, B para pieza Blanca
        elif(id == 2 ):
            self.tipo_pieza = "B" 
        else:
            self.tipo_pieza = "-"
        self.fila = fila
        self.columna = columna
        self.id = id
        self.indice_agrupacion = agrupacion
        

    def obt_fila(self):
        """Retorna la fila donde se encuentra la pieza"""
        return self.fila

    def obt_columna(self):
        """Retorna la columna donde se encuentra la pieza"""
        return self.columna

    def obt_id(self):
        """Retorna un entero con el identificador de la pieza"""
        return self.id
    
    def obt_tipo(self):
        """Retorna un string con el tipo de pieza a la que corresponde"""
        return self.tipo_pieza
    
    def asignar_tipo(self,tipo):
        """Retorna un string con el tipo de pieza a la que corresponde"""
        self.tipo_pieza = tipo
    
    def obt_agrupacion(self):
        """Retorna un entero con el indice de la agrupacion"""
        return self.indice_agrupacion    
    
    def asignar_indice_agrupacion(self,indice):
        """Asigna el indice del agrupamiento al que pertenece"""
        self.indice_agrupacion = indice
    def copiar_pieza(self):
        """copia una pieza y retorna la copia"""
        pieza_nueva = PiezaGo(self.obt_id(),self.obt_fila(),self.obt_columna(),self.obt_agrupacion())
        pieza_nueva.tipo_pieza = self.tipo_pieza 
        return  pieza_nueva  