class magesh:
    def odd_even(self):
        if self.a % 2 == 0:
            print('even')
        else:
            print('odd')
class parthiban(magesh):
    def big_value(self):
        if self.a > self.b:
            print(f'{self.a} is the biggest value')
        else:
            print(f'{self.b} is the biggest value')

class praveen(parthiban):
    def sod(self):
        num = self.a
        result = 0
        for i in range(num):
            digit = num % 10
            result = result + digit
            num = num // 10
        print(result)
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a)

x = praveen(250,500)
x.odd_even()
x.big_value()
x.sod()