from I_Pieza import I_Pieza

class PiezaGo(I_Pieza):
    """Representa una pieza del juego Go"""

    def __init__(self,id,fila,columna,agrupacion):
        """Constructor de la clase.
        
        Parametros: id : identificador de la pieza.
                    fila : fila donde se coloca la pieza.
                    columna : columna donde se agrega la pieza.
                    agrupacion : agrupacion a la que pertenece una pieza."""
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
        """Retorno : fila donde se encuentra la pieza"""
        return self.fila

    def obt_columna(self):
        """Retorno : columna donde se encuentra la pieza"""
        return self.columna

    def obt_id(self):
        """Retorno : entero con el identificador de la pieza"""
        return self.id
    
    def obt_tipo(self):
        """Retorno : string con el tipo de pieza a la que corresponde"""
        return self.tipo_pieza
    
    def asignar_tipo(self,tipo):
        """Retorno : string con el tipo de pieza a la que corresponde"""
        self.tipo_pieza = tipo
    
    def obt_agrupacion(self):
        """Retorno : entero con el indice de la agrupacion"""
        return self.indice_agrupacion    
    
    def asignar_indice_agrupacion(self,indice):
        """Asigna el indice del agrupamiento al que pertenece"""
        self.indice_agrupacion = indice
        
    def copiar_pieza(self):
        """Copia una pieza del juego.
        
        Retorno : copia de una instancia de pieza"""
        pieza_nueva = PiezaGo(self.obt_id(),self.obt_fila(),self.obt_columna(),self.obt_agrupacion())
        pieza_nueva.tipo_pieza = self.tipo_pieza 
        return  pieza_nueva  