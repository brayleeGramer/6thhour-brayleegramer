#Name: Braylee Gramer
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
k=[]
players = int(input("enter number of players: "))
for i in range(players-1):
 j=int(input("rate"))
 k.append(j)
l=sum(k)
print(sum(k))
l/=players-1
print(l)