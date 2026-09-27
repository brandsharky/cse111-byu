import random

a = random.randint(1, 30)
b = random.randint(1, 30)
c = random.randint(1, 30)
print(f'DEBUG - a: {a}, b: {b}, c: {c}')

if (a + b > c) and (a + c > b) and (b + c > a):
  print("valid triangle")
else:
  print("invalid triangle")