def operations(a,b,opt):
    if opt == 1:
        return a+b
    elif opt == 2:
        return a-b
    elif opt == 3:
        return a*b
    elif opt == 4:
        return a/b
    else:
        return "No valid option"

print(operations(3,4,1))
print(operations(10,7,2))
print(operations(4,5,3))
print(operations(8,4,2))
print(operations(2,3,5))       