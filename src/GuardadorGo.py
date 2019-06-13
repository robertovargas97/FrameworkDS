from Guardador_juego import Guardar_juego
from JugadorGo import JugadorGo


class GuardarGo(Guardar_juego):

    def __init__(self,j1,j2,matriz,archivo):
        self.jugador_uno = j1
        self.jugador_dos = j2
        self.matriz = matriz
        self.archivo = archivo

    def guardar_estado(self):
        self.archivo= open("guardado.go","w+")

        self.jugador_uno = JugadorGo(0,1,0)
        self.jugador_uno.nombre = "aaron"
        self.jugador_uno.cant_piezas = 41
        self.jugador_uno.piezas_perdidas = 0

        self.jugador_dos = JugadorGo(0,2,0)
        self.jugador_dos.nombre = "denisse"
        self.jugador_dos.cant_piezas = 40
        self.jugador_dos.piezas_perdidas = 0
        
        self.guardar_nombres_jugadores()
        self.guardar_fichas_jugadores()
        #self.guardar_matriz()
    
    def guardar_nombres_jugadores(self):
        self.archivo.write("n1:%s\n" %self.jugador_uno.obt_nombre())
        self.archivo.write("n2:%s\n" %self.jugador_dos.obt_nombre())
    
    def guardar_fichas_jugadores(self):
        self.archivo.write("f1:%s\n" %self.jugador_uno.obt_piezas_restantes())
        self.archivo.write("f2:%s\n" %self.jugador_dos.obt_piezas_restantes())
    
    #def guardar_matriz(self):
    
    #def guarda_color_jugador(self):


if __name__ == "__main__":
    x = GuardarGo(0,0,0,0)
    x.guardar_estado()