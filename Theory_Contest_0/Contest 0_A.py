# t = int(input())
# nums = [int(n) for n in input().split()]
# add_t = t*(t+1)/2
# sum_num = sum(nums)
# print(int(add_t - sum_num))

t = int(input())
nums = input().split()
for x in range(1,t+1):
    if str(x) not in nums:
        print(x)
