import registration
import sqlite

user = registration.Register()
connecting = sqlite.connection()




#student.enterValues()

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
        connecting.insertUserValues(user.name, user.id, user.username, user.salt, user.hashed_password,
                                user.age, user.address)
    #    connecting.conn.commit()
else:
    user.login()
    connecting.authenticate(user.username,user.password)



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


