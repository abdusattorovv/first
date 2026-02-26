# # Ex 1

# print("Exercise 1")

# N = 10
# v = []

# for i in range(N):
#     num = int(input("Enter number: "))
#     v.append(num)

# print("Odd numbers:")
# for i in range(N):
#     if v[i] % 2 != 0:
#         print(v[i], end=" ")

# print("\nEven numbers:")
# for i in range(N):
#     if v[i] % 2 == 0:
#         print(v[i], end=" ")

# print("\n")

# # Ex 2

# print("Exercise 2")

# n = int(input("Enter n: "))
# v = []

# for i in range(n):
#     num = int(input("Enter number: "))
#     v.append(num)

# answer = 1

# while answer == 1:
#     x = int(input("Enter x: "))
#     count = 0

#     for i in range(n):
#         if v[i] == x:
#             count = count + 1

#     print("Value appears", count, "times")

#     answer = int(input("Continue? (1=yes, 0=no): "))

# print("End of exercise 2\n")


# Ex 3

# print("Exercise 3")

# v = []
# w = []

# for i in range(10):
#     num = int(input("Enter v number: "))
#     v.append(num)

# for i in range(10):
#     num = int(input("Enter w number: "))
#     w.append(num)

# max_diff = 0
# pos = 0

# for i in range(10):
#     diff = abs(v[i] - w[i])

#     if diff > max_diff:
#         max_diff = diff
#         pos = i

# print("Max difference:", max_diff)
# print("Position:", pos)
# print()


# #Ex 2

# print("Exercise 4")

N = 5
base = []
exp = []
power = []

for i in range(N):
    num = int(input("Enter base: "))
    base.append(num)

for i in range(N):
    num = int(input("Enter exponent: "))
    exp.append(num)

for i in range(N):
    result = 1

    for j in range(exp[i]):
        result = result * base[i]
        power.append(result)

for i in range(N):
    print(power[i], end=" ")




# # Ex 5

# print("Exercise 5")

# DIM = 11
# v = []

# for i in range(DIM):
#     num = float(input("Enter number: "))
#     v.append(num)

# max_len = 0
# cur_len = 0
# start = 0
# temp = 0

# for i in range(DIM):
#     if v[i] > 0:
#         if cur_len == 0:
#             temp = i
#         cur_len = cur_len + 1

#         if cur_len > max_len:
#             max_len = cur_len
#             start = temp
#     else:
#         cur_len = 0

# print("Longest sequence length:", max_len)
# print("Starts at index:", start)

# print("\nProgram finished.")




# n = int(input("Input list length"))
# v = []
# for i in range(n):
#     number = int(input(f"input {i}: "))
#     v.append(number)
# print(v)





# Ex 3
# step 1 10
# v = []
# w = []

# for i in range(10):
#     num = int(input(f"w[{i}]="))
#     w.append(num)

# for i in range(10):
#     num = int(input(f"v[{i}]="))
#     v.append(num)

# # step 2 absolute value
# d =[]

# for i in range(10):
#     d.append(abs(v[i]-w[i]))
# print("d[] =",d)

# # step 3 max and min value
# print(f"max ={max(d)}")




# Ex 4
# N = 5
# base = []
# exp = []
# power = []

# for i in range(N):
#     num =int(input("base:"))
#     base.append(num)

# for i in range(N):
#     num = int(input("exponent:"))
#     exp.append(num)



























# v = []
# w = []

# for i in range(10):
#     num = int(input("Enter v number: "))
#     v.append(num)

# for i in range(10):
#     num = int(input("Enter w number: "))
#     w.append(num)

# max_diff = 0
# pos = 0

# for i in range(10):
#     diff = abs(v[i] - w[i])

#     if diff > max_diff:
#         max_diff = diff
#         pos = i

# print("Max difference:", max_diff)
# print("Position:", pos)
# print()








# 1st way 
# fruitlist = ["apple","banana","kiwi"]
# # print(fruitlist)
# print(fruitlist[0:2])

# # 2nd way
# fruitlist2 = list(("banana", "apple","kiwi"))
# print(fruitlist2)









# List 
# Tuple 
# Set 
# Dictionary





# Summary:
# 1.print() - print a variable to the console
# 2.len() - find the length of a variable
# 3.type() - find the type of a variable



# append() - add an element to the end of a list
# insert() - add an element at a specific position in a list
# remove() - remove the first occurrence of an element from a list (by element)
# pop() - remove and return an element at a specific position in a list (by index)
# delete() - remove an element at a specific position in a list (by index)
# clear() - remove all elements from a list
# index() - find the index of the first occurrence of an element in a list



