import random

height = random.randint(24, 84)

print(f'DEBUG - height: {height}')

if height >= 52:
  print("You can ride by yourself!")
elif height >= 48:
  print("You can ride with an adult!")
else:
  print("Sorry, you are not tall enough to ride.")