import getpass

user_info = {'root':'123'}
def register():
    user = input('username: ')
    if user not in user_info:
        password = getpass.getpass('password: ')
        user_info.update({user:password})
        print('用户%s创建成功' % user)
    else:
        print('用户%s已存在' % user)

def login():
    user = input('user:')
    # if user in user_info and password == user_info[user]:  //简化为下面的 if 语句
    if user_info.get(user) == password:
        print('login sesscuful')
    else:
        print('用户%s不存在或密码错误' % user)
    # print('123')

def show_menu():
    info = '''(1) 注册
(2) 登陆
请输入(1/2):'''
    while True:
        cmds = {'1': register, '2': login}
        lag = input(info)
        if lag not in '12':
            print('无效输入')
            continue
        cmds[lag]()

def save_user():
    with open('/tmp/user.txt','a') as fobj:
        fobj.write(user_info)

if __name__ == '__main__':
    show_menu()