# a=('jithin','adarsh','rajesh','abhishek')
# print(a[2])
# print(a[1:3])
# print(a[-1])
# print(a[::-1])
# print(a[0:3 ])

a='adarsh'
b='jithin'
d=print(a[0:2]+b[2::])
c=(b[0:2] + a[2::])
# print(c)
# print(d)
# print(a)
# print(type(a))


a=[]
b=int(input("enter the range"))          
for i in range(b):
    c=int(input("enter the number"))
    a.append(c)                                             #print(a[::-1]) - descending order
    a.sort(reverse = False)                                #sort only used in ascending order 
print(a)         


                                                             #sort(reverse = True) - to get descending order
# def fun3(a,b):
#     c=a*b
#     print(c)
# fun3(4,3)



# a=[]
# b=int(input("enter the size "))          
# for i in range(b):
#     c=int(input("enter the number "))
#     a.append(c)
# print(a)



