def student(id,name,grade,*marks):
    '''
    print(f"ID : {id}")
    print(f"Name : {name}")
    print(f"Grade : {grade}")
    print(f"Marks : {marks}")
    '''
    print(f"Report Card for Stduent : {id}")
    print(f"Hello {name}")
    print(f"Your marks : {marks}")
    avg = sum(marks) / len(marks)
    print(f"Your average marks are {avg}")
    
id = input("Enter your id : ")
name = input("Enter your name : ")
grade = input("Enter your grade : ")
ph_marks = int(input("Enter your physics marks : "))
ch_marks = int(input("Enter your chemistry marks : "))
math_marks = int(input("Enter your maths marks : "))

student(id,name,grade,ph_marks,ch_marks,math_marks)
