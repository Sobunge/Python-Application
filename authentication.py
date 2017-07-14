import hashlib, uuid

#def tryAgain(retries=0):
 #   if retries > 10:
  #      return
   # try:
    #    answer = int(input('Answer:'))
    #except:
     #   retries += 1
      #  tryAgain(retries)

#tryAgain()


#password = 'sam'
#salt = uuid.uuid4().hex
#hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

#password1 = str(input("Password:"))
#salt = uuid.uuid4().hex
#hashed_password1 = hashlib.sha512(password1.encode('utf-8') + salt.encode('utf-8')).hexdigest()

#if hashed_password == hashed_password1:
  #  print("Success")
#else:
 #   print("Fail")



#try:
 #   while attempt<max_attampts:
  #      uname = input('Username:')
   #     password = input('Password:')
#
 #       if uname == 'admin' and password == 'khs9':
  #          print('Welcom Admin')
   #         break
    #    else:
     #       attempt += 1
      #      if attempt == max_attampts:
       #         raise RuntimeError("\n You have reached the maximum number of attempts allowed.")
        #    else:
         #       print('Wrong credentials. \n Try again or Press <CTRL + C> to exit \n')
          #      continue
#except KeyboardInterrupt:
 #   print('Terminated by the user . \n Good-bye')

#except RuntimeError as e:
 #   print('Goodbye')

