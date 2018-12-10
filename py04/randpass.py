import shutil
import random

def randpass(n = 8):
    a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = ''
    while True:
        d += random.choice(a)
        if len(d) == n:
            break
    return d
