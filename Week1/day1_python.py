#first_number = input("Enter first dollar amount: ")
#second_number = input("Enter second dollar amount: ")

#result = float(first_number) + float(second_number)
#print("$" + str(result))

def calculate_tip(total_cost, percentage):
    return total_cost * (percentage/100)

tip = calculate_tip(47,15)

if tip >= 10:
    print("THANK YOU!")
elif tip < 10 and tip >= 5:
    print("THANKS")
else:
    print("YOU ARE A BAD TIPPER")
print(tip)

