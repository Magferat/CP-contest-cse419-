t = int(input().strip())

while t > 0:

    n = int(input())
    nums = [int(i) for i in input().split()]
    i = 1
    sorted_ = 'NO'
    while i < n-1:
        if i+1 < n :
            if nums[i-1] <nums[i] < nums[i+1] and i+1 < n:
                i += 1
                sorted_ = 'YES'

            elif nums[i-1] < nums[i] and nums[i] > nums[i+1] and i+1 < n:
                s = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = s
                sorted_ = 'YES'
            else:
                    sorted_ = 'NO'
                    break

    print(sorted_)
    t-= 1