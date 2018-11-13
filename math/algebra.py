class Vector:
    def __init__(self, vector):
        if not isinstance(vector, list):
            raise Exception('Vector is not a list')
        self.vector = vector

    def __len__(self):
        return len(self.vector)

    def print(self):
        for item in self.vector:
            print('[ {} ]'.format(item))


class Matrix:
    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise Exception('Matrix is not a list')
        self.rows = len(matrix)
        self.cols = None
        for row in matrix:
            if not isinstance(row, list):
                raise Exception('Matrix row is not a list')
            if self.cols is None:
                self.cols = len(row)
            elif self.cols != len(row):
                raise Exception('Matrix has uneven columns')
        self.matrix = matrix

    def dimensions(self):
        return self.rows, self.cols

    def print(self):
        for row in self.matrix:
            print(row)


if __name__ == '__main__':
    v = Vector([1, 2, 3])
    v.print()
    print(len(v))

    m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m.print()
    print(m.dimensions())
