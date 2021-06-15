def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

print(fact(4))

def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact
print(factorial(4))