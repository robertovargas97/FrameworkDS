from ControladorGo import ControladorGo
from Controlador import Controlador
from VistaGo import VistaGo
from Vista import Vista


class Framework():
    
    vista_Go = VistaGo()
    vista_concreta = Vista(vista_Go)
    
    
    controlador_concreto = ControladorGo(vista_concreta)
    controlador_general = Controlador(controlador_concreto)
    
    
    controlador_general.iniciar_framework()
    
    if(controlador_general.obt_controlador_general().m_tablero):
        controlador_general.obt_controlador_general().mostrar_tablero()