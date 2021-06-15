# checking the string is palindrome or not
'''string = "madam"
rev_string = string[::-1]
if string == rev_string:
    print("palindrome")
else:
    print("non palindrome")

# checking the number is palindrome or not

num = int(input("enter the number:"))
string = str(num)
rev_string = string[::-1]
if string == rev_string:
    print("palindrome")
else:
    print("non palindrome")'''

# alternate method

n = int(input("enter the number:"))
temp = n
sum = 0

while n>0:
    sum = n % 10 + sum*10
    n = n // 10

if sum == temp:
    print("palindrome")
else:
    print("not a palindrome")

