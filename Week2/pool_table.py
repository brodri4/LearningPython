
from datetime import datetime
class Table:
    def __init__(self, number):
        self.name = f"Table {number}" 
        self.start_time = None
        self.end_time = None
        self.status = "Not Occupied"
        self.person_name = None

# If I want to create a file at the start of the day
# def create_daily_file():
#      today = datetime.now()
#      file_name = f"{today.month}-{today.day}-{today.year}.txt"
#      with open(file_name,"w") as file_object:
#         file_object.write(f"Customer data for {today.month}/{today.day}/{today.year}")
#      print("Daily File Created")
        

def check_in(list,number):
    if list[number-1].status == "Occupied":
                print(f"[Pool Table {number} is already Occupied]")
                input("Press Enter to return to menu: ")
    else:
        list[number-1].person_name = input("Enter Customer's Name: ")
        list[number-1].status = "Occupied"
        list[number-1].start_time = datetime.now()
        print()
        print(f"Check-In To Table {number} Successful")
        input("Press Enter to return to menu: ")

def check_out(list, number):
    if list[number-1].status == "Not Occupied":
                print(f"[Pool Table {number} is not Occupied]")
                input("Press Enter to return to menu: ")
    else:
        print()
        print(f"Checking Out of Table {number} | {list[number-1].person_name}")
        confirm = input("Confrim Y/N: ").upper()
        if confirm == "Y":
            list[number-1].status = "Not Occupied"
            list[number-1].end_time = datetime.now()
            total_time = datetime.now() - list[number-1].start_time
            seconds = total_time.total_seconds()
            hours = int(seconds/3600)
            mins = int(seconds/60)
            cost = mins * .5
            file_name = f"{datetime.now().month}-{datetime.now().day}-{datetime.now().year}.txt"
            with open(file_name,"a") as file_object:
                file_object.write(f"Pool Table Number: {number} \n")
                file_object.write(f"Start Time: {list[number-1].start_time.replace(microsecond=0)} \n")
                file_object.write(f"End Time: {list[number-1].end_time.replace(microsecond=0)} \n")
                file_object.write(f"Total Time: {hours} Hours and {mins % 60} Minutes \n")
                file_object.write(f"Cost: {cost} \n")
                print()
            print(f"The Total Is ${cost}")                
            list[number-1].start_time = None
            list[number-1].end_time = None
            print(f"Check-Out Of Table {number} Successful")
            input("Press Enter to return to menu: ")

def display(list):
    print("TABLE LIST STATUS")
    for i in range(0, len(list)):
        if list[i].start_time != None:
            total_time = datetime.now() - list[i].start_time
            seconds = total_time.total_seconds()
            hours = int(seconds/3600)
            mins = int(seconds/60) % 60
            start = list[i].start_time.strftime("%H:%M:%S")

            print(f"{list[i].name} | {list[i].status} | {list[i].person_name} | Start: {start} | Total Time: {hours} Hours, {mins} Minutes |")
        else:
            total_time = None
            print(f"{list[i].name} | {list[i].status} |") 
    

#create_daily_file()  <--- I would create the daily file here
tables = []
for i in range(1,13):
    tables.append(Table(i))
tables[0].status = "Occupied" #dummy example
tables[0].start_time = datetime(2020,9,16,12,22,34)
tables[0].person_name = "Rodriguez" 
while True:
    display(tables)
    response = input("Select Action | 1 to Check-In| 2 to Check-out| q to Quit: ").lower()
    if response == "q":
        break
    if response == "1":
        try:
            second_response = int(input("Select Table Number: "))    
        except ValueError:
            print("Not A Valid Answer")
        if second_response in range(1,len(tables)+1):
            check_in(tables,second_response)
    if response == "2":
        try:
            second_response = int(input("Select Table Number: "))    
        except ValueError:
            print("Not A Valid Answer")
        if second_response in range(1,len(tables)+1):
            check_out(tables, second_response)
            
            
            
            
            
            





