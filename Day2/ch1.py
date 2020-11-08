# Day 2 - Challenge 1
# 🚨 Don't change the code below 👇
two_digit_number = int(input("Type a two digit number: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
from math import log10

def digitize(x):
    n = int(log10(x))
    for i in range(n, -1, -1):
        factor = 10**i
        k = x // factor
        yield k
        x -= k * factor

res = list(digitize(two_digit_number))

for i in res:
  i = i + i

print(i - 1)
