def combinlistoflists (listoflists):
    combinlists = []

    for list in listoflists:
        for num in list:
         combinlists.append(num)
    return combinlists



listoflists = [[1,2],[4,5],[2,3],[7,8]]
finallist = combinlistoflists(listoflists)


print(finallist)