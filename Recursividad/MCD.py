

#Algoritmo de Euclides
n = int(input("Ingrese el numero mas pequeño: "))
m = int(input("Ingrese el numero mas grande: "))

def MCD(n, m):
    if m%n == 0:
        return n
    else:
        return MCD(m, n%m)                   

print("El MCD es: ", MCD(n,m))