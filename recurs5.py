def mysum(mylist):
    if len(mylist) < 2:
        return mylist[0]
    else:
        return mylist[0] + mysum(mylist[1:])

print(mysum([1, 2, 3, 4, 5, 6]))