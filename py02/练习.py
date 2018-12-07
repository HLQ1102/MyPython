print('111')
print(True + 10)
print(1.22)
print(0o11)
print("Tom\'s a cat")
stra = """
莫听穿林打叶声，何妨吟啸且徐行。
竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。
料峭春风吹酒醒，微冷，山头斜照却相迎。
回首向来萧瑟取，归去，也无风雨也无晴。"""
print(stra)
print('hello\nworld')
print('\n' * 5)
lines = '''
world
world
world
'''
print(lines)
# exit()
print(stra[1:3])
print(stra + lines)
print(stra * 2)
print(stra[1], '\n')
pyalias = 'python'
print(len(pyalias))
print(pyalias[:len(pyalias)])
print(pyalias[-2])
print(pyalias[1:4])
print(pyalias[1:-1])
print(pyalias[0:2])
print('\n' * 5)

list = [1, 2, 3, 4, 5, 6, 7]
zu = {'name':'xiao', 'age':'man'}
print(len(list))
print(zu['name'])
print(zu['age'])
print(pyalias[::2])
print(stra)
print(stra[::3],'\n')
print(pyalias)
print(pyalias[-1:-4:-2])
alist = [10, 20, 'xiao', 'wu', 'jiu', [1, 2, 3]]
print(alist[-1][-1])
alist.append('xixixiix')
print(alist)
atuple =  (10, 30, [1, 2, {'name':'xiao'}])
print(atuple)
if 'name' in atuple[-1][-1]:
    print(atuple[-1][-1]['name'])
print(pyalias[1])

if -0.0:
    print('ok')

if ' ':
    print('space is true')

if not []:
    print('kong list is Ture')
if ' ':
    print('space is True')

if 'xiao' == atuple[-1][-1]['name']:
    print('yes, I\'m')
stra = """
莫听穿林打叶声，何妨吟啸且徐行。
竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。
料峭春风吹酒醒，微冷，山头斜照却相迎。
"""
if stra[-1] == '\n':
    print("I'm Chainese!!")
if not None:
    print('11')

a = 100
b = 80
smaller = a if a < b else b
print(smaller)
print(smaller)