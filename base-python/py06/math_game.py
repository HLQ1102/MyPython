import random

def exam():
    nums = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    # print(nums)
    n = 3
    op = random.choice('+-')
    while n > 0:
        n -= 1
        print('请作答：%s%s%s=' % (nums[0], op, nums[1]), end='')
        c = int(input())
        if op == '+':
            result = nums[0] + nums[1]
        else:
            result = nums[0] - nums[1]
        if c == result:
            print('答案正确')
            break
        else:
            print('答案错误')
            continue

if __name__ == '__main__':
    # while True:
    #     exam()
    #     yn = input('Continue(y/n)? ').strip()[0]
    #     if yn in 'Nn':
    #         print('\nBye-bye')
    #         break
    exam()
