# //right angle triangle 

# n=int(input("enter the range"))
# for i in range(n):
#     for j in range(n-i):
#         print('j',end=" ")
#     print()

#// square

# n=int(input("enter the range: "))
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()

# // right triangle with number 


# n=int(input("enter the range "))
# for i  in range(n):
#     for j in range(i):
#         if j!=0:
#             print(j,end=" ")
#     print()

#// right triangle with same number , same number repeat

# n=int(input("enter the range "))
# for i in range(n+1):
#     if i!=0:
#         for j in range(i):
#             print(i,end=" ")     
#     print()


# // to print L shape


# n=int(input("enter the range"))
# for i in range(n):
#     for j in range(i):
#         if j==0 or i==n-1:
#             print("*",end=" ")
#     print()

# // to print square

# n=int(input("enter the range"))
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()
    

# n=int(input('enter the range'))
# for i in range(n):
#     for j in range (i+1):
#         print("*",end=" ")
#     print()



# a=int(input("enter range"))
# for i in range(a):
#     for j in range(a-i):
#         print("*",end=" ")
#     print()


# rows = 5



# a=int(input('enter the range'))
# for i in range(a, 0, -1):
#     print('*' * i)




# a=int(input('enter the number'))
# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()

# a = int(input('Enter the range: '))
# for i in range(1, a + 1):
#     spaces = ' ' * (a - i)
#     stars = '*' * (2 * i - 1)
#     print(spaces + stars)


# n = int(input("Enter the range: "))
# for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == 1 or i == n or j == 1 or j == n:  
#                 print(j, end=" ")  
#             else:
#                 print(" ", end=" ") 
#         print() 

# n = int(input("Enter the range: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print(j + 1, end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n=int(input("enter the range: "))
# for i in range(n):
#     print('*',end=" ")
# print()


# n = int(input("Enter the range: "))
# print(("* " * n + "\n") * n)


n = 7
for i in range(1, n + 1, 2):  
    spaces = (n - i) // 2
    print(" " * 4 * spaces, end="")  
    for j in range(1, i + 1):
        print(f"{j:<4}", end="")  
    print()



# import turtle as ben
# colors=['red']
# ben.speed(10)
# ben.pensize(5)


# for i in range(24):
#     ben.color(colors[i % len(colors)])
#     for j in range(4):
#         ben.forward(200)
#         ben.left(90)
#     ben.left(15)
# ben.done()
      