

def get(sex, age):
    print('I\'m a %s , today %s years old' %  (sex, age))

def myfunc(*args):
    print(args)

def myfunc2(**kwargs):
    print(kwargs)

def add(*alist):
    sum = alist[len(alist)]
    for i in (alist):
        sum += i
    print(sum)

if __name__ == '__main__':
    # get('boy', 11)
    # get(11,22)
    # get('girl', 18)
    # get(sex='gril', age=20)
    # get(age='44', sex='boy')
    # get('44', age='boy')
    # myfunc()
    # myfunc(10)
    # myfunc(20, 10, 'bob')
    # myfunc2()
    # myfunc2(haha = '11')
    # myfunc2(a = 'aa')
    # myfunc2(ahha = 10)
    # myfunc2(xiao = '11', wu='22')
    alist = (3,4,5)
    add(*alist)
    add(*'bb')
