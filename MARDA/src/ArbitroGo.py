from I_Arbitro import I_Arbitro

class ArbitroGo(I_Arbitro):
    
    def __init__(self,tablero):
        self.tablero = tablero
        
    def validar_fila(self,fila):
        """fila: fila en el tablero\n
        retorno : True si la fila es valida, False en caso contrario"""
        posicion_valida = True
        # Posicion no existe en el tablero
        if ((fila < 0) or (fila >= self.tablero.filas)):
            posicion_valida = False
        return posicion_valida
        
    def validar_columna(self,columna):
        """columna: columna en el tablero\n
        retorno : True si la columna es valida, False en caso contrario"""
        posicion_valida = True
        # Posicion no existe en el tablero
        if ((columna < 0) or (columna >= self.tablero.columnas)):
            posicion_valida = False
        return posicion_valida  

    def validar_posicion(self,fila,columna):
        """Valida si la posicion ingresada existe\n
        fila: fila en el tablero\n
        columna: columna en el tablero\n"""
        pos_valida = True 
        if (self.validar_fila(fila) == False)  or (self.validar_columna(columna) == False):
            pos_valida = False
        return pos_valida
    
    def saltar_turno(self, jugador):
        """Permite al jugador saltar su turno\n
        jugador : el jugador que ha decidido saltar el turno"""
        if jugador == 0:
            proximo_en_jugar = 1
        else:
            proximo_en_jugar = 0
        return proximo_en_jugar
    
    def verificar_tablero_lleno(self):
        """Verifica si ya no hay espacios en el tablero"""
        lleno = True
        for fila in range(self.tablero.filas):
            for columna in range(self.tablero.columnas):
                if(self.tablero.tablero_juego[fila][columna].obt_tipo() == "-"):
                    lleno = False
        return lleno

    def jugada_suicida(self,fila,col):
        j_suicida = False
        ficha_colocada = self.tablero.tablero_juego[fila][col]
        if ficha_colocada.obt_tipo() == "x":
            self.tablero.tablero_juego[fila][col].asignar_tipo("-")
            self.tablero.tablero_juego = self.tablero.copia_tablero
            self.tablero.agrupaciones = self.tablero.copia_agrupaciones
            j_suicida = True
        
        return j_suicida
    
    def terminar_juego(self, turnos_saltados):
        """Verifica si el juego ya acabo\n
        turnos_saltados : la cantidad de turnos saltados en una ronda. Si ambos jugadores saltan turno en la misma ronda, el juego acaba"""
        if(turnos_saltados == 2 or self.verificar_tablero_lleno() == True):
            return True
        else:
            return False
        
    def contar_puntos(self):
        puntos_jugador_1 = 0
        puntos_jugador_2 = 0
        for i in range(len(self.tablero.tablero_juego)):
            for j in range (len(self.tablero.tablero_juego[i])):
                if(self.tablero.tablero_juego[i][j].obt_tipo() == "N"):
                    puntos_jugador_1 = puntos_jugador_1 + 1
                    
                elif(self.tablero.tablero_juego[i][j].obt_tipo() == "B"):
                    puntos_jugador_2 = puntos_jugador_2 + 1
                
        return puntos_jugador_1,puntos_jugador_2
    
    def determinar_ganador(self,puntos_jugador_1,puntos_jugador_2):
        ganador = 0
        
        if(puntos_jugador_1 > puntos_jugador_2) :
            ganador = 1
        elif (puntos_jugador_2 > puntos_jugador_1):
            ganador = 2
            
        return ganador
    