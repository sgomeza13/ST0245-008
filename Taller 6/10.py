            
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
#Busqueda secuencial
def busqueda_secuencial_matriz(lis,num):
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if lis[i][j] == num:
                return True
    return False
for i in range(10):    
    print(i,': ',busqueda_secuencial_matriz(a,i))
#Busqueda Binaria
def busquea_binaria_matriz(lis,num):
    len_fila = len(lis)
    len_columna = len(lis[0])
    
    izq = 0
    der = len_columna * len_fila

    while izq <= der:
        mid = (izq+der)//2
        if lis[mid // len_columna][mid % len_columna] == num:
            return True
        elif lis[mid // len_columna][mid % len_columna] > num:
            der = mid-1
        else:
            izq = mid+1
    return False
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print('#############################')
for i in range(10):
    print(i, ": ",busquea_binaria_matriz(matriz,i))

