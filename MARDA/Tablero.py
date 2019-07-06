class Tablero():
    """Clase general encargada de representar una tablero."""
   
    def __init__(self,tablero_T):
        """Constructor de clase.
        
        Parametros: tablero_T: implementacion concreta de tablero."""
        self.tablero_concreto_t = tablero_T
   
    def crear_tablero(self):
        """Crea el tablero del juego con las respectivas dimensiones."""
        self.tablero_concreto_t.crear_tablero()
   
    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        self.tablero_concreto_t.limpiar_tablero()
   
    def colocar_ficha(self, fila, columna, jugador):
        """
        Parametros: fila , columna : posicion en el tablero.
                    jugador: instancia del jugador que coloca la pieza.
                    
        Retorno: True si se puede colocar la pieza, False en caso contrario."""
        return self.tablero_concreto_t.colocar_ficha(fila,columna,jugador)

    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe.
        
        Parametros :    fila: fila en el tablero.
                        columna: columna en el tablero."""
        return self.tablero_concreto_t.validar_posicion(fila,columna)
        
    def obt_tablero_concreto(self):
        """Retorno : instancia de tablero concreto para hacer uso de sus metodos propios"""
        return self.tablero_concreto_t
  
    