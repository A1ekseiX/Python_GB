class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Result {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else print('Negative!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


first_cells = Cell(25)
second_cells = Cell(10)
print(first_cells)
print(first_cells + second_cells)
print(second_cells - first_cells)
print(second_cells.make_order(6))
print(first_cells.make_order(12))
print(first_cells / second_cells)
