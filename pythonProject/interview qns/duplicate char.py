# to find duplicate char in string
# method 1
str = 'this is string'
dup = []
d = []
for i in str:

    if i not in dup:
        dup.append(i)
    else:
        d.append(i)
print(dup)
print(set(d))

#method 2
l = 'aaaaabbbbcccddddee'
d = []
for i in l:
    if i not in d:
        d.append(i)
d =''.join(d)
print(d)

# method 3
m = 'aaabbbcccddd'
s1 = (set(m))
print(s1)
output = ''.join(s1)
print(output)

l = ["", "magesh", "", "rocky"]

t = [i for i in l if i]
print(t)

def remove(string):
    return string.replace(" ", "")
print(remove("hello world"))