# Q6
def validate_age(user_input):
    """ Try and convert the user_input to be an integer, check to see if the age is between 0 and 123 inclusive,
    and return that integer. If the age is out of the accepted age range, raise a value error
    with the message "Age outside range!"
    """
    age = int(user_input)

    if not (0 <= age <= 123):
        raise ValueError("Age outside range!")

    return age


def handle_user_input():
    """ Prompt the user for an input of only numbers (no letters or special characters).
    Then call validate_age() to change that input to an integer. Handle any errors that
    might be generated using a try/except block. If you catch/except a ValueError, print out something like:
    "Invalid Age: {user_input}. contains non-numerical characters!"
    """
    user_age = input("Enter your age: ")

    try:
        age = validate_age(user_age)
        print(f"{age} is a valid age")
    except ValueError as e:
        print(f"Invalid Age: {user_age}. Message: {e}")





if __name__ == "__main__":
    handle_user_input()