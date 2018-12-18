score = int(input('分数：'))

if score >= 90:
    print('优秀')
elif 80 <= score < 90:
    print('good')
elif 70 <= score < 80:
    print('良')
elif 60 <= score < 70:
    print('及格')
else:
    print('加油吧！！')
