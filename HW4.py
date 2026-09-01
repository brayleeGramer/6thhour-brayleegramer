#Name: Braylee Gramer
#class 6th hour
#assignment: HW4

#1. Print "Hello World!"
"hello world"
print("hello world")

#2. import the 'math' library
import math


#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
floatvarx =float(input("enter a decimal" ))
intvary=int(input("enter an integer"))


#4. Create a variable with the value that is x and y added together.
varible2 = floatvarx + intvary

#5. Print the variable from #4.
print(varible2)

#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
varible3=varible2/3

#7. Print the variable from #6.
print(varible3)
#8. Create a variable with the value of the square root of y, then print the result.
varible4=math.sqrt(intvary)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
print(round(floatvarx,1))

#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
print(math.ceil(floatvarx))

#11. Use the floor function to round x down to the nearest whole number. Print the result.
print(math.floor(floatvarx))
