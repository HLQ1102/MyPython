import random

number = random.randint(1, 100)
# a= int(input('猜数（1-100）：'))
while 0 > -1:
    a = int(input('猜数（1-100）：'))
    if a > number:
        print('猜大了！')
    elif a < number:
        print('猜小了！')
    else:
        print('猜对了！，您真牛')
        break
