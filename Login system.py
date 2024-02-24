#a = {"wiz@hotmail.co.uk" : "123456"}
# print(a["wiz@hotmail.co.uk"])
x = []

class Account:
    def __init__(self, firstname, surname, useremail):
        self.firstname = firstname
        self.surname = surname
        self.useremail = useremail
        self.details = [firstname, surname, useremail]

    def create_password(self):
        i_password = input("create new password")
        self.details.append(i_password)
        print(self.details)
        x.append(self.details)

  
def login(em, pw):
    
    for i in x:
        try: 
            y =  i.index(em) + 1
        except:
            y = 0
        if em in i and pw == i[y]:
            print("Successful login")
            return True
    print("unsucessful login, try again")
    #login(em, pw)
    return False

#def login_attempt():


w = Account(input("firstname: "), input("surname: "), input("Enter email: "))
w.create_password()

a = login(input("Enter your email address: "), input("Enter your password: "))
a
tt = 0
while tt < 3 and a == False:
    tt += 1
    a = login(input("Enter your email address: "), input("Enter your password: "))
    
if a == False:
    print("Your accont has been locked please wait 24 hours")
#PROBLEM OF TRYING TO REPEAT THE LOGIN FUCTION 3 TIMES MAX WHEN UNSUCCESSFUL
#while tt < 2:
 #   login(input("Enter your email address: "), input("Enter your password: "))
  #  aa

    

#def login(em,pw):
  #  if existing_user(em):
   #     while pw != a[email]:
  #      print("incorrect password try again")
   #     password = input("enter password")
    #print("Login successful")
#email = input("Email: ")
#password = input("enter password: ")
#if email in a:
 #   while password != a[email]:
  #      print("incorrect password try again")
   #     password = input("enter password")
    #print("Login successful")

