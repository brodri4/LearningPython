from datetime import datetime
import json

class Table:
    def __init__(self, number):
        self.name = f"Table {number}" 
        self.start_time = None
        self.end_time = None
        self.status = "Not Occupied"

def check_in(list,number):
    if list[number-1].status == "Occupied":
                print(f"[Pool Table {number} is already Occupied]")
                input("Press any key to return to menu: ")
    else:
        list[number-1].status = "Occupied"
        list[number-1].start_time = datetime.now()
        print(f"Check-In To Table {number} Successful")
        input("Press any key to return to menu: ")

def check_out(list, number):
    if list[number-1].status == "Not Occupied":
                print(f"[Pool Table {number} is not Occupied]")
                input("Press any key to return to menu: ")
    else:
        list[number-1].status = "Not Occupied"
        list[number-1].end_time = datetime.now()
        total_time = datetime.now() - list[number-1].start_time
        seconds = total_time.total_seconds()
        hours = int(seconds/3600)
        mins = int(seconds/60)
        cost = mins * .5
        file_name = f"{datetime.now().month}-{datetime.now().day}-{datetime.now().year}.json"
        check_out_entry = {}
        check_out_entry["Pool Table Number"] = number
        check_out_entry["Start Time"] = list[number-1].start_time.replace(microsecond=0).strftime("%H:%M")
        check_out_entry["End Time"] = list[number-1].end_time.replace(microsecond=0).strftime("%H:%M")
        check_out_entry["Total Time"] = f"{hours} Hours and {mins % 60} Minutes"
        check_out_entry["Cost"] = cost
        check_outs.append(check_out_entry)
        with open(file_name, "w") as file_object:
            json.dump(check_outs, file_object)
        print(f"The Total Is ${cost}")                
        list[number-1].start_time = None
        list[number-1].end_time = None
        print(f"Check-Out Of Table {number} Successful")
        input("Press any key to return to menu: ")

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
check_outs = []
for i in range(1,13):
    tables.append(Table(i))
tables[0].status = "Occupied"
tables[0].start_time = datetime(2020,9,15,12,22,34) #dummy example
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