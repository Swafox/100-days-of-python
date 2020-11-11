# Day 5 - Challenge 3
#Write your code below this row 👇
# 3 Fizz
# 5 Bizz
# 15 FizzBizz
for i in range(1, 101):
  if (i % 3 == 0):
    print("Fizz")
  elif (i % 5 == 0):
    print("Bizz")
  elif (i % 3 == 0 and i % 5 == 0):
    print("FizzBizz")
  else:
    print(i)
