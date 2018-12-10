import keyword
import string

str1 = 'abcdefghijkl'

def get_str():
    STR = input('输如入字符串')
    return STR

def pan_zifu(zifu):
    if zifu[0] in string.ascii_letters + '_':
       return zifu
    else:
        return 0
def pan_guanjian():



if __name__ == '__main__':
