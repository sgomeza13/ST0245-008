def torres(a):
    if a == 0:
        return 1
    else: 
        po = 2 * torres(a-1)
        return po
        

h = int(input("Ingrese la cantidad de discos: "))
print(torres(h))