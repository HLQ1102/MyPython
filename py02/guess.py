import random

number = random.randint(1, 100)
a= int(input('猜数（1-100）：'))
for
if a > number:
    print('猜大了！')
    print('我是：', number)
elif a < number:
    print('猜小了！')
    print('我是：', number)
else:
    print('猜对了！，您真牛')
    print('我是：', number)
