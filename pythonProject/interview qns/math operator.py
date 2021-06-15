def add(x, y):
    while y != 0:
        carry = x & y
        print(carry)
        x = x ^ y
        print(x)
        y = carry << 1
        print(y)
    print(x)
add(5, 4)