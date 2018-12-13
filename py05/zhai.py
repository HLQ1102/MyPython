
zhan = [1, 2]

def ya_zhai(num):
    zhan.append(num)

def chu_zhai():
    return zhan.pop()

def cha_zhan(num = -1):
    return zhan[num]

def main():
    info = ''''这是一个栈，默认[1, 2]:
    (1)压栈
    (2)出栈
    (3)查询栈
    '''
    print(info)
    a = int(input())
    if a == 1:
        b = input('''①：压数值
②：压字符
            ''')
        if b == '1':
            ya_zhai(int(input('请输入数字：')))
            print(zhan)
        elif b == '2':
            ya_zhai(input('请输入字符：'))
            print(zhan)
        else:
            print('错误输入')
    elif a == 2:
        chu = chu_zhai()
        print(chu, '已弹出')
    elif a == 3:
        b = int(input('查询第几个元素：'))
        print(cha_zhan(b - 1))
    else:
        print('输入错误')

if __name__ == '__main__':
    while True:
        if int(input('输入0结束对栈操作:')) == 0:
            break
        main()