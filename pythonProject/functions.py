input_1 = int(input('enter the value of input_1:'))
input_2 = int(input('enter the value of input_2:'))

def addition_operation():
    c = input_1 + input_2
    print(f'the sum of value is {c}')

def subtraction_operation():
    addition_operation()
    floor_division()
    d = input_1 - input_2
    print(f'the result is {d}')

def division_operation():
    div = input_1/input_2
    print(f'the division result is {div}')

def floor_division():
    f_d = input_1//input_2
    print(f'the result of f.d is {f_d}')

x =lambda a,b: a*b
print(x(a=10,b=20) )

def myfunc(n):
    return lambda a: a*n
 
if __name__ == '__main__':
    subtraction_operation()
    division_operation()
    myfunc(10)