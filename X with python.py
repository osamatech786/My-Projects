'''
Drawing 'X' by using loops in python
8/3/20
'''
print()
a = 1
b = 10


# loop for half X
while(a <= 6):
    print(' '*a, 'XxxX', ' '*b, 'XxxX')
    a = a+1
    b = b-2
print(a*' ', 'XXxxxxXX')

# reversing the whole process for half X
x = 6
y = 0

while(x >= 1):
    print(' '*x, 'XxxX', ' '*y, 'XxxX')
    x = x-1
    y = y+2
