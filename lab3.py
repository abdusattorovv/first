# x = int(input("What's x? "))
# y = int(input("What's y? "))
# z = int(input("What's z? "))
# v = int(input("What's v? "))
# if x >= y and x >= z and x >= v:
#     largest = x
# elif y >= x and y >= z:
#     largest = y
# else:
#     largest = z
# print("The largest number is:", largest)


n = int(input("Enter how many numbers: "))

total = 0

for i in range(n):
    number = int(input("Enter a number: "))
    total = total + number

average = total / n

print("Average:", average)

