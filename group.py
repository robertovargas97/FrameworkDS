
class ficha:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.indice_lista=-1


def crear_matriz(matrix,r,c):
    # For user input
    for i in range(r):          # A for loop for row entries
        a =[]
        for j in range(c):      # A for loop for column entries
             a.append(0)
        matrix.append(a)

def imp_matriz(matrix,r,c):
    # For printing the matrix
    for i in range(r):
        for j in range(c):
            print(matrix[i][j].color, end = " ")
        print()
    print("\n\n")

def colocar_ficha(matrix,x,y,val, lista_de_listas):
    ficha = matrix[x][y]
    ficha.x = x
    ficha.y = y
    ficha.color = val
    ficha.indice_lista = len(lista_de_listas)
    lista = []
    lista.append(ficha)
    lista_de_listas.append(lista)
    verifica_vecinos(matrix,ficha,lista_de_listas)
    for i in range(len(lista_de_listas)):
        print(len(lista_de_listas[i]),"\n")  

def posicion_valida(x,y):
    if x < 0 or x >= 9 or y < 0 or y >= 9:
        return False
    return True 

def verifica_vecinos(matrix,ficha,lista_de_listas):
    #si la posicion de arriba es valida y el color de es igual
    if posicion_valida((ficha.x)-1,ficha.y) and matrix[ficha.x-1][ficha.y].color == ficha.color: 
        fichaArr = matrix[ficha.x-1][ficha.y]
        agrupar(lista_de_listas[ficha.indice_lista],lista_de_listas[fichaArr.indice_lista],lista_de_listas)
    
    #si la abajo de arriba es valida y el color de es igual
    if posicion_valida((ficha.x)+1,ficha.y) and matrix[ficha.x+1][ficha.y].color == ficha.color:
        fichaAbj = matrix[ficha.x+1][ficha.y]
        agrupar(lista_de_listas[ficha.indice_lista],lista_de_listas[fichaAbj.indice_lista],lista_de_listas)
    #der
    if posicion_valida((ficha.x),ficha.y+1) and matrix[ficha.x][ficha.y+1].color == ficha.color:
        fichaDer = matrix[ficha.x][ficha.y+1]
        agrupar(lista_de_listas[ficha.indice_lista],lista_de_listas[fichaDer.indice_lista],lista_de_listas)
    #izq
    if posicion_valida((ficha.x),ficha.y-1) and matrix[ficha.x][ficha.y-1].color == ficha.color:
        fichaIzq = matrix[ficha.x][ficha.y-1]
        agrupar(lista_de_listas[ficha.indice_lista],lista_de_listas[fichaIzq.indice_lista],lista_de_listas)    


def agrupar(grupoA,grupoB,lista_de_listas):
    ficha_gregada = grupoA[0]
    #el atributo del indice de donde esta la agrupacion cambia
    indiceB = (grupoB[0].indice_lista)+1 #tengo que hacer corrimiento al atributo de indice 
    # en varias listas
    
    for i in range(indiceB,len(lista_de_listas)):
        for j in range(len(lista_de_listas[i])):
            lista_de_listas[i][j].indice_lista -=1
    # la lista que se va a combinar adquiere el valor que tiene grupoA que es la ficha mas reciente
    for i in range(1,len(grupoA)):       
        grupoA[i].indice_lista = grupoA[0].indice_lista
    
    grupoA.extend(grupoB)
    lista_de_listas.remove(grupoB) 

def analizar_libertades_grupos(matrix,lista_de_listas):
    for i in range(len(lista_de_listas)):
        if libertades_agrupamiento(matrix,lista_de_listas[i]) == 0:
            eliminar_agrupamiento(lista_de_listas[i])


def libertades_agrupamiento(matrix,agrupamiento):
    for i in range(len(agrupamiento)):
        if libertades_ficha(matrix,agrupamiento[i]) > 0:
            return 1

    return 0        

def libertades_ficha(matrix,ficha):
    libertades = 0
    if posicion_valida(ficha.x-1,ficha.y) and matrix[ficha.x-1][ficha.y].color == 0:
        libertades += 1
    if posicion_valida(ficha.x+1,ficha.y) and matrix[ficha.x+1][ficha.y].color == 0:
        libertades += 1
    if posicion_valida(ficha.x,ficha.y+1) and matrix[ficha.x][ficha.y+1].color == 0:
        libertades += 1
    if posicion_valida(ficha.x,ficha.y-1) and matrix[ficha.x][ficha.y-1].color == 0:
        libertades += 1
    return libertades   

def eliminar_agrupamiento(agrupamiento):
    for i in range(len(agrupamiento)):
        agrupamiento[i].color = -1

def main():
    lista_de_listas = []
    matrix = [[ficha(0,0,0) for j in range(9)] for i in range(9)]
    #crear_matriz(matrix,9,9)
    imp_matriz(matrix,9,9)
    
    while(1):
        r = int(input("Digite fila\n"))
        c = int(input("Digite columna\n"))
        tipo = int(input("Digite color 1 o 2\n"))
        colocar_ficha(matrix,r,c,tipo, lista_de_listas)
        analizar_libertades_grupos(matrix, lista_de_listas)
        imp_matriz(matrix,9,9)


if __name__ == "__main__":
    main()
