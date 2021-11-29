src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
numbers = []
for x in src:
    if x not in numbers:
        numbers.append(x)
print(numbers)
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]
print(result)
