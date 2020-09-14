#first_name = input("What's your first name: ")
#last_name = input("What's your last name: ")

#full_name = {}
#full_name["first_name"] = first_name
#full_name["last_name"] = last_name

#print(full_name)
#print("My name is " + full_name["last_name"] + ", " + full_name["first_name"])
#print(f'My name is {full_name["last_name"]}, {full_name["first_name"]}')

person = {"first_name": "Boris", "last_name": "Rodriguez"}
address = {"street": "1200 Richmond", "state": "TX", "zipCode": "44567"}
address2 = {"street": "123 Main Street", "state": "GA", "zipCode": "23456"}
addresses = [address, address2]
person["addresses"] = addresses
print(person)