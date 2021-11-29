nums = (i for i in range(1, 17) if i % 2 != 0)
while True:
    try:
        print(next(nums))
    except StopIteration:
        print("StopIteration")
        break
