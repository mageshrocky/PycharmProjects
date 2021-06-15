
try:
    f = open('sample1.txt','x')
    f.close()
    print('success')
except Exception as e:
    print(e)