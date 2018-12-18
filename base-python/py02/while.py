import random

n = 1
sum = 0
while n <= 100:
    sum += n
    n += 1
print(sum)


m = 100
sxh = []
while m <= 999:
    bai = m // 100
    shi = m // 10 % 10
    ge  = m % 10
    if bai ** 3 + shi ** 3 + ge ** 3 == m:
        sxh.append(m)
    m += 1
print('水仙花数是：',sxh)

j = 0
sxh = []
for j in range(100,999):
    bai = j // 100
    shi = j // 10 % 10
    ge  = j % 10
    if bai ** 3 + shi ** 3 + ge ** 3 == j:
        sxh.append(j)
    j += 1
print('水仙花数是：',sxh)
print('水仙花数一共有', len(sxh),'位')

sxh = []
for i in range(1,101):
    sj = random.random()*100//1
    sxh.append(sj)
print(sxh)


# print(len(sxh))



sum100 = 0
counter = 0
while counter < 100:
    counter += 1
    if counter % 2 :
        continue
    sum100 += counter
print(sum100)
