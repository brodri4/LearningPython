class Shopping_list:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.grocery_items = []
  
class Grocery_item:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

def grocery_list_info():
    title_list = input("Name of the store: ").upper()
    address_list = input("Address: ").upper()
    master_list.append(Shopping_list(title_list, address_list)) 

def grocery_item_info(number):
    name = input('Name of item: ').upper()
    price = float(input('Price of item: '))
    quantity = input('Quantity of item: ')
    master_list[number - 1].grocery_items.append(Grocery_item(name, price, quantity))
    response = input("Add another item to this list?(Y/N): ").upper()
    return response

def show_list(list):
    for i in range(0, len(list)):
        print(f'#{i+1} - {list[i].title} at {list[i].address}')
        for j in range(0, len(list[i].grocery_items)):
            item_title = list[i].grocery_items[j].title
            item_price = list[i].grocery_items[j].price
            item_quantity = list[i].grocery_items[j].quantity
            print(f'{item_title} - ${item_price} - Quantity: {item_quantity}')
    input("Press ENTER/RETURN to return to menu: ")

def options():
    message = """
    Press 1 to add a shopping list
    Press 2 to add an item to a list
    Press 3 to all lists
    Press q to quit
    """
    print(message)
    answer = input(" ")
    return answer

master_list = []
response = options()

while response != "q":
    if response == "1":
        grocery_list_info()
    elif response == "2":
        for i in range(0, len(master_list)):
            print(f"{i+1}-{master_list[i].title}")
        print(f"{len(master_list)+1}-Return to menu")
        choice = int(input('Add to which list?: '))
        if choice in range(1,len(master_list)+ 1):
            answer_2 = grocery_item_info(choice)
            while answer_2 != "N":
                answer_2 = grocery_item_info(choice)    
    elif response == "3":
        show_list(master_list)
    #    for i in range(0, len(master_list)):
    #        print(f'{i+1} - {master_list[i].title}')
    #        for j in range(0, len(master_list[i].grocery_items)):
    #            print(master_list[i].grocery_items[j].title)
    #    input("Press ENTER/RETURN to return to menu: ")
    response = options()


