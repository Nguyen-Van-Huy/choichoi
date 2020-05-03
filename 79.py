class A:
    def __init__(self):
        self.a=1
        self.__b=1
    def getY(self):
        return self.__b
obj = A()
obj.a = 45
print(obj.a)
