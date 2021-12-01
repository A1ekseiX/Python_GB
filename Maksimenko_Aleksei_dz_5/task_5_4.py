numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
nums = set()
for el in numbers:
    [unique.add(el) if el not in nums else unique.discard(el)]
    nums.add(el)
print([name for name in numbers if name in unique])
