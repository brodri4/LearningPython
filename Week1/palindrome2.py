def palindrome():
    word = input("Type a word: ")
    word_fowards=[]
    word_backwards=[]
    result = True

    for i in range(len(word)-1, -1, -1):
        word_backwards.append(word[i])
    for i in range(0, len(word)):
        word_fowards.append(word[i])
    if word_fowards != word_backwards:
        result = False
    return result    

answer = palindrome()
if answer == True:
    print("The word is a Palendrome")
if answer == False:
    print("The word is not a Palendrome")