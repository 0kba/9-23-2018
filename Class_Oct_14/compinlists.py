def combinlistoflists (listoflists):
    combinlists = []

    for list in listoflists:
        if list is None:
            continue #move on to the next item
        for num in list:
                combinlists.append(num)

    return combinlists



listoflists = [[1,2],None,[4,5],None,[2,3],[7,8], None]
finallist = combinlistoflists(listoflists)


print(finallist)