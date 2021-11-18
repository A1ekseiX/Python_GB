employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in range(len(employees)):
    names = employees[el].split()
    print(f'"Привет, {names[-1].capitalize()}"')
