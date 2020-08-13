import time
n = int(input("Ingrese el numero: "))

def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n<2:
        return 1
    else:
        return n*(get_recursive_factorial(n-1))

def  get_iterative_factorial(n):
    res = 1
    for i in range(n):
        res *= (i+1)
    return res
print(get_recursive_factorial(n))
print(get_iterative_factorial(n))

start_time = time.time() 
get_recursive_factorial(n) 
print("Recursion--- %s seconds ---" % (time.time() - start_time)) 
start_time = time.time() 
get_iterative_factorial(n) 
print("Iteration--- %s seconds ---" % (time.time() - start_time))        