class Matrix:

    matrix_id = 0

    def __init__(self, arg = [[0]]):
        self.__id = Matrix.matrix_id
        Matrix.matrix_id +=1
        self.raw = []
        self.raws = len(arg)
        self.cols = len(arg[0])
        for i in range(self.raws):
            self.raw.append(arg[i])
        self.dimentions = str(self.raws) + 'X' + str(self.cols)

    def get_id (self):
        return self.__id

    def descibtion (self):
        if (self.raws == 1 and self.cols == 1):
            return str(self.raw)[1:-1]
        else:
            self.temp='['
            for x in self.raw:
                self.temp += str(x)
                self.temp += '\n'
            self.desc = self.temp[:-1]
            self.desc += ']'
            return self.desc


a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
#a = Matrix()
print(a.raws)
print(a.cols)
print(a.dimentions)
print(a.get_id())
print(a.descibtion())
