class Accessory:
    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        pass


class Pen(Accessory):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой')


class Pencil(Accessory):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом')


class Marker(Accessory):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Marker('Маркер')
