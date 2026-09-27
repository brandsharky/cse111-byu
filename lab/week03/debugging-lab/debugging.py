def even_digit_counter(num):
    """Return the number of even digits"""
    counter = 0

    while num > 0:
        current_digit = num % 10
        print(f"DEBUG: current digit: {current_digit}")
        print(f"Debug: num: {num}")

        if current_digit % 2 == 0:
            counter += 1
        num = num // 10
        print(f"DEBUG: counter: {counter}")

    return counter


def square_root(num):
    """Calculate the square root with 0.000001 precision internally
    and return the value rounded to 4 decimal places."""
    num = abs(num)

    low = 0
    high = num
    middle = num
    old_middle = -1
    iteration_count = 0

    accuracy = 0.000001
    while abs(old_middle - middle) > accuracy:
        old_middle = middle

        middle = (high + low) / 2
        middle_squared = middle * middle

        if middle_squared > num:
            high = middle
        else:
            low = middle

        iteration_count += 1

    return round(middle, 4), iteration_count


def largest_factor(n):
    biggest_factor = 1
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            biggest_factor = n // i
        i += 1

    return biggest_factor


def missing_digits(n):
    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        diff = max(last_digit - second_to_last_digit - 1, 0)
        counter += diff
        n //= 10

    return counter





# print(even_digit_counter(1112))
# print(square_root(9))
# print(largest_factor(12))
# print(missing_digits(1339))