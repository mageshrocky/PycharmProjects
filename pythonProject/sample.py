class A:
    def display(self,a,b):
        c = a+b
        print(c)
class B(A):
    def play(self,a,b):
        super().display()
        d = a+b
        print(d)
z = B()
z.play(5,6)

