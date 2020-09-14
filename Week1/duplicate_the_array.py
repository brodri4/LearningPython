def duplicate_the_array(array):
    for i in range(0, len(array)):
        array.append(array[i])
    return array

answer = duplicate_the_array([1,2,-3,4,5])
answer2 = duplicate_the_array([1])
print(answer)
print(answer2)
