import time
import pickle as pic

t1 = time.strftime('%Y-%m-%d')
print(time.ctime())
# a = [
#     {'date':'tmplate', 'in':'template', 'out':'tmeplate', 'yu_e':10000, 'beizhu':'tmplate'}
# ]

with open('/tmp/zhangben.txt', 'rb') as f:
    jilu = pic.load(f)

a = jilu


def clock():
    clo = time.strftime('%Y-%m-%d')
    a[-1]['date'] = clo

def in_out():
    info = '''(+)进账
(-)出账
请输入(+/-):'''
    lag = input(info).strip()
    jin_e = int(input('  金额:'))
    if lag == '+':
        a[-1]['in'] = jin_e
        a[-1]['out'] = 0
        a[-1]['yu_e'] += jin_e
    elif lag == '-':
        a[-1]['out'] = jin_e
        a[-1]['yu_e'] -= jin_e
        a[-1]['in'] = 0


def beizhu():
    dscr = input('请输入对该笔账备注：').strip()
    a[-1]['beizhu'] = dscr

def cunchu():
    # a = [{'date': 'tmplate', 'in': 'template', 'out': 'tmeplate', 'yu_e': 'template', 'beizhu': 'tmplate'}]
    with open('/tmp/zhangben.txt', 'wb') as f:
        pic.dump(a, f)

def jizhang():
    clock()
    print(a)
    in_out()
    print(a)
    beizhu()
    print(a)
    cunchu()

def chazhang():
    with open('/tmp/zhangben.txt', 'rb') as f:
        jilu = pic.load(f)
    # a = jilu.copy()
    # for i in jilu:
    #     print(jilu[i])
    for i in range(1,len(jilu)):
        for j in jilu[i]:
            print('%s is：' % j, jilu[i][j], end='\t\t')
        print()
    # print(jilu)
    # print(jilu, '\n',len(jilu))


def show_menu():
    info ='''(0) 记账:
(1) 查账:
请输入(0/1)'''
    print('记账开始')
    a.append(a[0].copy())
    print(a)
    while True:
        action = input(info).strip()[0]
        if action not in '01':
            continue
        elif action == '0':
            jizhang()
        elif action =='1':
            chazhang()

if __name__ == '__main__':
    show_menu()
    # chazhang()
    # cunchu()