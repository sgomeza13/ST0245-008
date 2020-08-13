palabra = str(input("Ingrese la palabra: "))
def impR(s,cont):
    if cont <= len(s):
        print(s[:cont])
        impR(s, cont+1)

impR(palabra, 1)




