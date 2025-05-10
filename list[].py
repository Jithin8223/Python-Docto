# a=['jithin','Reshma','Vismaya','Riya',100,2.5,3j]
# a.append('Cyberpark')
# a.insert(1,'Cyberpark')
# a[1]='Cyberpark'
# a.pop(2)
# a.remove('jithin')
# print(a)

# print(a)
# print (a[::-1])
# print(a[1:5])

# a.insert(1,'meenakshi')


  
# a.remove('amal') 
# print(a)

# print(a.index('jinu')) 
# print(len(a))  
# # print(a) 

# a=4.5
# print(type(a))
# import random
# print(random.randint(1,25))

# a=[]
# for i in range(5):
#     c=input('enter data')
#     a.append(c)
# print(a)



# a=[]
# a.append('jithin')
# print(a)



# a=['jithin','sandeep',5,'anfas','jinu',10,'adarsh',2.5]
# # print(a)

# a.append('adwaith')                                 #to add          
# print(a)

# a[1] = 'jeevan'            # to change
# print(a)


# a.insert(1, 'adwaith')         #  add an element in to a specific index
# print(a)

# a.pop(3)                          # to delete element from last
# print(a)

# a.remove('jinu')             # to remove an element according to value
# print(a)

# print(a.index('jinu'))         # to get index (position)

# print(len(a))                   # to know the length



# a=['adarsh',25,'rizwan',22,.6,'jithin','jithin']
# a.append('jithin')
# a.insert(1,'jithin')
# a[1]='apple'
# print(a)
# a.pop()
# a.remove('adarsh')
# print(len(a))
# b=a.index('rizwan')
# print(a)


# a=['adarsh','riswan','jithin',25,62,'subuhan']
# a.append('jeevan')
# print(a)
# a.insert(2,'shebin')
# a[5]='python'
# a.pop()
# a.remove('jithin')
# print(a)
# print(len(a))
# b=a.index('jithin')
# print(b)  

# a=[]
# a.append('adarsh',100)
# print(a)

# a=['adarsh','riswan','jithin',25,62,'subuhan']
# print(a)

# a=('jithin')
# print(a[1:5])
# print(a[0:5:3])
# print(a[1])
# print(a[::-1])
# print(a[3::])
# print(a[3::-1])         #reverse

# print(a[1:5])         #slice

# dict={1:'veni',2:'neha',3:'priya'}
# print(dict)

# my_list = ['jithin', 'muhammed', 100, 'jithin', 'adarsh', 500]

# new_list = [item for item in my_list if item != 'jithin']
# print(new_list)


# n = []  # Initialize an empty list
# a = int(input('Enter the range: '))  # Prompt the user to enter the range

# for i in range(a):
#     k = input('Enter a string or number: ')  # Prompt the user to enter a string or number
#     try:
#         value = float(k) if '.' in k else int(k)
#     except ValueError:
#         # If conversion fails, keep the input as a string
#         value = k
#     n.append(value)  # Append the value to the list

# print(n)  # Print the final list

# n = []
# a = int(input('Enter the range: '))
# for i in range(a):
#     k = input('Enter the string or number: ')
#     n.append(int(k) if k.isnumeric() else k)
# print(n)




# n = []
# a = int(input('Enter the range: ')) 
# for i in range(a):
#     k = int(input('Enter a value: '))  
#     n.append(k)  
# print('Sum:', sum(n)) 
# print('List:', n)  



# a=[]
# n=input('enter the range')
# for i in range(3):
#     k=input('enter the value')
#     a.append(k)
# print(a)

# sum=0
# for i in (a):
#     sum=sum+i
# print('Your Total is ',sum)


n = []  
# a = input('Enter the range: ')

for i in range(3):
    k = input('Enter a string, number, or complex number: ')  
    try:
        
        if 'j' in k:
            value = complex(k)
        elif '.' in k:
            value = float(k)  
        else:
            value = int(k)  
    except ValueError:
        
        value = k
    n.append(value)  

print(n)

# my_list = [1, 2, 3]
# my_list.extend([4, 5]) 
# print(my_list)  

