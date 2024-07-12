# # # n = int(input())
# # #
# # # def fact_B(n):
# # #     if n <= 1:
# # #         return 1
# # #     else:
# # #         return (n * fact_B(n-1))
# # #
# # # r = fact_B(n)2
# #
# # # print(r)
# # #
# # import math
# # n = int(input())
# # r = math.factorial(n)
# # print(r)
# # j = 0
# # for i in f"{r}"[::-1]:
# #     if i == '0':
# #         j += 1
# #     if i != '0':
# #         break
# #
# # print(j)
# #
# #
# #
# import math
# n = 5
#
# while n < 1555:
#     j = 0
#     r = math.factorial(n)
#     for i in f"{r}"[::-1]:
#         if i == '0':
#                 j += 1
#         if i != '0':
#                 break
#
#     x = n // 5 + (n//25) + n//125 + n// 625
#
#     if j != x :
#         print(f"{n}! = {j} ==== {x} ===")
#
#     n += 5

# n = int(input())
#
p = int(input())

x = 0
while p >= 5:
    p //= 5
    x += p
print(x)

