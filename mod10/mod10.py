numbers = [12, 8, 9, 10, 20]


def double(values):
	return [value * 2 for value in values]


doubled = double(numbers)

print(f"original numbers {numbers}")
print(f"doubled numbers {doubled}")