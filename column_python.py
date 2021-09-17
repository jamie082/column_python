#!/usr/bin/python3

# 0, 3, 5, 7, 9
# 2, 4, 6, 8, 10

print('\n')

num = int(input("Insert num: "))
print ('\n')

print("Column #1")
for x in range (0, num, 3): # have num multiple of 3 
    if num % 3 == 0:
        print("We're on time %d" % (x))

print ("\n")

for y in range (2, num, 2): # have num multiple of 2
    if num % 2 == 0:
        print ("We're on time %d" % (y))

    else:
        print("Error!\n")
        break
