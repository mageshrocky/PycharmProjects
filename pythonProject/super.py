from multipledispatch import dispatch


class one:
    @dispatch(int, str)
    def display(age, name):
        print(age)
        print(name)

    @dispatch(float)
    def display(salary):
        print(salary)
        print("salary")

    @dispatch(str)
    def display(name):
        print(name)
        print("name")


b = one
b.display(23, 'nisar')
b.display(10000.11)
b.display('mlk')