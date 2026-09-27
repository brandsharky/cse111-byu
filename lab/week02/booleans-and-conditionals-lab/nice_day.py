import random

temperature = random.randint(30, 100)

print(f'DEBUG - temperature: {temperature}')

if 80 >= temperature >= 65:
    print("It's a nice day!")
else:
    print("It's not nice out.")