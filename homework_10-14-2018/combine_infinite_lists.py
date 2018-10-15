def combineinfinitelists (listofinfinitelists):
    inttype = 3              # int type variable to compare with
    combinedlist = []        # empty list to add our result to it

    for listornum in listofinfinitelists:       # iterating over the main list

        if type(inttype) != type(listornum):     # if it isn't numbers so it is a list go to the next line
            for list in listornum:               # iterate over that particular list

                if type(inttype) != type(list):        # if it isn't numbers so it is a list go to the next line
                    listofinfinitelists.append(list)   # if it is a list take it and add it to our main list
# ( the benefit that now we have it just a list not a list inside a list inside a list and
# it will go all the way to the end of our list which means we will iterate over it again later in our loop)

                else: combinedlist.append(list)  # add the numbers to our result list

        else: combinedlist.append(listornum)    # add the numbers to our result list

    return combinedlist   # return our result list



listofinfinitelists = [[1,2],[[2,3],[4,4],[[3,4],[[[3323,323],[323,434,434],[434433,434]],[4343,545]],[77,88]],[545,665]],[4,5]]


printablelist =combineinfinitelists(listofinfinitelists)  # using the function on the above list

print(printablelist)
