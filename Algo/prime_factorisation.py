import sys

n = int(sys.stdin.readline())

# ================== O(N) ============== soln
# s = {}
# i = 2
# while i <= n :
#     while n % i == 0:
#             if i not in s :
#                 s[i] = 1
#             else:
#                 s[i] += 1
#             n /= i
#     i += 1
#
#
# print(s)
# ======================== O(root n) ========================
s = {}
i = 2
while i*i <= n :
     while n % i == 0:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
            n /= i
     i += 1

if n > 1 :
    s[n] = 1


print(s)