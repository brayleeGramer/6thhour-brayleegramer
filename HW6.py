#Name:Braylee Gramer

#Class: 6th Hour

#Assignment: HW6

#1. Create a list with 9 different numbers inside.
numlist=[26,4,6,8,10,12,14,16,18]

#2. Sort the list from highest to lowest.
numlist.sort()
print(numlist)

#3. Create an empty list.
nolist=[]

#4. Remove the median number from the first list and add it to the second list.
mediannumber=numlist.pop(4)
nolist.append(mediannumber)
print(nolist)

#5. Remove the first number from the first list and add it to the second list.
numlist.remove(26)
onenumber=numlist.pop(1)
nolist.append(onenumber)
#6. Print both lists.
print(nolist)
print(numlist)

#7. Add the two numbers in the second list together and print the result.
nolistsubsum=nolist[0]+nolist[1]
print(nolistsubsum)

#8. Add the sum from #7 to the first list.
numlist.append(nolistsubsum)
print(numlist)

#9. Sort the first list from lowest to highest and print it.
numlist.sort()
print(numlist)