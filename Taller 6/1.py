def elminar_rep(lis):
    lis2 = []
    for i in lis:
        if i not in lis2:
            lis2.append(i)
    return lis2

                 
nums = [4,7,11,4,9,5,11,7,3,5]
print(elminar_rep(nums))
            



