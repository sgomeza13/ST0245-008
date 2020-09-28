def shellSort(lista):
    cont = 1
    mitad = len(lista)//2
    while mitad > 0:
      for posicion_inicial in range(mitad):#ir al esta el rango que se llama mitad
        reducir_busqueda(lista, posicion_inicial, mitad)

      print("pasada",cont,":", lista)

      mitad = mitad // 2
      cont += 1


def reducir_busqueda(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap): #gap es el salto que se va dar 

        current_value = nlist[i]
        posicion = i

        while posicion>=gap and nlist[posicion-gap]>current_value:
            nlist[posicion]=nlist[posicion-gap]
            posicion = posicion-gap

        nlist[posicion]=current_value

lista = [8,43,17,6,40,16,18,97,11,7]
shellSort(lista)
    