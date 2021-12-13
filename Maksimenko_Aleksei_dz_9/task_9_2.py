class Road:
    def __init__(self, _length, _width, thickness):
        self._length = _length
        self._width = _width
        self.thickness = thickness
        self.mass()

    def mass(self):
        return (self._length * self._width * 25 * self.thickness) / 1000


r = Road(20, 5000, 5)
print(f'result: {r.mass()} tons')
