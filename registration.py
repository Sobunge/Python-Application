import hashlib, uuid

class Register:

    __trials = 0
    __max_trials = 10

    def enterValues(self):
        self.name = str(input("Enter Name:"))
        self.username = str(input("Enter Username:"))
        print("Enter Role \n1.Student \n2.Lecture")
        role = int(input("Role:"))
        if role == 1:
            self.role = 'Student'
            self.id = str(input("Enter Reg No:"))
        elif role == 2:
            self.role = 'Lecture'
            self.id = str(input("Enter Employee Id:"))
        self.password = str(input("Enter Password:"))
        self.salt = uuid.uuid4().hex
        self.hashed_password = hashlib.sha512(self.password.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()
        self.age = int(input("Enter age:"))
        self.address = str(input("Enter Address:" ))

    def login(self):
        print('######## Login #########')
        self.username = str(input("Enter Username:"))
        self.password = str(input("Enter Password:"))

    def tryAgain(self):
        if self.__trials == self.__max_trials:
            print("You have reached the maximum trials")
            return
        try:
            self.answer = int(input('Answer:'))
        except:
            print("The answer you entered is neither 1 nor 2. \nTry again")
            self.__trials += 1
            self.tryAgain()
        else:
            while self.answer != 1 and self.answer != 2:
                print("The answer you entered is neither 1 nor 2 \nTry again")
                self.tryAgain()

    def display(self):
        print("Name:",self.name)
        print("Role:",self.role)
        print("Id:",self.id)
        print("Username:",self.username)
        print("Password:", self.hashed_password)
        print("Age:",self.age)
        print("Address:",self.address)

    def registration(self):
        print("######### Registration #########")
        self.enterValues()
        print('')
        print("Confirm if the details below are correct ")
        self.display()
        print("\nIs the above information correct \n1.Yes \n2.No")
        self.tryAgain()

