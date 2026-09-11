# Constants
PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1

DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12

COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28

PI = 3.14159265



def number_of_pizzas(guests):
    """
    Takes the total number of guests as a parameter and determines how many large, medium, and small pizzas
    to purchase by dividing the number of guests and then continuing to divide the remainder by the next pizzas
    size. If one guest still doesn't have pizzas, then it adds one more small_pizza.
    Returns number of large_pizzas, medium_pizzas, and small_pizzas.
    """

    large_pizzas = 0
    medium_pizzas = 0
    small_pizzas = 0

    large_pizzas = guests // PEOPLE_PER_LARGE
    guests = guests % PEOPLE_PER_LARGE

    medium_pizzas = guests // PEOPLE_PER_MEDIUM
    guests = guests % PEOPLE_PER_MEDIUM

    small_pizzas = guests // PEOPLE_PER_SMALL
    guests = guests % PEOPLE_PER_SMALL

    if guests > 0:
        small_pizzas += 1

    return large_pizzas, medium_pizzas, small_pizzas


def total_area_of_pizzas(large_pizzas, medium_pizzas, small_pizzas):
    """
    Takes in the number of each size pizzas and calculates
    the area of each sized pizza and totals all the areas.
    Returns the total_area of all the pizzas.
    """

    large_pizza_area = large_pizzas * (PI * (DIAMETER_LARGE / 2) ** 2)
    medium_pizza_area = medium_pizzas * (PI * (DIAMETER_MEDIUM / 2) ** 2)
    small_pizza_area = small_pizzas * (PI * (DIAMETER_SMALL / 2) ** 2)

    total_area = large_pizza_area + medium_pizza_area + small_pizza_area

    return total_area


def pizza_area_per_guest(total_area, guests):
    """
    Takes total area of pizzas and number of guests.
    Calculates the area of pizzas per guest.
    Returns the total_area / guests.
    """

    return total_area / guests


def calculate_total(large_pizzas, medium_pizzas, small_pizzas, tip):
    """
    Takes in number of large_pizzas, medium_pizzas, small_pizzas, and the desired tip as parameters.
    Totals the cost of all the pizzas and then adds the desired tip, which is given as an integer.
    Returns the total cost of all the pizzas
    """

    total = 0

    total += large_pizzas * COST_LARGE
    total += medium_pizzas * COST_MEDIUM
    total += small_pizzas * COST_SMALL

    total += (total * (tip/100))

    return total



def main():
    # Ask for number of guests
    guests = int(input("Please enter how many guests to order for:\n"))

    # Calculate and display number of pizzas needed
    large_pizzas, medium_pizzas, small_pizzas = number_of_pizzas(guests)
    print(f"{large_pizzas} large pizzas, {medium_pizzas} medium pizzas, and {small_pizzas} small pizzas will be needed.")

    # Calculate and display total area of all pizzas and area per person
    print()
    total_pizza_area = total_area_of_pizzas(large_pizzas, medium_pizzas, small_pizzas)
    avg_pizza_area = pizza_area_per_guest(total_pizza_area, guests)
    print(f"A total of {total_pizza_area:.2f} square inches of pizza will be ordered ({avg_pizza_area:.2f} per guest).")

    # Ask for tip amount
    print()
    tip = int(input("Please enter the tip as a percentage (i.e. 10 mean 10%):\n"))

    # Calculate and display total cost of all pizzas
    total = calculate_total(large_pizzas, medium_pizzas, small_pizzas, tip)
    print(f"The total cost of the event will be: ${total:.2f}")





if __name__ == "__main__":
    main()