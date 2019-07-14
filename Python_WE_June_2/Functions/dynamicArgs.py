def add(*x):
    #print(x)
    s = 0
    for i in range(len(x)):
        s += x[i]
    print(s)
    

add(4,5)
add(4,5,6)
add(6,5,3,2,4,6)
add(23,45,4,78,5,12,56,6)
