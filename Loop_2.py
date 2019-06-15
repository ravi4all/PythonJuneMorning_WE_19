'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
'''
n = int(input("Enter the number : "))
for i in range(1,11):
    print('{} * {} = {}'.format(n,i,i*n))
