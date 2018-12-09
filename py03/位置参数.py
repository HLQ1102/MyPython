import sys

a = int(sys.argv[1])
# print(2 * a)

for i in range(1, int(sys.argv[1]) + 1):
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j),end='\t' )
    print()

# 位置参数默认保存在一个列表里面，其类型是string
