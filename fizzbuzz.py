choice = input("Choose a number: ")
number = int(choice)
if number % 3 == 0 and number % 5 != 0:
    print("FIZZ") 
elif number % 5 == 0 and number % 3 !=0:
    print("BUZZ")
elif number % 5 == 0 and number % 3 == 0:
    print("FIZZBUZZ")