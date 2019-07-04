from I_Controlador import I_Controlador

class Controlador(I_Controlador):
    
    def __init__(self,controlador_T):
    #Atributo de clase que podran usar las clases hijas
        self.controlador_concreto_t = controlador_T

    def iniciar_framework(self):
        """Inicia la interaccion entre el modelo y la vista para mostrar el framework"""
        self.controlador_concreto_t.iniciar_framework()
      
    def boton_autores_presionado(self):
        """Responde al evento de presionar el boton de autores para indicarle a la vista que debe mostrar una nueva ventana"""
        self.controlador_concreto_t.boton_autores_presionado()

    def boton_reglas_presionado(self):
        """Responde al evento de presionar el boton de reglas para indicarle a la vista que debe mostrar una nueva ventana"""
        self.controlador_concreto_t.boton_reglas_presionado()

    def validar_nombre(self,len_nombre,nom_j,num_j):
        self.validar_nombre(len_nombre,nom_j,num_j)
    
    def obtener_nombres(self):
        self.controlador_concreto_t.obtener_nombres()
    
    def elegir_color(self):
        self.controlador_concreto_t.elegir_color
    
    def movimiento_jugador(self,jugador,fila,columna,tablero,vista):
        self.controlador_concreto_t.movimiento_jugador(jugador,fila,columna,tablero,vista)
    
    def iniciar_tablero(self):
        self.controlador_concreto_t.iniciar_tablero()
       
    def obt_controlador_general(self):
        return self.controlador_concreto_t