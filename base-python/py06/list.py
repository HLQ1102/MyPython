from random import randint

# alist = [randint(90,100) for i in range(10)]
# print(set(alist))
# print(alist)
# print(alist.count(100))

import sys, keyword, string

# first_chs = string.ascii_letters + '_'
# all_chs = first_chs + string.digits
#
# def check_id(idt):
#     if keyword.iskeyword(idt):
#         return "%s is keyword" % idt
#
#     if idt[0] not in first_chs:
#         return "1st invalid"
#
#     for ind, ch in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return "char in postion #%s invalid" % (ind + 2)
#
#     return "%s is valid" % idt
#
#
# if __name__ == '__main__':
#     print(check_id(sys.argv[1]))

# import sys, keyword, string
#
# tou_str = string.ascii_letters + '_'
# hou_str = string.ascii_letters + string.digits + '_'
#
# def pan_var(var):
#     if keyword.iskeyword(var):
#         print('变量%s是不关键字' % var)
#         return 0
#     if var[0] not in tou_str:
#         print('变量%s需要以字母或\'_\'开头' % var)
#         return 0
#     else:
#         for ind, ch in enumerate(var):
#             if ch not in hou_str:
#                 print('变量只能由数字，字母，下划线组成')
#                 exit(1)
#         return 1
#
#
#
#
#
# import sys
#
# def unix2dos(fname):
#     dst_fname = fname + '.txt'
#
#     with open(fname) as src_fobj:
#         with open(dst_fname, 'w') as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip() + '\r\n'
#                 dst_fobj.write(line)
#
# # if __name__ == '__main__':
# #     unix2dos(sys.argv[1:])
#
# # if __name__ == '__main__':
    # b = pan_var('2b')
    # print(b)
    # for ind, ch in enumerate(sys.argv[1]):
    #     print(ind, '  ', ch)


# def gen(obj):
#     a = []
#     for line in obj:
#         if len(a) != 10:
#             a.append(line)
#         else:
#             yield a
#             a = []
#     yield a
#
# if __name__ == '__main__':
#     path = '/etc/passwd'
#     with open(path, 'r')as obj:
#         # for line in gen(obj):
#         #     print(line)
#         #     print()
#         print(gen(obj))


from functools import partial

def hah(h, k):
    print(h ,end='\t')
    print(k)
    print(h + k)
if __name__ == '__main__':
    bb = partial(hah,10)
    bb(70)
