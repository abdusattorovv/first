# Ex 1

# print("Exercise 1 - First Series")

# for i in range(10):
#     for j in range(10):
#         print("(", i, ",", j, ")", end=" ")
#     print()

# print("\nExercise 1 - Second Series")

# for i in range(10):
#     for j in range(10):
#         print(i * 10 + j, end=" ")
#     print()

# Ex 2



print("Figure 5:")
n= int(input("Input n: "))
for i in range(n):
    for j in range(n):
        if i==j or i==n-1-j:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# #Ex 3

# print("\nExercise 3")

# while True:
#     n = int(input("Input n: "))

#     if n <= 0:
#         break

#     print("*" * n)

# print("Execution terminated.")


# Ex 4

# print("\nExercise 4 - Floyd Triangle")

# n = int(input("Enter number of rows: "))

# number = 1

# for i in range(1, n + 1):
#     for j in range(i):
#         print(number, end=" ")
#         number = number + 1
#     print()


# print("\nPrint only first n numbers of Floyd Triangle")

# n = int(input("Enter how many numbers: "))

# number = 1
# row = 1

# while number <= n:
#     for i in range(row):
#         if number > n:
#             break
#         print(number, end=" ")
#         number = number + 1
#     print()
#     row = row + 1





# Ex 4.2
