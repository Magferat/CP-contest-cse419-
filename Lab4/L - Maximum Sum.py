import sys

t = int(sys.stdin.readline())

while t > 0 :

    n,k = list(map(int, sys.stdin.readline().split()))
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    # print(nums)
    all_s = []
    min_s =sum(nums[0:2*k])
    max_s =sum( nums[-k::])


    if min_s < max_s :
        s = sum(nums) - min_s
        all_s.append(s)
        # sys.stdout.write(str(s) + "\n")
    if min_s >= max_s :
        s = sum(nums) - max_s
        all_s.append(s)
        # sys.stdout.write(str(s) + "\n")

    while k > 0 :

        mins = nums[0] + nums[1]
        if mins < nums[-1] :
            nums.pop(0)
            nums.pop(0)
            # print(nums, "h1")
        else:
            nums.pop(-1)
            # print(nums, "h2")

        k-= 1

    s = sum(nums)
    all_s.append(s)
    all_s.sort()

    sys.stdout.write(str(all_s[-1])+"\n")
    t -= 1
