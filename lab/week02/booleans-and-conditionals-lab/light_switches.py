import random

switchA = random.randint(0, 1)
switchB = random.randint(0, 1)
switchC = random.randint(0, 1)
switchD = random.randint(0, 1)

print(f'DEBUG - switchA: {switchA}, switchB: {switchB}, switchC: {switchC}, switchD: {switchD}')

if switchA and switchB and switchC and switchD:
  print("on")
else:
  print("off")