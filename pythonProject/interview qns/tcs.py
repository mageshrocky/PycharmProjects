x = int(input("number of tasks:"))
y = int(input("no.of.tasks for one member for one day:"))
z = int(input("no.of.allocated days:"))

f = y*5
c = f*z

if c >= x:
    print("1")
else:
    print("0")

