import random

grade = random.randint(0, 100)

print(f'DEBUG - grade: {grade}')

if 100 >= grade >= 90:
  print("A")
elif 89 >= grade >= 80:
  print("B")
elif 79 >= grade >= 70:
  print("C")
elif 69 >= grade >= 60:
  print("D")
elif 59 >= grade >= 0:
  print("F")