from functools import wraps


def decorate(callback):
    @wraps(callback)
    def wrapper(*args):
        arguments = callback(*args)
        for arg in args:
            print(f'{arg}: {type(arg)}',end=',')
            print()
        return arguments

    return wrapper


@decorate
def calc_cube(number):
    return number ** 3


@decorate
def calc_box(length, width):
    return length * width


@decorate
def my_str(name, text="Hi"):
    print(text, name)
    return name, text


area_1 = calc_cube(5)
print(f"result: {area_1}")

num_1 = int(input("Number: "))
num_2 = int(input("Number: "))
area_2 = calc_box(num_1, num_2)
print(f'result: {area_2}')

area_3 = my_str("Alex")
