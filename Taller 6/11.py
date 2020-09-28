import random
def quickSort(lis):
    if len(lis) <= 1:
        return lis
    else:
        izq = []
        der = []
        pivot = lis[len(lis)//2]
        del(lis[len(lis)//2])
        for i in range(0,len(lis)):
            if lis[i] > pivot:
                der.append(lis[i])
            else:
                izq.append(lis[i])
        return quickSort(izq) + [pivot] + quickSort(der) 
lis = [654,654,321,5,4,6,8,41,3,-4,646]
#print(quickSort(lis))

a = []
b = []
for i in range(60):
    a.append(random.randrange(60))
for j in range(100):
    b.append(random.randrange(100))

a = quickSort(a)
b = quickSort(b)
c = a+b
c = quickSort(c)
print(c)