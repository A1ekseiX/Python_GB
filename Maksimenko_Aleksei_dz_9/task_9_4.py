from random import choice
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.go()
        self.turn_direction()
        self.stop()
        self.show_speed()
        self.police()

    def go(self):
        print(f'{self.name} on start')

    def stop(self):
        print(f'{self.name} stopped')

    def turn_direction(self):
        a = choice(['left', 'right'])
        print(f'{self.name} is turning {a}')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')

    def police(self):
        if self.is_police:
            print(f'{self.name} is police car')
        else:
            print(f'{self.name} is not police car')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            print(f'Speed of {self.name} is higher than allowed for town car')
        else:
            print(f'Speed of {self.name} is normal for town car')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            print(f'Speed of {self.name} is higher than allow for work car')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


auto_1 = SportCar(randint(40, 240), 'Blue', 'A-7', False)
auto_2 = TownCar(randint(40, 140), 'Grey', 'Is-350', False)
auto_3 = WorkCar(randint(40, 140), 'Black', 'GLE', False)
auto_4 = PoliceCar(randint(40, 240), 'Black', 'Mustang', True)
