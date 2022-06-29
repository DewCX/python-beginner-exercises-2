#Control Flow and Logical Operators

#Write a program that works out whether if a given number is an odd or even number.

#Answer

from turtle import window_height


"""number = int(input("Please enter a number: \n"))

number_odd_or_even = number % 2

if number_odd_or_even == 0:
    print(f"{number} is even because reaminder is {number_odd_or_even}")
else:
    print(f"{number} is odd because remainder is {number_odd_or_even}")""",


#Write a program that interprets the Body Mass Index based on a user's weight and height.It should tell them the iterpretation of their BMI based on the BMI value.
"""
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese
"""

#Answer
"""weight = int(input("Please enter your weight: \n"))
height = float(input("Please enter your height: \n"))

bmi = weight / (height ** 2)
bmi_as_int = int(bmi)

if bmi_as_int <= 18.5:
    print(f"Your bmi is {bmi_as_int}.You are underweight.")
elif bmi_as_int >18.5 and bmi_as_int <= 25:
    print(f"Your bmi is {bmi_as_int}.You are normal weight.")
elif bmi_as_int >25 and bmi_as_int <= 30:
    print(f"Your bmi is {bmi_as_int}.You are overweight.")
elif bmi_as_int >30 and bmi_as_int <= 35:
    print(f"Your bmi is {bmi_as_int}.You are obese.")
else:
    print(f"Your bmi is {bmi_as_int}.You are clinically obese.")"""


#Write a program that works out whether if a given year is a leap year.A normal year has 365 days,leap years have 366 ,with an extra day in February.

#Answer
"""year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")"""



#Python pizza program
#Ask a user pizza size(S,M or L), ask are they want to add pepperoni and ask them that are they want to extra cheese?
#Based on user's order,work out their final bill.

"""
Small Pizza : $10
Medium Pizza : $15
Large Pizza : $19

Pepperoni for small pizza : +4$
Pepperoni for medium and large pizza : +$5

Extra cheese for any size pizza : +$1
"""

#Answer
"""size = input("What size pizza do you want? S,M or L : \n")
add_pepperoni = input("Do you want pepperoni? Y or N : \n")
extra_cheese = input("Do you want extra cheese? Y or N : \n")

bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 19

if add_pepperoni == "Y":
    if size == "S":
        bill += 4
    else:
        bill += 5
    
if extra_cheese == "Y":
    bill += 1

print("Your final bill is:",bill)"""


#Love Calculator
#You are going to write a program that tests the compatibility between two people.We're going to use the super scientific method recommended by BuzzFeed.

"""
1-For love scores less than 10 or greater than 90 , the message should be:"Your score is x, you go together like coke and mentos."

2-For love scores between 40 and 50,the messages should be:
"Your score is y, you are alright together."

3-Otherwise,the message will just be their score e.g.:
"Your score is z."
"""


#Answer
"""name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score_int = int(love_score)
if love_score_int < 10 or love_score_int > 90:
    print(f"Your score is {love_score_int} , you go together like coke and mentos ")
elif love_score_int >= 40 and love_score_int <= 50:
    print(f"Your score is {love_score_int} , you are alright together.")
else:
    print(f"Your score is {love_score}")"""


#Treasure island


        #     ____...------------...____
        #        _.-"` /o/__ ____ __ __  __ \o\_`"-._
        #      .'     / /                    \ \     '.
        #      |=====/o/======================\o\=====|
        #      |____/_/________..____..________\_\____|
        #      /   _/ \_     <_o#\__/#o_>     _/ \_   
        #      \_________\####/_________/
        #       |===\!/========================\!/===|
        #       |   |=|          .---.         |=|   |
        #       |===|o|=========/     \========|o|===|
        #       |   | |         \() ()/        | |   |
        #       |===|o|======{'-.) A (.-'}=====|o|===|
        #       | __/ \__     '-.\uuu/.-'    __/ \__ |
        #       |==== .'.'^'.'.====|
        #   jgs |  _\o/   __  {.' __  '.} _   _\o/  _|

"""
print("------------------------------------------------------------------------------------------------")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You are at a crossroad,where do you want to go? Type 'left' or 'right':  \n" ).lower()

if choice1 == "right" :
    choice1_2 = input("You saw a lion.Are you going to runaway or stayed where you are and fight with it ? Type 'Y' or 'N' ").upper()
    if choice1_2 == "N":
        print("Continue the game")
        choice1_3 = input("You've come to jungle.There is a car in the middle of the jungle.Type 'wait' to check area.Type 'move' to get the car as fast as you can. ").lower()
        if choice1_3 == "wait":
            choice1_4 = input("You arrive at the heart of the cave in island.There is a gate with 3 paths.One black,one red and one green.Which colour do you choose? ").lower()
            if choice1_4 == "black":
                print("It's full of darkness.You are lost.Game over.")
            elif choice1_4 == "red":
                print("It's a monkey's chief room.You got killed by chief.Game over.")
            elif choice1_4 == "green":
                print("You found the treasure! You Win!")
            else:
                print("You chose a gate that doesn't exist.Game over.")    
        else:
            print("You got attacked by monkeys.You are dead , game over.")
    else:
        print("Sometimes you just need to runaway dont be hero.Game over , you are dead.")
        
else:
    print("Wrong way you are dead.")
    
"""