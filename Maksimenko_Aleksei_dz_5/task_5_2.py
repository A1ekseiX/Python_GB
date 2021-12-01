tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

c = ((x, y) for x, y in zip(tutors, klasses))
print(c)
while True:
    try:
        print(next(c))
    except StopIteration:
        print("StopIteration")
        break
