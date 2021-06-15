marks = []

for i in range(5):
    mark = float(input('enter the mark:'))
    marks.append(mark)
print(marks)

print('total marks:', sum(marks))

print('highest mark:', max(marks))

print('lowest mark:', min(marks))

print('average mark:', sum(marks)/len(marks))

print('percentage:', (sum(marks)/500)*100)