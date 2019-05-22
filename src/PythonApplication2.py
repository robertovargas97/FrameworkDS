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


def pedir_fila(tablero):
    """Pide la fila donde se quiere colocar la pieza\n
    retorno: el numero de fila que se ingreso"""
    salir = False
    fila = 0
    while(salir == False):
        try:
            fila = int(
                input("Ingrese la fila en la que desea colocar la ficha: "))
            if (tablero.validar_fila(fila) == True):
                salir = True
            else:
                raise ValueError
        except ValueError:
            print("Fila invalida.")

    return fila


def pedir_columna(tablero):
    """Pide la columna donde se quiere colocar la pieza\n
    retorno: el numero de columna que se ingreso"""
    salir = False
    columna = 0
    while(salir == False):
        try:
            columna = int(
                input("Ingrese la columna en la que desea colocar la ficha: "))
            if (tablero.validar_columna(columna) == True):
                salir = True
            else:
                raise ValueError
        except ValueError:
            print("Columna invalida.")

    return columna


def pedir_posicion(tablero):
    """Se pide la posicion donde se colocara la pieza en el tablero"""
    fila = pedir_fila(tablero)
    columna = pedir_columna(tablero)
    return fila, columna


def pedir_cantidad_piedras():
    salir = False
    j1 = False
    j2 = False

    while (salir == False):
        try:
            if(j1 == False):
                piedras_j1 = int(
                    input("Jugador 1 ingrese la cantidad de piedras que elige: "))
                j1 = True  # Si la opcion del j1 es correcta

            if (j2 == False):
                piedras_j2 = int(input("Jugador 2 ingrese 1 o 2 piedras: "))
                if(piedras_j2 == 1 or piedras_j2 == 2):
                    salir = True
                else:
                    raise ValueError
        except ValueError:
            print("Ingrese una cantidad de piedras valida.")

    return piedras_j1, piedras_j2

def nigiri(piezasj1, piezasj2):
    """Manera en la que se decide que jugador va primero,el jugador 1 elige una cantidad de piedras sin ensenarlas y\n\
    el jugador 2 elige una para decir impar o dos para decir par si acierta entonces empieza con negras sino con blancas"""
    resultado = 1
    # Si j2 eligio una piedra y la suma es impar entonces inicia
    if(piezasj2 == 1 and ((piezasj1 + piezasj2) % 2 != 0)):
        resultado = 2
    # Si j2 eligio dos piedras y la suma es par entonces inica
    elif (piezasj2 == 2 and ((piezasj1 + piezasj2) % 2 == 0)):
        resultado = 2
    return resultado


def mostrar_resultado_nigiri(color, piedras_j1, piedras_j2):
    print("El jugador 1 eligio ", piedras_j1,
          " piedra(s), mientras que el jugador 2 eligio ", piedras_j2, "piedra(s).\n")
    if(color == 1):
        print("\nEl jugador 1 juega con las piedras negras.")
        print("El jugador 2 juega con las piedras blancas.\n")

    else:
        print("El jugador 1 juega con las piedras blancas.")
        print("El jugador 2 juega con las piedras negras.")


def mostrar_jugador_en_turno(jugador):
    print(jugador.obt_nombre(), "en turno.")
    print(jugador.obt_nombre(), " tiene: ",
          jugador.obt_piezas_restantes(), " piezas\n")
    print("¿Desea saltar el turno?\n")
    print("1. Si\n2. No\n")


def realizar_jugada(tablero, jugador, contrincante):
    movimiento_jugador = False
    while(movimiento_jugador == False):
        fila, columna = pedir_posicion(tablero)
        if (tablero.colocar_ficha(fila, columna, jugador) == False):
            print("\nNo puede colocar una ficha en esta posicion!!!\n")
        else:
            movimiento_jugador = True
            jugador.asignar_cant_piezas(-1)
            contrincante.asignar_piezas_perdidas(
                tablero.revisar_eliminar_agrupamientos())

#######################################################################################################################################################

def main():

    negro = 1
    blanco = 2
    opc_correcta = False
    # Se muestran las opciones iniciales
    mostrar_menu_inicial()

    while(opc_correcta == False):  # En caso de que no se presione 1 para jugar o dos para salir
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
                piedras_j1, piedras_j2 = pedir_cantidad_piedras()

                color = nigiri(piedras_j1, piedras_j2)
                mostrar_resultado_nigiri(color, piedras_j1, piedras_j2)

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
                        try:
                            saltar = int(input("Digite una opcion: "))
                            if(saltar == 1):
                                proximo_en_jugar = tableroGo.saltar_turno(jugador1)
                            elif(saltar == 2):
                                realizar_jugada(tableroGo, jugador1, jugador2)
                                proximo_en_jugar = 2
                            else:
                                raise ValueError
                        except ValueError:
                            print("Ingrese una opcion valida.")

                    elif (proximo_en_jugar == 2):
                        mostrar_jugador_en_turno(jugador2)
                        try:
                            saltar = int(input("Digite una opcion: "))
                            if(saltar == 1):
                                proximo_en_jugar = tableroGo.saltar_turno(jugador2)
                            elif(saltar == 2):
                                realizar_jugada(tableroGo, jugador2, jugador1)
                                proximo_en_jugar = 1
                            else:
                                raise ValueError
                        except ValueError:
                            print("Ingrese una opcion valida.")

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
