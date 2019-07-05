class Arbitro():
   
    def __init__(self,arbitro_T):
    #Atributo de clase que podran usar las clases hijas
        self.arbitro_contreto_t = arbitro_T

    def validar_posicion(self,fila,columna):
        return self.arbitro_contreto_t.validar_posicion(fila,columna)
    
    def obt_arbitro_concreto(self):
        return self.arbitro_contreto_t

    