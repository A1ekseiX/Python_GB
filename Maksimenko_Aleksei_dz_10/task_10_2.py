from abc import ABC, abstractmethod


class Textile(ABC):
    total_count = 0

    @abstractmethod
    def total(self):
        pass


class Coat(Textile):
    def __init__(self, size):
        self.size = size
        Coat.total_count += self.total

    def __str__(self):
        return f'Пальто: размер: {self.size}, расход ткани: {self.total}, общий расход ткани: {Coat.total_count:.02f}'

    @property
    def total(self):
        tot = self.size / 6.5 + 0.5
        return float(f'{tot:.02f}')


class Jacket(Textile):
    def __init__(self, height):
        self.height = height
        Jacket.total_count += self.total

    def __str__(self):
        return f'Костюм: рост: {self.height}, расход ткани: {self.total}, общий расход: {Jacket.total_count:.02f}'

    @property
    def total(self):
        tot = (self.height * 2 + 0.3) / 100
        return float(f'{tot:.02f}')


coat = Coat(58)
print(coat)
jacket = Jacket(195)
print(jacket)
coat_1 = Coat(48)
print(coat_1)
jacket_1 = Jacket(168)
print(jacket_1)
