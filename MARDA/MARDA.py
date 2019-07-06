from Controlador import Controlador

class MARDA():
    """Clase encargada de iniciar el MARDA."""

    def iniciar_MARDA(self):
        controlador = Controlador()
        controlador.iniciar_framework()
    
        if(controlador.m_tablero):
            controlador.mostrar_tablero()

if __name__ == "__main__":
    marda = MARDA()
    marda.iniciar_MARDA()