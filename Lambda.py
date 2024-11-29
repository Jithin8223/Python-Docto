# f=lambda a: a*a

# a=lambda x,y: x*y
# print(a(2,3))

# a=[1,2,3,4,5,6,7,8,9,10]        #to find even numbers
# b=filter(lambda x: x%2==0,a)
# print(list(b))

# for i in range(31):
#     if i%2==0:
#         print(i)


# a=[1,2,3,4,5,6,7,8,9,10]        #to find odd numbers
# b=filter(lambda x: x%2==1,a)
# print(list(b))

a=[1,2,3,4,5]
b=map(lambda x: x**3,a)
print(list(b))


# from functools import reduce
# numbers = [1,2,3,4,5]
# product = reduce(lambda x,y: x*y, numbers)
# print(product)



# f= lambda a: a*a