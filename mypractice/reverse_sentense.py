sentence = "My name is Michele"

def rev_sentence (sentence):
    sentence_list = []
    word = ""
    for char in sentence:
        if char == " " or char == ".":
            sentence_list.append(word)
            word = ""
        else:
            word = word + char
    sentence_list.append(word)

    return print(sentence_list[::-1])

print(rev_sentence(sentence))