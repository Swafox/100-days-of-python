# Day 3 - Exercise 2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
'''
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''
#Write your code below this line 👇

BMI = round(weight / height ** 2)

if (BMI < 18.5):
  BMI = str(BMI)
  print("Your BMI is " + BMI + ", you are underweight")
elif (BMI < 25):
  BMI = str(BMI)
  print("Your BMI is " + BMI + ", you have a normal weight.")
elif (BMI < 30):
  BMI = str(BMI)
  print("Your BMI is " + BMI + ", you are slightly overweight")
elif (BMI < 35):
  BMI = str(BMI)
  print("Your BMI is " + BMI + ", you are slightly obese")
elif (BMI > 35):
  BMI = str(BMI)
  print("Your BMI is " + BMI + ", you are clinically obese")
