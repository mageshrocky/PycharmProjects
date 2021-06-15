import math
dic = {"magesh": 75, "nisar": 95, "praveen": 90, "raj": 98}

z = dic.values()
n = dic.keys()
for i in n:
    m = dic[i]
    #x = float(input("enter your percentage:"))
    if m >= 90:
        print(f"{i} is selected")
    else:
        print(f"{i} is not selected")

