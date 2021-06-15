class one:
    def display(self):
        print('c')


class two(one):
    def display(self):
        #super().display()

        print('d')


y = two()
y.display()
