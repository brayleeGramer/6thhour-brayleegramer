#Name: Braylee Gramer
#Class: 6th Hour
#Assignment: HW11
#from HW5
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100

randomlist=[random.randint(1,100),random.randint(1,100),random.randint(1,100)]
#3. Print the list.
print(randomlist)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if randomlist[0]>=randomlist[1]and randomlist[0]>=randomlist[2]:
    print("1st number is the biggest number")
elif randomlist[1]>=randomlist[2]and randomlist[1]>=randomlist[0]:
    print("2nd number is the biggest number")
else:
    print("3rd number is the biggest number")

#5. Tie the result (the largest number) from #4 to a variable called "num".
num=max(randomlist[0],randomlist[1],randomlist[2])



#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2==0:

    print("num is an even number")
    if num%3==0:
        print("the number is divisible by 3")
    else:
            print("num is not divisible by 2 or 3")

elif num % 3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3 and 2")