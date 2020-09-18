#a to the power b : power(3,4) = 81

def power(a,b):
    pow = 1
    if b == 0:
        return 1
    elif b < 0:
        for i in range(1, b*(-1)+1):
            pow = a * pow
        return print(1/pow) 
    else: 
        for i in range(1, b+1):
            pow = a * pow
        return print(pow)

power(5,-4)