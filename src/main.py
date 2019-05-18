from TableroGo import TableroGo  # Se importa la clase como tal y no como modulo
from JugadorGo import JugadorGo
import sys


def mostrar_menu_inicial():
    print("Bienvenido al juego de Go \n")  # Menu inicial
    print("1. Jugar\n")
    print("2. Salir del menu\n")


def mostrar_menu_colores():
    print("\n\nQue color de ficha desea? \n")  # Menu color
    print("1. Fichas Negras \n")
    print("2. Fichas Blancas\n")


def preguntar_nombres():
    nombre1 = input("Digite el nombre del jugador 1: ")
    nombre2 = input("Digite el nombre del jugador 2: ")
    return nombre1, nombre2


def pedir_coordenadas():
    fila = int(input("Ingrese la fila en la que desea colocar la ficha: "))
    columna = int(
        input("Ingrese la columna en la que desea colocar la ficha: "))
    return fila, columna

def jugador_en_turno(jugador):
    print(jugador.obt_nombre(), "en turno")

def main():
    negro = 1
    blanco = 2
    # Se muestran las opciones iniciales
    mostrar_menu_inicial()
    try:
        opcion = int(input("Digite una opcion: "))
        if(opcion == 1):
            
            tableroGo = TableroGo()  # Instancia de la clase Tablero
            tableroGo.crear_tablero()

            nombre1, nombre2 = preguntar_nombres()

            # Se muestran las opciones de color
            mostrar_menu_colores()
            # Este print puede omitirse una vez que tengamos las reglas
            print("Inicia el jugador con las fichas negras\n\n")

            color = int(input("Digite una opcion: "))

            if(color == 1):
                print("\n\nEl jugador 1 juega con las fichas negras")
                jugador1 = JugadorGo(1, negro, nombre1)
                jugador2 = JugadorGo(2, blanco, nombre2)
                proximo_en_jugar = 1

            else:
                print("\n\nEl jugador 1 juega con las fichas blancas")
                jugador1 = JugadorGo(1, blanco, nombre1)
                jugador2 = JugadorGo(2, negro, nombre2)
                proximo_en_jugar = 2

            
            tableroGo.mostrar_tablero()

            continuar = 1
            while(continuar == 1):

                if(proximo_en_jugar == 1):
                    
                    jugador_en_turno(jugador1)
                    fila, columna = pedir_coordenadas()

                    if (tableroGo.colocar_ficha(fila, columna, jugador1, jugador1.obt_color_pieza()) == False):
                        print("\nNo puede colocar una ficha en esta posicion!!!\n")
                    else:
                        proximo_en_jugar = 2

                else:
        
                    jugador_en_turno(jugador1)
                    fila, columna = pedir_coordenadas()

                    if (tableroGo.colocar_ficha(fila, columna, jugador2, jugador2.obt_color_pieza()) == False):
                        print("\nNo puede colocar una ficha en esta posicion!!!\n")
                    else:
                        proximo_en_jugar = 1

                tableroGo.mostrar_tablero()
                
        else:
            return 0

    except ValueError:
        print("Debe ingresar un valor correcto")
    except KeyboardInterrupt:
        print("Se interrumpio el programa con Ctrl + C ")
        return 0


if __name__ == "__main__":
    main()
