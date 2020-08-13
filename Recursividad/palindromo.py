palabra = str(input("Ingrese una cadena para invertir: "))
 
def invertir(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s)-1] + invertir (s[:-1])
def palindromo(s):
    s2 = invertir(s)
    if s.lower() == s2.lower():
        return True
    else:
        return False    
print(palindromo(palabra))        