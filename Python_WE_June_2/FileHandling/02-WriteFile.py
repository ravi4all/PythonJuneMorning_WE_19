text = ["ram122@gmail.com","123ram@gmail.com",
        "#ram11@gmail.com","ram$21@gmail.com",
        "ram@gmail,com",]

# file = open('data.txt', 'w')
# for data in text:
#     file.write(data+'\n')
#
# file.close()
#
# file = open('data.txt', 'a')
# id = "ramesh12@gmail.com"
# file.write(id)
# file.close()
id = "12ramesh@gmail.com"
with open('data.txt', 'a') as file:
    file.write(id)
