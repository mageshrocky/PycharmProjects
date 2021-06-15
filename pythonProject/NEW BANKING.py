m = ['mango', 'grape', 'fig']
n = [20, 50, 35]
z = dict(zip(m, n))
print(z)
print(z['mango'])
print(m.index('mango'))
z['mango'] = 30
i = m.index('mango')
print(i)