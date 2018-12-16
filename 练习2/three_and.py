#!/usr/bin/env python3
nums = [-1,0,1,2,-1,-4]


def three(nums):
    nums1 = nums
    bb = []
    bao = []
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            if j == i:
                continue
            b = nums[j]
            for k in range(len(nums)):
                if j == i or j == k or i == k:
                    continue
                c = nums[k]
                if a + b + c == 0:
                    bb.append([a, b, c])
    bao = bb
    return bao


if __name__ == '__main__':
    bao = []
    # for aa in three(nums):
    #     cc = aa.sort()
    #     if aa not in bao:
    #         bao.append(aa)
    # for i in three(nums):
    #     i.sort()
    #     # cc = set(i)
    #     if i not in bao:
    #         print(i, end=' ')
    #         bao.append(i)

        # if i not in bao:
        #     print(i)
    # bao = set(bao)
    # for i in bao:
    print('\n', three(nums))
