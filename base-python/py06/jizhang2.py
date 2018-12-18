import os
import pickle as pic
import time

def cost(record):
    # print('cost')
    date = time.strftime('%Y-%m-%d')
    jin_e = int(input('请输入记账金额：'))
    comment = input('备注：')
    with open(record, 'rb') as fobj:
        data = pic.load(fobj)
    balance = data[-1][-2] - jin_e
    data.append([date, 0, jin_e, balance, comment])
    with open(record,'wb') as fobj:
        pic.dump(data, fobj)


def save(record):
    # print('save')
    date = time.strftime('%Y-%m-%d')
    while True:
        try:
            jin_e = int(input('请输入记账金额：'))
            comment = input('备注：')
            break
        except (KeyboardInterrupt, EOFError):
            print('输入错误')
            continue
    with open(record, 'rb') as fobj:
        data = pic.load(fobj)
    balance = data[-1][-2] - jin_e
    data.append([date, jin_e, 0, balance, comment])
    with open(record,'wb') as fobj:
        pic.dump(data, fobj)

def query(record):
    # print('query')
    print('%-12s%-10s%-10s%-10s%-20s' %('date', 'save', 'cost', 'balance','comment'))
    with open(record, 'rb') as fobj:
        data = pic.load(fobj)
    for line in data:
        print('%-12s%-10s%-10s%-10s%-20s' % tuple(line))


def show_menu():
    record = 'record.data'
    cmds = {'0': cost, '1': save, '2': query}
    init_data= [
        [time.strftime('%Y-%m-%d'), 0, 0, 10000, '记账开始'],
    ]
    if not os.path.exists(record):
        with open(record, 'wb') as fobj:
            pic.dump(init_data, fobj)

    prompt = '''(0) 开销
(1) 收入
(2) 查询
(3) 推出
请选择(0/1/2/3): '''
    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in '0123':
            print('无效输入')
            continue
        if choice == '3':
            print('bey-bey!!')
            exit(0)
        cmds[choice](record)

if __name__ == '__main__':
    show_menu()