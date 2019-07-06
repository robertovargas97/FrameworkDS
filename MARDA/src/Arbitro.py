class Arbitro():
    """Clase general encargada de toda la validacion y reglamentacion del juego."""
   
    def __init__(self,arbitro_T):
        """Constructor de clase.
        
        Parametros:     arbitro_T: implementacion concreta de arbitro."""
        self.arbitro_concreto_t = arbitro_T

    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe.
        
        Parametros:     fila: fila en el tablero.
                        columna: columna en el tablero.
                        
        Retorno : True si la posicion es valida, False en caso contrario."""
        return self.arbitro_concreto_t.validar_posicion(fila,columna)
    
    def obt_arbitro_concreto(self):
        """Retorno: instancia concreta de arbitro para hacer uso de sus metodos especificos."""
        return self.arbitro_concreto_t

    