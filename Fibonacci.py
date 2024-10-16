n=int(input("enter number:"))
a=0
b=1
for i in range(n):
    temp=a+b
    a=b
    b=temp
    print(b)


# n = int(input("Enter the number of terms: "))

# a = 0
# b = 1

# if n < 1:
#   print("Please enter a positive integer.")
# elif n == 1:
#   print("Fibonacci series: 0")
# else:
#   print("Fibonacci series:")
#   for i in range(0, n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

# print(calc(20))

# a = [1, 7, 5, [9, 4, 2], 6, 3]
# b= a[3].index(4)
# print(b)


