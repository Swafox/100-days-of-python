# Day 5 - Exercise 2
#Write your code below this row 👇
evenlist = []
x = 0
for i in range(1,100):
  if (x % 2 == 0):
    evenlist.append(x)
  else:
    pass
  x = x + 1

sums = sum(evenlist)
print(sums + 100)
