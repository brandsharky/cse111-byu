import random



def roll_die(sides):
    """Return a random integer in the range [1, sides]."""
    if not sides >= 1:
        raise ValueError

    return random.randint(1, sides)


def roll_dice(n, sides):
    """Return a list of length `n` of random integers in [1, sides]."""
    if not n >= 0 or not sides >= 1:
        raise ValueError

    results = [roll_die(sides) for i in range(n)]

    return results


def simulate_coin_flips(n):
    """Simulate flipping a fair coin `n` times.

    Return a tuple (heads_count, tails_count).
    """
    if n < 0:
        raise ValueError
    heads_count = sum(random.random() < 0.5 for i in range(n))
    return (heads_count, n - heads_count)


def random_float_range(a, b):
    """Return a random float uniformly in [a, b).

    Assumes a < b.
    """
    if not a < b:
        raise ValueError

    return a + (b - a) * random.random()


def choose_random_element(seq):
    """Choose and return a random element from a non-empty sequence.

    If `seq` is empty, return None.
    """
    if not seq:
        return None

    return random.choice(seq)


def shuffle_list(seq):
    """Return a new list that is a shuffled copy of `seq`.

    The input `seq` must not be mutated by this function.
    """
    seq_copy = seq[:]
    random.shuffle(seq_copy)
    return seq_copy


def weighted_choice(items, weights):
    """Choose a random item from `items` with probabilities proportional to `weights`.

    - `items` and `weights` must be the same length and non-empty.
    - All weights must be non-negative, and the sum must be > 0.
    """
    if len(items) != len(weights) or len(items) == 0:
        raise ValueError
    if any(weight < 0 for weight in weights):
        raise ValueError
    total = sum(weights)
    if total <= 0:
        raise ValueError

    dart = (total) * random.random()

    running_total = 0
    for item, weight in zip(items, weights):
        running_total += weight
        if running_total > dart:
            return item
    return items[-1]


def estimate_pi(n_samples):
    """Estimate pi using Monte Carlo sampling of points in the unit square.

    Generate `n_samples` random (x, y) in [0, 1) x [0, 1) and return
    4 * (# points with x^2 + y^2 <= 1) / n_samples.
    """
    if not n_samples >= 1:
        raise ValueError

    points = 0

    for i in range(n_samples):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1.0:
            points += 1

    return 4 * points / n_samples









if __name__ == "__main__":
    # random.seed(12345)
    # print(roll_die(6))

    # random.seed(2024)
    # print(roll_dice(5, 6))

    # random.seed(7)
    # print(simulate_coin_flips(10))

    # random.seed(11)
    # v = random_float_range(1.5, 3.5)
    # print(1.5 <= v < 3.5)

    # random.seed(21)
    # print(choose_random_element(['a', 'b', 'c', 'd']))

    # data = [1, 2, 3, 4, 5, 6]
    # random.seed(99)
    # out = shuffle_list(data)
    # print(data)
    # print(out)

    # random.seed(0)
    # print(estimate_pi(1000))

    pass