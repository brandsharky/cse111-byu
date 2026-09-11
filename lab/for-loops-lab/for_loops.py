import math


def every_other_letter(string):
    """
    This function takes a string and returns a new string with every other
    letter, starting with the first.
    >>> every_other_letter("hello")
    'hlo'
    >>> every_other_letter("abcdefg")
    'aceg'
    >>> every_other_letter("A")
    'A'
    """
    new_string = ""
    for index in range(0, len(string)):
        if index % 2 == 0:
            new_string += string[index]
    return new_string


def print_triangle():
    """
    This function takes a number n as console input and prints a triangle of numbers with n rows.
    """

    n = int(input("Enter a positive integer: "))

    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def increment_numbers(numbers):
    """
    >>> lst = [1, 2, 3, 4, 5]
    >>> increment_numbers(lst)
    >>> lst
    [2, 3, 4, 5, 6]
    """

    for num in numbers:
        num += 1

    return numbers


def average_temperature(temps):
    """
    Given a list of temperatures, temps, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """

    total = 0

    for temp in temps:
        total += temp

    return total / len(temps)


def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """

    avg = average_temperature(temps)

    count = 0

    for temp in temps:
        if avg - temp >= 5:
            count += 1

    return f"There were {count} day(s) more than 5 degrees above the average of {avg:.1f}."


def reverse_lines(input, output):
    with open(input, "r") as in_file:
        lines = in_file.readlines()

    reversed_lines = []
    for line in lines:
        stripped_line = line.strip()
        reversed_line = line[::-1]
        reversed_lines.append(reversed_line + "/n")
    reversed_lines = reversed_lines[::-1]

    with open(output, "w") as out_file:
        out_file.writelines(reversed_lines)






if __name__ == "__main__":
    # print(every_other_letter(""))
    # print_triangle()
    # print(increment_numbers([1, 2, 3, 4, 5]))
    # print(average_temperature([72.2, 68.7, 67.4, 77.3, 81.6, 83.7]))
    print(hot_days([72.2, 68.7, 67.4, 77.3, 81.6, 83.7]))