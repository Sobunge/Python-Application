import sqlite3
import hashlib, uuid

class connection:

    def connect(self):
        self.conn = sqlite3.connect("student.db")
        print("Connection successful")

    def createTable(self):
        self.conn.execute( ''' CREATE TABLE USERS(
                    NAME char(100) NOT NULL,
                    ID CHAR(12) NOT NULL,
                    USERNAME CHAR(100) NOT NULL,
                    ROLE CHAR(8) NOT NULL,
                    SALT TEXT NOT NULL,
                    PASSWORD CHAR(100) NOT NULL,
                    AGE INT NOT NULL,
                    ADDRESS TEXT
        );''')


    def createTableUnits(self):
        self.conn.execute(''' CREATE TABLE UNITS(
                           NAME char(100) NOT NULL,
                           UNITCODE CHAR(8) PRIMARY KEY NOT NULL,
                           YEAR INT NOT NULL,
                           SEMESTER INT NOT NULL,
                           CAT1 INT NOT NULL,
                           CAT2 INT NOT NULL,
                           MAINEXAM INT NOT NULL,
                           TOTALMARKS INT NOT NULL,
                           GRADE CHAR(2) NOT NULL

           );''')

    def insertUserValues(self,name,id,username,role,salt,password,age,address):
        self.conn.execute('INSERT INTO USERS(NAME,ID,USERNAME,ROLE,SALT,PASSWORD,AGE,ADDRESS) \
                          values("%s","%s","%s","%s","%s","%s","%d","%s")' %\
                          (name,id,username,role,salt,password,age,address))
        print("Registration is successful")

    def registerUnits(self,name,unitCode,year,semester):
        self.conn.execute(''' INSER INTO USERS(NAME,UNITCODE,YEAR,SEMESTER)\
                           values("%s","%s","%d","%d")''' %\
                          (name,unitCode,year,semester))
        print("Registration is successful")

    def authenticate(self,uname,pword):
        self.cursor = self.conn.execute("SELECT NAME,USERNAME,ROLE,SALT,PASSWORD from USERS")
        for row in self.cursor:
            name = row[0]
            username = row[1]
            self.role = row[2]
            salt = row[3]
            psword = row[4]

            password = hashlib.sha512(pword.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            if username == uname and password == psword:
                print("######### Success #########")
                print('welcome',name)
                print('Role',self.role)
                break
            elif username != uname and password != psword:
                print("The details you entered is incorrect.")
                exit("Goodbye............................")
                break


    def displayValues(self):
        self.cursor = self.conn.execute("SELECT NAME,ID,USERNAME,ROLE,AGE,ADDRESS from USERS")
        for row in self.cursor:
            print("Name:",row[0])
            print("Regno:",row[1])
            print("Username:",row[2])
            print("Role:",row[3])
            print("Age:",row[4])
            print("Address:",row[5],'\n')
            continue

        print("Operation done successfully")
        self.conn.close()

