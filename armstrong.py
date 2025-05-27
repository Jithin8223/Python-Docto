a=int(input("enter number"))
b=0
n=a
while a>0:
    s=a%10
    s=s*s*s
    b=s+b
    a=a//10
if n==b:
    print('armstrong')
else:
    print('not')

# The above code is for checking whether a number is armstrong or not.