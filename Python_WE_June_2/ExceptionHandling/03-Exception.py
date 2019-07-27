try:
    file = open('file_1.txt',"w")
    data = "hello this is exception handling"
    file.write(data)
    # d = file.read()
    # print(d)
except BaseException as ex:
    print(ex)
finally:
    print("I will always execute")
    file.close()