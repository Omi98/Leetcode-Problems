digit1 = [1, 2, 3]

# convert the entire list to a single integer using .join() method
result = int("".join(str(i) for i in digit1))
result = result + 1
# convert the integer to a list of individual digits
result = [int(i) for i in str(result)]
print(result)

# ----------------------------
digit2 = [9]

result = int("".join(str(i) for i in digit2))
result = result + 1
result = [int(i) for i in str(result)]
print(result)

# ----------------------------
digit3 = [9, 9]

result = int("".join(str(i) for i in digit3))
result = result + 1
result = [int(i) for i in str(result)]
print(result)
