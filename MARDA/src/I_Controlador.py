import abc
from abc import ABC


class I_Controlador(ABC):

    @abc.abstractmethod
    def iniciar_framework(self):
        """Inicia la interaccion entre el modelo y la vista para mostrar el framework"""
        pass
      
    @abc.abstractmethod
    def boton_autores_presionado(self):
        """Responde al evento de presionar el boton de autores para indicarle a la vista que debe mostrar una nueva ventana"""
        pass
  
    @abc.abstractmethod
    def boton_reglas_presionado(self):
        """Responde al evento de presionar el boton de reglas para indicarle a la vista que debe mostrar una nueva ventana"""
        pass

    @abc.abstractmethod
    def validar_nombre(self,len_nombre,nom_j,num_j):
        pass
    
    @abc.abstractmethod
    def obtener_nombres(self):
        pass
    
    @abc.abstractmethod
    def elegir_color(self):
        pass
    
    @abc.abstractmethod
    def movimiento_jugador(self,jugador,fila,columna,tablero,vista):
        pass
    
    @abc.abstractmethod
    def iniciar_tablero(self):
        pass