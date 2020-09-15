
from datetime import datetime
class Table:
    def __init__(self, number):
        self.name = f"Table {number}" 
        self.start_time = None
        self.end_time = None
        self.status = "Not Occupied"
    #    if self.start_time != None:
    #        self.status = "Occupied"
        

def display(list):
    print("TABLE LIST STATUS")
    for i in range(0, len(list)):
        if list[i].start_time != None:
            total_time = datetime.now() - list[i].start_time
            seconds = total_time.total_seconds()
            hours = int(seconds/3600)
            mins = int(seconds/60) % 60
            start = list[i].start_time.strftime("%H:%M:%S")

            print(f"{list[i].name} | {list[i].status} | Start: {start} | Total Time: {hours} Hours, {mins} Minutes |")
        else:
            total_time = None
            print(f"{list[i].name} | {list[i].status} |") 
    


tables = []
for i in range(1,13):
    tables.append(Table(i))
tables[0].status = "Occupied"
tables[0].start_time = datetime(2020,9,15,12,22,34)
while True:
    display(tables)
    response = input("Select Action| 1 to Check-In| 2 to Check-out| q to Quit: ").lower()
    if response == "q":
        break
    if response == "1":
        try:
            second_response = int(input("Select Table Number: "))    
        except ValueError:
            print("Not A Valid Answer")
        if second_response in range(1,len(tables)+1):
            if tables[second_response-1].status == "Occupied":
                print(f"[Pool Table {second_response} is already Occupied]")
                input("Press any key to return to menu: ")
            else:
                tables[second_response-1].status = "Occupied"
                tables[second_response-1].start_time = datetime.now()
                print(f"Check-In To Table {second_response} Successful")
                input("Press any key to return to menu: ")
    if response == "2":
        try:
            second_response = int(input("Select Table Number: "))    
        except ValueError:
            print("Not A Valid Answer")
        if second_response in range(1,len(tables)+1):
            if tables[second_response-1].status == "Not Occupied":
                print(f"[Pool Table {second_response} is not Occupied]")
                input("Press any key to return to menu: ")
            else:
                tables[second_response-1].status = "Not Occupied"
                tables[second_response-1].end_time = datetime.now()
                total_time = datetime.now() - tables[second_response-1].start_time
                seconds = total_time.total_seconds()
                mins = int(seconds/60)
                cost = mins * .5
                print(f"The Total Is ${cost}")                
                tables[second_response-1].start_time = None
                tables[second_response-1].end_time = None
                print(f"Check-Out Of Table {second_response} Successful")
                input("Press any key to return to menu: ")
    
    












