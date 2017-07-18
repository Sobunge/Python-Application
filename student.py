import registration
import sqlite

user = registration.Register()
connecting = sqlite.connection()


connecting.connect()

#introductory statements
print("##########################")
print("What do you want to do: \n1.Register \n2.Login")
user.tryAgain()
if user.answer == 1:
    user.registration()

    while user.answer == 2:
        print("What do you want to do next. \n1.Try Again \n2.Exit")
        user.tryAgain()
        if user.answer == 1:
            user.registration()
        else:
            exit('Goodbye ...............................')

    if user.answer == 1:
        connecting.insertUserValues(user.name,user.id,user.username,user.role,user.salt,user.hashed_password,
                                    user.age,user.address)
    #    connecting.conn.commit()
else:
    user.login()
    connecting.authenticate(user.username,user.password)

print("Enter your Role \n 1.Student \n 2.Lecture")

role = int(input("Answer:"))

if connecting.role == 1:
    print("Which examination do you want to view \n 1.Year 1 semester 1 \n 2.Year 1 Semester 2\
                                                 \n 3.Year 2 Semester 1 \n 4.Year 2 Semester 2 \
                                                 \n 5.Year 3 Semester 1 \n 6.Year 3 Semester 2 \
                                                 \n 7.Year 4 Semester 1 \n 8.Year 4 Semester 2")
    answer = int(input("Answer:"))

    if answer == 1:
        print("######### Year 1 Semester 1 #########")
    elif answer == 2:
        print("######### Year 1 Semester 2 #########")
    elif answer == 3:
        print("######### Year 2 Semester 1 #########")
    elif answer == 4:
        print("######### Year 2 Semester 2 #########")
    elif answer == 5:
        print("######### Year 3 Semester 1 #########")
    elif answer == 6:
        print("######### Year 3 Semester 2 #########")
    elif answer == 7:
        print("######### Year 4 Semester 1 #########")
    elif answer == 8:
        print("######### Year 1 Semester 1 #########")
    else:
        print("You entered an invalid reponse")

elif connecting.role == 2:

        print("Which examination do you want to Enter \n 1.Year 1 semester 1 \n 2.Year 1 Semester 2\
                                                     \n 3.Year 2 Semester 1 \n 4.Year 2 Semester 2 \
                                                     \n 5.Year 3 Semester 1 \n 6.Year 3 Semester 2 \
                                                     \n 7.Year 4 Semester 1 \n 8.Year 4 Semester 2")
        answer = int(input("Answer:"))

        if answer == 1:
            print("######### Year 1 Semester 1 #########")
        elif answer == 2:
            print("######### Year 1 Semester 2 #########")
        elif answer == 3:
            print("######### Year 2 Semester 1 #########")
        elif answer == 4:
            print("######### Year 2 Semester 2 #########")
        elif answer == 5:
            print("######### Year 3 Semester 1 #########")
        elif answer == 6:
            print("######### Year 3 Semester 2 #########")
        elif answer == 7:
            print("######### Year 4 Semester 1 #########")
        elif answer == 8:
            print("######### Year 1 Semester 1 #########")
        else:
            print("You entered an invalid reponse")




        #connecting.insertValues(student.name, student.regNo, student.username, student.salt, student.hashed_password,
         #                       student.age, student.address)
        #connecting.conn.commit()
            #student.login()
            #connecting.authenticate(student.username, student.password)

            #student.registration()
               # connecting.insertValues(student.name, student.regNo, student.username, student.salt,
                #                        student.hashed_password,
                 #                       student.age, student.address)
                #connecting.conn.commit()
                 #   student.login()
                #    connecting.authenticate(student.username, student.password)
    #student.login()
    #connecting.authenticate(student.username,student.password)

#creating a table

#connecting.createTable()


#connecting.displayValues()

connecting.conn.close()


