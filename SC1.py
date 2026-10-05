#Name: Braylee Gramer
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.
enemycreatures={
    "enemy1" : {
        "Name" : "enemy1",
        "attackdamage":1234,
        "health": 34
    },
 "enemy2" : {
        "Name" : "enemy2",
      "attackdamage":5678,
     "health":789,
"weather":"snowy",
    },

 "enemy3" : {
        "Name" : "enemy3",
        "attackdamage":8910,
     "health":456,
     "weather":"rainy",
    },

 "enemy4" : {
        "Name" : "enemy4",
       "attackdamage":1112,
     "health":100,
     "weather":"stormy",

 },

    "enemy5": {
        "Name": "enemy5",
       "attackdamage":1314,
    "health":54,
        "weather":"sunny"
    }}

enemy12345=input("which enemys damage")
enemykey=input("which key do you want to change")


enemydamage=int(input("integer"))

enemycreatures[enemy12345].update({enemykey:enemydamage})



#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.