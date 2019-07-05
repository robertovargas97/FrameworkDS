class Tablero():
   
    def __init__(self,tablero_T):
    #Atributo de clase que podran usar las clases hijas
        self.tablero_concreto_t = tablero_T
   
    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        self.tablero_concreto_t.crear_tablero()
   
    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        self.tablero_concreto_t.limpiar_tablero()
   
    def colocar_ficha(self, fila, columna, jugador):
        """fila , columna : posicion en el tablero\n
        jugador: instancia del jugador que coloca la pieza\n
        Retorno: True si se puede colocar la pieza, False en caso contrario"""
        return self.tablero_concreto_t.colocar_ficha(fila,columna,jugador)


    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe\n
        fila: fila en el tablero\n
        columna: columna en el tablero\n"""
        return self.tablero_concreto_t.validar_posicion(fila,columna)
        
    def obt_tablero_concreto(self):
        """Retorna la instancia de la pieza concreta para hacer uso de sus metodos propios"""
        return self.tablero_concreto_t
  
    