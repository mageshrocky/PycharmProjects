import math
import datetime

print("selection process")
z = datetime.datetime.utcnow()
print(z)
list = ["magesh","rajesh","hari","nisar"]

for i in list:
    print(i)
    x = float(input("enter your percentage:"))
    y = math.isclose(x,100,abs_tol=15)
    if y:
        print(f"{i} is selected")
    else:
        print(f"{i} is not selected")