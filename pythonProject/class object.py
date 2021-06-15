class magesh:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a + self.b
        print(c)

    def subtraction(self):
        d = self.a - self.b
        print(d)


a = magesh(5, 6)

a.add()
a.subtraction()
