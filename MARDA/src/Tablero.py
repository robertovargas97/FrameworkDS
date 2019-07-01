class Tablero():
    """Representa el tablerodel juego\nHereda de un tablero abstract,pero tambien realiza la herencia multiple\n
    para que herede de una pieza concreta y pueda utilizar sus metodos"""
    #No contiene atributos en comun ya que cada tablero especifico contendra los suyos

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
        self.tablero_concreto_t.colocar_ficha(fila,columna,jugador)


    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe\n
        fila: fila en el tablero\n
        columna: columna en el tablero\n"""
        self.tablero_concreto_t.validar_posicion(fila,columna)
        
    def obt_tablero_concreto(self):
        """Retorna la instancia de la pieza concreta para hacer uso de sus metodos propios"""
        return self.tablero_concreto_t
  
  
if __name__ == "__main__":
    
    from TableroGo import TableroGo 
    
    tablero_T = TableroGo()
    
    tablero_concreto = Tablero(tablero_T)
    
    tablero_concreto.crear_tablero()
    
    tablero_concreto.obt_tablero_concreto().mostrar_tablero()
    