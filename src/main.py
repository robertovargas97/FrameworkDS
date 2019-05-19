from TableroGo import TableroGo  # Se importa la clase como tal y no como modulo
from JugadorGo import JugadorGo

def mostrar_menu_inicial():
    print("\nBienvenido al juego de Go.\n")  # Menu inicial
    print("1. Jugar.")
    print("2. Salir del menu.\n")

def pedir_nombres():
    nombre1 = input("\nDigite el nombre del jugador 1: ")
    nombre2 = input("Digite el nombre del jugador 2: ")
    return nombre1, nombre2

################################## No se si estos metodos que vienen pueden ir en tablero #########################################################################################################
def pedir_cantidad_piedras():
    salir = False
    j1 = False
    j2 = False
    
    while (salir == False):
        try:
            if(j1 == False): 
                piedras_j1 = int(input("Jugador 1 ingrese la cantidad de piedras que elige: "))
                j1 = True # Si la opcion del j1 es correcta
                
            if (j2 == False):
                piedras_j2 = int(input("Jugador 2 ingrese 1 o 2 piedras: "))
                if(piedras_j2 == 1 or piedras_j2 == 2):
                    salir = True
                else:
                    raise ValueError
        except ValueError:
            print("Ingrese una cantidad de piedras valida.")
            
    return piedras_j1, piedras_j2


def mostrar_jugador_en_turno(jugador):
    print(jugador.obt_nombre(), "en turno.")
    print(jugador.obt_nombre()," tiene: ",jugador.obt_piezas_restantes()," piezas\n")


def realizar_jugada(tablero,jugador,contrincante):
    movimiento_jugador = False
    while(movimiento_jugador == False):
        fila, columna = tablero.pedir_posicion()            
        if (tablero.colocar_ficha(fila, columna, jugador) == False):
            print("\nNo puede colocar una ficha en esta posicion!!!\n")
        else:
            movimiento_jugador = True
            jugador.set_cant_piezas(-1)
            contrincante.set_piezas_perdidas(tablero.revisar_eliminar_agrupamientos())
            
            

def main():
    
    negro = 1
    blanco = 2
    opc_correcta = False
    # Se muestran las opciones iniciales
    mostrar_menu_inicial()
    
    while(opc_correcta == False): #En caso de que no se presione 1 para jugar o dos para salir
        try:
            opcion = int(input("Digite una opcion: "))
            if(opcion == 1):
                opc_correcta == True
                # Instancia de la clase Tablero
                tableroGo = TableroGo()
                tableroGo.crear_tablero()
                nombre1, nombre2 = pedir_nombres() 

                print("\nComienza el Nigiri")
                
                # Este print puede omitirse una vez que tengamos las reglas
                print("Inicia el jugador con las piedras negras.\n")
                piedras_j1,piedras_j2 = pedir_cantidad_piedras()
                
                color = tableroGo.nigiri(piedras_j1,piedras_j2)
                tableroGo.mostrar_resultado_nigiri(color,piedras_j1,piedras_j2)

                if(color == 1):
                    jugador1 = JugadorGo(1, negro, nombre1)
                    jugador2 = JugadorGo(2, blanco, nombre2)
                    proximo_en_jugar = 1

                else:
                    jugador1 = JugadorGo(1, blanco, nombre1)
                    jugador2 = JugadorGo(2, negro, nombre2)
                    proximo_en_jugar = 2
                                
                continuar_jugando = 1
                while(continuar_jugando == 1):
                    tableroGo.mostrar_tablero()

                    if(proximo_en_jugar == 1):
                        mostrar_jugador_en_turno(jugador1)
                        realizar_jugada(tableroGo,jugador1,jugador2)
                        proximo_en_jugar = 2
                
                    elif (proximo_en_jugar == 2):
                        mostrar_jugador_en_turno(jugador2)
                        realizar_jugada(tableroGo,jugador2,jugador1)
                        proximo_en_jugar = 1
 
            elif (opcion == 2):
                return 0
            else:
                raise ValueError

        except ValueError:
            print("Debe ingresar un valor correcto.")
        except KeyboardInterrupt:
            print("Se interrumpio el programa con Ctrl + C. ")
            return 0


if __name__ == "__main__":
    main()
