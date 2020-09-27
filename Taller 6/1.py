def elminar_rep(lis):
    #rep = False
    lis2 = []
    for i in lis:
        if i not in lis2:
            lis2.append(i)
    return lis2

def busqueda_secuencial(lista,valor):
    posicion = 0
    encontrado = False
    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion += 1    
    if encontrado == True:
        return encontrado, posicion
    else:
        return encontrado         

        
nums = [4,7,11,4,9,5,11,7,3,5]
print(elminar_rep(nums))
            



