n = (input("enter the binary number:"))
for i in n:
    if i in ("0", "1"):
        print("true")
    else:
        print("false")

def bin(num):
    p = set(num)
    print(p)
    s = {"0", "1"}
    if s == p or p == {"0"} or p == {"1"}:
        print("yes")
    else:
        print("no")
num = (input("enter the binary number:"))
bin(num)