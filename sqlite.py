import sqlite3
import hashlib, uuid

class connection:

    def connect(self):
        self.conn = sqlite3.connect("student.db")
        print("Connection successful")

    def createTable(self):
        self.conn.execute( ''' CREATE TABLE DETAILS(
                    NAME char(100) NOT NULL,
                    REGNO CHAR(12) NOT NULL,
                    USERNAME CHAR(100) NOT NULL,
                    SALT TEXT NOT NULL,
                    PASSWORD CHAR(100) NOT NULL,
                    AGE INT NOT NULL,
                    ADDRESS TEXT
        );''')

    def insertValues(self,name,regno,username,salt,password,age,address):
        self.conn.execute('INSERT INTO DETAILS(NAME,REGNO,USERNAME,SALT,PASSWORD,AGE,ADDRESS) \
                          values("%s","%s","%s","%s","%s","%d","%s")' %\
                          (name,regno,username,salt,password,age,address))
        print("Registration is successful")


    def authenticate(self,uname,pword):
        self.cursor = self.conn.execute("SELECT USERNAME,SALT,PASSWORD from DETAILS")
        for row in self.cursor:
            username = row[0]
            salt = row[1]
            psword = row[2]

            password = hashlib.sha512(pword.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            if username == uname and password == psword:
                print("Success")
                break
            else:
                print("Fail")


    def displayValues(self):
        self.cursor = self.conn.execute("SELECT NAME,REGNO,USERNAME,AGE,ADDRESS from DETAILS")
        for row in self.cursor:
            print("Name:",row[0])
            print("Regno:",row[1])
            print("Username:",row[2])
            print("Age:",row[3])
            print("Address:",row[4],'\n')

        print("Operation done successfully")
        self.conn.close()

