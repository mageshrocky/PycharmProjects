'''for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while (i != 0):
        digit = i % 10
        result = result + digit ** n
        i = i // 10
    if num == result:
        print(num)'''

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibo(n-1) + fibo(n-2)
n = int(input("enter the number:"))
for i in range(1, n+1):
    print(fibo(i))