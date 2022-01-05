class Digit(ValueError):
    pass


my_list = []

while True:
    print('s - stop')
    try:
        element = input('Введите число в список:')
        if element == 's':
            print('The end')
            break
        if not element.isdigit():
            raise Digit(element)
        my_list.append(int(element))
    except Digit as e:
        print("It's not a number:", e)
print(my_list)
