class Vector():
    def __init__(self, L):
        self.L = L
        self.n = len(L)
    def __str__(self):
        return str(self.L)
    def __len__(self):
        return self.n
    def __add__(self, other):
        if type(other) is Vector:
            if self.n != other.n:
                raise IndexError("Vectors Have Different Lengths")
            else:
                L = []
                for i in range(self.n):
                    L.append(self.L[i]+other.L[i])
                return_vect = Vector(L)
                return return_vect
        else:
            raise TypeError("Vector + NonVector")
    def __mul__(self, other):
        if type(other) is Vector:
            if self.n != other.n:
                raise IndexError("Vectors Have Different Lengths")
            else:
                inc = 0
                for i in range(self.n):
                    inc += self.L[i]*other.L[i]
                return inc
        if type(other) is int or type(other) is float:
            L=[]
            for i in range(self.n):
                L.append(self.L[i]*other)
            return_vect = Vector(L)
            return return_vect
        else:
            raise TypeError("Need Vector * int, float, or vector")
    def __eq__(self, other):
        if type(other) is Vector:
            if self.n != other.n:
                return False
            else:
                same = True
                for i in range(self.n):
                    if self.L[i] != other.L[i]:
                        same = False
                return same
        else:
            raise TypeError("Vector == NonVector")
    def magnitude(self):
        inc = 0
        for i in range(self.n):
            inc += self.L[i] ** 2
        return inc ** 0.5
    

class Matrix():
    def __init__(self, L):
        #L is a List of Lists (List of the Rows)
        self.L = L
        self.m = len(L) #number of rows
        self.n = len(L[0]) #number of columns
        valid_matrix = True
        for i in range(self.m):
            if len(self.L[i]) != self.n:
                valid_matrix = False
        if not(valid_matrix):
            raise AttributeError("All Columns must have the same number of elements")
    def __str__(self):
        return str(self.L)
    def __len__(self):
        return [self.m, self.n]
    def __add__(self, other):
        if type(other) is Matrix:
            if self.m != other.m or self.n != other.n:
                raise IndexError("Matricies Must Be Same Size")
            else:
                L = [[] for i in range(self.m)]
                for i in range(self.m):
                    for j in range(self.n):
                        L[i].append(self.L[i][j]+other.L[i][j])
                return_matrix = Matrix(L)
                return return_matrix
        else:
            raise TypeError("Matrix + NonMatrix")
    def __mul__(self, other):
        if type(other) is Vector:
            if self.n != other.n:
                raise IndexError("Matrix's n must match vector's n")
            else:
                L = []
                for i in range(self.m):
                    inc = 0
                    for j in range(self.n):
                        inc += self.L[i][j] * other.L[j]
                    L.append(inc)
                return_vect = Vector(L)
                return return_vect
        if type(other) is int or type(other) is float:
            L=[[] for i in range(self.m)]
            for i in range(self.m):
                for j in range(self.n):
                    L[i].append(self.L[i][j]*other)
            return_matrix = Matrix(L)
            return return_matrix
        if type(other) is Matrix:
            if self.n != other.m:
                raise IndexError("Matrix_1's n must equal Matrix_2's m")
            else:
                L = [[] for i in range(self.m)]
                for i in range(self.m):
                    for j in range(other.n):
                        inc = 0
                        for k in range(self.n):
                            inc += self.L[i][k] * other.L[k][j]
                        L[i].append(inc)
                return_matrix = Matrix(L)
                return return_matrix
        else:
            raise TypeError("Need Matrix * int, float, vector, or matrix")
    def __eq__(self, other):
        if type(other) is Matrix:
            if self.m != other.m or self.n != other.n:
                return False
            else:
                same = True
                for i in range(self.m):
                    for j in range(self.n):
                        if self.L[i][j] != other.L[i][j]:
                            same = False
                return same
        else:
            raise TypeError("Matrix == NonMatrix")
