with open('img_1.jpg','rb') as file:
    data = file.read()
    x = [3,3,5,5]
    # print(data)

with open('img_2.jpg','wb') as file:
    file.write(data)
    x[0] = 100
    print(x)