#!/usr/bin/python3

# 0, 3, 5, 7, 9
# 2, 4, 6, 8, 10

digit_1 = 1 # #starting sequence
print('\n')

num = int(input("Insert num: "))
print ('\n')

digit_2 = 2  # starting sequence
print("Column #1")
for x in range (digit_1, num, 3): # have num multiple of 3 
    if num % 3 == 0:
        print("We're on time %d" % (x))

print ("\n")

print ('Column #2')
for y in range (digit_2, num, 2): # have num multiple of 2
    if num % 2 == 0:
        print ("We're on time %d" % (y))
