print('GRADE CARD 2024')
a=input('enter name of student')
b=int(input('enter the mark of Chem '))
c=int(input('enter the mark of Phy '))
d=int(input('enter the mark of Bio '))
total=b+c+d
if total>290:
    print(' Congralutaions you got A+')
elif total>280:
    print(' You got A grade excellent')
elif total>270:
    print(' you got B+ very good')
elif total>260:
    print(' you got good B grade')
elif total>250:
    print(' mm not bad C+')
elif total>240:
    print(' average C grade')
else:
    print(' oops fail')
m=b+c+d
print(m)
