# Day 3 - Challenge 5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
firstname = name1.lower()
secondname = name2.lower()
tcount = firstname.count('t') + firstname.count('r') + firstname.count('u') + firstname.count('e') + secondname.count('t') + secondname.count('r') + secondname.count('u') + secondname.count('e')

lcount = secondname.count('l') + secondname.count('o') + secondname.count('v') + secondname.count('e') + firstname.count('l') + firstname.count('o') + firstname.count('v') + firstname.count('e')

resultz = str(tcount) + str(lcount)
resultz = int(resultz)
if (resultz < 10 or resultz > 90):
  print(f"Your score is {resultz}, you go together like coke and mentos.")

elif (resultz < 50):
  print(f"Your score is {resultz}, you are alright together.")

else:
  print(f"Your score is {resultz}.")
