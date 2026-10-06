from operator import add, mul



#region Q1
def product(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a an integer >= 1")

    total = 1
    for i in range(1, n + 1):
        total *= i

    return total

def summation(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a an integer >= 0")

    total = 0
    for i in range(1, n + 1):
        total += i

    return total
#endregion

#region Q2

def square(x):
    return x * x

def sqrt(x):
    return x ** 0.5  # x^0.5 == √x

def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    total = 0
    for num in numbers:
        total += num

    return total // len(numbers)


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers)
    # `sorted` returns a sorted list. `sorted` works.
    if len(numbers) % 2 == 0:
        left_mid = len(numbers) // 2
        right_mid = left_mid + 1
        return mean([left_mid, right_mid])
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    seen = []
    counts = []
    curr_high_num = 0
    curr_high_count = 0

    for num in numbers:
        if num in seen:
            n_index = seen.index(num)
            counts[n_index] += 1
        else:
            seen.append(num)
            counts.append(1)
            n_index = seen.index(num)
        if counts[n_index] > curr_high_count:
            curr_high_num = num
            curr_high_count = counts[n_index]

    return curr_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers:
        total_dist += square(num - avg)

    return sqrt(total_dist / len(numbers))


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    num_mean = mean(numbers)
    num_median = median(numbers)
    num_mode = mode(numbers)
    num_std_dev = std_dev(numbers)

    return num_mean, num_median, num_mode, num_std_dev
#endregion

#region Q3
def product_short(n):
    pass


def summation_short(n):
    pass


def accumulate(merger, initial, n):
    pass
#endregion

#region Q4
#endregion

#region Q5
#endregion