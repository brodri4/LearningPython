first_input = input("Enter a number: ")
operand = input("Enter an operand. Options include +,-,*,/: ")
second_input = input("Enter another number: ")
first_number = float(first_input)
second_number = float(second_input)

def sum(first_number, second_number):
    return first_number + second_number
def subtract(first_number, second_number):
    return first_number - second_number
def multiply(first_number, second_number):
    return first_number * second_number
def divide(first_number, second_number):
    return first_number / second_number


if operand in "+":
    answer = sum(first_number, second_number)
    print(answer)
elif operand in "-":
    answer = subtract(first_number, second_number)
    print(answer)
elif operand in "*":
    answer = multiply(first_number, second_number)
    print(answer)
elif operand in "/":
    answer = divide(first_number, second_number)
    print(answer)
else:
    print("Invalid Operand")