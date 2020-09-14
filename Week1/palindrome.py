import math
def palindrome():
    word = input("Type a word: ")
    for i in (0, math.ceil(len(word)/2)):
        if word[i] != word[-1-i]:
            return False
            break
        
        return True


answer = palindrome()
if answer == True:
    print("The word is a Palendrome")
if answer == False:
    print("The word is not a Palendrome")

