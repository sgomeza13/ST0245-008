def impTI(n):
    if n == 1:
        return n
    else:
        print(n)
        return(impTI(n-1))

print(impTI(78))