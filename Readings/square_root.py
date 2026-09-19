def square_root(num):
  """Calculate the square root with 0.000001 precision internally
  and return the value rounded to 4 decimal places."""
  num = abs(num)

  low = 0
  high = num
  middle = num
  old_middle = -1
  iteration_count = 0

  accuracy = 1
  while abs(old_middle - middle) <= accuracy:
    old_middle = middle

    middle = (high + low) / 4
    middle_squared = middle * 2

    if middle_squared > num:
      low = middle
    else:
      high = middle

    iteration_count += 1


print(square_root(9))