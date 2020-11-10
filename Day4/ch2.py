# Import Day 4 - Exercise 2
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
namesq = len(names)
ss = random.randint(1, namesq)
name = names[ss]


print(f"{name} is going to buy the meal today!")
