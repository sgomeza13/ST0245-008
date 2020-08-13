palabra = str(input("Ingrese una cadena para invertir: "))
 
def invertir(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s)-1] + invertir (s[:-1])
print(palabra,invertir(palabra))