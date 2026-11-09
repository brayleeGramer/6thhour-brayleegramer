#Name: Braylee Gramer
#Class: 6th Hour
#Assignment: HW14

import random


#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i>=0:
    print(i)
    i-=1

else:
     print("hello world ")


#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
h=1
while h<=30:

    if h % 2==0:
        print(h)
    h+=1


#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
k=1
while k<=30:
    if k % 3!=0:
        print(k)
    k+=1


#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
j=random.randint(1,6)

while True:
    print(j)
    if j==1:
        break
    j = random.randint(1, 6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
l=int(input("give me a number"))
while l!= 0:
    if l==0:
        break

    else:
        l = int(input("give me a number"))
