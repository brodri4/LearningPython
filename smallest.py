def smallest(array):
    smallest_num = array[0]
    for i in range(1,len(array)):
        if array[i] < smallest_num:
            smallest_num = array[i]
    return smallest_num

answer = smallest([1,2,3,4,5,6])
answer2 = smallest([3,6,1,8,4,0])
answer3 = smallest([4])
answer4 = smallest([-3,3,0,9,-10,4])

print(answer)
print(answer2)
print(answer3)
print(answer4)
