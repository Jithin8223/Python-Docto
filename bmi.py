a=int(input('enter weight'))
b=int(input('enter height'))
c=(a/b*b)
print(c)
if c<=18:
    print('under weight')
elif c<=25:
    print('normal weight')
elif c<=30:
    print('over weight')
else:
    print('you are in danger')            