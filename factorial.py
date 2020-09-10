def factorial():
    number = int(input("Choose a number: "))
    for i in range(1, number):
        number = number * i 
    return number

answer = factorial()
print(answer)