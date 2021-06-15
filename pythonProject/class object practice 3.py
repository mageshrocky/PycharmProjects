class one:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a + self.b
        print(c)

    def sub(self):
        d = self.a - self.b
        print(d)


class two(one):
    def mult(self):
        x = self.a * self.b
        print(x)

    def div(self):
        y = self.a / self.b
        print(y)


class three(two):
    def modulo(self):
        j = self.a % self.b
        print(j)

    def odd_even(self):
        if self.a % 2 == 0:
            print('even')
        else:
            print('odd')


m = three(10, 20)
m.add()
m.sub()
m.mult()
m.div()
m.modulo()
m.odd_even()
