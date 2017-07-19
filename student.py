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
        connecting.insertUserValues(user.name, user.id, user.username, user.role, user.salt, user.hashed_password,
                                    user.age, user.address)
    #    connecting.conn.commit()

    print("What do you want to do next ? \n 1.Login \n 2.Exit")
    user.tryAgain()
    if user.answer == 1:
        user.login()
        connecting.authenticate(user.username, user.password)
    elif user.answer == 2:
        exit('Goodbye.................................')

else:
    user.login()
    connecting.authenticate(user.username,user.password)



if connecting.role == 'Student':
    print("What do you want to do next \n 1.Register Units \n 2.View marks")
    user.tryAgain()
    if user.answer == 1:
        print("Which period would you want to register its units \n 1.Year 1 semester 1 \n 2.Year 1 Semester 2\
                                                        \n 3.Year 2 Semester 1 \n 4.Year 2 Semester 2 \
                                                        \n 5.Year 3 Semester 1 \n 6.Year 3 Semester 2 \
                                                        \n 7.Year 4 Semester 1 \n 8.Year 4 Semester 2")
        user.tryAgainAgain()
        if user.answer == 1:
            print("######### Year 1 Semester 1 #########")
        elif user.answer == 2:
            print("######### Year 1 Semester 2 #########")
        elif user.answer == 3:
            print("######### Year 2 Semester 1 #########")
        elif user.answer == 4:
            print("######### Year 2 Semester 2 #########")
        elif user.answer == 5:
            print("######### Year 3 Semester 1 #########")
        elif user.answer == 6:
            print("######### Year 3 Semester 2 #########")
        elif user.answer == 7:
            print("######### Year 4 Semester 1 #########")
        elif user.answer == 8:
            print("######### Year 4 Semester 2 #########")

    if user.answer == 2:
        print("Which examination do you want to view \n 1.Year 1 semester 1 \n 2.Year 1 Semester 2\
                                                 \n 3.Year 2 Semester 1 \n 4.Year 2 Semester 2 \
                                                 \n 5.Year 3 Semester 1 \n 6.Year 3 Semester 2 \
                                                 \n 7.Year 4 Semester 1 \n 8.Year 4 Semester 2")
        user.tryAgainAgain()

        if user.answer == 1:
            print("######### Year 1 Semester 1 #########")
        elif user.answer == 2:
            print("######### Year 1 Semester 2 #########")
        elif user.answer == 3:
            print("######### Year 2 Semester 1 #########")
        elif user.answer == 4:
            print("######### Year 2 Semester 2 #########")
        elif user.answer == 5:
            print("######### Year 3 Semester 1 #########")
        elif user.answer == 6:
            print("######### Year 3 Semester 2 #########")
        elif user.answer == 7:
            print("######### Year 4 Semester 1 #########")
        elif user.answer == 8:
            print("######### Year 4 Semester 2 #########")

elif connecting.role == 'Lecture':
    print("Which examination do you want to Enter \n 1.Year 1 semester 1 \n 2.Year 1 Semester 2\
                                                     \n 3.Year 2 Semester 1 \n 4.Year 2 Semester 2 \
                                                     \n 5.Year 3 Semester 1 \n 6.Year 3 Semester 2 \
                                                     \n 7.Year 4 Semester 1 \n 8.Year 4 Semester 2")
    user.tryAgainAgain()

    if user.answer == 1:
        print("######### Year 1 Semester 1 #########")
    elif user.answer == 2:
        print("######### Year 1 Semester 2 #########")
    elif user.answer == 3:
        print("######### Year 2 Semester 1 #########")
    elif user.answer == 4:
        print("######### Year 2 Semester 2 #########")
    elif user.answer == 5:
        print("######### Year 3 Semester 1 #########")
    elif user.answer == 6:
        print("######### Year 3 Semester 2 #########")
    elif user.answer == 7:
        print("######### Year 4 Semester 1 #########")
    elif user.answer == 8:
        print("######### Year 4 Semester 2 #########")


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


