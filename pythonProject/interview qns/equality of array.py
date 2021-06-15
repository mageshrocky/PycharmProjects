l1 = [10, 20, 30, 40, 50]
l2 = [20, 50, 30, 40, 70]
z1 = []
z2 = []
count1 = 0
count2 = 0
for i in range(0, len(l1)):
    if l1[i] == l2[i]:
        z1.append(l1[i])
        count1 += 1
        print('true')
    else:
        z2.append(l1[i])
        count2 += 1
        print('false')
d = {'equal': z1, 'not equal': z2}
print(d)
print(f'no.of.equal.elements: {count1}')
print(f'no.of.non equal.elements: {count2}')
