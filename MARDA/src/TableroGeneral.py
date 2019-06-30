from I_Tablero import I_Tablero
from TableroGo import TableroGo


class TableroGeneral(TableroGo,I_Tablero):
    """Representa el tablerodel juego\nHereda de un tablero abstract,pero tambien realiza la herencia multiple\n
    para que herede de una pieza concreta y pueda utilizar sus metodos"""
    #No contiene atributos en comun ya que cada tablero especifico contendra los suyos

    def __init__(self,tablero_concreto):
    #Atributo de clase que podran usar las clases hijas
        self.tablero_concreto = tablero_concreto
   
    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        self.tablero_concreto.crear_tablero()
   
    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        self.tablero_concreto.limpiar_tablero()
   
    def colocar_ficha(self, fila, columna, jugador):
        """fila , columna : posicion en el tablero\n
        jugador: instancia del jugador que coloca la pieza\n
        Retorno: True si se puede colocar la pieza, False en caso contrario"""
        self.tablero_concreto.colocar_ficha(fila,columna,jugador)


    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe\n
        fila: fila en el tablero\n
        columna: columna en el tablero\n"""
        self.tablero_concreto.validar_posicion(fila,columna)
        
    # def mostrar_tablero(self):
    #     """Muestra en pantalla el tablero"""
    #     pass
        
    # def esta_libre(self, fila, columna):
    #     """fila , columna : posicion en el tablero\n
    #     Retorno : True en caso de que la posicion para colocar la ficha este libre,False en caso contrario"""
    #     pass
    
    # def validar_fila(self,fila):
    #     """fila: fila en el tablero\n
    #     retorno : True si la fila es valida, False en caso contrario"""
    #     pass
    
    # def validar_columna(self,columna):
    #     """columna: columna en el tablero\n
    #     retorno : True si la columna es valida, False en caso contrario"""
    #     pass
    