s = input('enter any string:')
res = {}
for i in s:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
for key, value in res.items():
    if value > 1:
        print(key, end=" ")
print(res)

