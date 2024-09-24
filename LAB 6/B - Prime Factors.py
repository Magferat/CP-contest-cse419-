




# num = 100
#
# while num != 0 :
#     num = int(sys.stdin.readline())
#     # print(num)
#     if num != 0 :
#         # print("H")
#         factors = {}
#         i = 2
#         f_str = str(num) + " = "
#         if num < 0 :
#             factors[-1] = 1
#             f_str = str(num) + " = " + "-1 x "
#             num *= (-1)
#         while i * i <= num:
#             while num % i == 0 :
#                 # if i not in factors :
#                 #     factors[i] = 1
#                 # else:
#                 #     factors[i] += 1
#                 f_str += str(i) + " x "
#                 num //= i
#             i += 1
#         if num > 1 :
#             # factors[num] = 1
#             f_str += str(num) + " x "
#         f_str = f_str[0:-3]
#         sys.stdout.write(f_str+"\n")




# 90
# 1234567891
# 18991325453139
# 12745267386521023
# 0


# -190
# -191
# -192
# -193
# -194
# 195
# 196
# 197
# 198
# 199
# 200
# 0
