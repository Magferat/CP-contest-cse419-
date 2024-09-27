import sys

t = int(sys.stdin.readline())

while t > 0 :

    n = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    if n < 2 :
        sys.stdout.write("0\n")
    else:
        p1 = max(nums) - nums[0]
        p2 = nums[-1] - min(nums)
        d = max(p1,p2)

        for i in range(n) :
            d = max(d, nums[i-1]-nums[i])
        sys.stdout.write(str(d)+"\n")
    t -= 1