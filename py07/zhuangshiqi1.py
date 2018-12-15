# def login(funct):
#     def inner(*args,**kwargs):
#         print('passed user veriftcation...')
#         return funct(*args,**kwargs)
#     return inner
#
# #@login
# @login
# def tv(*args,**kwargs):
#     print('welcom %s to TV page %s' % (args, kwargs))
#     return 88
# #tv = login(tv)
# dic = {'k1':'v1','k2':'v2'}
# li = ['python','java']
# t = tv(li, dic)
# print(t)
# #print(tv(dic,li))
# # tv(dic, li)
# # aa = login(tv)

import os
dd = os.walk('/tmp/demo')
for path, fdir, fname in os.walk('/tmp/demo'):
    print(path)
