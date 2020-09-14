def prime_or_not():
    number = int(input("Choose a number: "))
    if number <= 1: #Negatives, 0, and 1 are not primes
        return False
    elif number == 2:
        return True
    else:    
        for i in range(2 , number):
            if number % i == 0:
                return False
                break
        return True
    

x = prime_or_not()
if x == True:
    print("Your Number Is Prime")
if x == False:
    print("Your Number Is Not Prime")            

