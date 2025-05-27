# print('GRADE CARD 2024')
# a=input('enter name of student')
# b=int(input('enter the mark of Chem '))
# c=int(input('enter the mark of Phy '))
# d=int(input('enter the mark of Bio '))
# total=b+c+d
# if total>290:
#     print(' Congralutaions you got A+')
# elif total>280:
#     print(' You got A grade excellent')
# elif total>270:
#     print(' you got B+ very good')
# elif total>260:
#     print(' you got good B grade')
# elif total>250:
#     print(' mm not bad C+')
# elif total>240:
#     print(' average C grade')
# else:
#     print(' oops fail')
# m=b+c+d
# print(m)

print('GRADE CARD 2024')

a = input('Enter name of student: ')

while True:
    b = int(input('Enter the marks of Chemistry: '))
    c = int(input('Enter the marks of Physics: '))
    d = int(input('Enter the marks of Biology: '))
    
    total = b + c + d
    
    if not total <= 300:
        print("Total marks exceed 300! Please re-enter the marks.\n")
    else:
        break


if total > 290:
    print('Congratulations! You got A+')
elif total > 280:
    print('You got A grade! Excellent!')
elif total > 270:
    print('You got B+! Very good!')
elif total > 260:
    print('You got B grade! Good!')
elif total > 250:
    print('C+! Not bad!')
elif total > 240:
    print('C grade! Average performance!')
else:
    print('Oops! You failed.')

print(f'Total Marks = {total}')



