first_input = input("Enter a number: ")
operand = input("Enter an operand. Options include +,-,*,/: ")
second_input = input("Enter another number: ")
first_number = float(first_input)
second_number = float(second_input)

if operand in "+":
    answer = first_number + second_number
    print(answer)
elif operand in "-":
    answer = (first_number) - (second_number)
    print(answer)
elif operand in "*":
    answer = (first_number) * (second_number)
    print(answer)
elif operand in "/":
    answer = (first_number) / (second_number)
    print(answer)
else:
    print("Error")

