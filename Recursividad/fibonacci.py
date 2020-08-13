n = int(input("Ingrese un valor: "))

def fiboR(n):
    if n <= 2:
        return 1
    return (fiboR(n-1)+fiboR(n-2))

print(fiboR(n))            