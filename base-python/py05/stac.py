
def push_it():
    print('push')

def pop_it():
    print('pop')

def view_it():
    print('show')

def show_menu():
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    while True:
        cmds = {'0':push_it, '1':pop_it, '2': view_it}
        player = input(prompt).strip()[0]
        if player == '3':
            print('再见!!')
            break
        cmds[player]()
        # if player == '0':
        #     push_it()
        # elif player == '1':
        #     pop_it()
        # else:
        #     view_it()

if __name__ == '__main__':
    show_menu()