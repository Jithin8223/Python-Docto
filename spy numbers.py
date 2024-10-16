num=int(input("enter the number"))
sum=0
pro=1
while num>0:
    b=num%10
    sum=sum+b
    pro=pro*b
    num=num//10
if(sum==pro):

    print('Spy Number')
else:
    print('Not')

