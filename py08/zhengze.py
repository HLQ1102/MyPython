import re

aa = 'hello-world.tar.gz'
print(aa.split('-'))
cc = re.split('\.|-', 'hello-world.tar.gz') # 以'.'或'-'去分割字符串
print(cc)  # ['hello', 'world', 'tar', 'gz']
dd = 'Hi name, Nice to meet you name'.replace('name', 'xiao')
print(dd)  # Hi xiao, Nice to meet you xiao

import re

data = 'his phon number is : 150889912'
re.search('.+', data).group()        # 匹配所有
re.search('.+(\d+)', data).group()   # 默认+/× 都是贪婪匹配，符合将匹配所有
re.search('.+(\d+)', data).group(1)  # 配置结果是'2' ，匹配数字的最后一位，前面被+贪婪匹配完了
re.search('.+(\d+)', data).group(0)  # 0为默认显示方式，完全显示
re.search('.+?(\d+)', data).group(1) # 显示括号里面的匹配项
re.search('.+?(\d+)', data).groups(1)# 正则表达式匹配对象通过groups函数获取子组
  # 结果 -> ('150889912',)