from TableroGo import TableroGo  # Se importa la clase como tal y no como modulo
from JugadorGo import JugadorGo
import sys


def main():
    print("Bienvenido al juego de Go \n");
    print("1. Jugar\n");
    print("2. Salir del menu\n");

    opcion = int(input("Digite una opcion: "))
    if(opcion == 1):
        continuar = 1
        proximo_en_jugar = 1
        tableroGo = TableroGo()  # Instancia de la clase Tablero
        tableroGo.crear_tablero()
       
        print("Que color de ficha desea? \n")
        print("1. Fichas Negras \n")
        print("2. Fichas Blancas\n")
        color = int(input("Digite una opcion: "))
        if(color == 1):
            print("El jugador 1 juega con las fichas negras")
            jugador1 = JugadorGo(1)
            jugador2 = JugadorGo(2)
       
        else:
            print("El jugador 1 juega con las fichas blancas")
            jugador1 = JugadorGo(2)
            jugador2 = JugadorGo(1)
        
        print("Inicia el jugador con las fichas negras")
        tableroGo.mostrar_tablero()
     #   print("Jugador ", jugador.obt_id(), "ha perdido:  0 piezas \n")
        #while(continuar == 1 ):
        #    try:
        #        if(proximo_en_jugar == 1):
        #            print("Jugador 1 en turno")
        #            fila = int(input("Ingrese la fila en la que desea colocar la ficha: "))
        #            columna = int(input("Ingrese la columna en la que desea colocar la ficha: "))
                    
        #            if (jugador1.colocar_ficha(fila, columna, tableroGo) == False):
        #                    print("No\n")
        #            else: 
        #                proximo_en_jugar = 2
            
        #        else:
        #            print("Jugador 2 en turno")
        #            fila = int(input("Ingrese la fila en la que desea colocar la ficha: "))
        #            columna = int(input("Ingrese la columna en la que desea colocar la ficha: "))

        #            if (jugador2.colocar_ficha(fila, columna, tableroGo) == False):
        #                print("No\n")
        #            else:    
        #                proximo_en_jugar = 1
                    
        #        tableroGo.mostrar_tablero()
            
        #        if(proximo_en_jugar == 1):
        #            jugador2.analizar_jugada(jugador1)
        #        else:
        #            jugador1.analizar_jugada(jugador2)    
                    
        #    except ValueError : 
        #        print("Debe ingresar un valor de celda correcto")
        #    except KeyboardInterrupt :
        #        print("Se interrumpio el programa con Ctrl + C ")
    
           
    else:
        try:
            print("Presione cualquier tecla para salir")
        except KeyboardInterrupt:
            sys.exit()


    
        return 0 
            
    
           
        
    


if __name__ == "__main__":
    main()