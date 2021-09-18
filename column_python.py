#!/usr/bin/python3

# 0, 3, 5, 7, 9
# 2, 4, 6, 8, 10

digit_1 = 1 # #starting sequence
print('\n')

num = int(input("Lines of output: "))
print('\n')
    
mod_x = 3  # starting sequence
print("Modulus % 3 (3)")
for x in range (digit_1, 3): # have num multiple of 3 
    if num % 3 == 0:
        print("We're on time %d" % (x))

    else:
       # print("* ERROR %d" % (x))
       break

print ("\n")


# second column
p = 0
digit_2 = 2
print ('Modulus % 2 (2)')
print ("The factors of ", digit_2, "are: ")
for y in range (num): # line count numbers, first loop
    for p in range (digit_2, num, 10): # second loop
        if num % 2 == 0:
            print ("We're on time %d" % (p))

        else:
            print("Not a % of 2\n")

print ('\n')
print ('Column #3 (LIST NUMBER)')
for p in range (1, num, 1):
    print ("We're on time %d" % (p))
