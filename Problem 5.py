#JT KIM
#APRIL 9
#PROBLEM 5 NEW LIST WITH UNIQUE ELEMENTS OF THE FIRST LIST

xlist = [1, 3, 3, 3, 6, 2, 3, 5]
ulist = []
for element in xlist:
    if element not in ulist:
        ulist.append(element)
print (ulist) 
