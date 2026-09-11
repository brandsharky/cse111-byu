def format_date(month, day, year=2025):
    # Check if both month and day are valid for the given year
    if validate_month(month) and validate_day(day, month, year) and year >= 0:
        return f"{month:02d}/{day:02d}/{year}"
    return False


def validate_month(month):
    return 1 <= month <= 12


def validate_day(day, month, year):
    # Handle February leap year rules
    # A year is a leap year if divisible by 4, but NOT 100 unless also divisible by 400
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Define max days for each month (index 1 to 12)
    month_days = {
        1: 31, 2: 29 if is_leap else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }

    return 1 <= day <= month_days[month]


if __name__ == "__main__":
    print(format_date(12, 25, 2023))  # Output: 12/25/2023
    print(format_date(1, 2))          # Output: 01/02/2026
    print(format_date(4, 31, 2026))   # Output: False (April only has 30 days)