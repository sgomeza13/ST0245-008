n = int(input("Ingrese el numero de filas: "))

def pascal(n):
  if n == 0:
    return []

  elif n == 1:
    return [[1]]
  
  else:
    lis = [1]
    lisPrev = pascal(n-1)
    res = lisPrev[-1]
    for i in range(len(res)-1):
      lis.append(res[i]+res[i+1])
    lis += [1]
    lisPrev.append(lis)
  return lisPrev

triangulo = pascal(n)
for i in range(n):
  print(triangulo[i])




