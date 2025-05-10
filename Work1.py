# a={1,5,4,8,7,4,9}
# num=int(input("enter number"))
# k=len(a)
# for i in a



# b={}
# a=[1,1,1,5,5,3,3,1,4,4,4,2,2,2,2]
# for i in a:
#     if i in b:
#         b[i]=b[i]+1
#     else:
#         b[i]=1
# print(b)


# a = [1,1,1,2,2,3,3,5,5,4,4,4,6]
# count=1
# ele=2
# for i in range(1, count+1):
#    print("The element", ele, "occurs", count, "times.") 


# s=0
# b=int(input('enter element'))
# for b in a:
#     s=s+1
# print(s)


# a = [1,1,1,2,2,2,3,3,4,4,4,5,5]
# count=0
# k=len(a)
# b=int(input("enter element"))
# for i in range (k):
#     if a[i]==b:
#         count=count+1
# print("The element", b, "occurs", count, "times.")    



# a=[]
# num=int(input("enter the range"))
# for i in range(num):
#     b=int(input('enter number'))
#     a.append(b)
#     a.sort()
#     b=a[::-1]
    
# print(b[1])

# a=5
# b=3
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# a=5
# b=3
# a,b=b,a
# print(a,b)

# a='Nandana'
# b=a[1:5]
# print (b)


# a=[]
# b=input('enter add elements')
# c=int(input("enter a number"))
# for i in range(0,5):
#     a.append(6)
# print(a)

# x=int(input("Enter a number:"))
# sum=0
# for i in range(1,x):
#     if x%i==0:
#         sum=sum+i
# if sum>x:
#     print(x,"is abundant")
# elif sum==x:
#     print(x,"is perfect")
# elif sum<x:
#     print(x,"is deficient")


# 1   what is variables
# 2   data types
# 3   what is python
# 4   what is numeric data types
# 5   example of float
# 6   purpose of using pop in list
# 7   purpose of using append
# 8   what is String 
# 9   list represent with what
# 10  how to add element in a specific index position







# import matplotlib.pyplot as plt
# import numpy as np

# def hexagon(x_center, y_center, size):
#     """Create the vertices of a hexagon centered at (x_center, y_center) with a given size."""
#     angle_offset = np.pi / 6  # 30 degrees
#     return [
#         (
#             x_center + size * np.cos(angle_offset + 2 * np.pi * i / 6),
#             y_center + size * np.sin(angle_offset + 2 * np.pi * i / 6)
#         )
#         for i in range(6)
#     ]

# def plot_honeycomb(rows, cols, size):
#     """Plot a honeycomb pattern with a given number of rows, columns, and hexagon size."""
#     fig, ax = plt.subplots()

#     for row in range(rows):
#         for col in range(cols):
#             x = col * 3/2 * size
#             y = np.sqrt(3) * size * (row + 0.5 * (col % 2))  # Staggered rows
#             hexagon_points = hexagon(x, y, size)
#             hexagon_polygon = plt.Polygon(hexagon_points, edgecolor='black', facecolor='yellow', alpha=0.6)
#             ax.add_patch(hexagon_polygon)

#     ax.set_aspect('equal')
#     ax.autoscale_view()
#     plt.axis('off')  # Remove axis
#     plt.show()

# # Parameters
# rows = 10  # Number of rows of hexagons
# cols = 10  # Number of columns of hexagons
# size = 1.0  # Size of each hexagon

# # Generate the honeycomb pattern
# plot_honeycomb(rows, cols, size)


# import random

# random_number = random.randint(1, 101)
# print("The randomly picked number is:", random_number)

# a=input('enter character')
# for b in a:
#     if a.count(b) == 1:
#         print(b, end=" ")



# str1 = "Listen"
# str2 = "SiLeNt"

# # Remove spaces and convert to lowercase
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()

# # Check if sorted characters of both strings are equal
# if sorted(str1) == sorted(str2):
#     print(f'"{str1}" and "{str2}" are anagrams.')
# else:
#     print(f'"{str1}" and "{str2}" are not anagrams.')


# s = "abcabcbb"
# char_index_map = {}  # Dictionary to store the last index of each character
# left = 0  # Left pointer of the window
# max_length = 0  # Variable to store the length of the longest substring

# for right in range(len(s)):
#     # If character is already in the current window, move the left pointer
#     if s[right] in char_index_map and char_index_map[s[right]] >= left:
#         left = char_index_map[s[right]] + 1

#     # Update the last index of the current character
#     char_index_map[s[right]] = right

#     # Calculate the length of the current window
#     max_length = max(max_length, right - left + 1)

# print(max_length)  # Output: 3



# num=int(input("Enter the number to be multiplied: "))

# n=11
# for i in range(1,n):
#     res = i*num
#     print(i, "*",  num, "=", res, end="")
#     print()


# vehicle = []

# while True:
#     choice = int(input("1 for Add vehicle\n 2 for Display vehicle"))
#     if choice == 1:
#         no = int(input("Vehicle number: "))
#         name = input("Name: ")
#         price = int(input("Price: "))
#         wheels = int(input("No. of Wheels: "))
#         list1 = []
#         list1.append(no)
#         list1.append(name)
#         list1.append(price)
#         list1.append(wheels)
#         vehicle.append(list1)
#     if choice == 2:
#         num = int(input("Number of wheels"))

#         for i in vehicle:
#             if i[3] == num:
#                 print(i[0])
#                 print(i[1])
#                 print(i[2])
#                 print(i[3])


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


# numbers = [2, 8, 12, 4, 6]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest number:", largest)

# num = 785691
# sorted_num = int("".join(sorted(str(num), reverse=True)))
# print(sorted_num)


# s = "hello world"
# s = s.replace("o", "")
# print(s)
 
# Input: A number from the user
# num = input("Enter an integer: ")

# # Loop through digits from 0 to 9 and count occurrences
# for digit in "0123456789":
#     count = num.count(digit)
#     print(f"{digit}: {count}")

# num = input("Enter an integer: ")
# for digit in "0123456789":
#     count = num.count(digit)
#     if count > 0:  
#         print(f"{digit}: {count}")


# import random
# random_number = random.randint(1, 17)
# print("Random Number:", random_number)


# a="10000000"
# print(a)


# a=10
# b=20

# a, b = b, a
# print("a:", a)
# print("b:", b)  



class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  # Output: Generic animal sound
dog.speak()     # Output: Woof!
cat.speak()     # Output: Meow!