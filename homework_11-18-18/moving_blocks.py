# one book
# take it to the dest
#
# two books
# take the smallest to the temp
# take the biggest to the dest
# take the smallest to the dest
#
# three books
# take the smallest to the dest
# take the medium to the temp
# take the smallest to the temp
# take the biggest to the dest
# take the smallest to the source
# take the medium to the dest
# take the smallest to the dest

def move(blocks,source,temp,destination):
    if blocks == 0:
        return
    elif blocks ==1:
        return print(f"move {blocks} to {destination}")
    elif blocks ==2:
        return moving_two_blocks(blocks,temp,destination)


def moving_two_blocks(blocks,temp,destination):
    print(f"move {blocks-1} to {temp} ")
    print(f"move {blocks} to {destination}")
    print(f"move {blocks-1} to {destination}")
    return


print(move(2,"a","b","c"))