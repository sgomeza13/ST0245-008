# Program to find most frequent 
# element in a list
  
def contarVotos(lis):
    cont = 0
    num = lis[0]
      
    for i in range(0,len(lis)):
        numero_votos = lis.count(lis[i])
        if(numero_votos > cont):
            cont = numero_votos
            num = lis[i]
    print("El candidato con mas votos es:",num)
    return num
  
List = [2, 1, 2, 2, 1, 3,5,6,4,5,8,8,8,8,8,4,2,4,5,9,6,23,1,4,8,1,2,33,4,2,5,8,6,9,8,4,2,323,6,5,89,8]
contarVotos(List)