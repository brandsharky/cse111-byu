def fahrenheit_to_celsius(f):
    return int((f - 32) * (5 / 9))


def celsius_to_fahrenheit(c):
    return int(c * (9 / 5) + 32)


def converter():
    user_input = str(input("Enter 'f' to convert from Fahrenheit to Celsius, or 'c' to convert from Celsius to Fahrenheit: "))
    temp = int(input("Enter the temperature: "))

    if user_input == 'f':
        print(fahrenheit_to_celsius(temp))
    elif user_input == 'c':
        print(celsius_to_fahrenheit(temp))
    else:
        print("Invalid choice.")





if __name__ == "__main__":
    converter()