
def registration():
    student = []
    fullName = str(input("Full name:"))
    regNo = str(input("Registration Number:"))
    email = str(input("E-mail:"))
    gender = str(input("Gender:"))
    department = str(input("Department:"))
    course = str(input("Course:"))

    print("Please confirm is these are your details")
    print(" Name: %s \n Registration Number: %s \n E-mail: %s \n Gender: %s "
          "\n Department: %s \n Course: %s" % (fullName, regNo, email, gender, department,
                                               course))

    answer = int(input("Are these details correct: \n 1.Yes \n 2.No \n Answer:"))


    print(student)






print('Welcome to our registration portal \n')

registration()

