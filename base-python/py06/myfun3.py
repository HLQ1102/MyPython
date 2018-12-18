from random import randint
import subprocess

def myfun(n):
    if n == 1:
        return n
    return n * myfun(n - 1)

def sort(seq):
    if len(seq) < 2:
        return seq

    middle = seq[0]
    smaller = []
    big = []

    for item in seq[1:]:
        if item > middle:
            big.append(item)
        else:
            smaller.append(item)

    return sort(smaller) + [middle] + sort(big)


if __name__ == '__main__':
    # print('%e' % myfun(30))
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(sort(nums))

