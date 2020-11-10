# Day 4 - Challenge 3
# 🚨 Don't change the code below 👇
import math 

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
p = str(position)
li = list(p)
s = []
for e in li:
    a = int(e)
    s.append(a)

if (s[0] == 1):
  if (s[1] == 1):
    row1 = ["X","⬜️","⬜️"]
  if (s[1] == 2):
    row1 = ["⬜️","X","⬜️"]
  else:
    row1 = ["⬜️","⬜️","X"]

elif (s[0] == 2):
  if(s[1] == 1):
    row2 = ["X","⬜️","⬜️"]
  if (s[1] == 2):
    row2 = ["⬜️","X","⬜️"]
  else:
    row2 = ["⬜️","⬜️","X"]

else:
  if(s[1] == 1):
    row3 = ["X","⬜️","⬜️"]
  if (s[1] == 2):
    row3 = ["⬜️","X","⬜️"]
  else:
    row3 = ["⬜️","⬜️","X"]

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
