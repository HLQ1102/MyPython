
def push_it(alist):
    content = input('请输入压栈内容: ').strip()
    if content:
        alist.append(content)

def pop_it(alist):
    if a:
        print('弹出\033[32;1m%s\033[0m' % alist.pop())

def view_it(alist):
    if alist:
        print('\033[32;1m%s\033[0m' % alist)
    else:
        print('\033[31;1m空栈\033[0m')

def show_menu(a):
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

        cmds[player](a)
        # if player == '0':
        #     push_it()
        # elif player == '1':
        #     pop_it()
        # else:
        #     view_it()

if __name__ == '__main__':
    a = []
    show_menu(a)