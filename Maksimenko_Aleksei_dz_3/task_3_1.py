def num_translate(num):
    numbers = {'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'
               }
    if num.istitle() and numbers.get(num.lower()):
        return numbers.get(num.lower()).title()
    else:
        return numbers.get(num)


your_number = input('number in English from 1 to 10: ')
print(num_translate(your_number))
