try:
    num = int(input())
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('ddd')
except (KeyboardInterrupt, EOFError):
    print('\nbey-bey')
else:
    print(213)