# Day 2 - Challenge 3
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#Write your code below this line 👇
till = 90 - int(age)

days = str(till * 365)
weeks = str(till * 52)
months = str(till * 12)

print("You have " + days + " days, " + weeks +" weeks, and " + months + " months left.")
