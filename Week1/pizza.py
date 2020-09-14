def create_pizza(size, *toppings): # * means variable argument
    print(f"The pizza {size}")
    
    for t in toppings:
        print(t)
    
def deliver_pizza(address):
    print(f"Deliver Pizza at {address}.")