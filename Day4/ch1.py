# Day 4 - Challenge 1
#Remember to use the random module 👇
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

f = random.randint(0,1)
if f == 1:
  print("Heads")
else:
  print("Tails")
