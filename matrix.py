from array1 import Array2D


class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, Scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = Scalar

    def scaleBy(self, Scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= Scalar

        print(self[r, c])

    def Scalared(self, Scalar):
        print("Matrix:")
        for r in range(self.numRows()):
            print(" ")
            for c in range(self.numCols()):
                self[r, c] *= Scalar
                print(self[r, c], end=" ")

    def transpose(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] = self[c, r]
                return self[c, r]
        print("Transpose of your matrix: ")
        print(" ")

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix size not compitable with add operation."

        newMatrix = Matrix(self.numRows(), self.numCols())

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]

        return newMatrix
    print(" ")

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix size not compitable with add operation."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix
    print(" ")

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numCols() == self.numRows(), \
            "Matrix size not compitable with add operation."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                for cx in range(self.numCols()):
                    newMatrix[r, c] += self[r, cx] * rhsMatrix[cx, c]

        return newMatrix
    print(" ")


def display(x):
    for i in range(x.numRows()):
        print('')
        for j in range(x.numCols()):
            print(x[i, j], end=' ')


print(" ")


def setitem(x):
    for i in range(x.numRows()):
        print('')
        for j in range(x.numCols()):
            x[i, j] = int(input('Enter value %d, %d=' % (i, j)))
    print(" ")


a = Matrix(2, 2)
setitem(a)
print("Your Matrix A: ")
display(a)
print(" ")
b = Matrix(2, 2)
setitem(b)
print("Your Matrix B: ")
display(b)
print(" ")
display(a.transpose())
print(" ")
print("Your Added Matrix: ")
display(a + b)
print(" ")
print("Multiple of your Matrix is: ")
display(a * b)
print(" ")
print("Your Subtracted Matrix: ")
display(a - b)
print(" ")
a.Scalared(3)
