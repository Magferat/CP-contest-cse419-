import sys

t = int(sys.stdin.readline().strip())


while t > 0:

    nums = [int(i) for i in sys.stdin.readline().split()]

    a = sum(nums)
    p = False
    for i in nums:
        if a - i >= 10:
            p = True
            break
    if p:
        print('YES')

    else:
        print('NO')

    t -= 1