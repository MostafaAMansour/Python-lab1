'''
Simple Login System
'''
userNames = ['Ahmed','Ali','Amr']
passwords = ['1394','6078','9345']
userName = input("Please enter your name: ")
if userName in userNames:
    password = input("Please enter your password: ")
    if password == passwords[userName.index(userName)]:
        print(f"welcome back {userName}")
    else:
        print("Incorrect password")
else:
    print("incorrect UserName")
#-------------------------------------------------------------#
'''
#dictionary#
database = {'Ahmed':'1394','Ali':'6078','Amr':'9345'}
userName = input("Please enter your name: ")
if userName in database:
    password = input("Please enter your password: ")
    if password == database[userName]:
        print(f"welcome back {userName}")
    else:
        print("Incorrect password")
else:
    print("incorrect User_Name")

'''