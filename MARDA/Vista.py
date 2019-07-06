
class Vista():
    """Clase general encargada de representar una vista"""

    
    def __init__(self,vista_T):
        """Constructor de clase.
        
        Parametros: vista_T: implementacion concreta de vista."""
        self.vista_contreta_t = vista_T

    def dibujar_tablero(self, tablero, restantes_j1, restantes_j2, nombre1, nombre2, jugador_en_turno):
        """Dibuja las celdas del tablero en la ventana de pygame.
        
        Parametros: restantes_j1 : piezas restantes del jugador 1.
                    restantes_j2 : piezas restantes del jugador 1.
                    nombre1:    nombre del jugador 1.
                    nombre2:    nombre del jugador 2.
                    jugador_en_turno : jugador que esta jugando actualmente."""""
        self.vista_contreta_t.dibujar_tablero(tablero, restantes_j1, restantes_j2, nombre1, nombre2, jugador_en_turno)

    def mostrar_reglas_juego(self):
        """Muestra un msj que indica las reglas mas importates a la hora de jugar"""
        self.vista_contreta_t.mostrar_reglas_juego()
     
    def mostrar_ventana_autores(self):
        """Muestra la ventana de los autores del framework"""
        self.vista_contreta_t.mostrar_ventana_autores()
        
    def mostrar_menu_nombres(self):
        """Muestra la ventana para ingresar los nombres de cada jugador"""
        self.vista_contreta_t.mostrar_menu_nombres()
    
    def obt_vista_concreta(self):
        """Retorno : instancia de la vista concreta para hacer uso de sus metodos propios"""
        return self.vista_contreta_t
    

    
    
 
     
