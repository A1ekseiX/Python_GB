class DivisionError(Exception):
    pass


try:
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter a number: "))
    if number_2 == 0:
        raise DivisionError("Division by zero!")
except (ValueError, DivisionError) as e:
    print(e)
else:
    print(number_1 / number_2)
finally:
    print("Operation completed")
