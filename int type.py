list = [1, "learning python", [], object() ]
for int in list:
    thekind = type (int)
    print(f" (( {int } )) type is { thekind}")


#
# result__________________________________________
#  (( 1 )) type is <class 'int'>
#  (( learning python )) type is <class 'str'>
#  (( [] )) type is <class 'list'>
#  (( <object object at 0x000002114E01E0C0> )) type is <class 'object'>
