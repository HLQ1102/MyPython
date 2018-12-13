from random import randint

def func1(n):
    return n % 2

def func2(n):
    return n + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(list(filter(lambda n: n % 2, nums)))  #
    print(list(map(func2, nums)))  # 加工列表
    print(list(map(lambda n: n + 1, nums)))  # 写成匿名函数


    for i in range(1, 10):
        global x
        x = randint(1, 10)
        print(x, end='\t')
    print()

    from functools import partial
    def add(a, b, c, d, e):
        return a + b + c + d + e
    myadd = partial(add, 10, 20, 30, 40)
    partial(myadd)
    myadd(100)
    print(myadd(10))