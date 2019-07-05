from Tablero import Tablero
from PiezaGo import PiezaGo
from ArbitroGo import ArbitroGo

import random


class TableroGo(Tablero):
    """Implementacion especifica de un tablero de Go"""

    # Las filas y columnas se toman como valores por defecto
    def __init__(self, filas=9, columnas=9):
        self.filas = filas
        self.columnas = columnas
        self.tablero_juego = []
        self.agrupaciones = []
        self.copia_tablero = []
        self.copia_agrupaciones = []
        self.arbitro = ArbitroGo(self)

    def crear_tablero(self):
        """Crea el tablero del juego especifico con las respectivas dimensiones"""
        self.tablero_juego = [PiezaGo(-1,-1,-1,-1)] * self.filas  # Crea las filas del tablero
        for fila in range(self.filas):
            self.tablero_juego[fila] = [PiezaGo(-1, -1,-1,-1)] * self.columnas  # Crea las columnas del tablero
        # return self.tablero_juego
        
###########################################################################################################################################
    def mostrar_tablero(self):
        """Muestra en pantalla el tablero"""
        # Este for coloca el numero de columnas para mayor facilidad a la hora de colocar una posicion
        print()
        for i in range(self.filas):
            if(i == 0):
                print("   ", i, " ", end="")
            else:
                print(i, " ", end="")
        print()

        # Aca se empieza a imprimir la matriz como tal
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if(columna == 0):
                    print(
                        fila, " ", self.tablero_juego[fila][columna].obt_tipo(), " ", end="")
                else:
                    print(self.tablero_juego[fila][columna].obt_tipo(), " ", end="")
            print()
        print()
        
    def mostrar_tablero_copia(self):
        """Muestra en pantalla el tablero"""
        # Este for coloca el numero de columnas para mayor facilidad a la hora de colocar una posicion
        print()
        for i in range(self.filas):
            if(i == 0):
                print("   ", i, " ", end="")
            else:
                print(i, " ", end="")
        print()

        # Aca se empieza a imprimir la matriz como tal
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if(columna == 0):
                    print(
                        fila, " ", self.copia_tablero[fila][columna].obt_tipo(), " ", end="")
                else:
                    print(self.copia_tablero[fila][columna].obt_tipo(), " ", end="")
            print()
        print()
################################################################################################################################################

    def limpiar_tablero(self):
        """Limpia el tablero para reiniciar el juego"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.tablero_juego[fila][columna] = '-'
                
    def esta_libre(self, fila, columna):
        """fila , columna : posicion en el tablero\n
        Retorno : True en caso de que la posicion para colocar la ficha este libre,False en caso contrario"""
        posicion_valida = True
        if (self.tablero_juego[fila][columna].obt_tipo() != '-'):
            posicion_valida = False       
        return posicion_valida
                
    def colocar_ficha(self, fila, columna, jugador):
        """fila , columna : posicion en el tablero\n
        jugador: instancia del jugador que coloca la pieza\n
        Retorno: True si se puede colocar la pieza, False en caso contrario"""
        posicion_valida = False
        if(self.esta_libre(fila,columna) == True):
            pieza_nueva = PiezaGo(jugador.obt_color_pieza(), fila, columna,len(self.agrupaciones))
            jugador.piezas_colocadas.append(pieza_nueva)
            # Coloca la ficha en el tablero
            self.copia_tablero = self.copiar_tablero()
            self.copia_agrupaciones = self.copiar_agrupciones()
            self.tablero_juego[fila][columna] = pieza_nueva
            #cada ficha agregada se agrupa sola para posteriormente ver si se puede agrupar
            #con otras agrupaciones
            nuevo_agrupamiento = []
            nuevo_agrupamiento.append(pieza_nueva)
            
            self.agrupaciones.append(nuevo_agrupamiento)
            self.verificar_agrupamientos_vecinos(pieza_nueva)

            posicion_valida = True 
        
        return posicion_valida

    def verificar_agrupamientos_vecinos(self,ficha):
        """Verifica si es posible agruparse con grupos vecinos\n
        ficha: instancia de ficha que se va a colocar en el tablero"""
        fila = ficha.obt_fila()
        columna = ficha.obt_columna()

        if self.arbitro.validar_posicion(fila-1,columna) and self.tablero_juego[fila-1][columna].obt_tipo() == ficha.obt_tipo():
            ficha_arriba = self.tablero_juego[fila-1][columna]
            if ficha.obt_agrupacion() != ficha_arriba.obt_agrupacion():
                self.agrupar(ficha.obt_agrupacion(),ficha_arriba.obt_agrupacion())
        
        if self.arbitro.validar_posicion(fila+1,columna) and self.tablero_juego[fila+1][columna].obt_tipo() == ficha.obt_tipo():
            ficha_abajo = self.tablero_juego[fila+1][columna]
            if ficha.obt_agrupacion() != ficha_abajo.obt_agrupacion():
                self.agrupar(ficha.obt_agrupacion(),ficha_abajo.obt_agrupacion())
        
        if self.arbitro.validar_posicion(fila,columna+1) and self.tablero_juego[fila][columna+1].obt_tipo() == ficha.obt_tipo():
            ficha_der = self.tablero_juego[fila][columna+1]
            if ficha.obt_agrupacion() != ficha_der.obt_agrupacion():
                self.agrupar(ficha.obt_agrupacion(),ficha_der.obt_agrupacion())
            
        if self.arbitro.validar_posicion(fila,columna-1) and self.tablero_juego[fila][columna-1].obt_tipo() == ficha.obt_tipo():
            ficha_izq = self.tablero_juego[fila][columna-1]
            if ficha.obt_agrupacion() != ficha_izq.obt_agrupacion():
                self.agrupar(ficha.obt_agrupacion(),ficha_izq.obt_agrupacion())
    
    def agrupar(self,indiceA,indiceB):
        """Agrupa las fichas vecinas en caso de que sea posible,puede agrupar agrupamientos\n
        indiceA : indice del agrupamiento de la ficha recien colocada\n
        indiceB : indice del agrupamiento que va a anadir"""
        agrupA = self.agrupaciones[indiceA]
        agrupB = self.agrupaciones[indiceB]
        inicio_corrimiento = indiceB+1

        for i in range(inicio_corrimiento,len(self.agrupaciones)):
            self.actualizar_indice_agrupamiento(self.agrupaciones[i],i-1)
            
        self.actualizar_indice_agrupamiento(agrupB,indiceA-1)
        agrupA.extend(agrupB)
        self.agrupaciones.remove(agrupB)
    
    def actualizar_indice_agrupamiento(self,agrupamiento,indice_nuevo):
        """Actualiza el indice del agrupamiento de la ficha que se acaba de colocar\n
        agrupamiento : agrupamiento al que se le actualiza el indice\n
        indice_nuevo : nuevo valor de indice del agrupamiento"""
        for i in range(len(agrupamiento)):
            agrupamiento[i].indice_agrupacion = indice_nuevo
    
    def revisar_eliminar_agrupamientos(self):
        """Verifica si algun agrupamiento tiene inidice invalido para eliminarlo del tablero"""
        fichas_eliminadas=0
        for index in range(len(self.agrupaciones)):
            if self.libertades_agrupamiento(self.agrupaciones[index]) == 0:
                fichas_eliminadas+=self.invalidar_agrupamiento(self.agrupaciones[index])
        
        return fichas_eliminadas        

    def libertades_agrupamiento(self,agrupamiento):
        """Retorna si un grupo tiene grados de libertad"""
        for index in range(len(agrupamiento)):
            if self.libertades_ficha(agrupamiento[index]) >=1:
                return 1
        return 0

    def libertades_ficha(self,ficha):
        """Retorna si una ficha tiene grados de libertad\n
        ficha : la ficha a la que se le revisan los grados de libertad"""
        fila = ficha.obt_fila()
        columna = ficha.obt_columna()

        if self.arbitro.validar_posicion(fila-1,columna) and (self.tablero_juego[fila-1][columna].obt_tipo() == "-" or self.tablero_juego[fila-1][columna].obt_tipo() == "x"):
            return 1  
        if self.arbitro.validar_posicion(fila+1,columna) and (self.tablero_juego[fila+1][columna].obt_tipo() == "-" or self.tablero_juego[fila+1][columna].obt_tipo() == "x"):
            return 1
        if self.arbitro.validar_posicion(fila,columna+1) and (self.tablero_juego[fila][columna+1].obt_tipo() == "-" or self.tablero_juego[fila][columna+1].obt_tipo() == "x"):
            return 1
        if self.arbitro.validar_posicion(fila,columna-1) and (self.tablero_juego[fila][columna-1].obt_tipo() == "-" or self.tablero_juego[fila][columna-1].obt_tipo() == "x"):
            return 1 
        return 0
    
    def invalidar_agrupamiento(self,agrupamiento):
        """Invalida un agrupamiento\n
        agrupamiento : agrupamiento que se invalidara"""
        for index in range(len(agrupamiento)):
            agrupamiento[index].asignar_tipo("x") 
        return len(agrupamiento)       

    def copiar_tablero(self):
        tablero_copia = [[PiezaGo(-1,-1,-1,-1) for j in range(self.columnas)] for i in range(self.filas)]

        for fil in range(self.filas):
            for col in range(self.columnas):
                tablero_copia[fil][col] = self.tablero_juego[fil][col].copiar_pieza()
        return tablero_copia    

    def copiar_agrupciones(self):
        copia_agrups = []
        for i in range(len(self.agrupaciones)):
            lista = []
            for j in range(len(self.agrupaciones[i])):
                #tengo que llenar la copia de las agrupaciones
                #con referencias al tablero copiado
                fila = self.agrupaciones[i][j].obt_fila()
                col = self.agrupaciones[i][j].obt_columna()
                lista.append(self.copia_tablero[fila][col])

            copia_agrups.append(lista)

        return copia_agrups
        
        
        
        