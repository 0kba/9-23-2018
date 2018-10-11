testCase1 = "test string is a test"
testCase2 = "wood  is  from  nature and nature is wood  "
testCase3 = "word words  so so"
testCase4 = "a lot of spaces    and spaces "


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
    finallistofwords = []
    for word in words:
        if word in uniquewords:
            continue
        else:
            uniquewords.append(word)
    for w in uniquewords:
        if w != '':
            finallistofwords.append(w)
        else: continue

    finalstringwords = ""
    for a in finallistofwords:
        if a != 0:
            finalstringwords = finalstringwords + " " + a
        else: finalstringwords = a

    return finalstringwords



result = getuniquewords(testCase1)
print(result)

result = getuniquewords(testCase2)
print(result)

result = getuniquewords(testCase3)
print(result)

result = getuniquewords(testCase4)
print(result)


# ______________________________________________________________
# result
# test string is a
#  wood is from nature and
#  word words so
#  a lot of spaces and

