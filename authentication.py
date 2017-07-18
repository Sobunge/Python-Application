#import sqlite
import registration

#connecting = sqlite.connection()
#user = registration.Register()

#connecting.connect()

#connecting.createTable()

#connecting.createTableUnits()
#user.enterValues()
#connecting.insertUserValues(user.name,user.id,user.username,user.role,user.salt,
#                            user.hashed_password,user.age,user.address)

#connecting.conn.commit()
#user.login()
#connecting.authenticate(user.username,user.password)


#connecting.conn.close()

class Units:
    def registerUnits(self):
        self.unitName = str(input("Unit Name:"))
        self.uniCode = str(input("Unit Code:"))

    def enterMarks(self):
        Cat1 = int(input("Cat 1 marks:"))
        while Cat1>30 and Cat1<0:
            Cat1 = int(input("Cat 1 marks:"))
        self.Cat1 = (Cat1/30)*15
        Cat2 = int(input("Cat 2 marks:"))
        while Cat2>30 and Cat2<0:
            Cat2 = int(input("Cat 2 marks:"))
        self.Cat2 = (Cat2/30)*15
        mainExam = int(input("Main Exam marks:"))
        while mainExam>30 and mainExam<0:
            mainExam = int(input("Main Exam marks:"))
        self.mainExam = (mainExam/100)*70

        self.totalMarks = self.Cat1 + self.Cat2 + self.mainExam

        if self.totalMarks>=70:
            self.grade = 'A'
        elif self.totalMarks>=60 and self.totalMarks<70:
            self.grade = 'B'
        elif self.totalMarks>=50 and self.totalMarks<60:
            self.grade = 'C'
        elif self.totalMarks>=40 and self.totalMarks<50:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def displayMarks(self):
        print("Unit Name:",self.unitName)
        print("Unit Code:",self.uniCode)
        print("Cat 1:",self.Cat1)
        print("Cat 2:",self.Cat2)
        print("Main Exam:",self.mainExam)
        print("Total Marks:",self.totalMarks)
        print("Grade:",self.grade)


