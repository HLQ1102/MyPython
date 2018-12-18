import keyword
import string

str1 = 'abcdefghijkl'

def get_str():
    STR = input('输如入字符串')
    return STR

def pan_zifu(zifu):
    # print('123')
    if zifu[0] in string.ascii_letters + '_':
        return zifu
    else:
        return 0
def pan_guanjian(zifu):
    return keyword.iskeyword(zifu)

if __name__ == '__main__':
    zifu = get_str()
    if pan_zifu(zifu) == 0:
        print('error: 变量名必须以字母和下滑线\'_\'开头')
        exit(1)
    if pan_guanjian(zifu) == True:
        print('error: 变量是一个关键字，已退出')
        exit(2)
    print('变量%s定义成功' % zifu)
