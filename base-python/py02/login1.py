import getpass

user1 = input('input username: ')
pass1 = getpass.getpass('input password: ')
userlist = ['bob', 'Tom', 'Jim', 'Cat']
n = 0
# for len(userlist) > n:
password = {userlist[0]:'123456', }
if user1 in userlist and pass1 == password[user1]:
    print('Login successful!!')
else:
    print('Login inorrect')