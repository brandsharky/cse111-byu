item = ""
total = 0
items = []
prices = []

while item != "done":
  item = str(input("Item? "))
  if item == "done":
    break

  items.append(item)

  price = float(input("Price? "))
  prices.append(price)
  total += price


print()

for i in range(0, len(items)):
  print(f"{items[i]}: ${prices[i]}")

print(f"Total: ${total}")