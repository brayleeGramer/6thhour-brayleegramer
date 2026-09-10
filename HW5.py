#Name:Braylee Gramer
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello world")

#1. Create a list with 5 strings containing 5 different names in it.
familynamelist = ["Chris","Britney","Braylee","Landi","Kelbie","aya","Harely"]
#2. Append a new name onto the Name List.
familynamelist.append("cope")
#3. Print out the 4th name on the list.
print(familynamelist [3])

#4. Create a list with 4 different integers in it.
intlist=[45,87,60,43]
print(intlist)

#5. Insert a new integer into the 2nd spot and print the new list.
intlist.insert(2,56)
print(intlist)
#6. Sort the list from lowest to highest and print the sorted list.
intlist.sort()
print(intlist)
#7. Add the 1st three numbers on the sorted list together and print the sum.
intlist_subsum=intlist[0]+intlist[1]+intlist[2]
print(intlist_subsum)

#8. Create a list with two strings, two variables, and two boolean values.
randomlist=["fry","dog",27,28,False,True]

#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(randomlist[int(input("give me an index value from one to six"))])