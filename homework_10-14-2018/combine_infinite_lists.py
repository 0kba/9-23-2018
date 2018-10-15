def combineinfinitelists (listofinfinitelists):

    combinedlist = []        # empty list to add our result to it

    for listornum in listofinfinitelists:       # iterating over the main list

        if type(combinedlist) == type(listornum):     # if it is a list go to the next line
            for list in listornum:               # iterate over that particular list

                if type(combinedlist) == type(list):        # if it is a list go to the next line
                    listofinfinitelists.append(list)   # if it is a list take it and add it to our main list
# ( the benefit that now we have it just a list not a list inside a list inside a list and
# it will go all the way to the end of our list which means we will iterate over it again later in our loop)

                else: combinedlist.append(list)  #  it means it is ready add it to our result list

        else: combinedlist.append(listornum)    #  it means it is ready add it to our result list

    return combinedlist     # return our result list



listofinfinitelists = [[1,2],[[2,3],[4,4],[[3,4],[[[3323,323],[323,434,434],[434433,434]],[4343,545]],[77,88]],[545,665]],[4,5]]
printablelist =combineinfinitelists(listofinfinitelists)  # using the function on the above list


listoflistsstrings =[[[1,2],[None],None,[3,4]],[[3,4],["hello","there"]]]
printabletringlits = combineinfinitelists(listoflistsstrings)



print(printablelist)
print(printabletringlits)

# ________________________________________________________________________________
# result
# [1, 2, 4, 5, 2, 3, 4, 4, 545, 665, 3, 4, 77, 88, 4343, 545, 3323, 323, 323, 434, 434, 434433, 434]
# [1, 2, 3, 4, 3, 4, 'hello', 'there']
