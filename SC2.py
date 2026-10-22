#Name: Braylee Gramer
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
h = float(input("give me your height in inches """))
W = float(input("give me your weight in pounds "))
BMI = (W/(h**2))*703
print("you are a ",BMI)

if BMI<18.5:
    print("You are underweight")
elif 18.5<BMI<24.9:
    print("You are normal")
elif 25<BMI<29.9:
    print("You are overweight")
elif 30<BMI:
    print("You are obese")