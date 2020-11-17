student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] // model
x = thisdict.get("model") // value

thisdict["color"] = "red" // adds value red to color
'''
for x in student_scores:
  score = student_scores[x]
  if (score < 70):
    student_grades[x] = "Fail"
  elif (score < 80):
    student_grades[x] = "Acceptable"
  elif (score < 90):
    student_grades[x] = "Exceeds Expectations"
  elif (score < 100):
    student_grades[x] = "Outstanding"


# 🚨 Don't change the code below 👇
print(student_grades)
