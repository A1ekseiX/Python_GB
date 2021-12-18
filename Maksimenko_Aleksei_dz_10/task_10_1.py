class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        scheme = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                scheme[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in scheme]))

    def __str__(self, scheme=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in scheme]))


matrix = Matrix([[6, 40, 33],
                 [27, 15, 68],
                 [45, 81, 19]],
                [[24, 5, 3],
                 [7, 9, 49],
                 [25, 12, 89]])

print(matrix.__add__())
