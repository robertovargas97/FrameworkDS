from Vista import Vista
from Modelo import Modelo

class Controlador:

    def __init__(self):
        """Class initializer."""
        # Se crea la vista y el modelo en el controlador (Composition)
        self.vista = Vista(self) # Pass a Controller's reference to View
        self.model = Modelo()
        self.vista.mostrar_pantalla_inicial()
        self.n1 = None
        self.n2 = None
        
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
        self.vista.avisar_inicio_nigiri(self.n1,self.n2)
        self.vista.mostrar_ventana_nigiri() 
        
    def validar_nombre(self,len_nombre,nom_j,n_valido,num_j):
        if((len_nombre < 1 or ("Nombre del jugador") in nom_j ) and (n_valido == False) ):
            self.vista.error_nombre(num_j)
        else: 
            n_valido = True
            print("Nombre: ",nom_j)
            self.vista.deshabilitar_input_nombre(num_j)
            return n_valido
        
    def obtener_nombres(self):
        nom_j1 = str(self.vista.nombre1.get())
        nom_j2 = str(self.vista.nombre2.get())
        len_n1 = len(nom_j1)
        len_n2 = len(nom_j2)
        n1_valido = False
        n2_valido = False
        
        n1_valido = self.validar_nombre(len_n1, nom_j1 ,n1_valido,1)
        n2_valido = self.validar_nombre(len_n2, nom_j2 ,n2_valido,2)
        
        if( n1_valido and n2_valido ):
            self.vista.deshabilitar_boton_listo()
            self.vista.habilitar_boton_continuar()
            self.n1 = nom_j1
            self.n2 = nom_j2
            #Aqui ya se pueden dar los nombres ya sea al modelo o colocarlos en algo en 
            #el controlador
     
    def obtener_cantidad_piedras(self):
        print("Hola jaja")
        
    def retornar_nombre_jugador1(self):
        return self.n1 #Puede que sea el modelo el que devuelva esto
    
    def retornar_nombre_jugador2(self):
        return self.n2 #Puede que sea el modelo el que devuelva esto

        
        
        
controlador = Controlador()


