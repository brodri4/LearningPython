#OPTION 1
# import pizza
#pizza.create_pizza(16, "Mushrooms", "Onion")

#OPTION 2
#from pizza import create_pizza
#create_pizza(16, "Mushrooms", "Onion")

#OPTION 3
#import pizza as p
#p.create_pizza(16, "Mushrooms", "Onion")

#size = input("Enter size for pizza: ") 
#toppings = input("Enter toppings: ")    
    #for index in range(0, len(toppings)):
    #    print(toppings[index])

#create_pizza(16, "Mushroom", "Onion", "Chicken")

#DICTIONARIES

# airport = {key: value}
#airport = {"HOBBY":"Hobby International Airport", "AirportCode":345} #2 Keys
#print(airport["HOBBY"])

#adding a key to a dictionary
#airport["IAH"] = "George Bush Intercontinental Airport"
#name = airport["IAH"]
#print(name)

#an empty dictionary
user = {}
user["first_name"] = "John"
user["last_name"] = "Doe"
user[100] = "Hello 100"
#print(user)

#iterate through a dictionary
# OPTION 1
#for key in user:
    #print(user[key])

#using values function
#OPTION 2
#for value in user.values():
    #print(value)

# Loop through both Keys and values
#for key, value in user.items():
    #print(key, value)    

# Deleting From A Dictionary
#car = {"model": "Accord", "make": "Honda", "electric": False}
#print(car)
#del car["electric"]
#print(car)

#Creating a nested dictionary
address = {"street": "1200 Richmond", "state": "TX", "zipCode": "44567"}
customer = {"firstName": "John", "lastName": "Doe", "address": address}
print(customer)
