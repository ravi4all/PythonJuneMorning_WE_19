'''
for i in range(6):
    for j in range(6):
        print("{} + {} = {}".format(i,j,i+j))
'''

for i in range(6):
    for j in range(i):
        print('*', end='')
    print()

for i in range(6):
    for j in range(i):
        print(j+1, end='')
    print()

for i in range(6):
    for j in range(i):
        print(i, end='')
    print()


for i in range(10):
    for j in range(10 - i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()
