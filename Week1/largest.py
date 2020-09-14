def largest(array):
    largest_num = array[0]
    for i in range(1,len(array)):
        if array[i] > largest_num:
            largest_num = array[i]
    return largest_num

answer = largest([1,2,3,4,5,6.6])
answer2 = largest([3,6,1,8,4,0])
answer3 = largest([4.5])
answer4 = largest([-3,3,0,9,-10.,4])

print(answer)
print(answer2)
print(answer3)
print(answer4)


