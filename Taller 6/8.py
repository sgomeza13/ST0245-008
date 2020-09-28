def Omerge(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        ## LLamada recursiva para cada lista 
        Omerge(mitadIzquierda)
        Omerge(mitadDerecha)
        i,j,k=0,0,0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)

nums = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
Omerge(nums)
""" Despues de tres llamadas recursivas, la lista se ve asi: [21,1] esto lo podemos apreciar al correr el programa porque se implenentaron unos "print" para facilitar su visualización
¿Por qué? porque el elagoritmo está diseñado para dividir la lista original en listas más pequeñas mediante recursión, primero se divide a la mitad, luego esta primera mitad se vuelve a 
dividir en mitades y así sucesivamente hasta que queden listas de un solo elemento para luego mezclar estas listas en el orden correcto.
En esta implementacion del algoritmo decidimos que trabaje con la primera mitad primero, es decir dividimos la mitad de la izquierda primero y la mitad de la derecha segundo
pero si lo quisieramos podemos trabajar con la mitad de la derecha primero y el resultado final sería el mismo, veamos """

def OmergeDerecha(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        ## LLamada recursiva para cada lista 
        Omerge(mitadDerecha) #primero se trabaja con la segunda mitad
        Omerge(mitadIzquierda) #luego con la primera
        i,j,k=0,0,0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)
print("* AQUI COMIENZA EL SEGUNDO ORDENAMIENTO PARA DEMOSTRAR LO DICHO ANTERIORMENTE*")    
OmergeDerecha(nums)