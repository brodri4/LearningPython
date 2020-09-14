def missing_element(array):
    array.sort()
    missing_no = 9 
    #The array only has 9 elements. It can only check up to the 8th index
    for i in range(0, len(array)):
        if array[i] != i:
            missing_no = i
            break
    return missing_no

answer = missing_element([3,6,5,8,0,4,1,7,2])
answer2 = missing_element([3,6,5,8,9,4,1,7,2])
answer3 = missing_element([3,6,5,8,0,4,9,7,2])

print(answer)
print(answer2)
print(answer3)