import random

lag = True
counter = [0, 0, 0]
while lag:
    if counter[0] == 2 or counter[1] == 2:
        lag = False
        continue
    # elif counter[1] == 2:
    #     lag = False
    #     continue

    # if  counter[2] == 3:
    #     lag = False
    #     continue
    counter[2] = counter[2] + 1

    print(counter[2])
    all_choice =['石头', '剪刀', '布']
    latest = """
    (0) 石头
    (1) 剪刀
    (2) 布
    请出拳（0/1/2）"""
    computer = random.choice(all_choice)
    index = int(input(latest))
    palyer = all_choice[index]
    win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

    print('您的出拳是：',palyer,'\n计算机的出拳是：', computer)
    if computer == palyer:
        print('\033[32;1m平局\033[0m')
    elif [palyer, computer] in win_list:
        print('\033[31;1m赢了\033[0m')
        counter[0] += 1
    else:
        print('\033[31;1m输了\033[0m')
        counter[1] += 1
else:
    print(counter[0], ':',counter[1],'\n共进行',counter[2],'局')
    if counter[0] > counter[1]:
        print('\033[32;1m玩家获胜\033[0m')
    elif counter[0]< counter[1]:
        print('\033[31;1m电脑胜\033[0m')
    else:
        print('\033[32;1m平局\033[0m')





