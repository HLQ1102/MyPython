def set_age(name, age):
    if not 0 < age < 100:
        raise  ValueError('age值错误')
    print('%s有%s米长' % (name, age))
def set_age2(name, age):
    assert 0 < age < 100, '长度超范围了'


if __name__ == '__main__':
    set_age2('蟒蛇',150)