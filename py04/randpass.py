import random

a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def randpass(n = 8):
    d = ''
    while True:
        d += random.choice(a)
        if len(d) == n:
            break
    return d
