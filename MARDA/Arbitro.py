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
    
    def saltar_turno(self, jugador):
        """Permite al jugador saltar su turno.
        
        Parametros: jugador : el jugador que ha decidido saltar el turno.
        
        Retorno: el siguiente jugadir en turno (int)."""
        return self.arbitro_concreto_t.saltar_turno(jugador)
    
    def terminar_juego(self, turnos_saltados):
        """Verifica si el juego ya acabo.Si ambos jugadores saltan turno en la misma ronda, el juego acaba.
        
        Parametros: turnos_saltados : la cantidad de turnos saltados en una ronda."""
        return self.arbitro_concreto_t.terminar_juego(turnos_saltados)
    
    
    def obt_arbitro_concreto(self):
        """Retorno: instancia concreta de arbitro para hacer uso de sus metodos especificos."""
        return self.arbitro_concreto_t

    