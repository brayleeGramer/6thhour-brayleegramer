#Name:Braylee Gramer
#Class: 6th Hour
#Assignment: HW9


#1. Print Hello World!
print("Hello World")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
Brayleecardictonary={
    "brand":"jeep",
"model":"compass",
"year":[2019,2018,2017]
}

#3. Print the keys of the dictionary from #2.
print(Brayleecardictonary)

#4. Print the values of the dictionary from #2
print(Brayleecardictonary["model"])

#5. Print one of the three numbers from the list by itself
print(Brayleecardictonary["year"][0])

#6. Using the update function, add a fourth key to the dictionary and give it a value.
Brayleecardictonary.update({"color":"black"})

#7. Print the entire dictionary from #2 with the updated key and value.
print(Brayleecardictonary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
threeclassmates={ "student1" : {
        "Name" : "Misa",
        "Grade" : 10,
        "shirtcolor":"white"
    },
    "student2" : {
        "Name" : "raphael",
        "Grade" : 11,
        "Shirtcolor" : "red",
    },
    "student3" : {
        "Name" : "owen",
        "Grade" : 12,
        "shirtcolor" : "white",
    },
}



#9. Print the names of all three classmates on the same line.
print(threeclassmates["student1"]["Name"],threeclassmates["student2"]["Name"],threeclassmates["student3"]["Name"])

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
threeclassmates.pop("student1")
print(threeclassmates)
