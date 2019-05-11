from TableroGo import TableroGo  # Se importa la clase como tal y no como modulo
from JugadorGo import JugadorGo


def main():

    continuar = 1
    proximo_en_jugar = 1
    tableroGo = TableroGo()  # Instancia de la clase Tablero
    tableroGo.crear_tablero()
    tableroGo.mostrar_tablero()

    jugador1 = JugadorGo(1)
    #print(jugador1.obt_piezas_restantes())
    # jugador1.eliminar_pieza()
    # print(jugador1.obt_piezas_restantes())

    jugador2 = JugadorGo(2)
    #print(jugador1.obt_piezas_restantes())
    # jugador1.eliminar_pieza()
    # print(jugador1.obt_piezas_restantes())
    
    while(continuar == 1 ):
        try:
            if(proximo_en_jugar == 1):
                print("Jugador 1 en turno")
                fila = int(input("Ingrese la fila en la que desea colocar la ficha: "))
                columna = int(input("Ingrese la columna en la que desea colocar la ficha: "))
                    
                if (jugador1.colocar_ficha(fila, columna, tableroGo) == False):
                        print("No\n")
                else: 
                    proximo_en_jugar = 2
            
            else:
                print("Jugador 2 en turno")
                fila = int(input("Ingrese la fila en la que desea colocar la ficha: "))
                columna = int(input("Ingrese la columna en la que desea colocar la ficha: "))

                if (jugador2.colocar_ficha(fila, columna, tableroGo) == False):
                    print("No\n")
                else:    
                    proximo_en_jugar = 1
                    
            tableroGo.mostrar_tablero()
                    
        except ValueError : 
            print("Debe ingresar un valor de celda correcto")
        except KeyboardInterrupt :
            print("Se interrumpio el programa con Ctrl + C ")
            return 0 
            
    
           
        
    


if __name__ == "__main__":
    main()
