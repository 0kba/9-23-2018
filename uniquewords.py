testCase1 = "test string is a test"
testCase2 = "wood  is  from  nature and nature is wood  "
testCase3 = "test string is a test"
testCase4 = "test string is a test"


def getwords(sentence):
    words = []
    currentword = ""
    for char in sentence:
        if char == " ":
            words.append(currentword)
            currentword = ""
        else:
            currentword = currentword + char
    words.append(currentword)
    return words


def getuniquewords(sentence):
    words = getwords(sentence)
    uniquewords = []
    for word in words:
        if word in uniquewords:
            continue
        uniquewords.append(word)
    return uniquewords


result = getuniquewords(testCase1)
print(result)

result = getuniquewords(testCase2)
print(result)

result = getuniquewords(testCase3)
print(result)

result = getuniquewords(testCase4)
print(result)


