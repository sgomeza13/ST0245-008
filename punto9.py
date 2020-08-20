n = int(input("Ingrese el numero de filas: "))
def  pascal(row, column):
          if row < 0 and column < 0:
                return 0
          elif row == 0 and column == 0:
                return 1
          else:
            return pascal(row-1,column) + pascal(row-1,column-1)

def PascalTriangle(num):
    if (num <= 0):
        print('numero debe ser mayor a cero')
    
    for r in range(num):
        for c in range(r+1):
            print((pascal(c,r)))
            print('\n')
                  
PascalTriangle(n)                  