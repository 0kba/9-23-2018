

listoflists = [ ['Mohammed', 95], ['Ali', 90] , ['Sam', 100], ['Al', 99] ]

def criteriaGrade (listoflists , grade):

  resultlist =[]

  for a in listoflists:
     if a[1] >= grade:
        resultlist.append(a[0])
  return resultlist

print(criteriaGrade(listoflists,99))

# _________________________________________________________
# result ['Sam', 'Al']