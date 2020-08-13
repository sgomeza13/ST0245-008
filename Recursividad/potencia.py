x = int(input("Ingrese la base: "))
n = int(input("Ingrese el exponente: "))

def potencia(x,n):
    if(n==0):
        return 1
    else:
        return x*(potencia(x,n-1))
print("El resultado es: ",potencia(x,n)) 
