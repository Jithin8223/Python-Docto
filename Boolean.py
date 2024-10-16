# a = ('jithin','amal','abhi')
# for i in range(a):
#     if a:
#         print('subuhan is true')
# else:
#     print(' is false')
# b = False

# if a:
#     print('subuhan is true')
# else:
#     print(' is false')

a=('adarsh','jithin','veni','neha','shabeer')
b=input('enter the name')
if b in a:
    print('true')
else:
    print('false')

# b=True
# print(type(b))


import turtle as ben

ben.speed(10)
ben.color("violet")
ben.pensize(5)

for i in range(24):
    for j in range(3):
        ben.forward(200)
        ben.left(90)
        ben.left(15)
ben.done()