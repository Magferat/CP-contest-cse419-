import sys

n,k,x = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

pre_num = []
new = []
i = 1
group = 1
while i < n :
    d = nums[i] - nums[i-1]
    if d > x :
        pre_num.append(d)
        new.append(i-1)
        group += 1
    i += 1
pre_num.sort()
if k > 0 :
    for i in pre_num :
        m = i/x - 1
        # if m < 0 :
        #     m*= -1
        print(i,m,k,k-m)
        k -= m
        if k > 0:
            group-= 1

print(nums)
print(pre_num)
print(new)
print(group)