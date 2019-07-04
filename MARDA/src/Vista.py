
class Vista():
    
    def __init__(self,vista_T):
    #Atributo de clase que podran usar las clases hijas
        self.vista_contreta_t = vista_T

    def dibujar_tablero(self, tablero, restantes_j1, restantes_j2, nombre1, nombre2, jugador_en_turno):
        """   """
        self.vista_contreta_t.dibujar_tablero(tablero, restantes_j1, restantes_j2, nombre1, nombre2, jugador_en_turno)

    def mostrar_reglas_juego(self):
        """   """
        self.vista_contreta_t.mostrar_reglas_juego()
     
    def mostrar_ventana_autores(self):
        """   """
        self.vista_contreta_t.mostrar_ventana_autores()
        
    def mostrar_menu_nombres(self):
        """   """
        self.vista_contreta_t.mostrar_menu_nombres()
    
    def obt_vista_concreta(self):
        """   """
        return self.vista_contreta_t
    

    
    
 
     
