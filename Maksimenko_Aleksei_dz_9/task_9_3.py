class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        full_income = self._income.get('wage') + self._income.get('bonus')
        return f'result: {full_income}'


a = Position('Остап', 'Сулейман', 'Авантюрист', 15000, 45000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
