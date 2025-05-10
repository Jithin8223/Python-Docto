# a=('shithin','raseena','rafi','jouhara','jithin')
# b=input('enter your name')
# if b in a: 
#     print('True')
# else:
#     print('False')


# a=int(input('enter your age'))
# if a>18:
#     print('adult')
# elif a>15:
#     print('young')
# elif a>10:
#     print('boy')
# else:
#     print('not eligible')


# a=int(input('enter your age'))
# if a>25:
#     print('young')
# else:
#     print('not eligible')

    
# a=input('enter name')
# print('hello',a,'welcome')


# a=int(input('enter number'))
# if a>25:
#     print('young')
# elif a>18:
#     print('adult')
# else:
#     print('not eligible')


# a=int(input('enter number'))
# if a>40:
#     print('pass')     
# else:
#     print('fail')
    
# a='sachin'
# print(a[::-1])

# a = input('enter name')
# b = input('enter name')
# c = a+ ' ' +b
# print(c)

# a = 'hjh '

# b = ' jkhk'

# c=a+b
# print(c)



# a=input('enter student name')
# m=int(input('marks in maths'))
# c=int(input('marks in chemistry'))
# p=int(input('marks in physics'))
# f=m+c+p
# if f>290:
#     print('A+')
# elif f>270:
#     print('A')
# elif f>260:
#     print('B+')
# elif f>240:
#     print('B')
# elif f>220:
#     print('C+')
# elif f>200:
#     print('c')                
# else:
#     print('failed')    

# a=input('enter username')
# b=int(input('enter password'))
# if a=='swetha2000'and b==1234:
#     print('welcome')
# else:
#     print('access denied')

# a=input('enter you name')
# b=int(input('enter your reg'))
# c=int(input('english'))
# d=int(input('malayalam'))
# e=int(input('biology'))
# f=c+d+e
# if f>90:
#         print ('A+')
# elif f>280:
#         print ('A') 
# elif f>260:
#         print ('B+')
# elif f>240:
#         print ('B')
# elif f>220:
#         print('c+') 
# elif f>160:
#         print('D') 
# else :
#      print ('failed')  


# a=input('Enter Username')
# b=int(input('Enter Passsword'))

# if a=='adarsh' or b==123:
#     print('welcome')
# else:
#     print('sorry')



# a=int(input('enter the age of rasheed'))
# if a>18:
#     print('welcome rasheed')
# else:
#     print('pattillaa rasheed')



# Number of students
# num_students = 3

# # Collecting details for each student and printing results
# for i in range(num_students):
#     name = input('Enter name: ')
#     math = int(input('Marks in Maths: '))
#     chemistry = int(input('Marks in Chemistry: '))
#     physics = int(input('Marks in Physics: '))

#     f = math + chemistry + physics

#     if f> 290:
#         grade = 'A+'
#     elif f > 270:
#         grade = 'A'
#     elif f > 260:
#         grade = 'B+'
#     elif f > 240:
#         grade = 'B'
#     elif f > 220:
#         grade = 'C+'
#     elif f > 200:
#         grade = 'C'
#     else:
#         grade = 'Failed'

#     print(f'{name} has scored {f} marks and has received grade {grade}.')


# dig = int(input('Enter the range: '))
# for i in range(dig):
#     name = input('Enter name: ')
    
#     while True:
#         math = int(input('Marks in Maths: '))
#         chemistry = int(input('Marks in Chemistry: '))
#         physics = int(input('Marks in Physics: '))
        
#         f = math + chemistry + physics
        
#         if f <= 300:
#             break 
#         else:
#             print("Error: Total marks cannot exceed 300. Please re-enter the marks.")
    
#     if f > 290:
#         grade = 'A+'
#     elif f > 270:
#         grade = 'A'
#     elif f > 260:
#         grade = 'B+'
#     elif f > 240:
#         grade = 'B'
#     elif f > 220:
#         grade = 'C+'
#     elif f > 200:
#         grade = 'C'
#     else:
#         grade = 'Failed'

#     print(f'{name} has scored {f} marks and has received grade {grade}.')

    



for i in range(1):
    name = input('Enter name: ')
    math = int(input('Marks in Maths: '))
    chemistry = int(input('Marks in Chemistry: '))
    physics = int(input('Marks in Physics: '))
    
    f = math + chemistry + physics
    
    if f > 300:
        print("Error: Total marks cannot exceed 300. Please re-enter the marks.")
        continue
    
    if f > 290:
        grade = 'A+'
    elif f > 270:
        grade = 'A'
    elif f > 260:
        grade = 'B+'
    elif f > 240:
        grade = 'B'
    elif f > 220:
        grade = 'C+'
    elif f > 200:
        grade = 'C'
    else:
        grade = 'Failed'

    print(f'{name} has scored {f} marks and has received grade {grade}.')
