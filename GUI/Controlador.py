from Vista import Vista
from Modelo import Modelo

class Controlador:

    def __init__(self):
        """Class initializer."""
        # Se crea la vista y el modelo en el controlador (Composition)
        self.vista = Vista(self) #Referencia a la vista
        self.model = Modelo()
        self.nombre1 = ""
        self.nombre2 = ""
        self.piedras_jugador1 = 0
        self.piedras_jugador2 = 0
        
    def iniciar_interaccion(self):
        self.vista.mostrar_pantalla_inicial()
        
    def boton_autores_presionado(self):
        self.vista.mostrar_autores()
    
    def boton_reglas_presionado(self):
        self.vista.mostrar_reglas()
        
    def boton_entrar_presionado(self,op):
        self.vista.mostrar_menu_inicial(op)

    def boton_volver_presionado(self,ventana, metodo, opcion):
        self.vista.volver(ventana, metodo, opcion)
        
    def boton_jugar_presionado(self):
        self.vista.mostrar_menu_nombres()
        
    def boton_continuar_presionado(self):
        #Cambiar por si es el modelo el que debe dar los nombres
        self.vista.avisar_inicio_nigiri(self.nombre1,self.nombre2)
        self.vista.mostrar_ventana_nigiri() 
        
    def validar_nombre(self,len_nombre,nom_j,n_valido,num_j):
        n_valido = False
        if((len_nombre < 1 or ("Nombre del jugador") in nom_j ) and (n_valido == False) ):
            self.vista.error_nombre(num_j)
        else: 
            n_valido = True
            self.vista.deshabilitar_input_nombre(num_j)
            
        return n_valido
        
    def obtener_nombres(self):
        nom_j1 = str(self.vista.nombre1.get())
        nom_j2 = str(self.vista.nombre2.get())
        len_nombre1 = len(nom_j1)
        len_nombre2 = len(nom_j2)
        nombre1_valido = False
        nombre2_valido = False
        
        nombre1_valido = self.validar_nombre(len_nombre1, nom_j1 ,nombre1_valido,1)
        nombre2_valido = self.validar_nombre(len_nombre2, nom_j2 ,nombre2_valido,2)
        
        if( nombre1_valido and nombre2_valido ):
            self.vista.deshabilitar_boton_listo()
            self.vista.habilitar_boton_continuar(1)
            self.nombre1 = nom_j1
            self.nombre2 = nom_j2
            #Aqui ya se pueden dar los nombres ya sea al modelo o colocarlos en algo en 
            #el controlador
     
    def validar_cantidad_piedras(self,piedras_jugador,num_jugador):
        piedras_validas = False
        try:
            #Se intenta provocar el error
            piedras = int(piedras_jugador)
            if (num_jugador == 1):
                piedras_validas = True
                self.vista.deshabilitar_input_piedras(num_jugador)
                
            elif (num_jugador == 2 ):
                if (piedras > 0 and piedras <= 2):
                    piedras_validas = True
                    self.vista.deshabilitar_input_piedras(2)
                else:
                    raise Exception 
                
        except Exception:
            #Cambiar por si es el modelo el que debe dar los nombres
            if(num_jugador == 1):
                    self.vista.error_piedras(self.nombre1,1)
            elif (num_jugador == 2):
                    self.vista.error_piedras(self.nombre2,2)
                    
        return piedras_validas
                    
      
    def obtener_cantidad_piedras(self):
        piedras_j1_validas = False
        piedras_j2_validas = False
        
        piedras_j1 = self.vista.piedras_j1.get()
        piedras_j1_validas = self.validar_cantidad_piedras(piedras_j1,1)
        
        piedras_j2 = self.vista.piedras_j2.get()
        piedras_j2_validas = self.validar_cantidad_piedras(piedras_j2,2)
                
        if(piedras_j1_validas and piedras_j2_validas):
            self.vista.deshabilitar_boton_listo_nigiri()
            self.vista.habilitar_boton_continuar(2)
            self.piedras_jugador1 = piedras_j1
            self.piedras_jugador2 = piedras_j2
            #Aqui ya se pueden dar las piedras ya sea al modelo o colocarlos en algo en 
            #el controlador
            
    def retornar_nombre_jugador1(self):
        return self.nombre1 #Puede que sea el modelo el que devuelva esto
    
    def retornar_nombre_jugador2(self):
        return self.nombre2 #Puede que sea el modelo el que devuelva esto

    def main(self):
         self.iniciar_interaccion()
        
        
if __name__ == "__main__":
    controlador = Controlador()
    controlador.main()


