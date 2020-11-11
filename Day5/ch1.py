# Day 5 - Challenge 1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
tot = 0
for i in student_heights:
  tot = tot + i

print(round(tot / len(student_heights)))
