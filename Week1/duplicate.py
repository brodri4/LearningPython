def duplicate_remove(array):
    return list(dict.fromkeys(array))

answer = duplicate_remove([1,2,3,4,4])
answer2 = duplicate_remove([1,2,3,4,5])
answer3 = duplicate_remove([1,2,1,2,4])
answer4 = duplicate_remove([2,2,2,2])

print(answer)
print(answer2)
print(answer3)
print(answer4)