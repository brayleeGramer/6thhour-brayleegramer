#Name: Braylee Gramer
#Class: 6th Hour
#Assignment: HW8

#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
varible1=random.randint(1,10)
varible2=random.randint(1,10)
varible3=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(varible1,varible2,varible3)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
varible4=(2+varible1)
varible5=(varible2-4)
varible6=(varible3*1.5)

#6. Print each result from #5 on the same line.
print(varible4,varible5,varible6)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
rand_num_list = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
rand_num_list.sort()
print(rand_num_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
varible7=rand_num_list[1]+rand_num_list[2]+rand_num_list[3]
print(varible7)
#10. Create a list with 5 names of other students in this class and print the list.
classlist=["owen","oywn","misia","mathew","raphael"]
print(classlist)
#11. Shuffle the list in #10 and print the list again.
shuffle(classlist)
print(classlist)

#12. Print a random choice from the list of names from #10.
print(random.choice(classlist))