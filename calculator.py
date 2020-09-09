first_number = input("Enter a number: ")
operand = input("Enter an operand. Options include +,-,*,/: ")
second_number = input("Enter another number: ")
    
if operand in "+":
    answer = int(first_number) + int(second_number)
    print(answer)
elif operand in "-":
    answer = int(first_number) - int(second_number)
    print(answer)
elif operand in "*":
    answer = int(first_number) * int(second_number)
    print(answer)
elif operand in "/":
    answer = int(first_number) / int(second_number)
    print(answer)
else:
    print("Error")

