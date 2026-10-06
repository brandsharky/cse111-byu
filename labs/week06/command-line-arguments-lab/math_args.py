import sys



# Q3
def main():
    """
    Retrieves command line arguments, validates them, and calls the appropriate function.
    """
    try:
        args = sys.argv
        if args[1] == "add" and len(args) > 2:
            for num in args[2:]:
                if not num.isdigit():
                    raise ValueError("All arguments after 'add' must be numbers")
            print(add(args[2:]))
        elif args[1] == "multiply" and len(args) > 2:
            for num in args[2:]:
                if not num.isdigit():
                    raise ValueError("All arguments after 'multiply' must be numbers")
            print(multiply(args[2:]))
        else:
            raise ValueError("Invalid command. Use 'add' or 'multiply', followed by one or more numbers")
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except IndexError:
        print(f"Error: Not enough arguments given. Use 'add' or 'multiply', followed by one or more numbers. Please try again.")


def add(lst):
    """
    This function takes a list of integers and returns their sum.
    """
    total = 0
    for num in lst:
        total += int(num)
    return total


def multiply(lst):
    """
    This function takes a list of integers and returns their product.
    """
    product = 1
    for num in lst:
        product *= int(num)
    return product





if __name__ == "__main__":
    main()