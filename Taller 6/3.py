#Se usó el algoritmo de selección porque este en cada pasada busca el elemento mas pequño del arreglo 
#y lo pone al princicpio de la lista, en el siguiente programa se aprecia mejor esto:
def ordenamientoSeleccion(lis):
    for i in range(0,2): #Pongo el for de 0 a dos para que solo haga dos pasadas como lo dice en la pregunta
        print(lis)
        minimo = i
        for j in range(i+1,len(lis)):
            if lis[j] < lista[minimo]:
                minimo = j
        if min is not i:
            lis[i],lis[minimo] = lis[minimo],lis[i]
    return lis            

lista = [47,3,21,32.56,92]#La lista que nos da el ejercicio
print(ordenamientoSeleccion(lista))#Como queda la lista despues de las dos pasadas      
