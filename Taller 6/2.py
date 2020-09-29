def eliminar_repetidos_ordenado(lis):
    lis2 = []
    for i in lis:
        if i not in lis2:
            lis2.append(i)
    return lis2
#Como use el mismo algoritmo que en el punto 1 la complejidad es la misma (o(n)) y aunque este la lista ordenada se va a recorrer todo el arreglo pase lo que pase entonces no hay diferencia 
# entre la una y la otra. 