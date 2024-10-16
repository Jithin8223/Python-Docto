
# start = 1
# end = 5
# prime=[]
# for i in range(start,end+1):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         prime.append(i)
# print(prime)


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# for num in range(500,5001):
#     if is_prime(num):
#         print(num)


# start = 500
# end = 5001
# prime = []
# for i in range(start, end + 1):
#     is_prime = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime.append(i)
# print(prime)


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


