# Prime Number
'''
num = 29

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")
'''

min_range = int(input("Enter min number : "))
max_range = int(input("Enter max number : "))

for num in range(min_range, max_range):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print("Prime Number",num)




        
