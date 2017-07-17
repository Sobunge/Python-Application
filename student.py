import registration
import sqlite

student = registration.Register()
connecting = sqlite.connection()




#student.enterValues()

connecting.connect()

#introductory statements
print("##########################")
print("What do you want to do: \n1.Register \n2.Login")
student.tryAgain()
if student.answer == 1:
    student.registration()

    while student.answer == 2:
        print("What do you want to do next. \n1.Try Again \n2.Exit")
        student.tryAgain()
        if student.answer == 1:
            student.registration()
        else:
            exit('Goodbye ...............................')

    if student.answer == 1:
        connecting.insertValues(student.name, student.regNo, student.username, student.salt, student.hashed_password,
                                student.age, student.address)
    #    connecting.conn.commit()
else:
    student.login()
    connecting.authenticate(student.username,student.password)



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


