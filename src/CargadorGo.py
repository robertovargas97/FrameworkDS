from Cargador_juego import Cargar_juego


class CargadorGO(Cargar_juego):


    def cargar_estado(self,archivo):
        print("cargando estado\n")
    
    def cargar_jugador_en_turno(self,jugador_en_turno):
        print("jugador en turno\n")

    
    def cargar_fichas_j1(self,jugador):
        print("cargando fichas\n")


    def main(self):
        self.cargar_estado()


if __name__ == "__main__":
    Cargador = CargadorGO()
    Cargador.main()
    