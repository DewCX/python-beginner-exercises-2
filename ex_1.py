#Data Types

#Write a program that adds the digits in a 2 digit number.e.g. if the input was 35,then the output should be 3 + 5 = 8

#Answer
"""two_digit_number = input("Type two digit number: ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result_digit = int(first_digit) + int(second_digit)

print(result_digit)"""

#BMI Calculator

#Write a program that calculates the Body Mass Index(BMI) from a user's weight and height.(Formula : bmi = weight / (height**2))

#Answer
"""weight = float(input("Please enter your weight: \n"))
height = float(input("Please enter your height: "))

bmi = weight / (height**2)
bmi_as_int = int(bmi)

print("Your body mass index is: ",bmi_as_int)"""


#Life in weeks
#Create a program using maths and f-Strings that tells us how many days,weeks,months we have left if we live until 90 years old.

#Answer
"""age = input("What is your current age?\n")

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52

print(f"You have {days_remaining} days , {weeks_remaining} weeks , and {months_remaining} months left. ")"""


#Tip calculator

#Use inputs to take total price of bill and percentage tip(10,12,15), take information to user with using input how many people to split the bill and the program will give us how many should pay each person.

#Answer

"""bill = float(input("What was the total bill?:\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?: \n"))
people = int(input("How many people split the bill?: \n"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
each_person_pay = total_bill / people
final_amount = round(each_person_pay,2)
print(f"Each person should pay {final_amount} dollars.")"""






