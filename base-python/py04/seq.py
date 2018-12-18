hi = 'hello'
alilst = [10, 20, 30]
for i in range(len(hi)):
    print(i, hi[i])

print(list(enumerate(alilst)))

for i, j in enumerate(alilst):
    print(i, j)

for i in enumerate(alilst):
    print(i)

# print(enumerate(alilst))
hihi = list(enumerate(alilst))
print(hihi[2][0])

print(alilst)
print(sorted(alilst))


